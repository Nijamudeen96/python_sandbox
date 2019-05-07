# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

import datetime
import time

#After pip install
from camelcase import CamelCase

today = datetime.date.today()
timestamp = time.time()

c = CamelCase()
print(c.hump('hello there world'))

print(today)
print(timestamp)

#Own module
from validator import validate_email


email = 'test@test.com'
print('email: '+ str(validate_email(email)))
