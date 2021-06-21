from GoogleNews import GoogleNews


def newsList(startDate, endDate, stock_ticker):
    news = []
    googlenews = GoogleNews(start=startDate, end=endDate)
    googlenews.search(stock_ticker)
    result = googlenews.result()
    for i in result:
        news.append("Author: "+ i['media'] + '\n' + 'Title: '+ i['title'] + '\n' + 'Link: '+ i['link'] + '\n')
    return news