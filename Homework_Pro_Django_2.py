# Task 1

import re

def pattern_1(text):
    pattern = r"Rb+r"
    output = re.findall(pattern, text)
    return output

''' Revise '''

text ="Rbr_ttttt_Rbbbr_jklgljk_RbbbR_"
print(pattern_1(text))


# Task 2

def card_valid(card):
    if re.fullmatch(r"\d{4}-\d{4}-\d{4}-\d{4}", card):
        return True
    else:
        return False

''' Revise '''

card = "9999-9999-9999-9999"
print(card)
print (card_valid(card))
print (card_valid('9999-9999-9999-999a'))

# Task 3

def email_valid(email):
    if re.fullmatch(r"[0-9a-zA-Z][\w\-]+@[a-zA-Z]+\.[a-zA-Z]+", email):
        return True
    else:
        return False

''' Revise '''

email = "s_o_me-One@mailseRvice.domain"
print(email)
print(email_valid(email))
email = "some-o-ne@mailservice.domain"
print(email_valid(email))


# Task 4

def login_valid(login):
    if re.fullmatch(r"[0-9a-zA-Z]{2,10}", login):
        return True
    else:
        return False


''' Revise '''

login = "Python3"
print(login)
print(login_valid(login))
login = "Python3333333"
print(login_valid(login))

    





