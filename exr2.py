

print('-----------------------------------')
print('Welcome in Rock Paper Scissors Game')
print('-----------------------------------')

while true:
    print("" "Choose one of these words" Rock - Paper - Scissors" """)
    player1 = input(">>>")
    player2 = input(">>>")

# rock , scissors = Rock
  if player1.lower() == 'rock' and player2.lower() == 'scissors':
       print("player 1 in winner.......")
elif   player2.lower() == 'rock' and player1.lower() == 'scissors':
    print("player 2 in winner.......")
# rock , scissors = Rock
elif player1.lower() == 'scissors' and player2.lower() == 'Paper':
    print("player 1 in winner.......")

elif player1.lower() == 'Paper' and player2.lower() == 'Paper':
    print("player 2 in winner.......")
# rock , scissors = Rock
elif player1.lower() == 'Paper' and player2.lower() == ' rock':
    print("player 1 in winner.......")
elif player1.lower() == 'Paper' and player2.lower() == 'Paper':
    print("player 2 in winner.......")
elif player1.lower() =='exit'or player2.lower()=='exit':
