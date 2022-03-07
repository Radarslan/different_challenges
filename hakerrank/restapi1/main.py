import os
import requests


def getNumDraws(year):
    number_of_matches = 0
    for team_goals in range(11):
        try:
            response = requests.get(
                url=f"https://jsonmock.hackerrank.com/api/football_matches?"
                    f"year={year}&"
                    f"team1goals={team_goals}&"
                    f"team2goals={team_goals}&"
                    f"page=1"
            )
        except Exception as e:
            continue
        if response and response.json():
            number_of_matches += response.json().get("total", 0)

    return number_of_matches



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = getNumDraws(year)

    fptr.write(str(result) + '\n')

    fptr.close()
