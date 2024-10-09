import file_operations
import faker
import random
import os


os.makedirs('cards', mode=0o777, exist_ok=False)


from faker import Faker


skills_list = ['Стремительный прыжок', 
'Электрический выстрел', 
'Ледяной удар',
'Стремительный удар',
'Кислотный взгляд',
'Тайный побег',
'Ледяной выстрел',
'Огненный заряд']
runic_skills = []


for i in range(len(skills_list)):
    runic_skills.append(skills_list[i])
    update_skill=runic_skills[i].replace('а', 'а͠')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('б', 'б̋')
    runic_skills[i]=update_skill 
    update_skill=runic_skills[i].replace('в', 'в͒͠')
    runic_skills[i]=update_skill 
    update_skill=runic_skills[i].replace('г', 'г͒͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('д', 'д̋')
    runic_skills[i]=update_skill 
    update_skill=runic_skills[i].replace('е', 'е͠')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('ё', 'ё͒͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('ж', 'ж͒') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('з', 'з̋̋͠')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('и', 'и') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('й', 'й͒͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('к', 'к̋̋')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('л', 'л̋͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('м', 'м͒͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('н', 'н͒')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('о', 'о̋') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('п', 'п̋͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('р', 'р̋͠')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('с', 'с͒') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('т', 'т͒') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('у', 'у͒͠')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('ф', 'ф̋̋͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('х', 'х͒͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('ц', 'ц̋')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('ч', 'ч̋͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('ш', 'ш͒͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('щ', 'щ̋')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('ъ', 'ъ̋͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('ы', 'ы̋͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('ь', 'ь̋')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('э', 'э͒͠͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('ю', 'ю̋͠')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('я', 'я̋')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('А', 'А͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Б', 'Б̋') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('В', 'В͒͠')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Г', 'Г͒͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Д', 'Д̋') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Е', 'Е')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Ё', 'Ё͒͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Ж', 'Ж͒') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('З', 'З̋̋͠')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('И', 'И') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Й', 'Й͒͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('К', 'К̋̋')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Л', 'Л̋͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('М', 'М͒͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Н', 'Н͒')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('О', 'О̋') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('П', 'П̋͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Р', 'Р̋͠')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('С', 'С͒') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Т', 'Т͒') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('У', 'У͒͠')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Ф', 'Ф̋̋͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Х', 'Х͒͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Ц', 'Ц̋')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Ч', 'Ч̋͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Ш', 'Ш͒͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Щ', 'Щ̋')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Ъ', 'Ъ̋͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Ы', 'Ы̋͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Ь', 'Ь̋')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Э', 'Э͒͠͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Ю', 'Ю̋͠') 
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace('Я', 'Я̋')
    runic_skills[i]=update_skill
    update_skill=runic_skills[i].replace(' ', ' ')
    runic_skills[i]=update_skill


def main():
    for number in range(10):
        pers_skills = random.sample(runic_skills, 3)
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
        
        
        file_operations.render_template('charsheet.svg', 'cards/processed_charsheet_{}.svg'.format(number), context)


if __name__ == '__main__':
    main()        

