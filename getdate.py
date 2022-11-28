import arrow
from htmldate import find_date
from datetime import datetime
import torch

print(11)
when = find_date('https://github.com/dependabot')
updated = datetime.strptime(when,'%Y-%m-%d')
hu = arrow.get(updated)
print('Last updated:'+hu.humanize())
