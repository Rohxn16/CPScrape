import requests as req
from datetime import datetime,timezone
import pytz

def validDate(date):
    # We gotta compare the starting date of the 
    utc = pytz.utc
    event_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S %Z").replace(tzinfo=utc)
    current_utc_time = datetime.utcnow().replace(tzinfo=utc)
    if event_date > current_utc_time:
        return True
    else:
        return False

URL = 'https://kontests.net/api/v1/code_chef'
def fetchUpcomingContests():
    
    res = req.get(url=URL)
    contests = res.json();
    
    # Now acc to my observation there are some invalid data here as well, so we gotta compare them by the date and filter out the unsitable ones
    validContests = []
    for contest in contests:
        if(validDate(contest['start_time'])):
            validContests.append([contest['name'],contest['start_time'],contest['end_time'],contest['duration']])
    
    return validContests
fetchUpcomingContests()
