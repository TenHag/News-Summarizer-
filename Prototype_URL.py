#GETTING Articles

import requests
import newspaper
from Summarize_Function import summarize

def get_articles(query):
    url = 'https://newsapi.org/v2/everything'
    params = {'q': query, 'sortBy': 'relevancy', 'apiKey': '7189a40a8cc3490993d2073174f15610', 'pageSize': 5}
    response = requests.get(url, params=params)
    content = response.json()
    articles = content['articles']
    all_articles = []
    for article in articles:
        article_title = article['title']
        article_url = article['url']
        article_text = article.get('description', '')
        
        try:
            article_obj = newspaper.Article(article_url)
            article_obj.download()
            article_obj.parse()
            article_text = article_obj.text
        except Exception as e:
            print(f"Error: {e}")
        
        article_summary= summarize(article_text)
        all_articles.append({'title': article_title, 'text': article_summary, 'url': article_url})
    return all_articles
