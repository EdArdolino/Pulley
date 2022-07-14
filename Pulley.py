from requests_html import HTMLSession
import time

##
# @Author: Ed Ardolino
# @Version 1.0
# @Creation Date: 6-29-2022
##

##
#
# Python webscraper to pull all GitHub repo chnages to your local machine 
#
##

# Function to start Pulley
def start():
    print("\n Choose which operation you would like to do:\n 1.) Pull existing repo's \n 2.) Add a repo")
    response = input("Please enter a number from the list above: ")
    while response not in {"1", "2"}:
        response = input("Invalid input, please enter a number from the list above")

