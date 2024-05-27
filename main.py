import requests
from bs4 import BeautifulSoup
import time
import sys
from googlesearch import search

# Color codes
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[90m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Banner
def banner():
    print(f"{bcolors.OKBLUE}{bcolors.BOLD}  _ _             _ ")
    print(f"{bcolors.OKBLUE}{bcolors.BOLD} /\/\   ___  _ __ (_) |_ _ __ __ _| |_ ___  _ __")
    print(f"{bcolors.OKBLUE}{bcolors.BOLD}/    \ / _ \| '_ \| | __| '__/ _` | __/ _ \| '__|")
    print(f"{bcolors.OKBLUE}{bcolors.BOLD}/ /\/\ \ (_) | | | | | |_| | | (_| | || (_) | |")
    print(f"{bcolors.OKBLUE}{bcolors.BOLD}\/    \/\___/|_| |_|_|\__|_|  \__,_|\__\___/|_|")
    print(f"{bcolors.ENDC}\n")
    time.sleep(1)

# Google search function with loading animation
def google_search(query, num_results=10):
    print("Searching websites:")
    results = []
    for i, result in enumerate(search(query, num=10, stop=num_results, pause=2), start=1):
        results.append(result)
        sys.stdout.write('\r')
        sys.stdout.write(f"[{'=' * (i * 10 // num_results):<10}] {i * 10 // num_results * 10}%")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")
    return results

# Save results to file
def save_results_to_file(results, filename):
    with open(filename, 'w') as file:
        for result in results:
            file.write(result + '\n')

# Display search results
def display_results(results):
    for i, result in enumerate(results, start=1):
        print(f"{bcolors.OKGREEN}{i}. {result}{bcolors.ENDC}")

if __name__ == "__main__":
    while True:
        banner()
        print(f"{bcolors.OKCYAN}===========================")
        print(f"{bcolors.WARNING}site:website intext:content/name : Search Tags Or Comments")
        print(f"{bcolors.OKCYAN}===========================")
        print(f"{bcolors.WARNING}\"content\" filetype:pdf OR filetype:xlsx OR filetype:docx : Search Public Pfd Or Docs")
        print(f"{bcolors.OKCYAN}===========================")
        print(f"{bcolors.WARNING}\"content\" \"site/place\" : Search if victim mentioned their country, city or college etc")
        print(f"{bcolors.OKCYAN}===========================")
        print(f"{bcolors.WARNING}Filetype Operator: Search for specific file types (e.g., PDF, XLSX, DOCX)")          
        print(f"{bcolors.OKCYAN}===========================")
        print(f"{bcolors.WARNING}Intitle Operator: Search for specific words in the title")
        print(f"{bcolors.OKCYAN}===========================")
        print(f"{bcolors.WARNING}Inurl Operator: Search for specific words in the URL")
        print(f"{bcolors.OKCYAN}===========================")
        print(f"{bcolors.WARNING}Related Operator: Find sites related to a specified URL")
        print(f"{bcolors.OKCYAN}===========================")
        print(f"{bcolors.WARNING}Cache Operator: View cached version of a URL")
        print(f"{bcolors.OKCYAN}===========================")
        print(f"{bcolors.WARNING}Site Operator: Limit search to a specific website")
        print(f"{bcolors.OKCYAN}===========================")
        print(f"{bcolors.WARNING}Wildcards Operator: Use wildcards in search queries")
        print(f"{bcolors.OKCYAN}===========================")
        print(f"{bcolors.WARNING}Location Operator: Search for results based on location: city, country")
        print(f"{bcolors.OKCYAN}===========================")
        print(f"{bcolors.WARNING}Language Operator: Search for results in a specific language")
        print(f"{bcolors.OKCYAN}===========================")
        print(f"{bcolors.WARNING}Date Operator: Search for results within a specific time frame")
        print(f"{bcolors.OKCYAN}==========================={bcolors.ENDC}")
        print(f"{bcolors.WARNING}platform:@username : Social Media Operator")
        print(f"{bcolors.OKCYAN}==========================={bcolors.ENDC}")
        print(f"{bcolors.WARNING}IP:xx.xxx.xxx.xx : Ip address operator Search for websites hosted on a specific IP address")
        print(f"{bcolors.OKCYAN}==========================={bcolors.ENDC}")
        print(f"{bcolors.WARNING}Phone Number Operator : phone number : 9XXXXXXXX3 ")
        print(f"{bcolors.OKCYAN}==========================={bcolors.ENDC}")
        print(f"{bcolors.WARNING}username operator : username : name ")
        print(f"{bcolors.OKCYAN}==========================={bcolors.ENDC}")
        print(f"{bcolors.WARNING}inbody: keyword : Search for specific words in the body of the content")
        print(f"{bcolors.OKCYAN}==========================={bcolors.ENDC}")
        print(f"{bcolors.WARNING}link:example.com : Search for pages linking to a specific URL")
        print(f"{bcolors.OKCYAN}==========================={bcolors.ENDC}")
        print(f"{bcolors.WARNING}site:linkedin.com in: keyword : LinkedIn search within connections")
        print(f"{bcolors.OKCYAN}===========================\n{bcolors.ENDC}")
        
        
            
            
            
        query = input("Enter your search to dork: ")
        num_results = int(input("Enter the number of search results you want: "))
        filename = input("Enter the filename to save the results to: ")

        search_results = google_search(query, num_results)

        show_results = input("Do you want to see the search results? (Y/N): ").upper()
        if show_results == "Y":
            display_results(search_results)
        
        save_results = input("Do you want to save the results to a text file? (Y/N): ").upper()
        if save_results == "Y":
            save_results_to_file(search_results, filename)
            print(f"{bcolors.OKGREEN}Search results saved to {filename}{bcolors.ENDC}")
        
        restart = input("Do you want to restart the search? (Y/N): ").upper()
        if restart != "Y":
            break
