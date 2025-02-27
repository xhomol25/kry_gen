import requests
import psycopg2

# připojení k databázi
conn = psycopg2.connect(database="databaze", user="uzivatel", password="heslo", host="server", port="5432")

# získání dat o úkolech
cur = conn.cursor()
cur.execute("SELECT id, nazev FROM ukoly")
rows = cur.fetchall()

# výpis dostupných úkolů
print("Dostupné úkoly:")
for row in rows:
    print(f"{row[0]}. {row[1]}")

# uživatel zvolí konkrétní úkol
vybrany_ukol = input("Vyberte úkol, který chcete řešit: ")

# odeslání požadavku na server
response = requests.get(f'http://example.com/tasks/{vybrany_ukol}')
task = response.json()

# výpis úkolu
print(f'Název úkolu: {task["name"]}')
print(f'Popis úkolu: {task["description"]}')

# zobrazení nápovědy
show_help = input('Chceš zobrazit nápovědu k úkolu? (ano/ne): ')
if show_help.lower() == 'ano':
    print(f'Nápověda k úkolu {task["name"]}: {task["help"]}')

# vyhodnocení správnosti výsledku
vysledek = input('Zadej výsledek: ')
if int(vysledek) == task["result"]:
    print('Správně!')
    # přidat další úkol do databáze
else:
    print('Špatně, zkus to znovu.')