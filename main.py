from SimpleScraper import SimpleScraper


def main():
    ScrapyScrape = SimpleScraper(number=50)
    while True == True:
        user_action = input('clean, analyze, unique, export, exit or search? ')
        if user_action == 'clean':
            ScrapyScrape.clean_data()
        if user_action == 'search':
            ScrapyScrape.search()
        if user_action == 'exit' or user_action == 'quit':
            quit()
        if user_action == 'analyze' or user_action == 'analyse':
            ScrapyScrape.analyze()
        if user_action == 'unique':
            ScrapyScrape.determine_unique()
        if user_action == 'export':
            ScrapyScrape.export()

if __name__ == '__main__':
    main()