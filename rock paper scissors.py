
while True:
	player1 = input("Choose your play: ")
	if player1 == "quit":
		break
	player2 = input("Choose your play: ")
	if player2 == "quit":
		break
		
	
	if (player1 == player2):
		print("It's a draw!")
	
	elif (player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
		print("Player 1 wins!") 
	
	elif (player2 == "rock" and player1 == "scissors") or (player2 == "paper" and player1 == "rock") or (player2 == "scissors" and player1 == "paper"):
		print("Player 2 wins!")
		
	else: print("ERROR")
