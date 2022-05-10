import requests
from bs4 import BeautifulSoup
import numpy as np
import re
import os
import cssutils


def articles():
    list_links = []
    list_titles = []
    # url definition
    url = "https://www.dawn.com/business"

    # Request
    r1 = requests.get(url)
    r1.status_code

    # We'll save in coverpage the cover page content
    coverpage = r1.content

    # Soup creation
    soup1 = BeautifulSoup(coverpage, 'html.parser')

    # News identification
    coverpage_news = soup1.find_all('article', class_='story')
    len(coverpage_news)

    # url definition
    url_bbc = "https://www.bbc.com/news/business"

    # Request
    r1_bbc = requests.get(url_bbc)
    r1_bbc.status_code

    # We'll save in coverpage the cover page content
    coverpage_bbc = r1_bbc.content

    # Soup creation
    soup1_bbc = BeautifulSoup(coverpage_bbc, 'html.parser')

    # News identification
    coverpage_news_bbc = soup1_bbc.find_all('div', { 'class': 'gel-layout' })

    # print(coverpage_news_bbc)

     # url definition
    url_daily_pk = "https://en.dailypakistan.com.pk/business"

    # Request
    r1_daily_pk = requests.get(url_daily_pk)
    r1_daily_pk.status_code

    # We'll save in coverpage the cover page content
    coverpage_daily_pk = r1_daily_pk.content

    # Soup creation
    soup1_daily_pk = BeautifulSoup(coverpage_daily_pk, 'html.parser')

    # News identification
    coverpage_news_daily_pk = soup1_daily_pk.find_all('div', { 'class': 'tt-post' })
    # print(coverpage_daily_pk)

    url_cnn = "https://edition.cnn.com/business"

    # Request
    r1_cnn = requests.get(url_cnn)
    r1_cnn.status_code

    # We'll save in coverpage the cover page content
    coverpage_cnn = r1_cnn.content

    # Soup creation
    soup1_cnn = BeautifulSoup(coverpage_cnn, 'html.parser')

    # News identification
    coverpage_news_cnn = soup1_cnn.find_all('article', { 'class': 'cd' })
    # print(coverpage_news_cnn)
    number_of_articles = 20
    
    # print('hello',coverpage_news_bbc)

    
    # for i in range(10):

    #     bbc_news_heading = soup1_bbc.find('a', { 'class': 'gs-c-promo-heading' }).get_text()
    #     print(bbc_news_heading)
    #     list_titles.append(bbc_news_heading)
    #     for img in coverpage_news_bbc:
    #         print(img['src'])
    #         list_links.append(img['src'])

    

    news_contents = []
    
    final_article = []
    image = []
    # hello = []
    for n in np.arange(0, number_of_articles):
            
        # Getting the link of the article
        link = coverpage_news[n].find('a')['href']
        # link_bbc_news = coverpage_news_bbc[n].find_all('h3')
        # for link in link_bbc_news:
        #     print(link.text)
        # list_links.append(link)
        image = coverpage_news[n].find_all('img')
        for img in image:
            # print(img['src'])
            list_links.append(img['src'])
        # image.append(img)
        # Getting the title
        title = coverpage_news[n].find('a').get_text()
        list_titles.append(title)
        a = coverpage_news_daily_pk[n].find_all('div', {'class':'img-responsive'})
        for i in a:
            style = cssutils.parseStyle(i['style'])
            url = style['background-image']
            url = url.replace('url(','').replace(')', '')
            list_links.append(url)
            # print(url)
        # print(a)

        b = coverpage_news_daily_pk[n].find('a', {'class':'tt-post-title'})
        list_titles.append(b.get_text())
        # print(b.get_text())
        
        # c = coverpage_news_cnn[n].find_all('img', {'class':'media__image'})
        # print((c))
        # for i in c:
        #     # print(i['src'])
        #     list_links.append(i['src'])
        # d = coverpage_news_cnn[n].find_all('span', {'class':'cd__headline-text'})
        # # print(d)
        # for i in d:
        #     # print(i.text)
        #     list_titles.append(i.text)
        
        # print(link_bbc_news)
        # link_bbc_news_images = coverpage_news_bbc[n].find('img')
        # print(link_bbc_news_images)
        # for img in link_bbc_news_images:
        #     print(img['src'])
            # list_links.append(img['src'])

        # list_titles.append(link_bbc_news)
        
        # para = coverpage_news[n].find('div', _class='story__excerpt').get_text()
        # hello.append(para)
        # Reading the content (it is divided in paragraphs)
        
    #     article = requests.get(link)
    #     print(article)
    #     article_content = article.content
    #     # print(article_content)
    #     soup_article = BeautifulSoup(article_content, 'html.parser')
    #     body = soup_article.find_all('story__content')
        
    #     print('hello',body)
    #     # Unifying the paragraphs
    #     list_paragraphs = []
    #     for p in np.arange(0, len(body)):
    #         paragraph = body[p].get_text()
    #         list_paragraphs.append(paragraph)
            
    #         final_article = " ".join(list_paragraphs)    
    #     # Removing special characters
    #     final_article = re.sub("[^a-zA-Z]", "", final_article)
            
    #     news_contents.append(final_article)
    # print(news_contents)
    # print(list_links)
    # print(list_titles)
    # print(hello)
    # importing modules
    # for img in image:
    #     if img.has_attr('src'):
    #         print(img['src'])
    # f = open(os.path.join(str(settings.MEDIA_ROOT) , "artices.txt"), "w+")
    # f.write("Articles")
    # f.write("\n")
    # f.write("\n")
    # for i in range(number_of_articles):
    #     f.write(str(i+1)+'. ')
    #     f.write(list_links[i])
    #     f.write("\n")
    #     f.write(list_titles[i])
    #     f.write("\n")
    # f.close()
    print(len(list_links), len(list_titles))
    # print(list_links)
    final_list = []
    for i in range(len(list_links)):
        final_list.append({
            'links':list_links[i], 
            'titles':list_titles[i]
            })
    # print(final_list)
    return final_list
    
    # # initializing variables with values
    # fileName = 'articles.pdf'
    # documentTitle = 'Articles'
    # title = 'Technology'
    # subTitle = 'The largest thing now!!'
    # textLines = [
    #     'Technology makes us aware of',
    #     'the world around us.',
    # ]
    # # image = 'image.jpg'
    
    # # creating a pdf object
    # pdf = canvas.Canvas(fileName)
    
    # # setting the title of the document
    # pdf.setTitle(documentTitle)
    
    # # registering a external font in python
    # # pdfmetrics.registerFont(
    # #     TTFont('abc', 'SakBunderan.ttf')
    # # )
    
    # # creating the title by setting it's font
    # # and putting it on the canvas
    # # pdf.setFont('abc', 36)
    # # pdf.drawCentredString(300, 770, title)
    
    # # # creating the subtitle by setting it's font,
    # # # colour and putting it on the canvas
    # # pdf.setFillColorRGB(0, 0, 255)
    # # pdf.setFont("Courier-Bold", 24)
    # # pdf.drawCentredString(290, 720, subTitle)
    
    # # drawing a line
    # # pdf.line(30, 710, 550, 710)
    
    # # creating a multiline text using
    # # textline and for loop
    # text = pdf.beginText(40, 680)
    # text.setFont("Courier", 18)
    # text.setFillColor(colors.red)
    # for i in range(number_of_articles):
    #     text.textLine(list_links[i])
    #     text.textLine(list_titles[i])
    # pdf.drawText(text)
    
    # # drawing a image at the
    # # specified (x.y) position
    # # pdf.drawInlineImage(image, 130, 400)
    
    # # saving the pdf
    # pdf.showPage()
    # pdf.save()