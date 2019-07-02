# Systematically search for hits on Google

I had to do a systematic literature review, but did not wish to manually work my way through all google pages, opening each link by hand. So I wrote a program for that. You still have to close it though, but saves at least 50% of clicking. It's very simple and only works through the command line, you also need to use python. This is a tool, not a program.

## Quick overview of functionalitites, menu has 5 options:
- clean: CAREFUL, this cleans the text files containing the data, so you need to start over if you do this. Run this command first time to create initial files.
- search: You can enter some terms, Google will return the 50 highest links (you can change the number property of the SimpleScraper when initiating to edit this). Beware, Google is not keen on you scraping it, so don't send them too many requests at once. This function just appends to the files for eternity, so remember to run clean when starting a new research.
- unique: This action removes all duplicate url links you found by searching.
- analyze: Each link in the unique_data text file is opened in your browser, it then prompts you for a couple of important criteria which are: source ('What is the source of this?'), authority ('Is the source reputable?'), method ('Is the method well defined?'), objectivity ('Is it an objective article?'), date ('Enter year'), novelty ('Does it contain a novel element?'), tier ('Enter which tier it belongs to, 1st, 2nd, 3rd'), notes ('In case you have any free additions). The progress is automatically saved after each entry. Don't make mistakes or you have to rectify them in the textfile.
This data is stored in the systematic literature review text file with a semicolon between them. You can import that in your excel or R later.
- exit: Closes the program, you can alternatively of course throwing your computer out of the window will do the trick as well (or angrily F4ing)

### Additional note: watch the lowercase letters, using capitals in commands will probably not work.

## Dependencies to install

- Beautifulsoup4 or bs4 (same thing)
- requests

Rest already comes with Python installed.