import sys
import logging
import requests

logging.basicConfig(level=logging.INFO)

assert len(sys.argv) == 2
post_endpoint = sys.argv[1]

try:
    request = requests.get(post_endpoint, timeout=2500)
except requests.exceptions.RequestException as e:
    logging.error(e)
    sys.exit(1)

assert request.status_code == 200

json = request.json()
posts_builder = ''

for post in json['results']:
    title, href = post['title'], post['href']
    posts_builder += f'🔹 <a href="{href}">{title}</a>\n'

posts_builder = posts_builder[:-1]

with open('README.template.md', mode='r', encoding='utf-8') as template_file, \
        open('README.md', mode='w', encoding='utf-8') as output_file:
    output_file.write(template_file.read().replace('{% posts %}', posts_builder))

logging.info('Yay, it worked! ✨')
