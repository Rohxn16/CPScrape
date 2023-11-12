from scrape_cf import fetch_contests


def CFScrape():
    contests = fetch_contests()
    return contests