from bs4 import BeautifulSoup
from requests import get


URL = 'https://nn.hh.ru/resume/c1e0653900074b39780039ed1f7a4832516453'
BLOCKS = ['ключевые навыки', 'занятость', 'график работы', 'желаемая зарплата']

def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    return get(url, headers=headers).text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    employment = soup.find('div', {'class': 'resume-block-item-gap'}).findAll('p')[0].text
    schedule = soup.find('div', {'class': 'resume-block-item-gap'}).findAll('p')[1].text
    salary = soup.find('span', {'class': 'resume-block__salary resume-block__title-text_salary'}).text
    list_key_skills = soup.find('div', {'id': 'key-skills'}).find_all_next('span', 'bloko-tag__section bloko-tag__section_text')
    key_skills = ''
    for skill in list_key_skills:
        key_skills += f' {skill.text}'
    print(key_skills)
def main():
    html = get_html(URL)
    get_data(html)

if __name__ == '__main__':
    main()