# scrapperEOL
Simple scrapper to get information about fish species from a csv of lakes and rivers from New York State

Code divides into three main functions:
1. find_links(): This function gets all fish species from a csv file and tries to fetch a link to a page about it on eol.org and save it to a txt file with the appropriate name.
2. get_attr(): This function reads a file with links and tries to get specific attributes from the data page (fragments of links to particular attributes are in the txt file) and returns an array of fish with attributes.
3. attr_to_n4j(): This function converts an array of attributes to create queries for Neo4J and saves the queries to a text file.
