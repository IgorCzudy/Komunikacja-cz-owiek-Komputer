'''
    Pierwsze zadanie określam jako łatwę. Bibliotekę matplotlib wykorzystywałem już w
    sprawozdaniach z innych przedmiotów. Zadanie drugię jest już znaczeni trudniejsze.
    Musziałem wiele googlować i doczytywać dokumentację. Przymróżyłem oko na parę
    wizualnych niedociągnięć w tym zadaniu. Dwie funkcje służa do wczytywania danych.
    (read do zadania pierwszego, red to bar do zadania drugiego.) Następnie funkcja
    myplot tworzy wykres pierwszy, a myplot_2 wykres drugi.

Igor Czudy 145198
'''

import matplotlib.pyplot as plt
#plt.rcParams['text.usetex'] = True


def average(lst):
    return sum(lst) / len(lst)

def read(nazwa_pliku):

    plik=open(nazwa_pliku,"r")

    matrix=[]
    zm=0
    naglowki=[]
    for linia in plik:
        if zm==0:
            zm+=1
            naglowki.append(linia)
        else:
            matrix.append(list(map(float,linia.split(',')[1:])))
    matrix=matrix[1:]
    #print(matrix)
    OX=[]
    OY=[]
    for i in range(len(matrix)):
        OX.append(matrix[i][0])
        OY.append(average(matrix[i][1:]))
    plik.close()
    return OX,OY


def read_to_bar(nazwa_pliku):

    plik=open(nazwa_pliku,"r")

    matrix=[]
    zm=0
    naglowki=[]
    for linia in plik:
        if zm==0:
            zm+=1
            naglowki.append(linia)
        else:
            matrix.append(list(map(float,linia.split(',')[1:])))
    matrix=matrix[1:]
    #print(matrix)
    plik.close()
    return matrix[-1][1:]

def myplot(nazwy_plikow,colors):
    i = 0
    fig, ax1 = plt.subplots()

    for nazwa in nazwy_plikow:
        X, Y = read(nazwa)

        ax1.plot(X, Y, color=colors[i], label=nazwa)
        ax1.tick_params(axis='y', labelcolor=colors[i])
        i += 1

    ax1.set_ylabel("Odsetek wygranych gier")
    ax1.set_xlabel("Rozegranych gier")
    plt.legend()
    plt.savefig('myplot.pdf')
    plt.close()

def myplot_2(nazwy_plikow,colors):
    markers=['o', 'v', '^', '<', '>', '8', 's', 'p']
    i = 0
    fig, (ax1, ax2)= plt.subplots(1,2)

    for nazwa in nazwy_plikow:
        X, Y = read(nazwa)

        ax1.plot([x / 1000 for x in X], [y * 100 for y in Y], markers[i],color=colors[i], label=nazwa, ls='-', ms=7,markevery=25)
        ax1.tick_params(axis='y', labelcolor=colors[i])
        i += 1
    ax1.legend(nazwy_plikow)
    ax1.set_ylabel("Odsetek wygranych gier [%]")
    # ax1.set_xlabel(r'Rozegranych gier ( \times 1000)')
    ax1.set_xlabel('Rozegranych gier (X 1000)')
    ax1.set_title('Pokolenie')
    plt.legend()

    ax2.boxplot([read_to_bar(nazwa) for nazwa in nazwy_plikow], notch=True, showmeans=True)
    plt.savefig('myplot_2.pdf')

def main():
    nazwy_plikow=["1coev.csv","1coevrs.csv","1evolrs.csv","2coev.csv","2coevrs.csv"]
    colors=["red","blue","green","orange","black"]
    myplot(nazwy_plikow,colors)
    myplot_2(nazwy_plikow,colors)


if __name__ == '__main__':
    main()