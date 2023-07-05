from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()
response_text = response.text
# print(response_text)

soup = BeautifulSoup(response_text, "html.parser")
articles = soup.find_all(class_= "titleline")

article_texts = []
article_links = []

for article in articles:
    text = article.a.getText()
    article_texts.append(text)
    link = article.a["href"]
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvote)
find_max = max(article_upvote)
max_index = article_upvote.index(find_max)
print(article_texts[max_index],article_upvote[max_index])

# import lxml

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.a)
# all_anchor_tags = soup.find_all(name="a")

# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# # print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# # print(company_url)

# name = soup.select_one(selector="#name")
# # print(name)

# headings = soup.select(".heading")
# # print(headings)
