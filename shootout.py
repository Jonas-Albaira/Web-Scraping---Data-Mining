#ORIGINAL AUTHOR: NEIL SEAWARD https://github.com/sealneaward/template-py

#Program to show SHOUTOUT RESULTS in a game

# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import requests

# headers are often used to gain access to an otherwise locked API
HEADERS = {
    'Origin':'https://www.nhl.com',
    'Referer':'https//www.nhl.com/player/nikita-kucherov-8476453',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

# define function to be us  ed
def get_data(url):
    response = requests.get(url, headers=HEADERS)
    while response.status_code != 200:
        response = requests.get(url)
    # explore the response in developers tools to find the proper arrangement of your json response
    headers = response.json()['dates'][0]['games'][0]['linescore']['shootoutInfo']
    data = response.json()['dates'][0]['games'][0]['linescore']['shootoutInfo']
    data = pd.DataFrame(data, columns=headers)
    return data

# define the url
url = 'https://statsapi.web.nhl.com/api/v1/schedule?startDate=2018-01-27&endDate=2018-02-16&expand=schedule.teams,schedule.linescore,schedule.broadcasts.all,schedule.ticket,schedule.game.content.media.epg,schedule.radioBroadcasts,schedule.metadata,schedule.game.seriesSummary,seriesSummary.series&leaderCategories=&leaderGameTypes=R&site=en_nhlCA&teamId=14&gameType=&timecode=='
#url = api.football-data.org

# get the pandas data frame
data = get_data(url)

# print rows of information with column names
# to only take the first five rows of a frame, use print(data.head(5))
print(data.head())

data.to_csv('shootout_result.csv', index=False)