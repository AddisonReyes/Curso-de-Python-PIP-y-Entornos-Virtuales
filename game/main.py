import random


def choose_options():
  options = ('stone', 'paper', 'scissors')
  user_option = input('Stone, Paper or Scissors => ')
  user_option = user_option.lower()

  if not user_option in options:
    print('\nThat option is not valid')
    return None, None

  computer_option = random.choice(options)

  print('\nUser option =>', user_option)
  print('Computer option =>', computer_option)

  return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Tie!')

  elif user_option == 'stone':
    if computer_option == 'scissors':
      print('You win!')
      user_wins += 1

    else:
      print('Computer wins!')
      computer_wins += 1

  elif user_option == 'paper':
    if computer_option == 'stone':
      print('You win!')
      user_wins += 1

    else:
      print('Computer wins!')
      computer_wins += 1

  elif user_option == 'scissors':
    if computer_option == 'paper':
      print('You win!')
      user_wins += 1

    else:
      print('Computer wins!')
      computer_wins += 1

  return user_wins, computer_wins


def main():
  computer_wins = 0
  user_wins = 0  
  rounds = 1

  while True:
    print()
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print()
    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    if computer_wins == 2:
      print('The winner is the computer')
      break

    if user_wins == 2:
      print('The winner is the user')
      break


if __name__ == '__main__':
    main()