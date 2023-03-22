person_age = int (input ('\tHaiiii  :) \nHow old are you ? ' ))

if person_age < 2:
    print('"you are a baby"')
elif person_age >=2 and person_age < 4:
    print('"you are a toddler"')
elif person_age >=4 and person_age < 13:
    print('"you are a kid"')
elif person_age >=13 and person_age < 20:
    print('"you are a teenager"')
elif person_age >=20 and person_age < 65:
    print('"you are an adult"')
else:
    print('"you are an elder"')