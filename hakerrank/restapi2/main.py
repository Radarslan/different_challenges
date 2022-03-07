import os
import requests
import urllib


def getWinnerTotalGoals(competition, year):
    total_number_of_goals = 0
    url_encoded_competition = get_urlencoded_parameter_from(competition)

    url = f"https://jsonmock.hackerrank.com/api/football_competitions?name={url_encoded_competition}&year={year}"
    winner_data = get_data_from(url).get("data", [])[0]
    if winner_data:
        winner = winner_data.get("winner", "")
    if winner:
        winner = get_urlencoded_parameter_from(winner)
    total_number_of_goals += get_number_of_goals_for(url_encoded_competition, winner, year, "team1")
    total_number_of_goals += get_number_of_goals_for(url_encoded_competition, winner, year, "team2")

    return total_number_of_goals


def get_number_of_goals_for(url_encoded_competition, winner, year, team_to_look):
    total_number_of_goals = 0
    page = 1
    url = f"https://jsonmock.hackerrank.com/api/football_matches?" \
          f"competition={url_encoded_competition}&" \
          f"year={year}&" \
          f"{team_to_look}={winner}&" \
          f"page={page}"
    competition_data = get_data_from(url)
    if competition_data:
        total_pages = competition_data.get("total_pages", 0)
        total_number_of_goals += get_number_of_goals(competition_data, team_to_look)
    while page <= total_pages:
        page += 1
        url = f"https://jsonmock.hackerrank.com/api/football_matches?" \
              f"competition={url_encoded_competition}&" \
              f"year={year}&" \
              f"{team_to_look}={winner}&" \
              f"page={page}"
        competition_data = get_data_from(url)
        if competition_data:
            total_number_of_goals += get_number_of_goals(competition_data, team_to_look)
    return total_number_of_goals


def get_number_of_goals(competition_data, team_to_look: str):
    number_of_goals = 0
    for match in competition_data.get("data", []):
        number_of_goals += int(match.get(f"{team_to_look}goals", 0))
    return number_of_goals


def get_urlencoded_parameter_from(string: str):
    return urllib.parse.quote_plus(string)


def get_data_from(url):
    response = None
    try:
        response = requests.get(url=url)
    except Exception as e:
        pass

    if response and response.json():
        return response.json()
    return {}


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    competition = input()

    year = int(input().strip())

    result = getWinnerTotalGoals(competition, year)

    fptr.write(str(result) + '\n')

    fptr.close()
