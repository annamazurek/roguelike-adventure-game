from operator import itemgetter
path = 'result.txt'
# print best scores
print("\nHIGH SCORES:\n")
with open(path, 'r') as file:
    score_rows = file.readlines()

score_board = []
for row in score_rows:
    cols = row.split("|")
    score_board.append([cols[0], int(cols[2]), cols[3], cols[4]]) # select name and seconds pairs (convert second from string to int)
# print(score_board)
score_board = sorted(score_board, key=itemgetter(1)) # sort by second column (seconds)
i = 1
for row in score_board:
    print(str(i)+". "+row[0]+": "+str(row[1])+"sec" +" | " + str(row[2]) + " Moves" + " | " + str(row[3])) # shows ten biggest scores
    i += 1
    if i > 10:
        break
