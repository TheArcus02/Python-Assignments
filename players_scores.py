"""
You have to organize results of a professional spillikins league.
A spillikins match consists of two players collecting points.
The player with the greater amount of points wins the match.
You are given the results of  matches in form of:

player_id:points player_id:points

You have to sort the players in descending order according to the number
of matches they won. In case of a draw - in descending order according
to the number of points they got in all matches.
In case of yet another draw, in ascending order according to
their identifier (as in ASCII, i.e. 'Z' is before 'a').
(If a match ended in a draw it counts as no one winning.)

Input Format
The first line of input contains an integer N - the number of matches in the league.

Each of the following N lines contains the results of the match in the form of:

player_id:points player_id:points

Constraints
1 <= N <= 100

Each player_id is unique. player_id is a string composed of english letters.

Output Format
Some number of lines, each containing one player_id. They have to be sorted according to description above.
"""


def get_matches():
    matches_count = int(input(''))
    matches = []
    for i in range(matches_count):
        match = str(input(''))
        matches.append(match)

    return matches


def get_players_info(matches: []):
    players_wins = {}
    players_points = {}

    for match in matches:
        players = match.split(' ')

        names = []
        points = []

        for player in players:
            player_split = player.split(':')
            player_name = player_split[0]
            player_points = int(player_split[1])

            if player_name not in players_wins:
                players_wins[player_name] = 0
            if player_name not in players_points:
                players_points[player_name] = 0
            players_points[player_name] += player_points
            names.append(player_name)
            points.append(player_points)

        if points[0] > points[1]:
            players_wins[names[0]] += 1
        elif points[1] > points[0]:
            players_wins[names[1]] += 1

    return players_wins, players_points

def sort_players(wins: dict, points: dict):
    # [(Wins, Points, Name), ...]
    players_list = []
    for name, player_wins, player_points in zip(wins, wins.values(), points.values()):
        players_list.append((player_wins, player_points, name))

    return sorted(players_list, key=lambda item: (item[0]*-1, item[1]*-1, item[2]))

def main():
    matches = get_matches()
    wins, points = get_players_info(matches)
    sorted_players = sort_players(wins, points)
    for player in sorted_players:
        print(player[2])

main()
