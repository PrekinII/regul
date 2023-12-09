from pprint import pprint

import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:  # Читаем адресную книгу в формате CSV в список contacts_list:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

new_contacts = []

contacts_dict = {}


def contacts_spl(contacts, contacts_dict):
    patt = (
        r"^(\w*)(,?)(\s?)(\w*)(,?)(\s?)([\w\s?]*)(,?)(,?)(,?)([\w\s?]*)"
        r"(,?)([\w\s\–]*)(,?)((\+7\s?|8)?([(\s]?)(\d{3})"
        r"(\)?)([-\s]*)(\d{3})([-\s]*)(\d{2})([-\s]*)"
        r"(\d{2})(\s?)(\(?)([\w\.]*)(\s?)(\d*)(\)?))?(,?)([\w@\.]*)(,?)"
    )

    sub = r'\1,\4,\7,\11,\13,+7(\18)\21-\23-\25\26\28\30,\33'
    sub_name = r'\1 \4'
    res = (re.sub(patt, sub, contacts)).split(',')

    key_name = re.sub(patt, sub_name, contacts)
    if key_name in contacts_dict:
        z = list(zip(res, contacts_dict[key_name]))

        contacts_dict[key_name] = [a if b == '' else b for a, b in z]

    else:
        contacts_dict.setdefault(key_name, res)

    return contacts_dict


for i in contacts_list[1::]:
    contacts = ",".join(i)
    contacts_dict = contacts_spl(contacts, contacts_dict)

new_contacts.append(contacts_list[0])
for key, value in contacts_dict.items():
    new_contacts.append(value)
pprint(new_contacts)

# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts)
