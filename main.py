import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
def newsContent():
    contentToReturn={};
    contentToReturn['newsItems']=[];
    for i in range(1, 8):
        url = f"https://www.ndtv.com/business/cryptocurrency/news/page-{i}";
        cont = requests.get(url);
        soup = BeautifulSoup(cont.text, 'lxml');
        newsItems = soup.find_all('div', class_="news_Itm");
        for eachItem in newsItems:
            itemToReturn = {};
            newsImage = eachItem.find('img');
            newsHeading = eachItem.find('h2');
            newsSource = eachItem.find(class_='posted-by');
            newsContent = eachItem.find('p', class_="newsCont");
            if newsImage is not None: itemToReturn['imageURL'] = newsImage['src'];
            if newsHeading is not None: itemToReturn['heading'] = newsHeading.text;
            if newsSource is not None: itemToReturn['source'] = newsSource.text.strip();
            if newsContent is not None: itemToReturn['description'] = newsContent.text;
            if(bool(itemToReturn)): contentToReturn['newsItems'].append(itemToReturn);
    return contentToReturn;
app = FastAPI()
@app.get('/')
def home():
    newsPage = newsContent()
    return newsPage;
