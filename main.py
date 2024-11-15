
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

from datetime import datetime

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
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()


