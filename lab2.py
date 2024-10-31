import pandas
import xml.etree.ElementTree as ET


#------------------------------------------------EX-1
def cnt_more30():
    print('Задание 1')
    cnt = 0

    books_data = pandas.read_csv('books.csv', encoding='windows-1251', sep=';')

    for i in books_data.iloc[:, 1]:
        if len(i) > 30:
            cnt += 1
    print(cnt, '\n')


#------------------------------------------------EX-2
def looking_for_book():
    print('Задание 2')
    green, red = "\033[92m", "\033[91m"
    end, bold = "\033[0m", "\033[1m"

    books_data = pandas.read_csv('books.csv', encoding='windows-1251', sep=';')

    author_name = input('Введите автора: ')
    filtered_books = books_data[books_data['Автор'].str.contains(author_name, case=False, na=False)]
    allowed_years = [2014, 2016, 2017]

    if (not filtered_books.empty) and author_name:
        print('\nПо вашему запросу нашлось:')
        for _, row in filtered_books.iterrows():
            title = row['Название']

            arrival_date = pandas.to_datetime(row['Дата поступления'], format='%d.%m.%Y %H:%M')
            year = arrival_date.year

            if year in allowed_years:
                print(f'{bold}{title}{end} (поступление {year} — книгу взять {green}можно{end})')
            else:
                print(f'{title} (поступление {year} — книгу взять {red}нельзя{end})')
        print('')
    else:
        print('Не нашлось ни одной книги по этому автору\n')


#------------------------------------------------EX-3
def bibliografic_links():
    print('Задание 3')
    books_data = pandas.read_csv('books.csv', encoding='windows-1251', sep=';')

    bibliographic_links = []
    sample_books = books_data.sample(n=20, random_state=1)

    for _, row in sample_books.iterrows():
        author = row['Автор']
        title = row['Название']
        arrival_date = pandas.to_datetime(row['Дата поступления'], format='%d.%m.%Y %H:%M')
        year = arrival_date.year
        reference = f"{author}. {title} - {year}"
        bibliographic_links.append(reference)

    with open('bibliographic_links.txt', 'w', encoding='utf-8') as f:
        for i, ref in enumerate(bibliographic_links, start=1):
            f.write(f"{i}. {ref}\n")
    print("Список библиографических ссылок сохранён в 'bibliographic_links.txt'\n")


#------------------------------------------------EX-4
def ex4_xml():
    print('Задание 4')
    tree = ET.parse('currency.xml')
    root = tree.getroot()
    Name = []

    for cur in root.findall('Valute'):
        nominal = int(cur.find('Nominal').text)
        if nominal == 1:
            nm = cur.find('Name').text
            Name.append(nm)
    print('Список валют с номиналом 1:')
    print(Name)


if __name__ == "__main__" :
    cnt_more30()
    looking_for_book()
    bibliografic_links()
    ex4_xml()
