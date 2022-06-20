import requests
import json

def getData():
    return requests.get("https://egzaminy.uke.gov.pl/netpar/exams.json?category=R&division_id=14&q=&page_limit=20&page=1")

def utworzHTML(data):
    if not len(data):
        return "Brak terminów dla służby amatorskiej"

    kolumny = list(data[0].keys())

    old = ['date_exam', 'place_exam', 'info', 'province_name',
    'examinations_count', 'max_examinations', 'category', 'online']

    naglowekWiersza="<tr>"
    for i in range(len(kolumny)):
        if 'date_exam' in kolumny[i]:
            naglowekWiersza+="<th>Data egzaminu</th>"
        elif 'place_exam' in kolumny[i]:
            naglowekWiersza+="<th>Miejsce egzaminu</th>"
        elif 'info' in kolumny[i]:
            naglowekWiersza+="<th>Adres</th>"
        elif 'examinations_count' in kolumny[i]:
            naglowekWiersza+="<th>Zapisani</th>"
        elif 'province_name' in kolumny[i]:
            naglowekWiersza+="<th>Województwo</th>"
        elif 'max_examinations' in kolumny[i]:
            naglowekWiersza+="<th>Wolne miejsca</th>"
        elif 'online' in kolumny[i]:
            naglowekWiersza+="<th>Online</th>"
        elif 'category' in kolumny[i]:
            naglowekWiersza+="<th>Kategoria</th>"


    naglowekWiersza+="</hr>"

    rekordy=""
    for i in range(len(data)):
        rekordy+="<tr>"
        for j in range(len(kolumny)):
            if kolumny[j] in old:
                naglowek=kolumny[j]
                rekordy+="<td>"+str(data[i][naglowek])+"</td>"
        rekordy+="</tr>"

    poczatek = '''<!DOCKTYPE html>
    <html lang="en" dir="ltr">
    <head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
    <table class=table table-bordered table-striped">
    '''

    koniec = """</table></body></html>"""

    return poczatek+naglowekWiersza+rekordy+koniec

def zapiszHTML(data):
    with open("egzaminy.html",'w') as f:
        f.write(str(data))

if __name__ == "__main__":
    query = getData()
    js = json.loads(query.text)
    data = js['exams']
    ht = utworzHTML(data)
    zapiszHTML(ht)
