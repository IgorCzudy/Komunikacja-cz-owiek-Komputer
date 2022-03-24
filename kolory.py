#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division             # Division in Python 2.7

import math

import matplotlib
matplotlib.use('Agg')                       # So that we can render files without GUI
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

from matplotlib import colors

def plot_color_gradients(gradients, names):
    # For pretty latex fonts (commented out, because it does not work on some machines)
    #rc('text', usetex=True)
    #rc('font', family='serif', serif=['Times'], size=10)
    rc('legend', fontsize=10)

    column_width_pt = 400         # Show in latex using \the\linewidth
    pt_per_inch = 72
    size = column_width_pt / pt_per_inch

    fig, axes = plt.subplots(nrows=len(gradients), sharex=True, figsize=(size, 0.75 * size))
    fig.subplots_adjust(top=1.00, bottom=0.05, left=0.25, right=0.95)


    for ax, gradient, name in zip(axes, gradients, names):
        # Create image with two lines and draw gradient on it
        img = np.zeros((2, 1024, 3))
        for i, v in enumerate(np.linspace(0, 1, 1024)):
            img[:, i] = gradient(v)

        im = ax.imshow(img, aspect='auto')
        im.set_extent([0, 1, 0, 1])
        ax.yaxis.set_visible(False)

        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.25
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va='center', ha='left', fontsize=10)
    fig.savefig('my-gradients.pdf')

def hsv2rgb(h, s, v):
    if s==0:
        return (v, v, v)
    if s>0:
        h1=math.floor(h/60)
        f=(h/60)-h1
        p=v*(1-s)
        q=v*(1-(s*f))
        t=v*(1-(s*(1-f)))
        if h1==0:
            return(v,t,p)
        if h1==1:
            return(q,v,p)
        if h1==2:
            return(p,v,t)
        if h1==3:
            return(p,q,v)
        if h1==4:
            return(t,p,v)
        if h1==5:
            return(v,p,q)
def gradient_rgb_bw(v):
    #print(v)
    return (v, v, v)   #black 0,0,0 white 1,1,1

def fun(arg):
    l_2=np.linspace(0,1,1024)
    for i in range(len(l_2)):
        if arg==l_2[i]:
            return i

def gradient_rgb_gbr(v):    #  (0, 1-v,v) (v, 0, 1-v)
#green 0,1,0 blue 0,0,1 red 1,0,0   v from 0 to 1 /1024
    nr=fun(v)
    l = np.linspace(0,1,math.floor(1024/2))
    if nr<512:
        return (0, 1-l[nr],l[nr])
    else:
        return (l[nr%512], 0, 1-l[nr%512])

def gradient_rgb_gbr_full(v):
# green 0,1,0  cyan 0,1,1  blue 0,0,1  magenta 1,0,1  red 1,0,0    v from 0 to 1 /1024
    nr=fun(v)
    l = np.linspace(0,1,math.floor(1024/4))
    if nr<256:
        return (0, 1, l[nr%256])
    elif nr<512:
        return (0, 1-l[nr%256], 1)
    elif nr<768:
        return (l[nr%256], 0, 1)
    else:
        return (1, 0, 1-l[nr%256])



def gradient_rgb_wb_custom(v):
# white 1,1,1  magenta 1,0,1  blue 0,0,1    green 0,1,0fdas  cyan 0,1,1fds yellow 1,1,1   red 1,0,0  black0,0,0   v from 0 to 1 /1024
    nr=fun(v)
    l = np.linspace(0,1,math.floor(1024/7))
    if nr < 146:
        return (1, 1-l[nr % 146], 1)
    elif nr < 146*2:
        return (1-l[nr % 146], 0, 1)
    elif nr < 146*3:
        return (0, l[nr % 146], 1)
    elif nr <146*4:
        return (0, 1, 1-l[nr % 146])
    elif nr <146*5:
        return (l[nr % 146], 1, 0 )
    elif nr <146*6:
        return (1, 1-l[nr % 146], 0)
    else:
        return (1-l[nr % 146], 0, 0)

def gradient_hsv_bw(v):
    return hsv2rgb(0, 0, v)


def gradient_hsv_gbr(v):

    nr=fun(v)
    l2=np.linspace(90,359,1024)
    #print('nr',nr,'l2: ',l2)
    return hsv2rgb(l2[nr], 1 , 1)

def gradient_hsv_unknown(v):

    nr=fun(v)
    l2=np.linspace(0,90,1024)
    l2=l2[::-1]
    return hsv2rgb(l2[nr], 0.5 , 1)

def gradient_hsv_custom(v):

    nr=fun(v)
    l2=np.linspace(0,360,256)
    return hsv2rgb(l2[nr%256], 1 , 1)


if __name__ == '__main__':
    def toname(g):
        return g.__name__.replace('gradient_', '').replace('_', '-').upper()

    gradients = (gradient_rgb_bw, gradient_rgb_gbr, gradient_rgb_gbr_full, gradient_rgb_wb_custom,
                 gradient_hsv_bw, gradient_hsv_gbr, gradient_hsv_unknown, gradient_hsv_custom)

    plot_color_gradients(gradients, [toname(g) for g in gradients])
