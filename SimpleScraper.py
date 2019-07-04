import re
import requests
import bs4
import webbrowser
import time
import csv


class SimpleScraper:
    def __init__(self, number=50):
        self.url = 'https://www.google.com/search?q='
        self.pages = int(round(int(number)/10))

    def search(self):
        term = input('enter the search terms ')
        i = 1

        for page in range(self.pages):
            search_url = self.update_term(term, page*10)
            response = requests.get(search_url)
            print('-----------')
            print(search_url)
            if response is not None:
                soup = bs4.BeautifulSoup(response.text, 'html.parser')
                print('-----------')
                for link in soup.find_all('a',href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
                    link = link.get('href')
                    link = re.sub('\/url\?q=', '', link)
                    link = re.sub(r'&sa\S+', '', link)
                    link = re.sub('http://www.google.com/\S+','',link)
                    if link.startswith('https://accounts.google'):
                        pass
                    elif link.startswith('https://www.youtube.com'):
                        pass
                    elif link is not '':
                        print(str(i) + ' ' + link)
                        i +=1
                        self.store_data(link)
        print('quick slowdown before google bans you')
        time.sleep(5)

    def update_term(self, term, page):
        updated_term = re.sub(' ','+',term)
        search_url = self.url + updated_term + '&start={0}'.format(page) + '&hl=en'
        return search_url

    def store_data(self,link):
        file = open('data.txt', 'a')
        file.write(link+'\n')
        file.close()

    def clean_data(self):
        file = open('data.txt','w')
        file.close()
        file = open('results_systematic_review.txt', 'w')
        file.close()

    def analyze(self):
        file = open('results_systematic_review.txt', 'r')
        j = len(file.readlines()) #retrieve number you are at now
        file.close()

        file = open('unique_data.txt','r')
        url_list = []
        for url in file.readlines():
            url_list.append(url)
        file.close()

        i = 1 #Test to check how far we are in the data list in case you wish to stop in between
        for url in url_list:
            if i <= j:
                i += 1
            else:
                print('You are at number ', i,'/',len(url_list), ' now')
                try:
                    webbrowser.open(url)

                    '''Quality guidelines as described by Garousi, Felderer, Mantyla
                    #https://arxiv.org/ftp/arxiv/papers/1707/1707.02553.pdf'''
                    source = input('Who is the author or organization? \n')
                    date = input('Enter year of article \n')
                    relevance = input('Is this relevant for your query? \n')
                    if relevance == 'yes':
                        authority = input('Is the source reputable? Does the author have any authority in this field? \n')
                        method = input('Is the aim of the article clear? Is a method well described? \n')
                        claims = input('Are claims made by the authors supported by sources? \n')
                        objectivity = input('Does the article discuss the topic objectively? \n')
                        novelty = input('Does this enrich your research? \n')
                        tier = input('Enter which tier it belongs to: white, 1st, 2nd, 3rd? \n')
                    else:
                        authority = ''
                        method = ''
                        claims = ''
                        objectivity = ''
                        novelty = ''
                        tier = ''
                    notes = input('What does it say? Why is this important to in/exclude? What elements are '
                                  'interesting to investigate when revisting this link? \n')

                    file = open('results_systematic_review.txt', 'a')
                    file.write(source+'; '+authority+'; '+method+'; '+objectivity+'; '
                               +claims+'; '+date+'; '+novelty+'; '+tier+'; '
                               +relevance+'; '+notes+'\n')
                    file.close()
                except:
                    file = open('results_systematic_review.txt', 'a')
                    file.write('Not a viable link to analyze\n')
                    file.close()
                i += 1
                j += 1

    def determine_unique(self):
        file = open('data.txt','r')
        url_list = []
        for url in file.readlines():
            url_list.append(url)
        print('initial length of url list is ',len(url_list))
        file.close()
        unique_urls = set(url_list)
        print('this is reduced to ',len(unique_urls))
        file = open('unique_data.txt','w')
        for url in unique_urls:
            file.write(url)
        file.close()

    def export(self):
        file = open('results_systematic_review.txt', 'r')
        csvfile = open('results_systematic_review.csv', 'w', newline='')
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['Source; authority; method; objectivity; claims; date; novelty; tier; relevance; notes'])
        for line in file:
            print(line)
            writer.writerow([line])
        print('written results to csv file')
        csvfile.close()
        file.close()