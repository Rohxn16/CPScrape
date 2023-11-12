#Since codeforces already provides us with an API there is no need to build a scraper for this task
import requests as req

URL = 'https://codeforces.com/api/contest.list'

def fetch_contests(url=URL):
    res = req.get(url=url)

    if(res.status_code == 200):
        contests = res.json()['result']

        #now that we have the contests we need to filter out the upcoming ones
        upcoming = [contest for contest in contests if contest['phase'] == 'BEFORE']
        return upcoming
    
    else:
        return f'Error : {res.status_code}'
    

# if __name__ == '__main__':
#     upcoming = fetch_contests()
#     for contest in upcoming:
#         print(f"Contest ID: {contest['id']}, Name: {contest['name']}, Start Time: {contest['startTimeSeconds']}")