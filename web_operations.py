import requests
import pdfkit
import random
from bs4 import BeautifulSoup


def collect_data():

    #? Fetch a webpage
    response = requests.get(input("Enter url: "))

    #? get HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    #? print all links on the page
    for link in soup.find_all("a"):
        print(link.get("href"))


def create_pdf():
    n = random.randint(1, 99)
    url = input("Enter url: ")

    #? Output PDF file
    pdf_file = f"website_output {n}.pdf"

    #? HTML to PDF
    try:
        pdfkit.from_url(url, pdf_file)
        print(f"Successfully converted {url} to {pdf_file}")
    except Exception as e:
        print(f"Error occurred: {e}")


def select_choice():
    print("1. Display HTML contents \n2. Convert HTML to PDF")
    user_choice = input("_____________\nSelect one: ")

    if user_choice == "1":
        collect_data()
    elif user_choice == "2":
        create_pdf()
    else:
        print("Invalid input")
        select_choice()


select_choice()
