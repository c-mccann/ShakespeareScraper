from lxml import html
from bs4 import BeautifulSoup
import requests
import re
import collections


def scrape_play(playurl):
    r = requests.get(playurl)
    data = r.text
    soup = BeautifulSoup(data,"lxml")

    a_tags = soup.find_all('a')

    print("a_tags:  " + str(a_tags))
    print(soup.get_text())

    script_list = []
    current_character = ""

    p = re.compile('<a name="\d')


    print(str(a_tags[1]).split('>')[1][:-3])

    f = open("Shakespeare's Plays/"+str(a_tags[1]).split('>')[1][:-3] + ".txt", 'w')
    f.write(soup.get_text())
    f.close()




    # for line in a_tags:
    #
    #     line_as_string = str(line)
    #     print("SS line as string:   " + line_as_string)
    #
    #     if line_as_string.__contains__("speech"):
    #
    #         script_list.append("\n\n")
    #
    #         # if not current_character.__eq__(line_as_string.split('>')[2][:-3]):
    #         #     script_list.append('\n')
    #
    #         current_character = line_as_string.split('>')[2][:-3]
    #
    #
    #         script_list.append(current_character)
    #         # script_list.append('\n')
    #         # print(character)
    #
    #     if re.match(p,line_as_string):
    #         dialogue = line_as_string.split('>')[1][:-3]
    #
    #         script_list.append(dialogue + " ")
    #
    #     else:
    #         print("TESTER:      " +line_as_string.split('>')[1][:-3])
    #         script_list.append(line_as_string.split('>')[1][:-3])
    #         script_list.append('\n')
    #
    # # print(characterList)
    # # print(dialogueDict)
    # print(script_list)
    #
    # print("FILE IO:     " + script_list[1]+".txt")
    # f = open("Shakespeare's Plays/"+script_list[2] + ".txt", 'w')
    #
    # for line in script_list:
    #     f.write(line)
    #
    # f.close()
    #
    #
    # # list = firstPTag.text.split("<br>")
    # # print(list)
    #
    #
    #
    # # for line in firstPTag:
    # #     print(line)
    # #     print(line.text)
    # #     list = p.split(line.text)
    # #     print(list)
    # #     print('\n')
    #






    return



