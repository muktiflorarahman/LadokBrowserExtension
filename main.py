from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.student.ladok.se/student/app/studentwebb/examinationstillfallen/oppna-for-anmalan').text
print(html_text)
# soup = BeautifulSoup(html_text, 'lxml')
