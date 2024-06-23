>Engeto: Project 1
>První projekt pro akademii od Engeta. Tento program je psán na základě zkušeností nabraných za 2 měsíce studia Python Akademie.

**Textový analyzátor s pomocí funkcí**
------------------------------------------

Popis zadání
Tento program slouží k analyzování textů, kde uživatel má na vyběr 1 ze tří možností.
- Vyžádá si od uživatele přihlašovací jméno a heslo.
- Kód verifikuje, zda je uživatel registrovaný a zda zadal správné heslo. 
- Pokud je uživatel registrovaný, pozdraví jej a umožní mu analyzovat texty. Pokud není, upozorni jej a ukonči program.
- Výběr textu: Umožňuje uživateli vybrat jeden ze tří předdefinovaných textů z proměnné TEXTS pomocí číselného vstupu.
- Kontroluje, zda zadané číslo odpovídá počtu dostupných textů, pokud vybere nevhodné- program jej upozorní a uživatel může znovu vybrat jeden z textů.
- Program úspěšně analyzuje vybraný text, identifikuje a počítá různé typy slov a číselné řetězce, a sčítá numerické hodnoty.

Pro vybraný text spočítá následující statistiky:
- Počet slov.
- Počet slov začínajících velkým písmenem.
- Počet slov psaných velkými písmeny.
- Počet slov psaných malými písmeny.
- Počet čísel (ne cifer).
- Sumu všech čísel (ne cifer) v textu.
  
Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Vypada takto:
```
username:bob
password:123
----------------------------------------
Welcome to the app, bob
We have 3 texts to be analyzed.
----------------------------------------
Enter a number btw. 1 and 3 to select: 1
----------------------------------------
There are 54 words in the selected text.
There are 12 titlecase words.
There are 1 uppercase words.
There are 38 lowercase words.
There are 3 numeric strings.
The sum of all the numbers 8510
----------------------------------------
LEN|  OCCURENCES  |NR.
----------------------------------------
  1|*             |1
  2|*********     |9
  3|******        |6
  4|***********   |11
  5|************  |12
  6|***           |3
  7|****          |4
  8|*****         |5
  9|*             |1
 10|*             |1
 11|*             |1
```
