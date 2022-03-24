import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math

def cut():
# test 1-5

    image = cv.imread('test1.jpg')
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

    ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY|cv.THRESH_OTSU)

    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


    cv.drawContours(image, contours, -1, (0, 255, 0), 3)
    cv.imshow('wycinek_2', cv.resize(image, (300, 600)))

    cv.waitKey(0)
    cv.destroyAllWindows()

    card = sorted(contours, key=cv.contourArea,reverse=True)

    x,y,w,h = cv.boundingRect(card[0])

    image=image[y:y+math.floor(h/5),x:x+math.floor(w/5)]

    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret_2, thresh_2 = cv.threshold(gray, 0, 255, cv.THRESH_BINARY|cv.THRESH_OTSU)
    contours_2, hierarchy_2 = cv.findContours(thresh_2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


    card_2 = sorted(contours_2, key=cv.contourArea, reverse=True)
    x, y, w, h = cv.boundingRect(card_2[1])


    #cv.drawContours(image[y:y + h, x:x + w], [card_2[1]], -1, (0, 255, 0), 3)
    x_2, y_2, w_2, h_2 = cv.boundingRect(card_2[2])
    #cv.drawContours(image[y_2:y_2 + h_2, x_2:x_2 + w_2], [card_2[2]], -1, (0, 255, 0), 3)

    wycinek = cv.resize(image[y:y + h, x:x + w], (140, 200), 0, 0)
    #cv.imshow('wycinek', wycinek)

    wycinek_2 = cv.resize(image[y_2:y_2 + h_2, x_2:x_2 + w_2], (140, 200), 0, 0)
    cv.imshow('wycinek_2', cv.subtract(255, wycinek))
    cv.imshow('serce',cv.subtract(255, wycinek_2))

    cv.waitKey(0)
    cv.destroyAllWindows()

    return cv.subtract(255, wycinek_2),cv.subtract(255, wycinek)

def to_bin(im):
    gray = cv.cvtColor(im,cv.COLOR_BGR2GRAY)

    ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY|cv.THRESH_OTSU)
    return cv.resize(thresh, (140, 200), 0, 0)

def main():

    slownik = {'pik.jpg':0,'serce.jpg':0,'trefl.jpg':0,'karo.jpg':0}
    kolor, numer =list(map(to_bin, cut()))
    for i in slownik:
        k = to_bin(cv.imread(i))
        n_white_pix = np.sum((k + kolor) == 255)
        cv.imshow('serce', k + kolor)
        cv.waitKey(0)
        cv.destroyAllWindows()
        slownik[i]=n_white_pix
    print(slownik)
    print(max(slownik, key=slownik.get))


    slownik_2 = {'_K.jpg':0,'_J.jpg':0,'_D.jpg':0,'_2.jpg':0,'_3.jpg':0,'_4.jpg':0,'_5.jpg':0,'_6.jpg':0,'_7.jpg':0,'_8.jpg':0,'_9.jpg':0,'_10.jpg':0,'_A.jpg':0}

    for i in slownik_2:
        k = to_bin(cv.imread(i))
        n_white_pix = np.sum((k + numer) == 255)
        cv.imshow('serce', k + numer)
        cv.waitKey(0)
        cv.destroyAllWindows()
        slownik_2[i]=n_white_pix
    print(slownik_2)
    print(max(slownik_2, key=slownik_2.get))

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
