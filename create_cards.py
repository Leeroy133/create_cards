import file_operations
import faker
import random
import os
from faker import Faker


LETTERS_MAPPING = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' '
}
SKILLS_LIST = [
        'Стремительный прыжок',
        'Электрический выстрел',
        'Ледяной удар',
        'Стремительный удар',
        'Кислотный взгляд',
        'Тайный побег',
        'Ледяной выстрел',
        'Огненный заряд'
]
RUNIC_SKILLS = []


def main():
    for i in range(len(SKILLS_LIST)):
        RUNIC_SKILLS.append(SKILLS_LIST[i])
        for s in range(len(list(LETTERS_MAPPING.keys()))):
            update_skill=RUNIC_SKILLS[i].replace(list(LETTERS_MAPPING.keys())[s], list(LETTERS_MAPPING.values())[s])
            RUNIC_SKILLS[i]=update_skill
    for number in range(10):
        pers_skills = random.sample(RUNIC_SKILLS, 3)
        fake = Faker("ru_RU")
        context = {
            'first_name': fake.first_name_male(),
            'last_name': fake.last_name_male(),
            'job': fake.job(),
            'town': fake.city(),
            'strength':random.randint(3,18),
            'agility':random.randint(3,18),
            'endurance':random.randint(3,18),
            'intelligence':random.randint(3,18),
            'luck': random.randint(3,18),
            'skill_1': pers_skills[0],
            'skill_2': pers_skills[1],
            'skill_3': pers_skills[2]
        }
        os.makedirs('cards', mode=0o777, exist_ok=False)
        file_operations.render_template('charsheet.svg', 'cards/processed_charsheet_{}.svg'.format(number), context)


if __name__ == '__main__':
    main()