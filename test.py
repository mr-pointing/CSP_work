import csv

file = "leaderboard.csv"


def get_names(file_name):
    names = []

    with open(file_name, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
        for d in data:
            names.append(d['name'])

    return names

def get_scores(file_name):
    scores = []

    with open(file_name, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
        for d in data:
            scores.append(int(d['score']))

    return scores


def update_leaderboard(leader_names, leader_scores, player_name, player_score):
    index = 0

    for score in leader_scores:
        if score < player_score:
            break
        else:
            index = index + 1

    leader_names.insert(index, player_name)
    leader_scores.insert(index, player_score)
    leader_names.pop()
    leader_scores.pop()


names = get_names(file)
scores = get_scores(file)

update_leaderboard(names, scores, "Jeff", 60)


