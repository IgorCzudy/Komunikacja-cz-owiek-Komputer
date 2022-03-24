# Komunikacja-czlowiek-Komputer
Zadania, które wykonywałem na przedmiot komunikacja człowiek komputer.
Skrypt wykresy.py trzorzy dwa wykresy przy pomocy biblioteki matplotlib.
Skrypt kolory.py tworzy różne gradienty kolorów. 
Skrypt rozpoznawanie_kart.py to prosty program do rozpoznawania kart napisany przy pomocy biblioteki openCV. Nie zawiera on żadnych algorytmów sztucznej inteligencji. Działa on następująco. Na początku znajdowane są kontury karty, następnie sama karta jest wycinana. Kolejno w odpowiednich proporcjach wycianany jest prawy górny róg karty zawierający znak i liczbę. Wycięty znak o odwróconych jest nakładany na próbki przygotowanych wcześniej wszystkich wycinków. Po nałożeniu na siebie wszystkich możliwości kart, jako wynik wybierane jest nałożenie z największą ilościa białych pikseli. 
