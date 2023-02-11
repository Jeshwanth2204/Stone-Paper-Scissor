from getpass import getpass as input

print('THE ROCK OF ROME 🪨 , POWER OF PAPAER 📄, SUPER SCISSOR ✂️ ')
print()
print('Select your power(R, S or P)' )
print()
player1_score = 0
player2_score = 0


while True:
    print()
    player_1 = input('Player 1 > ').upper()
    player_2 =input('player 2 > ').upper()
  
    if player_1 == "R" :
      if player_2 == 'R' :
        print('Both Rock just clashed ! ')
      
      elif player_2 == 'P':
        print('Paper rolled up the rock')
        player1_score +=1
      
      elif player_2 == 'S':
        print('Rock broke the Scissor')
        player1_score +=1
      
      else:
        print ('Invalid syntax, not in my codes in your input !')
    
  
    elif player_1 == 'P':
      if player_2 == 'P':
        print('Both Papers became friends')
      
      elif player_2 == 'R':
        print('Paper rolled up the Rock')
        player2_score +=1
      elif player_2 == 'S':
        print('Scissors torn the paper')
        player2_score+=1
      else:
        print ('Invalid syntax, not in my codes in your input !')

    elif player_1 == 'S':
      if player_2 == 'S':
        print('Scissors became teammates now')
      elif player_2 == 'R':
        print('Rock broke the Scissor')
        player2_score +=1
      elif player_2 == 'P':
        print('Scissor makes the paper feel bad')
        player1_score +=1
      else:
        print ('Invalid syntax, not in my codes in your input !')
  
    if player1_score == 3 :
      print('player_1 won,total score',player1_score)
      break
    elif player2_score == 3:
      print('player2_won,total score',player2_score)
      print()
      break
    
    else:

      continue

    


