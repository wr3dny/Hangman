# Try to guess word

import random

words = ['poleaxe', 'sword', 'mouse', 'castle']

visual = [['_', '_', '_', '_', '_', '_'], ['|', ' ', ' ', ' ', '|', ' '], ['|', ' ', ' ', ' ', ' ', ' '],
          ['|', ' ', ' ', ' ', ' ', ' '], ['|', ' ', ' ', ' ', ' ', ' '], ['|', ' ', ' ', ' ', ' ', ' ']]

# for row in visual:
#     print(*row)

# visual[2][4] = 'O'
# visual[3][3] = '/'
# visual[3][4] = '|'
# visual[3][5] = '\\'
# visual[4][3] = '/'
# visual[4][5] = '\\'
#
# for row in visual:
#     print(*row)

word_to_guess = random.choice(words)
print(word_to_guess)

number_of_start = len(word_to_guess)
hidden_word = number_of_start * '*'
print(hidden_word)


def asker():
    ask_letter = input('What\'s your letter ? \n -->')
    return ask_letter


# def wrong(letter):
#     # if letter not in word_to_guess:
#
#     pass




def main():
    wrong = 0
    while wrong <= 5:
        letter = asker()
        if letter not in word_to_guess:
            wrong += 1
            letter = asker()
        elif letter in word_to_guess:
            print('Good')








    #     wrong += 1
    #     if wrong >= 6:
    #         print('The End')
    #         break
    # else:
    #     print('Good')
    #     print(wrong)








# while True:
#     ask_letter = input('Letter --> ').lower()
#
#     if ask_letter in word_to_guess:
#         for i in word_to_guess:
#             if i == ask_letter:
#                 print(i)


if __name__ == '__main__':
    main()
