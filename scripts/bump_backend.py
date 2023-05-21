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

logging.info('Yay, bumped! ✨')
