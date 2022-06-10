from bs4 import BeautifulSoup

# import lxml

WEBSITE_PATH = "./website.html"

with open(WEBSITE_PATH, "r", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# soup = BeautifulSoup(contents, "lxml") # when html.parser doesn't work

# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)   # first anchor tag found
# all_anchor_tags = soup.find_all(name="a")  # all anchor tags
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)
