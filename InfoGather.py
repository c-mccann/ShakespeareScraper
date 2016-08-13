from bs4 import BeautifulSoup
import requests
import re
import collections
import ShakespeareScraper

home_page_request = requests.get("http://shakespeare.mit.edu/")
home_page_data = home_page_request.text
home_page_soup = BeautifulSoup(home_page_data, "lxml")

# print(soup.prettify())

home_page_a_tags = home_page_soup.find_all('a')



for link_tags_on_home_page in home_page_a_tags:

    print("Tag:    " + str(link_tags_on_home_page))
    if re.match('<a href="', str(link_tags_on_home_page)):
        link_on_home_page = str(link_tags_on_home_page).split('"')[1]
        print("link:    " + link_on_home_page + "\n")

        if re.match("http", link_on_home_page):
            print("Absolute\n")
        else:
            works_request = requests.get("http://shakespeare.mit.edu/" + link_on_home_page)
            works_data = works_request.text
            works_soup = BeautifulSoup(works_data, "lxml")
            works_a_tags = works_soup.find_all('a')
            # print(newSoup.prettify())

            for link_tags_to_work in works_a_tags:

                # print("Line 4:  " + line4AsStr)
                link_to_work = str(link_tags_to_work).split('"')[1]
                print("Tag to work:         " + str(link_tags_to_work))
                print("link to work:        " + link_to_work)

                if link_to_work.__eq__("full.html"):
                    minus_index_sub = link_on_home_page[:-10]
                    print("Test:    http://shakespeare.mit.edu/" + minus_index_sub + link_to_work)
                    ShakespeareScraper.scrape_play("http://shakespeare.mit.edu/" + minus_index_sub + link_to_work)
                    # individualWorkRequest = requests.get("http://shakespeare.mit.edu/"+minusIndexSub+linkToWork)
                    # individualWorkData = individualWorkRequest.text
                    # individualWorkSoup = BeautifulSoup(individualWorkData,"lxml")
                    # for line in individualWorkSoup:
                    #     print("Unknown:     " + str(line))


