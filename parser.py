from bs4 import BeautifulSoup
from requests import get


URL = 'https://nn.hh.ru/resume/c1e0653900074b39780039ed1f7a4832516453'


def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    return get(url, headers=headers).text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    employment = soup.find('div', {'class': 'resume-block-item-gap'}).findAll('p')[0].text
    schedule = soup.find('div', {'class': 'resume-block-item-gap'}).findAll('p')[1].text
    salary = f"Желаемая зарплата: {soup.find('span', {'class': 'resume-block__salary resume-block__title-text_salary'}).text}"
    list_key_skills = soup.find('div', {'id': 'key-skills'}).find_all_next('span',
                                                                           'bloko-tag__section bloko-tag__section_text')
    key_skills = 'Ключевые навыки:'
    for skill in list_key_skills:
        if list_key_skills.index(skill) == 0:
            key_skills += f' {skill.text}'
        else:
            key_skills += f', {skill.text}'
    return [employment, schedule, salary, key_skills]


def write_to_file(file_name, *args):
    with open(f'{file_name}.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(*args))


def main():
    html = get_html(URL)
    write_to_file('info', get_data(html))


if __name__ == '__main__':
    main()
