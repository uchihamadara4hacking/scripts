#/bin/bash~
#programado por R4MSOLO
#Meu canal do youtube link encurtado ---> goo.gl/w3HQr3

from random import randint
import os,sys

os.system('clear')

print '''
________________________________________________________________________________________
  ____            _             _   _                 _   _                           _ 
 | __ )    __ _  | |_    __ _  | | | |__     __ _    | \ | |   __ _  __   __   __ _  | |
 |  _ \   / _` | | __|  / _` | | | | '_ \   / _` |   |  \| |  / _` | \ \ / /  / _` | | |
 | |_) | | (_| | | |_  | (_| | | | | | | | | (_| |   | |\  | | (_| |  \ V /  | (_| | | |
 |____/   \__,_|  \__|  \__,_| |_| |_| |_|  \__,_|   |_| \_|  \__,_|   \_/    \__,_| |_|
                               )___(
                           _______/__/_
                  ___     /===========|   ___
 ____       __   [\\\]___/____________|__[///]   __
 \   \_____[\\]__/___________________________\__[//]___
  \                                       |
   \   	                                              /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
__________________________________________________________________________________________ '''
#Essa parte cria nosso "oceano" :)
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print "  ".join(row) 
print "Vamos jogar Batalha Naval! \n"

print_board(board)

def random_row(board):
    return randint(0, len(board)-1)

def random_col(board):
    return randint(0, len(board[0])-1)

#Armazena o numero aleatorio nas variaveis ship_row e ship_col(linhas e colunas)
ship_row = random_row(board)
ship_col = random_col(board)

#print "[+]Localizacao do Navio \nLinha: ", ship_row + 1
#print "Coluna: ", ship_col + 1

print "\n"
try:
	for turn in range(4): 
		guess_row = int(raw_input("Adivinhe a Linha: "))
		guess_row -=1
		guess_col = int(raw_input("Adivinhe a Coluna: "))
		guess_col -= 1
		print "\n"

		if guess_row == ship_row and guess_col == ship_col:
			print "[+] Parabens, voce afundou meu navio!"
			os.system('clear')
			print '''
__     __             
\ \   / /             
 \ \_/ /__  _   _     
  \   / _ \| | | |    
   | | (_) | |_| |    
__ |_|\___/ \__,_|    
\ \        / (_)      
 \ \  /\  / / _ _ __  
  \ \/  \/ / | | '_ \ 
   \  /\  /  | | | | |
    \/  \/   |_|_| |_|
						   
							'''
			print "\n"
			break

		else:
			if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
				print "[!] Oops,isso nao e nem mesmo no oceano \n"
				sys.exit()
			elif(board[guess_row][guess_col] == "X"):
				print "[!] Voce ja tentou esse. \n"
			else:
				print "[-] Voce errou meu navio! \n"
			board[guess_row][guess_col] = "X"
	#conta mais uma volta e quando chega em 3 tentativas o programa escreve "Game Over!"
		print turn + 1, "de 4 tentativas!"
		if turn == 3:
			print " Game Over! \n"
		print_board(board)
		print "\n"
except ValueError:
sys.exit()
