

loss = 0
draw = 3
win = 6

result_scores = [0, 3, 6]
choice_scores = ['X','Y','Z']

options = { 'A' : ['Z', 'X', 'Y'],
            'B' : ['X', 'Y', 'Z'],
            'C' : ['Y', 'Z', 'X']
}


total_score = 0

with open('day_2_input.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    opponent_choice = line.split(' ')[0]
    your_choice = line.split(' ')[1]

    opponent_hand = options[opponent_choice]
    
    round_score = result_scores[choice_scores.index(your_choice)]

    hand_score = choice_scores.index(opponent_hand[choice_scores.index(your_choice)]) + 1

    total_score += round_score + hand_score


print(total_score)


