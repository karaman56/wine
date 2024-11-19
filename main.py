import pandas as pd
from collections import defaultdict
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

IMAGE_FOLDER = 'images/'

def main():
    excel_data_df = pd.read_excel(
        'wine.xlsx',
        sheet_name='wine_al',
        usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка', 'Акция']
    )
    data_list = excel_data_df.to_dict(orient='records')

    product_dict = defaultdict(list)

    for item in data_list:
        item = {key: (value if pd.notna(value) else '') for key, value in item.items()}
        item['Картинка'] = os.path.join(IMAGE_FOLDER, item['Картинка'])
        category = item['Категория']
        product_dict[category].append(item)

    current_year = datetime.now().year
    start_year = 1920
    years_difference = current_year - start_year
    ending_data = str(years_difference)
    ending = int(ending_data[-1])
    if ending == 0 or (5 <= ending <= 9):
        ending_year = 'лет'
    elif ending == 1:
        ending_year = 'год'
    else:
        ending_year = 'года'

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    rendered_page = template.render(
        text1="ПРОВЕРЕНО ВРЕМЕНЕМ",
        text2=(f"Уже {years_difference} {ending_year} с вами"),
        product_dict=product_dict
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()

