# EP 2019-1: Escape Insper
#
# Alunos: 

# - aluno A: Enrico Venturini Costa, enricovc@al.insper.edu.br
# - aluno B: Murilo Lima de Campos Menezes, murilolcm@al.insper.edu.br

import random
import sys,time


def carregar_cenarios():
	cenarios = {
		"inicio": {
			"titulo" : "Entrada Quatá 300",
			"descricao" : "Voce esta na entrada do Insper.",
			"opcoes": {
				"casa do pão de queijo": "seguir em direcao a casa do pão de queijo",
				"biblioteca": "ir para biblioteca",
				"andar dos professores": "subir pelo elevador até o andar dos professores."
			}
		},
		"casa do pão de queijo" : {
			"titulo" : "power up store",
			"descricao" : "voce chegou a power up store! Aqui voce pode comprar upgrades.",
			"opcoes" : {
				"vendedor": "falar com o vendedor para comprar seu upgrade.",
				"inicio" : "voltar para Entrada"
			}
		},
		"biblioteca" : {
			"titulo" : "biblioteca",
			"descricao": "voce chegou a biblioteca e encontrou um veterano irritado, derrote-o para ganhar XP e dinheiro",
			"opcoes" : {
				"lutar":"ganhar XP e dinheiro",
				"inicio":"voltar para a entrada"
			}
		},
		"andar dos professores" : {
			"titulo" : "salas dos professores",
			"descricao" : "voce chegou ao andar dos professores, mas tres estudantes level 5 travam a passagem para a sala do professor de Desoft. Derrote-os para seguir em frente.",
			"opcoes" : {
				"lutar" : "Desafiar cada estudante para acessar a sala do professor.",
				"inicio" : "voltar para a entrada"
			}
		},
		"vendedor" : {
			"titulo" : "Vendedor",
			"descricao" : "Fale com o vendedor para adquirir power ups",
			"opcoes" : {
				"comprar" : "Comprar um pão de queijo vital? (10 moedas)(+1 LVL)",
				"inicio" : "voltar para a entrada"
			}
		},
		"comprar" : {
			"titulo" : "Comprar",
			"descricao" : "Você comprou um pão de queijo vital por 10 moedas e subiu um level.",
			"opcoes" : {
				"inicio" : "voltar para a entrada"
			}
		},
		"lutar" : {
			"titulo" : "Vitória!!",
			"descricao" : "você derrotou o inimigo, e assim subiu de nivel e ganhou 10 moedas!",
			"opcoes" : {
				"inicio" : "voltar para a entrada"
			}
		},
		"desafiar" : {
			"titulo" : "Vitória!!",
			"descricao" : "Você derrotou o estudante LVL 5 e agora pode seguir para a sala do professor de Desoft",
			"opcoes" : {
				"inicio" : "voltar para a entrada",
				"sala do Toshi" : "Conversar com o professor"
			}
		},
		"sala do Toshi" : {
			"titulo" : "A hora da verdade.",
			"descricao" : "Você finalmente chegou à sala do Toshi! Derrote-o e o EP será adiado. Lembre-se, o Toshi é um NPC LVL 12!",
			"opcoes" : {
				"lutar até a morte" : "Ganhe e o EP é adiado, perca e é Game Over.",
				"andar dos professores" : "Voltar ao corredor do andar dos professores."

			}
		},
		"PAI DE TODOS" : {
			"titulo" : "AZEDOU MULEQUE!",
			"descricao" : "Você proferiu um de seus nomes em vão e ele te escutou! Ele quem, você pergunta? ELE! MARCOS LISBOA AKA MARQUITO DA GALERA AKA PAI DE TODOS! Derrote-o e você se formará imediatamente, mas será jubilado caso perca.",
			"opcoes" : {
				"descer a mão no marquito" : "Ahh fi... 3 meses de muay thai aqui, ele não guenta 3 minutos de trocação comigo."
			}
		},
		"descer a mão no marquito" : {
			"titulo" : "GG",
			"descricao" : "Game Over"
		},
		"lutar até a morte" : {
			"titulo" : "Sala do Toshi",
			"descricao" : "Você derrotou o Toshi e o EP foi adiado",
			"opcoes" : {
				"inicio" : "voltar ao inicio",
				"game over" : "Finalizar o jogo",
				"vasculhar" : "vasculhar a sala do professor"
			}
		},
		"vasculhar" : {
			"titulo" : "...",
			"descricao" : "você encontrou o PC do Toshi desbloqueado e descobriu funções inacreditáveis nele.",
			"opcoes" : {
				"Teleport" : "Teletransporte-se para qualquer sala do Insper",
				"LVL boost" : "Digite a senha e de LVL UP até o nível 100",
				"Notas PI" : "Editar sua nota na PI",
			}

		}
	}
	nome_cenario_atual = "inicio"
	return cenarios, nome_cenario_atual

def slow_print(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.01*random.randint(1,10))
	print()


def main():
	slow_print("Azedou, o EP1 chegou!")
	print()
	print("---------------------")
	print()
	avatar = input("Qual é o seu nome? ")
	print()
	slow_print("ééé {0}... A data de entrega do EP1 é amanhã e você ficou fazendo hora extra no suujinhus"
			", agora tem que correr atrás do prejuízo e tentar adiar essa bagaça."
			"Você está na entrada do Insper, veja se consegue encontrar o professor e convencê-lo a fazer a famosa 'boa'.".format(avatar))

	cenarios, nome_cenario_atual = carregar_cenarios()
	LVL = 1
	moedas = 0

	game_over = False
	monstro = False

	def heroi(LVL):
		if LVL == 1:
			healthpoints = 14
			hitpoints = 9
		else: 
			healthpoints = 10 
			hitpoints = 7 

		HP_heroi = healthpoints*LVL
		HIT_heroi = hitpoints + hitpoints*(LVL/5)

		return HP_heroi, HIT_heroi

	def personagens(LVL):

		healthpoints = 10
		hitpoints = 7

		HP = healthpoints*LVL
		HIT = hitpoints + hitpoints*(LVL/5)


		return HP, HIT



	while not game_over:
		cenario_atual = cenarios[nome_cenario_atual]

		slow_print(cenario_atual["titulo"])
		print()
		print("-"*len(cenario_atual["titulo"]))
		print()
		slow_print(cenario_atual["descricao"])
		print()
		print("LVL: {}".format(LVL))
		print("Moedas: {}".format(moedas))
		slow_print("Decida como seguir em frente.")
		print()


		opcoes = cenario_atual["opcoes"]
		if len(opcoes) == 0:
			slow_print("Rodou, fiote... o Toshi vai te jantar.")
			game_over = True

		else: 
			for opcao, descricao_da_opcao in cenario_atual["opcoes"].items():
				print("{0} : {1}".format(opcao, descricao_da_opcao))
			escolha = input("Eai, qual vai ser? ")

			if escolha in opcoes:
				nome_cenario_atual = escolha

			else: 
				slow_print("Moiou o bigode, sepa você perdeu...")
				game_over = True

		# Implementa o monstro aleatório

		x = random.randint(0,12)
		if x <= 3:
			monstro = True
 
		if monstro:

			lvl_monstro = random.randint(1,4)
			HP_monstro, HIT_monstro = personagens(lvl_monstro)
			HP_avatar, HIT_avatar = personagens(LVL)
			slow_print("Você encontrou um veterano LVL {}, e ele está te mandando buscar uma breja no suujus. Derrote-o para não se atrasar ainda mais.".format(lvl_monstro))
			print("Monstro - HP = {} Hitpoints = {}".format(HP_monstro, HIT_monstro))
			print("Avatar - HP = {} Hitpoints = {}".format(HP_avatar, HIT_avatar))


			# Inicio da implementação do combate com o monstro aleatório

			decisao = input("lutar ou fugir? ")

			if decisao == "lutar":
				print("BATALHA!")
				Round = 1
				while HP_monstro > 0 and HP_avatar > 0:
					HP_monstro = HP_monstro - HIT_avatar
					HP_avatar = HP_avatar - HIT_monstro
					print("Round: {}".format(Round))
					print("Vida do veterano: {0}".format(HP_monstro))
					print("Sua vida: {0}".format(HP_avatar))
					Round += 1 
				Round = 0 


				if HP_monstro < 0 and HP_avatar > 0:
					slow_print("Voce ganhou a luta!")
					LVL +=1 
					moedas += 10 
					slow_print("você ganhou 10 moedas e subiu de nível!")
					print("LVL = {0}".format(LVL))
					print("Moedas = {0}".format(moedas))
					
				elif HP_avatar < 0:
					slow_print("Voce morreu!")
					game_over = True
			elif decisao == "fugir":
				slow_print("Você fugiu!")
				

			else:
				slow_print("escolha errada.. você perdeu!")
				game_over = True


			# Fim da implementação do combate com o monstro aleatório



		# Implementa o sistema de compra de itens

		if cenario_atual == cenarios["vendedor"]:
			if escolha == "comprar":
				if moedas >= 10:
					moedas = moedas - 10
					LVL = LVL + 1 


		# Implementa a batalha na biblioteca

	    if cenario_atual == cenarios["biblioteca"]:
			HP_veterano, HIT_veterano = personagens(1)
			HP_avatar, HIT_avatar = heroi(LVL)
			print("Veterano - HP = {0} Hitpoints = {1}".format(HP_veterano, HIT_veterano))
			print("Avatar - HP = {0} Hitpoints = {1}".format(HP_avatar, HIT_avatar))
			if escolha == "lutar":
				
				Round = 1

				while HP_veterano > 0 and HP_avatar > 0:
					HP_veterano = HP_veterano - HIT_avatar
					HP_avatar = HP_avatar - HIT_veterano
					print("Round: {0}".format(Round))
					print("Vida do veterano: {0}".format(HP_veterano))
					print("Sua vida: {0}".format(HP_avatar))
					Round += 1 
				Round = 0 

				if HP_veterano < 0:
					LVL += 1 
					moedas += 10 
					
					

				elif HP_avatar < 0: 
					print("Você morreu!")


		# Implementa batalha na sala dos professores
		
		if cenario_atual == cenarios["andar dos professores"]:
			HP_veterano, HIT_veterano = personagens(5)
			HP_avatar, HIT_avatar = heroi(LVL)
			print("Veterano - HP = {0} Hitpoints = {1}".format(HP_veterano, HIT_veterano))
			print("Avatar - HP = {0} Hitpoints = {1}".format(HP_avatar, HIT_avatar))
	
			if LVL > 5:
				if escolha == "desafiar":

					Round = 1

					while HP_veterano > 0 and HP_avatar > 0:
						HP_veterano = HP_veterano - HIT_avatar
						HP_avatar = HP_avatar - HIT_veterano
						print("Round: {0}".format(Round))
						print("Vida do veterano: {0}".format(HP_veterano))
						print("Sua vida: {0}".format(HP_avatar))
						Round += 1 
					Round = 0 

					if HP_veterano < 0 and HP_avatar > 0:
						LVL += 1 
						moedas += 10 
					
					

					elif HP_avatar < 0: 
						print("Você morreu!")
				else:
					print("Você não está forte o suficiente! Volte quando estiver level 6 ou mais alto.")
					cenario_atual == cenarios["andar dos professores"]


		# Implementa a luta contra o Final Boss

		if cenario_atual == cenarios["sala do Toshi"]:
			HP_toshi, HIT_toshi = personagens(12)
			HP_avatar, HIT_avatar = heroi(LVL)

			print("Toshi - HP = {0} Hitpoints = {1}".format(HP_toshi, HIT_toshi))
			print("Avatar - HP = {0} Hitpoints = {1}".format(HP_avatar, HIT_avatar))

			if escolha == "lutar até a morte":

				Round = 1

				while HP_toshi > 0 and HP_avatar >0:
					HP_toshi = HP_toshi - HIT_avatar
					HP_avatar = HP_avatar - HIT_toshi
					print("Round: {0}".format(Round))
					print("Vida do Toshi: {0}".format(HP_toshi))
					print("Sua vida: {0}".format(HP_avatar))
					Round += 1
				Round = 0 

				if HP_toshi < 0 and HP_avatar > 0:
					slow_print("Parabéns! Você derrotou o professor e conseguiu adiar o EP!")
					slow_print("Toshi: Você me derrotou desta vez. o EP será adiado...")
					slow_print("Toshi: ai ai ai, fui derrotado por um mero bixo... o 'PAI DE TODOS' vai me demitir!")
					

				elif HP_avatar < 0:
					slow_print("Todo o esforço foi em vão... era melhor ter ficado no sujinhuus!")
					slow_print("Você morreu!")
					game_over = True






	slow_print("Azedou teu caldo, você morreu!")
   

# Programa Principal.
if __name__ == "__main__":
	random.seed(time.time())

	main()

	


