'''import re
res = re.finditer(r'[0-9]','hello World 76 34 90 23')

for i in res:
    print(i.group(),i.start())'''

'''import re

text='Java programming language'
res=re.sub('Java','Python',text)

print(res)'''

'''import re

res = re.split (r'[,:/0;]','dinesh,sanjay,tarak,jaswanth')

print(res)'''

'''import re

text = 'Sanjay is a good boy. he lives in kphb. Senjay loves everyone. Everyone loves Sanjey'

res = re.findall('S.nj.y',text)

print(res)'''

import re

#1. Validate Full Name
def validate_name(name):
    pattern = r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
    return bool(re.fullmatch(pattern, name))
#2. Validate Email
def validate_email(email):
    pattern = r'^[a-z0-9._]+@[a-z.-]+\.[a-z]{2,3}$'
    return bool(re.fullmatch(pattern, email))
#3.Validate Phonenumber
def validate_phone(phone):
    pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
    return bool(re.fullmatch(pattern, phone))
#4.Validate Password
def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@@$!%*?&]'
    return bool(re.fullmatch(pattern, password))
#5.Validate username
def validate_username(username):
    pattern = r'^[A-za-z0-9]{5,15}$'
    return bool(re.fullmatch(pattern, username))