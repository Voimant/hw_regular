import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",", )
    contacts_list = list(rows)


regular_phone = r"(\+7|8)\s*[\(]*(\d{3})[\)]*[\s*-]*(\d{3})[\s*-]*(\d{2})[\s*-]*(\d{2})[\s*-]*[\(]*([\w+\.]*)\s*([\d+]*)[\)]*"
subt = r'+7(\2)\3-\4-\5 \6\7'




if __name__ == "__main__":

    data_dict = []
    dict_1 = {}
    for i, c_list in enumerate(contacts_list):
        fio = ' '.join(c_list[0:3])
        list_fio = fio.split()
        if len(list_fio) < 3:
            list_fio.append("")
        for k in range(3):
            contacts_list[i][k] = list_fio[k]


    for list_1 in contacts_list:
        nf = ' '.join(list_1[0:2])
        value = (list_1[2::])
        if dict_1.get(nf,False) is False:
            dict_1[nf] = value
        else:
            for va in range(5):
                if dict_1[nf][va] == '':
                    dict_1[nf][va]  = value[va]



    for k,v in dict_1.items():
        x = k.split(' ',2)
        data_dict.append({
            'lastname': x[0],
            'first_name': x[1],
            'surname': v[0],
            'organization': v[1],
            'position': v[2],
            'phone': re.sub(regular_phone,subt,v[3]),
            'email': v[4],
            })


    with open("phonebook1.csv", "w",newline='') as f:
        datawriter = csv.writer(f, delimiter=';')
        for item in data_dict:
            datawriter.writerow([item['lastname'],item['first_name'],item['surname'],item['organization'],item['position'],item['phone'],item['email']])