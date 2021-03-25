import re
FILE = 'regex_sum_1201197.txt'

with open(FILE) as f:
    data = re.findall('[0-9]+', f.read())

print(sum( list(int(i) for i in data) ))


print( sum( [ int(i) for i in re.findall('[0-9]+',open('regex_sum_1201197.txt').read()) ] )  )
