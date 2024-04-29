Engeto: Project 1
První program na online python akademii od Engeta. Tento program je psán na základě zkušeností nabraných za 1 měsíc studia python Akademie. Psaní kódu trvalo 10 hodin.

Popis zadání
Tento program slouží k analyzování textů, kde uživatel má na vyběr 1 ze tří možností. Tyto texty jsou dostupné zde

Vyžádá si od uživatele přihlašovací jméno a heslo.
Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů v předem definovaném slovníku.
Pokud je uživatel registrovaný, pozdrav jej a umožni mu analyzovat texty. Pokud není, upozorni jej a ukonči program.
Program nechá uživatel vybrat mezi třemi texty, uloženými v proměnné TEXTS. Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí. Pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.
Pro vybraný text spočítá následující statistiky:
počet slov,
počet slov začínajících velkým písmenem,
počet slov psaných velkými písmeny,
počet slov psaných malými písmeny,
počet čísel (ne cifer),
sumu všech čísel (ne cifer) v textu.
Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:
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
