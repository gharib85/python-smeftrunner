# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 13:23:34 2017

@author: Xuanyou
"""

import numpy as np


def getBeta(WC):
    #Parameters
    G_u = np.matrix(np.arange(9).reshape((3,3))+1j*np.arange(9).reshape((3,3)))
    G_d = np.matrix(np.arange(9).reshape((3,3))+1j*np.arange(9).reshape((3,3)))
    G_e = np.matrix(np.arange(9).reshape((3,3))+1j*np.arange(9).reshape((3,3)))
    g = 1
    gp = 1
    gs = 1
    m = 1
    HIGHSCALE = 1
    Lambda = 1
    I3 = np.identity(3)

    #Functions previous defined...  #c.c.   # i in eta5
    Eta1=(3*np.trace(WC["uCurlyPhi"]@G_u.getH())+3*np.trace(WC["dCurlyPhi"]@G_d.getH())+np.trace(WC["eCurlyPhi"]@G_e.getH())+3*np.conj(np.trace(WC["uCurlyPhi"]@G_u.getH()))+3*np.conj(np.trace(WC["dCurlyPhi"]@G_d.getH()))+np.conj(np.trace(WC["eCurlyPhi"]@G_e.getH())))/2
    Eta2=-6*np.trace(WC["CurlyPhiq3"]@G_u@G_u.getH())-6*np.trace(WC["CurlyPhiq3"]@G_d@G_d.getH())-2*np.trace(WC["CurlyPhil3"]@G_e@G_e.getH())+3*(np.trace(WC["CurlyPhiud"]@G_d.getH()@G_u)+np.conj(np.trace(WC["CurlyPhiud"]@G_d.getH()@G_u)))
    Eta3=3*np.trace(WC["CurlyPhiq1"]@G_d@G_d.getH())-3*np.trace(WC["CurlyPhiq1"]@G_u@G_u.getH())+9*np.trace(WC["CurlyPhiq3"]@G_d@G_d.getH())+9*np.trace(WC["CurlyPhiq3"]@G_u@G_u.getH())+3*np.trace(WC["CurlyPhiu"]@G_u.getH()@G_u)-3*np.trace(WC["CurlyPhid"]@G_d.getH()@G_d)-3*(np.trace(WC["CurlyPhiud"]@G_d.getH()@G_u)+np.conj(np.trace(WC["CurlyPhiud"]@G_d.getH()@G_u)))+np.trace(WC["CurlyPhil1"]@G_e@G_e.getH())+3*np.trace(WC["CurlyPhil3"]@G_e@G_e.getH())-np.trace(WC["CurlyPhie"]@G_e.getH()@G_e)
    Eta4=12*np.trace(WC["CurlyPhiq1"]@G_d@G_d.getH())-12*np.trace(WC["CurlyPhiq1"]@G_u@G_u.getH())+12*np.trace(WC["CurlyPhiu"]@G_u.getH()@G_u)-12*np.trace(WC["CurlyPhid"]@G_d.getH()@G_d)+6*(np.trace(WC["CurlyPhiud"]@G_d.getH()@G_u)+np.conj(np.trace(WC["CurlyPhiud"]@G_d.getH()@G_u)))+4*np.trace(WC["CurlyPhil1"]@G_e@G_e.getH())-4*np.trace(WC["CurlyPhie"]@G_e.getH()@G_e)
    Eta5=1j*3/2*(np.trace(G_d@WC["dCurlyPhi"].getH())-np.conj(np.trace(G_d@WC["dCurlyPhi"].getH())))-1j*3/2*(np.trace(G_u@WC["uCurlyPhi"].getH())-np.conj(np.trace(G_u@WC["uCurlyPhi"].getH())))+1j*1/2*(np.trace(G_e@WC["eCurlyPhi"].getH())-np.conj(np.trace(G_e@WC["eCurlyPhi"].getH())))

    GammaH=np.trace(3*G_u@G_u.getH()+3*G_d@G_d.getH()+G_e@G_e.getH())
    Gammaq=1/2*(G_u@G_u.getH()+G_d@G_d.getH())
    Gammau=G_u.getH()@G_u
    Gammad=G_d.getH()@G_d
    Gammal=1/2*G_e@G_e.getH()
    Gammae=G_e.getH()@G_e

    XiB=2/3*(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])+8/3*(-np.trace(WC["CurlyPhil1"])+np.trace(WC["CurlyPhiq1"])-np.trace(WC["CurlyPhie"])+2*np.trace(WC["CurlyPhiu"])-np.trace(WC["CurlyPhid"]))
    Xie=2*np.einsum("prst,rs", WC["le"], G_e)-3*np.einsum("ptsr,rs", WC["ledq"], G_d)+3*np.einsum("ptsr,sr", WC["lequ1"], np.conj(G_u))
    Xid=2*(np.einsum("prst,rs", WC["qd1"], G_d)+4/3*np.einsum("prst,rs", WC["qd8"], G_d))-(3*np.einsum("srpt,sr", WC["quqd1"], np.conj(G_u))+1/2*(np.einsum("prst,sr", WC["quqd1"], np.conj(G_u))+4/3*np.einsum("prst,sr", WC["quqd8"], np.conj(G_u))))-np.einsum("srtp,sr", np.conj(WC["ledq"]), G_e)
    Xiu=2*(np.einsum("prst,rs", WC["qu1"], G_u)+4/3*np.einsum("prst,rs", WC["qu8"], G_u))-(3*np.einsum("ptsr,sr", WC["quqd1"], np.conj(G_d))+1/2*(np.einsum("stpr,sr", WC["quqd1"], np.conj(G_d))+4/3*np.einsum("stpr,sr", WC["quqd8"], np.conj(G_d))))+np.einsum("srpt,sr", WC["lequ1"], np.conj(G_e))

    Beta={}




    #equations of beta functions
    Beta["g"]=-19/6*g**3-8*g*m**2/HIGHSCALE**2*WC["CurlyPhiW"]


    Beta["gp"]=41/6*gp**3-8*gp*m**2/HIGHSCALE**2*WC["CurlyPhiB"]


    Beta["gs"]=-7*gs**3-8*gs*m**2/HIGHSCALE**2*WC["CurlyPhiG"]


    Beta["Lambda"]=12*Lambda**2+3/4*gp**4+3/2*g**2*gp**2+9/4*g**4-3*(gp**2+3*g**2)*Lambda+4*Lambda*GammaH-4*(3*np.trace(G_d@G_d.getH()@G_d@G_d.getH())+3*np.trace(G_u@G_u.getH()@G_u@G_u.getH())+np.trace(G_e@G_e.getH()@G_e@G_e.getH()))+4*m**2/HIGHSCALE**2*(12*WC["CurlyPhi"]+(-16*Lambda+10/3*g**2)*WC["CurlyPhiEmptySquare"]+(6*Lambda+3/2*(gp**2-g**2))*WC["CurlyPhiD"]+2*(Eta1+Eta2)+9*g**2*WC["CurlyPhiW"]+3*gp**2*WC["CurlyPhiB"]+3*g*gp*WC["CurlyPhiWB"]+4/3*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"])))


    Beta["m**2"]=m**2*(6*Lambda-9/2*g**2-3/2*gp**2+2*GammaH+4*m**2/HIGHSCALE**2*(WC["CurlyPhiD"]-2*WC["CurlyPhiEmptySquare"]))


    Beta["G_u"]=3/2*(G_u@G_u.getH()@G_u-G_d@G_d.getH()@G_u)+(GammaH-9/4*g**2-17/12*gp**2-8*gs**2)*G_u+2*m**2/HIGHSCALE**2*(3*WC["uCurlyPhi"]+1/2*(WC["CurlyPhiD"]-2*WC["CurlyPhiEmptySquare"])*G_u-WC["CurlyPhiq1"].getH()@G_u+3*WC["CurlyPhiq3"].getH()@G_u+G_u@WC["CurlyPhiu"].getH()-G_d@WC["CurlyPhiud"].getH()-2*(np.einsum("rpts,pt", WC["qu1"], G_u)+4/3*np.einsum("rpts,pt", WC["qu8"], G_u))-np.einsum("ptrs,pt", WC["lequ1"], np.conj(G_e))+3*np.einsum("rspt,pt", WC["quqd1"], np.conj(G_d))+1/2*(np.einsum("psrt,pt", WC["quqd1"], np.conj(G_d))+4/3*np.einsum("psrt,pt", WC["quqd8"], np.conj(G_d))))


    Beta["G_d"]=3/2*(G_d@G_d.getH()@G_d-G_u@G_u.getH()@G_d)+(GammaH-9/4*g**2-5/12*gp**2-8*gs**2)*G_d+2*m**2/HIGHSCALE**2*(3*WC["dCurlyPhi"]+1/2*(WC["CurlyPhiD"]-2*WC["CurlyPhiEmptySquare"])*G_d+WC["CurlyPhiq1"].getH()@G_d+3*WC["CurlyPhiq3"].getH()@G_d-G_d@WC["CurlyPhid"].getH()-G_u@WC["CurlyPhiud"]-2*(np.einsum("rpts,pt", WC["qd1"], G_d)+4/3*np.einsum("rpts,pt", WC["qd8"], G_d))+np.einsum("ptsr,tp", np.conj(WC["ledq"]), np.conj(G_e))+3*np.einsum("ptrs,pt", WC["quqd1"], np.conj(G_u))+1/2*(np.einsum("rpts,pt", WC["quqd1"], np.conj(G_u))+4/3*np.einsum("rpts,pt", WC["quqd8"], np.conj(G_u))))


    Beta["G_e"]=3/2*G_e@G_e.getH()@G_e+(GammaH-3/4*(3*g**2+5*gp**2))*G_e+2*m**2/HIGHSCALE**2*(3*WC["eCurlyPhi"]+1/2*(WC["CurlyPhiD"]-2*WC["CurlyPhiEmptySquare"])*G_e+WC["CurlyPhil1"].getH()@G_e+3*WC["CurlyPhil3"].getH()@G_e-G_e@WC["CurlyPhie"].getH()-2*np.einsum("rpts,pt", WC["le"], G_e)+3*np.einsum("rspt,tp", WC["ledq"], G_d)-3*np.einsum("rspt,pt", WC["lequ1"], np.conj(G_u)))


    Beta["Theta"]=-128*np.pi**2/g**2*m**2/HIGHSCALE**2*WC["CurlyPhiWtilde"]


    Beta["Thetap"]=-128*np.pi**2/gp**2*m**2/HIGHSCALE**2*WC["CurlyPhiBtilde"]


    Beta["Thetas"]=-128*np.pi**2/gs**2*m**2/HIGHSCALE**2*WC["CurlyPhiGtilde"]


    Beta["G"]=15*gs**2*WC["G"]


    Beta["Gtilde"]=15*gs**2*WC["Gtilde"]


    Beta["W"]=29/2*g**2*WC["W"]


    Beta["Wtilde"]=29/2*g**2*WC["Wtilde"]

    #c.c.
    Beta["CurlyPhi"]=-9/2*(3*g**2+gp**2)*WC["CurlyPhi"]+Lambda*(20/3*g**2*WC["CurlyPhiEmptySquare"]+3*(gp**2-g**2)*WC["CurlyPhiD"])-3/4*(g**2+gp**2)**2*WC["CurlyPhiD"]+6*Lambda*(3*g**2*WC["CurlyPhiW"]+gp**2*WC["CurlyPhiB"]+g*gp*WC["CurlyPhiWB"])-3*(g**2*gp**2+3*g**4)*WC["CurlyPhiW"]-3*(gp**4+g**2*gp**2)*WC["CurlyPhiB"]-3*(g*gp**3+g**3*gp)*WC["CurlyPhiWB"]+8/3*Lambda*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"]))+54*Lambda*WC["CurlyPhi"]-40*Lambda**2*WC["CurlyPhiEmptySquare"]+12*Lambda**2*WC["CurlyPhiD"]+4*Lambda*(Eta1+Eta2)-4*(3*np.trace(WC["uCurlyPhi"]@G_u.getH()@G_u@G_u.getH())+3*np.trace(WC["dCurlyPhi"]@G_d.getH()@G_d@G_d.getH())+np.trace(WC["eCurlyPhi"]@G_e.getH()@G_e@G_e.getH())+3*np.conj(np.trace(WC["uCurlyPhi"]@G_u.getH()@G_u@G_u.getH()))+3*np.conj(np.trace(WC["dCurlyPhi"]@G_d.getH()@G_d@G_d.getH()))+np.conj(np.trace(WC["eCurlyPhi"]@G_e.getH()@G_e@G_e.getH())))+6*GammaH*WC["CurlyPhi"]


    Beta["CurlyPhiEmptySquare"]=-(4*g**2+4/3*gp**2)*WC["CurlyPhiEmptySquare"]+5/3*gp**2*WC["CurlyPhiD"]+2*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"]))+2/3*gp**2*(2*np.trace(WC["CurlyPhiu"])-np.trace(WC["CurlyPhid"])-np.trace(WC["CurlyPhie"])+np.trace(WC["CurlyPhiq1"])-np.trace(WC["CurlyPhil1"]))+12*Lambda*WC["CurlyPhiEmptySquare"]-2*Eta3+4*GammaH*WC["CurlyPhiEmptySquare"]


    Beta["CurlyPhiD"]=20/3*gp**2*WC["CurlyPhiEmptySquare"]+(9/2*g**2-5/6*gp**2)*WC["CurlyPhiD"]+8/3*gp**2*(2*np.trace(WC["CurlyPhiu"])-np.trace(WC["CurlyPhid"])-np.trace(WC["CurlyPhie"])+np.trace(WC["CurlyPhiq1"])-np.trace(WC["CurlyPhil1"]))+6*Lambda*WC["CurlyPhiD"]-2*Eta4+4*GammaH*WC["CurlyPhiD"]

    #c.c.
    Beta["CurlyPhiG"]=(-3/2*gp**2-9/2*g**2-14*gs**2)*WC["CurlyPhiG"]+6*Lambda*WC["CurlyPhiG"]-2*gs*(np.trace(WC["uG"]@G_u.getH())+np.trace(WC["dG"]@G_d.getH())+np.conj(np.trace(WC["uG"]@G_u.getH()))+np.conj(np.trace(WC["dG"]@G_d.getH())))+2*GammaH*WC["CurlyPhiG"]

    #c.c.
    Beta["CurlyPhiB"]=(85/6*gp**2-9/2*g**2)*WC["CurlyPhiB"]+3*g*gp*WC["CurlyPhiWB"]+6*Lambda*WC["CurlyPhiB"]+gp*(-5*np.trace(WC["uB"]@G_u.getH())+np.trace(WC["dB"]@G_d.getH())+3*np.trace(WC["eB"]@G_e.getH())-5*np.conj(np.trace(WC["uB"]@G_u.getH()))+np.conj(np.trace(WC["dB"]@G_d.getH()))+3*np.conj(np.trace(WC["eB"]@G_e.getH())))+2*GammaH*WC["CurlyPhiB"]

    #c.c.
    Beta["CurlyPhiW"]=(-3/2*gp**2-53/6*g**2)*WC["CurlyPhiW"]+g*gp*WC["CurlyPhiWB"]-15*g**3*WC["W"]+6*Lambda*WC["CurlyPhiW"]-g*(3*np.trace(WC["uW"]@G_u.getH())+3*np.trace(WC["dW"]@G_d.getH())+np.trace(WC["eW"]@G_e.getH())+3*np.conj(np.trace(WC["uW"]@G_u.getH()))+3*np.conj(np.trace(WC["dW"]@G_d.getH()))+np.conj(np.trace(WC["eW"]@G_e.getH())))+2*GammaH*WC["CurlyPhiW"]

    #c.c.
    Beta["CurlyPhiWB"]=(19/3*gp**2+4/3*g**2)*WC["CurlyPhiWB"]+2*g*gp*(WC["CurlyPhiB"]+WC["CurlyPhiW"])+3*g**2*gp*WC["W"]+2*Lambda*WC["CurlyPhiWB"]+g*(3*np.trace(WC["uB"]@G_u.getH())-3*np.trace(WC["dB"]@G_d.getH())-np.trace(WC["eB"]@G_e.getH())+3*np.conj(np.trace(WC["uB"]@G_u.getH()))-3*np.conj(np.trace(WC["dB"]@G_d.getH()))-np.conj(np.trace(WC["eB"]@G_e.getH())))+gp*(5*np.trace(WC["uW"]@G_u.getH())+np.trace(WC["dW"]@G_d.getH())+3*np.trace(WC["eW"]@G_e.getH())+5*np.conj(np.trace(WC["uW"]@G_u.getH()))+np.conj(np.trace(WC["dW"]@G_d.getH()))+3*np.conj(np.trace(WC["eW"]@G_e.getH())))+2*GammaH*WC["CurlyPhiWB"]

    #problem with i as I*iCPV
    Beta["CurlyPhiGtilde"]=(-3/2*gp**2-9/2*g**2-14*gs**2)*WC["CurlyPhiGtilde"]+6*Lambda*WC["CurlyPhiGtilde"]+2j*gs*(np.trace(WC["uG"]@G_u.getH())+np.trace(WC["dG"]@G_d.getH())-np.conj(np.trace(WC["uG"]@G_u.getH()))-np.conj(np.trace(WC["dG"]@G_d.getH())))+2*GammaH*WC["CurlyPhiGtilde"]

    #i
    Beta["CurlyPhiBtilde"]=(85/6*gp**2-9/2*g**2)*WC["CurlyPhiBtilde"]+3*g*gp*WC["CurlyPhiWtildeB"]+6*Lambda*WC["CurlyPhiBtilde"]-1j*gp*(-5*np.trace(WC["uB"]@G_u.getH())+np.trace(WC["dB"]@G_d.getH())+3*np.trace(WC["eB"]@G_e.getH())+5*np.conj(np.trace(WC["uB"]@G_u.getH()))-np.conj(np.trace(WC["dB"]@G_d.getH()))-3*np.conj(np.trace(WC["eB"]@G_e.getH())))+2*GammaH*WC["CurlyPhiBtilde"]

    #i
    Beta["CurlyPhiWtilde"]=(-3/2*gp**2-53/6*g**2)*WC["CurlyPhiWtilde"]+g*gp*WC["CurlyPhiWtildeB"]-15*g**3*WC["Wtilde"]+6*Lambda*WC["CurlyPhiWtilde"]+1j*g*(3*np.trace(WC["uW"]@G_u.getH())+3*np.trace(WC["dW"]@G_d.getH())+np.trace(WC["eW"]@G_e.getH())-3*np.conj(np.trace(WC["uW"]@G_u.getH()))-3*np.conj(np.trace(WC["dW"]@G_d.getH()))-np.conj(np.trace(WC["eW"]@G_e.getH())))+2*GammaH*WC["CurlyPhiWtilde"]

    #i
    Beta["CurlyPhiWtildeB"]=(19/3*gp**2+4/3*g**2)*WC["CurlyPhiWtildeB"]+2*g*gp*(WC["CurlyPhiBtilde"]+WC["CurlyPhiWtilde"])+3*g**2*gp*WC["Wtilde"]+2*Lambda*WC["CurlyPhiWtildeB"]-1j*g*(3*np.trace(WC["uB"]@G_u.getH())-3*np.trace(WC["dB"]@G_d.getH())-np.trace(WC["eB"]@G_e.getH())-3*np.conj(np.trace(WC["uB"]@G_u.getH()))+3*np.conj(np.trace(WC["dB"]@G_d.getH()))+np.conj(np.trace(WC["eB"]@G_e.getH())))-1j*gp*(5*np.trace(WC["uW"]@G_u.getH())+np.trace(WC["dW"]@G_d.getH())+3*np.trace(WC["eW"]@G_e.getH())-5*np.conj(np.trace(WC["uW"]@G_u.getH()))-np.conj(np.trace(WC["dW"]@G_d.getH()))-3*np.conj(np.trace(WC["eW"]@G_e.getH())))+2*GammaH*WC["CurlyPhiWtildeB"]

    #i  #the coefficients of Eta5 is not equal
    Beta["uCurlyPhi"]=(10/3*g**2*WC["CurlyPhiEmptySquare"]+3/2*(gp**2-g**2)*WC["CurlyPhiD"]+32*gs**2*(WC["CurlyPhiG"]+1j*WC["CurlyPhiGtilde"])+9*g**2*(WC["CurlyPhiW"]+1j*WC["CurlyPhiWtilde"])+17/3*gp**2*(WC["CurlyPhiB"]+1j*WC["CurlyPhiBtilde"])-g*gp*(WC["CurlyPhiWB"]+1j*WC["CurlyPhiWtildeB"])+4/3*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"])))*G_u-(35/12*gp**2+27/4*g**2+8*gs**2)*WC["uCurlyPhi"]-gp*(5*gp**2-3*g**2)*WC["uB"]+g*(5*gp**2-9*g**2)*WC["uW"]-(3*g**2-gp**2)*G_u@WC["CurlyPhiu"]+3*g**2*G_d@WC["CurlyPhiud"].getH()+4*gp**2*WC["CurlyPhiq1"]@G_u-4*gp**2*WC["CurlyPhiq3"]@G_u-5*gp*(WC["uB"]@G_u.getH()@G_u+G_u@G_u.getH()@WC["uB"])-3*g*(WC["uW"]@G_u.getH()@G_u-G_u@G_u.getH()@WC["uW"])-16*gs*(WC["uG"]@G_u.getH()@G_u+G_u@G_u.getH()@WC["uG"])-12*g*G_d@G_d.getH()@WC["uW"]-6*g*WC["dW"]@G_d.getH()@G_u+Lambda*(12*WC["uCurlyPhi"]-2*WC["CurlyPhiq1"]@G_u+6*WC["CurlyPhiq3"]@G_u+2*G_u@WC["CurlyPhiu"]-2*G_d@WC["CurlyPhiud"].getH()-2*WC["CurlyPhiEmptySquare"]*G_u+WC["CurlyPhiD"]*G_u-4*np.einsum("rpts,pt", WC["qu1"], G_u)-16/3*np.einsum("rpts,pt", WC["qu8"], G_u)-2*np.einsum("ptrs,pt", WC["lequ1"], np.conj(G_e))+6*np.einsum("rspt,pt", WC["quqd1"], np.conj(G_d))+np.einsum("psrt,pt", WC["quqd1"], np.conj(G_d))+4/3*np.einsum("psrt,pt", WC["quqd8"], np.conj(G_d)))+2*(Eta1+Eta2-1j*Eta5)*G_u+(WC["CurlyPhiD"]-6*WC["CurlyPhiEmptySquare"])*G_u@G_u.getH()@G_u-2*WC["CurlyPhiq1"]@G_u@G_u.getH()@G_u+6*WC["CurlyPhiq3"]@G_d@G_d.getH()@G_u+2*G_u@G_u.getH()@G_u@WC["CurlyPhiu"]-2*G_d@G_d.getH()@G_d@WC["CurlyPhiud"].getH()+8*(np.einsum("rpts,pt", WC["qu1"], G_u@G_u.getH()@G_u)+4/3*np.einsum("rpts,pt", WC["qu8"], G_u@G_u.getH()@G_u))-2*(np.einsum("tsrp,pt", WC["quqd1"], G_d.getH()@G_d@G_d.getH())+4/3*np.einsum("tsrp,pt", WC["quqd8"], G_d.getH()@G_d@G_d.getH()))-12*np.einsum("rstp,pt", WC["quqd1"], G_d.getH()@G_d@G_d.getH())+4*np.einsum("tprs,pt", WC["lequ1"], G_e@G_e.getH()@G_e)+4*WC["uCurlyPhi"]@G_u.getH()@G_u+5*G_u@G_u.getH()@WC["uCurlyPhi"]-2*G_d@WC["dCurlyPhi"].getH()@G_u-WC["dCurlyPhi"]@G_d.getH()@G_u-2*G_d@G_d.getH()@WC["uCurlyPhi"]+3*GammaH*WC["uCurlyPhi"]+Gammaq@WC["uCurlyPhi"]+WC["uCurlyPhi"]@Gammau

    #i  #Eta5
    Beta["dCurlyPhi"]=(10/3*g**2*WC["CurlyPhiEmptySquare"]+3/2*(gp**2-g**2)*WC["CurlyPhiD"]+32*gs**2*(WC["CurlyPhiG"]+1j*WC["CurlyPhiGtilde"])+9*g**2*(WC["CurlyPhiW"]+1j*WC["CurlyPhiWtilde"])+5/3*gp**2*(WC["CurlyPhiB"]+1j*WC["CurlyPhiBtilde"])+g*gp*(WC["CurlyPhiWB"]+1j*WC["CurlyPhiWtildeB"])+4/3*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"])))*G_d-(23/12*gp**2+27/4*g**2+8*gs**2)*WC["dCurlyPhi"]-gp*(3*g**2-gp**2)*WC["dB"]-g*(9*g**2-gp**2)*WC["dW"]+(3*g**2+gp**2)*G_d@WC["CurlyPhid"]+3*g**2*G_u@WC["CurlyPhiud"]-2*gp**2*WC["CurlyPhiq1"]@G_d-2*gp**2*WC["CurlyPhiq3"]@G_d+gp*(WC["dB"]@G_d.getH()@G_d+G_d@G_d.getH()@WC["dB"])-3*g*(WC["dW"]@G_d.getH()@G_d-G_d@G_d.getH()@WC["dW"])-16*gs*(WC["dG"]@G_d.getH()@G_d+G_d@G_d.getH()@WC["dG"])-12*g*G_u@G_u.getH()@WC["dW"]-6*g*WC["uW"]@G_u.getH()@G_d+Lambda*(12*WC["dCurlyPhi"]+2*WC["CurlyPhiq1"]@G_d+6*WC["CurlyPhiq3"]@G_d-2*G_d@WC["CurlyPhid"]-2*G_u@WC["CurlyPhiud"]-2*WC["CurlyPhiEmptySquare"]*G_d+WC["CurlyPhiD"]*G_d-4*np.einsum("rpts,pt", WC["qd1"], G_d)-16/3*np.einsum("rpts,pt", WC["qd8"], G_d)+2*np.einsum("ptsr,tp", np.conj(WC["ledq"]), np.conj(G_e))+6*np.einsum("ptrs,pt", WC["quqd1"], np.conj(G_u))+np.einsum("rtps,pt", WC["quqd1"], np.conj(G_u))+4/3*np.einsum("rtps,pt", WC["quqd8"], np.conj(G_u)))+2*(Eta1+Eta2+1j*Eta5)*G_d+(WC["CurlyPhiD"]-6*WC["CurlyPhiEmptySquare"])*G_d@G_d.getH()@G_d+2*WC["CurlyPhiq1"]@G_d@G_d.getH()@G_d+6*WC["CurlyPhiq3"]@G_u@G_u.getH()@G_d-2*G_d@G_d.getH()@G_d@WC["CurlyPhid"]-2*G_u@G_u.getH()@G_u@WC["CurlyPhiud"]+8*(np.einsum("rpts,pt", WC["qd1"], G_d@G_d.getH()@G_d)+4/3*np.einsum("rpts,pt", WC["qd8"], G_d@G_d.getH()@G_d))-2*(np.einsum("rpts,pt", WC["quqd1"], G_u.getH()@G_u@G_u.getH())+4/3*np.einsum("rpts,pt", WC["quqd8"], G_u.getH()@G_u@G_u.getH()))-12*np.einsum("tprs,pt", WC["quqd1"], G_u@G_u.getH()@G_u)-4*np.einsum("ptsr,pt", np.conj(WC["ledq"]), G_e@G_e.getH()@G_e)+4*WC["dCurlyPhi"]@G_d.getH()@G_d+5*G_d@G_d.getH()@WC["dCurlyPhi"]-2*G_u@WC["uCurlyPhi"].getH()@G_d-WC["uCurlyPhi"]@G_u.getH()@G_d-2*G_u@G_u.getH()@WC["dCurlyPhi"]+3*GammaH*WC["dCurlyPhi"]+Gammaq@WC["dCurlyPhi"]+WC["dCurlyPhi"]@Gammad

    #i
    Beta["eCurlyPhi"]=(10/3*g**2*WC["CurlyPhiEmptySquare"]+3/2*(gp**2-g**2)*WC["CurlyPhiD"]+9*g**2*(WC["CurlyPhiW"]+1j*WC["CurlyPhiWtilde"])+15*gp**2*(WC["CurlyPhiB"]+1j*WC["CurlyPhiBtilde"])-3*g*gp*(WC["CurlyPhiWB"]+1j*WC["CurlyPhiWtildeB"])+4/3*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"])))*G_e-3/4*(7*gp**2+9*g**2)*WC["eCurlyPhi"]-3*gp*(g**2-3*gp**2)*WC["eB"]-9*g*(g**2-gp**2)*WC["eW"]+3*(g**2-gp**2)*G_e@WC["CurlyPhie"]-6*gp**2*WC["CurlyPhil1"]@G_e-6*gp**2*WC["CurlyPhil3"]@G_e+9*gp*(WC["eB"]@G_e.getH()@G_e+G_e@G_e.getH()@WC["eB"])-3*g*(WC["eW"]@G_e.getH()@G_e-G_e@G_e.getH()@WC["eW"])+Lambda*(12*WC["eCurlyPhi"]+2*WC["CurlyPhil1"]@G_e+6*WC["CurlyPhil3"]@G_e-2*G_e@WC["CurlyPhie"]-2*WC["CurlyPhiEmptySquare"]*G_e+WC["CurlyPhiD"]*G_e-4*np.einsum("rpts,pt", WC["le"], G_e)+6*np.einsum("rspt,pt", WC["ledq"], G_d)-6*np.einsum("rspt,pt", WC["lequ1"], np.conj(G_u)))+2*(Eta1+Eta2+1j*Eta5)*G_e+(WC["CurlyPhiD"]-6*WC["CurlyPhiEmptySquare"])*G_e@G_e.getH()@G_e+2*WC["CurlyPhil1"]@G_e@G_e.getH()@G_e-2*G_e@G_e.getH()@G_e@WC["CurlyPhie"]+8*np.einsum("rpts,pt", WC["le"], G_e@G_e.getH()@G_e)-12*np.einsum("rspt,tp", WC["ledq"], G_d@G_d.getH()@G_d)+12*np.einsum("rstp,pt", WC["lequ1"], G_u.getH()@G_u@G_u.getH())+4*WC["eCurlyPhi"]@G_e.getH()@G_e+5*G_e@G_e.getH()@WC["eCurlyPhi"]+3*GammaH*WC["eCurlyPhi"]+Gammal@WC["eCurlyPhi"]+WC["eCurlyPhi"]@Gammae

    #i
    Beta["eW"]=1/12*(3*gp**2-11*g**2)*WC["eW"]-1/2*g*gp*WC["eB"]-(g*(WC["CurlyPhiW"]+1j*WC["CurlyPhiWtilde"])-3/2*gp*(WC["CurlyPhiWB"]+1j*WC["CurlyPhiWtildeB"]))*G_e-6*g*np.einsum("rspt,pt", WC["lequ3"], np.conj(G_u))+WC["eW"]@G_e.getH()@G_e+GammaH*WC["eW"]+Gammal@WC["eW"]+WC["eW"]@Gammae

    #i
    Beta["eB"]=1/4*(151/3*gp**2-9*g**2)*WC["eB"]-3/2*g*gp*WC["eW"]-(3/2*g*(WC["CurlyPhiWB"]+1j*WC["CurlyPhiWtildeB"])-3*gp*(WC["CurlyPhiB"]+1j*WC["CurlyPhiBtilde"]))*G_e+10*gp*np.einsum("rspt,pt", WC["lequ3"], np.conj(G_u))+WC["eB"]@G_e.getH()@G_e+2*G_e@G_e.getH()@WC["eB"]+GammaH*WC["eB"]+Gammal@WC["eB"]+WC["eB"]@Gammae

    #i
    Beta["uG"]=-1/36*(81*g**2+19*gp**2+204*gs**2)*WC["uG"]+6*g*gs*WC["uW"]+10/3*gp*gs*WC["uB"]-gs*(4*(WC["CurlyPhiG"]+1j*WC["CurlyPhiGtilde"])+9*gs*(WC["G"]+1j*WC["Gtilde"]))*G_u-gs*(np.einsum("psrt,pt", WC["quqd1"], np.conj(G_d))-1/6*np.einsum("psrt,pt", WC["quqd8"], np.conj(G_d)))+2*G_u@G_u.getH()@WC["uG"]-2*G_d@G_d.getH()@WC["uG"]-WC["dG"]@G_d.getH()@G_u+WC["uG"]@G_u.getH()@G_u+GammaH*WC["uG"]+Gammaq@WC["uG"]+WC["uG"]@Gammau

    #i
    Beta["uW"]=-1/36*(33*g**2+19*gp**2-96*gs**2)*WC["uW"]+8/3*g*gs*WC["uG"]-1/6*g*gp*WC["uB"]-(g*(WC["CurlyPhiW"]+1j*WC["CurlyPhiWtilde"])-5/6*gp*(WC["CurlyPhiWB"]+1j*WC["CurlyPhiWtildeB"]))*G_u+g/4*(np.einsum("psrt,pt", WC["quqd1"], np.conj(G_d))+4/3*np.einsum("psrt,pt", WC["quqd8"], np.conj(G_d)))-2*g*np.einsum("ptrs,tp", WC["lequ3"], np.conj(G_e))+2*G_d@G_d.getH()@WC["uW"]-WC["dW"]@G_d.getH()@G_u+WC["uW"]@G_u.getH()@G_u+GammaH*WC["uW"]+Gammaq@WC["uW"]+WC["uW"]@Gammau

    #i
    Beta["uB"]=-1/36*(81*g**2-313*gp**2-96*gs**2)*WC["uB"]+40/9*gp*gs*WC["uG"]-1/2*g*gp*WC["uW"]-(-3/2*g*(WC["CurlyPhiWB"]+1j*WC["CurlyPhiWtildeB"])+5/3*gp*(WC["CurlyPhiB"]+1j*WC["CurlyPhiBtilde"]))*G_u+gp/12*(np.einsum("psrt,pt", WC["quqd1"], np.conj(G_d))+4/3*np.einsum("psrt,pt", WC["quqd8"], np.conj(G_d)))-6*gp*np.einsum("ptrs,tp", WC["lequ3"], np.conj(G_e))+2*G_u@G_u.getH()@WC["uB"]-2*G_d@G_d.getH()@WC["uB"]-WC["dB"]@G_d.getH()@G_u+WC["uB"]@G_u.getH()@G_u+GammaH*WC["uB"]+Gammaq@WC["uB"]+WC["uB"]@Gammau

    #i
    Beta["dG"]=-1/36*(81*g**2+31*gp**2+204*gs**2)*WC["dG"]+6*g*gs*WC["dW"]-2/3*gp*gs*WC["dB"]-gs*(4*(WC["CurlyPhiG"]+1j*WC["CurlyPhiGtilde"])+9*gs*(WC["G"]+1j*WC["Gtilde"]))*G_d-gs*(np.einsum("rtps,pt", WC["quqd1"], np.conj(G_u))-1/6*np.einsum("rtps,pt", WC["quqd8"], np.conj(G_u)))-2*G_u@G_u.getH()@WC["dG"]+2*G_d@G_d.getH()@WC["dG"]-WC["uG"]@G_u.getH()@G_d+WC["dG"]@G_d.getH()@G_d+GammaH*WC["dG"]+Gammaq@WC["dG"]+WC["dG"]@Gammad

    #i
    Beta["dW"]=-1/36*(33*g**2+31*gp**2-96*gs**2)*WC["dW"]+8/3*g*gs*WC["dG"]+5/6*g*gp*WC["dB"]-(g*(WC["CurlyPhiW"]+1j*WC["CurlyPhiWtilde"])-gp/6*(WC["CurlyPhiWB"]+1j*WC["CurlyPhiWtildeB"]))*G_d+g/4*(np.einsum("rtps,pt", WC["quqd1"], np.conj(G_u))+4/3*np.einsum("rtps,pt", WC["quqd8"], np.conj(G_u)))+2*G_u@G_u.getH()@WC["dW"]-WC["uW"]@G_u.getH()@G_d+WC["dW"]@G_d.getH()@G_d+GammaH*WC["dW"]+Gammaq@WC["dW"]+WC["dW"]@Gammad

    #i
    Beta["dB"]=-1/36*(81*g**2-253*gp**2-96*gs**2)*WC["dB"]-8/9*gp*gs*WC["dG"]+5/2*g*gp*WC["dW"]-(3/2*g*(WC["CurlyPhiWB"]+1j*WC["CurlyPhiWtildeB"])-gp/3*(WC["CurlyPhiB"]+1j*WC["CurlyPhiBtilde"]))*G_d-5/12*gp*(np.einsum("rtps,pt", WC["quqd1"], np.conj(G_u))+4/3*np.einsum("rtps,pt", WC["quqd8"], np.conj(G_u)))-2*G_u@G_u.getH()@WC["dB"]+2*G_d@G_d.getH()@WC["dB"]-WC["uB"]@G_u.getH()@G_d+WC["dB"]@G_d.getH()@G_d+GammaH*WC["dB"]+Gammaq@WC["dB"]+WC["dB"]@Gammad

    #I3 #coefficient not equal with manual!!!!!!
    Beta["CurlyPhil1"]=-1/4*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhil1"]-2/3*gp**2*(np.einsum("rstt", WC["ld"])+np.einsum("rstt", WC["le"])+2*np.einsum("rstt", WC["ll"])+np.einsum("rtts", WC["ll"])-np.einsum("rstt", WC["lq1"])-2*np.einsum("rstt", WC["lu"]))-1/2*(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])*G_e@G_e.getH()-G_e@WC["CurlyPhie"]@G_e.getH()+3/2*(G_e@G_e.getH()@WC["CurlyPhil1"]+WC["CurlyPhil1"]@G_e@G_e.getH()+3*G_e@G_e.getH()@WC["CurlyPhil3"]+3*WC["CurlyPhil3"]@G_e@G_e.getH())+2*np.einsum("rspt,tp", WC["le"], G_e.getH()@G_e)-2*(2*np.einsum("rspt,tp", WC["ll"], G_e@G_e.getH())+np.einsum("rtps,tp", WC["ll"], G_e@G_e.getH()))-6*np.einsum("rspt,tp", WC["lq1"], G_d@G_d.getH())+6*np.einsum("rspt,tp", WC["lq1"], G_u@G_u.getH())-6*np.einsum("rspt,tp", WC["lu"], G_u.getH()@G_u)+6*np.einsum("rspt,tp", WC["ld"], G_d.getH()@G_d)+2*GammaH*WC["CurlyPhil1"]+Gammal@WC["CurlyPhil1"]+WC["CurlyPhil1"]@Gammal

    #I3 #coefficient
    Beta["CurlyPhil3"]=2/3*g**2*(1/4*WC["CurlyPhiEmptySquare"]+np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"]))*I3-17/3*g**2*WC["CurlyPhil3"]+2/3*g**2*np.einsum("rtts", WC["ll"])+2*g**2*np.einsum("rstt", WC["lq3"])-1/2*WC["CurlyPhiEmptySquare"]*G_e@G_e.getH()+1/2*(3*G_e@G_e.getH()@WC["CurlyPhil1"]+3*WC["CurlyPhil1"]@G_e@G_e.getH()+G_e@G_e.getH()@WC["CurlyPhil3"]+WC["CurlyPhil3"]@G_e@G_e.getH())-2*(np.einsum("rtps,tp", WC["ll"], G_e@G_e.getH()))-6*np.einsum("rspt,tp", WC["lq3"], G_d@G_d.getH())-6*np.einsum("rspt,tp", WC["lq3"], G_u@G_u.getH())+2*GammaH*WC["CurlyPhil3"]+Gammal@WC["CurlyPhil3"]+WC["CurlyPhil3"]@Gammal

    #I3  #coefficient even terms not equal...
    Beta["CurlyPhie"]=-1/2*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhie"]-2/3*gp**2*(np.einsum("rstt", WC["ed"])+4*np.einsum("rstt", WC["ee"])-2*np.einsum("rstt", WC["eu"])+np.einsum("ttrs", WC["le"])-np.einsum("ttrs", WC["qe"]))+(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])*G_e.getH()@G_e-2*G_e.getH()@WC["CurlyPhil1"]@G_e+3*(G_e.getH()@G_e@WC["CurlyPhie"]+WC["CurlyPhie"]@G_e.getH()@G_e)-2*np.einsum("ptrs,tp", WC["le"], G_e@G_e.getH())+8*np.einsum("rspt,tp", WC["ee"], G_e.getH()@G_e)-6*np.einsum("rspt,tp", WC["eu"], G_u.getH()@G_u)+6*np.einsum("rspt,tp", WC["ed"], G_d.getH()@G_d)-6*np.einsum("ptrs,tp", WC["qe"], G_d@G_d.getH())+6*np.einsum("ptrs,tp", WC["qe"], G_u@G_u.getH())+2*GammaH*WC["CurlyPhie"]+Gammae@WC["CurlyPhie"]+WC["CurlyPhie"]@Gammae

    #I3  #coefficient???
    Beta["CurlyPhiq1"]=1/12*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhiq1"]-2/3*gp**2*(np.einsum("ttrs", WC["lq1"])+np.einsum("rstt", WC["qd1"])-2*np.einsum("rstt", WC["qu1"])+np.einsum("rstt", WC["qe"])-2*np.einsum("rstt", WC["qq1"])-1/3*np.einsum("rtts", WC["qq1"])-np.einsum("rtts", WC["qq3"]))+1/2*(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])*(G_u@G_u.getH()-G_d@G_d.getH())-G_u@WC["CurlyPhiu"]@G_u.getH()-G_d@WC["CurlyPhid"]@G_d.getH()+2*np.einsum("rspt,tp", WC["qe"], G_e.getH()@G_e)-2*np.einsum("ptrs,tp", WC["lq1"], G_e@G_e.getH())+3/2*(G_d@G_d.getH()@WC["CurlyPhiq1"]+G_u@G_u.getH()@WC["CurlyPhiq1"]+WC["CurlyPhiq1"]@G_d@G_d.getH()+WC["CurlyPhiq1"]@G_u@G_u.getH()+3*G_d@G_d.getH()@WC["CurlyPhiq3"]-3*G_u@G_u.getH()@WC["CurlyPhiq3"]+3*WC["CurlyPhiq3"]@G_d@G_d.getH()-3*WC["CurlyPhiq3"]@G_u@G_u.getH())-2*(6*np.einsum("ptrs,tp", WC["qq1"], G_d@G_d.getH())+np.einsum("psrt,tp", WC["qq1"], G_d@G_d.getH())+3*np.einsum("psrt,tp", WC["qq3"], G_d@G_d.getH())-6*np.einsum("ptrs,tp", WC["qq1"], G_u@G_u.getH())-np.einsum("psrt,tp", WC["qq1"], G_u@G_u.getH())-3*np.einsum("psrt,tp", WC["qq3"], G_u@G_u.getH()))-6*np.einsum("rspt,tp", WC["qu1"], G_u.getH()@G_u)+6*np.einsum("rspt,tp", WC["qd1"], G_d.getH()@G_d)+2*GammaH*WC["CurlyPhiq1"]+Gammaq@WC["CurlyPhiq1"]+WC["CurlyPhiq1"]@Gammaq

    #I3 #co
    Beta["CurlyPhiq3"]=2/3*g**2*(1/4*WC["CurlyPhiEmptySquare"]+np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"]))*I3-17/3*g**2*WC["CurlyPhiq3"]+2/3*g**2*(np.einsum("ttrs", WC["lq3"])+np.einsum("rtts", WC["qq1"])+6*np.einsum("rstt", WC["qq3"])-np.einsum("rtts", WC["qq3"]))-1/2*WC["CurlyPhiEmptySquare"]*(G_u@G_u.getH()+G_d@G_d.getH())+1/2*(3*G_d@G_d.getH()@WC["CurlyPhiq1"]-3*G_u@G_u.getH()@WC["CurlyPhiq1"]+3*WC["CurlyPhiq1"]@G_d@G_d.getH()-3*WC["CurlyPhiq1"]@G_u@G_u.getH()+G_d@G_d.getH()@WC["CurlyPhiq3"]+G_u@G_u.getH()@WC["CurlyPhiq3"]+WC["CurlyPhiq3"]@G_d@G_d.getH()+WC["CurlyPhiq3"]@G_u@G_u.getH())-2*(6*np.einsum("rspt,tp", WC["qq3"], G_d@G_d.getH())+np.einsum("rtps,tp", WC["qq1"], G_d@G_d.getH())-np.einsum("rtps,tp", WC["qq3"], G_d@G_d.getH())+6*np.einsum("rspt,tp", WC["qq3"], G_u@G_u.getH())+np.einsum("rtps,tp", WC["qq1"], G_u@G_u.getH())-np.einsum("rtps,tp", WC["qq3"], G_u@G_u.getH()))-2*np.einsum("ptrs,tp", WC["lq3"], G_e@G_e.getH())+2*GammaH*WC["CurlyPhiq3"]+Gammaq@WC["CurlyPhiq3"]+WC["CurlyPhiq3"]@Gammaq

    #I3 #co
    Beta["CurlyPhiu"]=1/3*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhiu"]-2/3*gp**2*(np.einsum("ttrs", WC["eu"])+np.einsum("ttrs", WC["lu"])-np.einsum("ttrs", WC["qu1"])+np.einsum("rstt", WC["ud1"])-4*np.einsum("rstt", WC["uu"])-4/3*np.einsum("rtts", WC["uu"]))-(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])*G_u.getH()@G_u-2*G_u.getH()@WC["CurlyPhiq1"]@G_u+3*(G_u.getH()@G_u@WC["CurlyPhiu"]+WC["CurlyPhiu"]@G_u.getH()@G_u)+G_u.getH()@G_d@WC["CurlyPhiud"].getH()+WC["CurlyPhiud"]@G_d.getH()@G_u-4*(3*np.einsum("rspt,tp", WC["uu"], G_u.getH()@G_u)+np.einsum("rtps,tp", WC["uu"], G_u.getH()@G_u))+2*np.einsum("ptrs,tp", WC["eu"], G_e.getH()@G_e)-2*np.einsum("ptrs,tp", WC["lu"], G_e@G_e.getH())+6*np.einsum("rspt,tp", WC["ud1"], G_d.getH()@G_d)-6*np.einsum("ptrs,tp", WC["qu1"], G_d@G_d.getH())+6*np.einsum("ptrs,tp", WC["qu1"], G_u@G_u.getH())+2*GammaH*WC["CurlyPhiu"]+Gammau@WC["CurlyPhiu"]+WC["CurlyPhiu"]@Gammau

    #I3 #co
    Beta["CurlyPhid"]=-1/6*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhid"]-2/3*gp**2*(2*np.einsum("rstt", WC["dd"])+2/3*np.einsum("rtts", WC["dd"])+np.einsum("ttrs", WC["ed"])+np.einsum("ttrs", WC["ld"])-np.einsum("ttrs", WC["qd1"])-2*np.einsum("ttrs", WC["ud1"]))+(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])*G_d.getH()@G_d-2*G_d.getH()@WC["CurlyPhiq1"]@G_d+3*(G_d.getH()@G_d@WC["CurlyPhid"]+WC["CurlyPhid"]@G_d.getH()@G_d)-G_d.getH()@G_u@WC["CurlyPhiud"]-WC["CurlyPhiud"].getH()@G_u.getH()@G_d+4*(3*np.einsum("rspt,tp", WC["dd"], G_d.getH()@G_d)+np.einsum("rtps,tp", WC["dd"], G_d.getH()@G_d))+2*np.einsum("ptrs,tp", WC["ed"], G_e.getH()@G_e)-2*np.einsum("ptrs,tp", WC["ld"], G_e@G_e.getH())-6*np.einsum("ptrs,tp", WC["ud1"], G_u.getH()@G_u)-6*np.einsum("ptrs,tp", WC["qd1"], G_d@G_d.getH())+6*np.einsum("ptrs,tp", WC["qd1"], G_u@G_u.getH())+2*GammaH*WC["CurlyPhid"]+Gammad@WC["CurlyPhid"]+WC["CurlyPhid"]@Gammad

        #co
    Beta["CurlyPhiud"]=-3*gp**2*WC["CurlyPhiud"]+(2*WC["CurlyPhiEmptySquare"]-WC["CurlyPhiD"])*G_u.getH()@G_d-2*G_u.getH()@G_d@WC["CurlyPhid"]+2*WC["CurlyPhiu"]@G_u.getH()@G_d+4*(np.einsum("rtps,tp", WC["ud1"], G_u.getH()@G_d)+4/3*np.einsum("rtps,tp", WC["ud8"], G_u.getH()@G_d))+2*G_u.getH()@G_u@WC["CurlyPhiud"]+2*WC["CurlyPhiud"]@G_d.getH()@G_d+2*GammaH*WC["CurlyPhiud"]+Gammau@WC["CurlyPhiud"]+WC["CurlyPhiud"]@Gammad

    # the einsum function is strong
    Beta["ll"]=-1/6*gp**2*np.einsum("st,pr", WC["CurlyPhil1"], I3)-1/6*g**2*(np.einsum("st,pr", WC["CurlyPhil3"], I3)-2*np.einsum("sr,pt", WC["CurlyPhil3"], I3))+1/3*gp**2*(2*np.einsum("prww,st", WC["ll"], I3)+np.einsum("pwwr,st", WC["ll"], I3))-1/3*g**2*np.einsum("pwwr,st", WC["ll"], I3)+2/3*g**2*np.einsum("swwr,pt", WC["ll"], I3)-1/3*gp**2*np.einsum("prww,st", WC["lq1"], I3)-g**2*np.einsum("prww,st", WC["lq3"], I3)+2*g**2*np.einsum("ptww,rs", WC["lq3"], I3)+1/3*gp**2*(-2*np.einsum("prww,st", WC["lu"], I3)+np.einsum("prww,st", WC["ld"], I3)+np.einsum("prww,st", WC["le"], I3))-1/2*(np.einsum("pr,st", G_e@G_e.getH(), WC["CurlyPhil1"])-np.einsum("pr,st", G_e@G_e.getH(), WC["CurlyPhil3"]))-np.einsum("pt,sr", G_e@G_e.getH(), WC["CurlyPhil3"])-1/2*np.einsum("sv,tw,prvw", G_e, np.conj(G_e), WC["le"])+np.einsum("pv,vrst", Gammal, WC["ll"])+np.einsum("pvst,vr", WC["ll"], Gammal)-1/6*gp**2*np.einsum("pr,st", WC["CurlyPhil1"], I3)-1/6*g**2*(np.einsum("pr,st", WC["CurlyPhil3"], I3)-2*np.einsum("pt,sr", WC["CurlyPhil3"], I3))+1/3*gp**2*(2*np.einsum("stww,pr", WC["ll"], I3)+np.einsum("swwt,pr", WC["ll"], I3))-1/3*g**2*np.einsum("swwt,pr", WC["ll"], I3)+2/3*g**2*np.einsum("pwwt,sr", WC["ll"], I3)-1/3*gp**2*np.einsum("stww,pr", WC["lq1"], I3)-g**2*np.einsum("stww,pr", WC["lq3"], I3)+2*g**2*np.einsum("srww,tp", WC["lq3"], I3)+1/3*gp**2*(-2*np.einsum("stww,pr", WC["lu"], I3)+np.einsum("stww,pr", WC["ld"], I3)+np.einsum("stww,pr", WC["le"], I3))-1/2*(np.einsum("st,pr", G_e@G_e.getH(), WC["CurlyPhil1"])-np.einsum("st,pr", G_e@G_e.getH(), WC["CurlyPhil3"]))-np.einsum("sr,pt", G_e@G_e.getH(), WC["CurlyPhil3"])-1/2*np.einsum("pv,rw,stvw", G_e, np.conj(G_e), WC["le"])+np.einsum("sv,vtpr", Gammal, WC["ll"])+np.einsum("svpr,vt", WC["ll"], Gammal)+6*g**2*np.einsum("ptsr", WC["ll"])+3*(gp**2-g**2)*np.einsum("prst", WC["ll"])


    Beta["qq1"]=1/18*gp**2*np.einsum("st,pr", WC["CurlyPhiq1"], I3)-1/9*gp**2*np.einsum("wwst,pr", WC["lq1"], I3)+1/9*gp**2*(2*np.einsum("prww,st", WC["qq1"], I3)+1/3*(np.einsum("pwwr,st", WC["qq1"], I3)+3*np.einsum("pwwr,st", WC["qq3"], I3)))+1/3*gs**2*(np.einsum("swwr,pt", WC["qq1"], I3)+3*np.einsum("swwr,pt", WC["qq3"], I3))-2/9*gs**2*(np.einsum("pwwr,st", WC["qq1"], I3)+3*np.einsum("pwwr,st", WC["qq3"], I3))+2/9*gp**2*np.einsum("prww,st", WC["qu1"], I3)-1/9*gp**2*np.einsum("prww,st", WC["qd1"], I3)+1/12*gs**2*(np.einsum("srww,pt", WC["qu8"], I3)+np.einsum("srww,pt", WC["qd8"], I3))-1/18*gs**2*(np.einsum("prww,st", WC["qu8"], I3)+np.einsum("prww,st", WC["qd8"], I3))-1/9*gp**2*np.einsum("prww,st", WC["qe"], I3)+1/2*(np.einsum("pr,st", G_u@G_u.getH(), WC["CurlyPhiq1"])-np.einsum("pr,st", G_d@G_d.getH(), WC["CurlyPhiq1"]))-1/2*(np.einsum("pv,rw,stvw", G_u, np.conj(G_u), WC["qu1"])-1/6*np.einsum("pv,rw,stvw", G_u, np.conj(G_u), WC["qu8"]))-1/2*(np.einsum("pv,rw,stvw", G_d, np.conj(G_d), WC["qd1"])-1/6*np.einsum("pv,rw,stvw", G_d, np.conj(G_d), WC["qd8"]))-1/8*(np.einsum("pv,tw,srvw", G_u, np.conj(G_u), WC["qu8"])+np.einsum("pv,tw,srvw", G_d, np.conj(G_d), WC["qd8"]))-1/8*(np.einsum("tw,rv,pvsw", np.conj(G_d), np.conj(G_u), WC["quqd1"])-1/6*np.einsum("tw,rv,pvsw", np.conj(G_d), np.conj(G_u), WC["quqd8"]))-1/8*(np.einsum("sw,pv,rvtw", G_d, G_u, np.conj(WC["quqd1"]))-1/6*np.einsum("sw,pv,rvtw", G_d, G_u, np.conj(WC["quqd8"])))+1/16*(np.einsum("tw,rv,svpw", np.conj(G_d), np.conj(G_u), WC["quqd8"])+np.einsum("sw,pv,tvrw", G_d, G_u, np.conj(WC["quqd8"])))+np.einsum("pv,vrst", Gammaq, WC["qq1"])+np.einsum("pvst,vr", WC["qq1"], Gammaq)+1/18*gp**2*np.einsum("pr,st", WC["CurlyPhiq1"], I3)-1/9*gp**2*np.einsum("wwpr,st", WC["lq1"], I3)+1/9*gp**2*(2*np.einsum("stww,pr", WC["qq1"], I3)+1/3*(np.einsum("swwt,pr", WC["qq1"], I3)+3*np.einsum("swwt,pr", WC["qq3"], I3)))+1/3*gs**2*(np.einsum("pwwt,sr", WC["qq1"], I3)+3*np.einsum("pwwt,sr", WC["qq3"], I3))-2/9*gs**2*(np.einsum("swwt,pr", WC["qq1"], I3)+3*np.einsum("swwt,pr", WC["qq3"], I3))+2/9*gp**2*np.einsum("stww,pr", WC["qu1"], I3)-1/9*gp**2*np.einsum("stww,pr", WC["qd1"], I3)+1/12*gs**2*(np.einsum("ptww,sr", WC["qu8"], I3)+np.einsum("ptww,sr", WC["qd8"], I3))-1/18*gs**2*(np.einsum("stww,pr", WC["qu8"], I3)+np.einsum("stww,pr", WC["qd8"], I3))-1/9*gp**2*np.einsum("stww,pr", WC["qe"], I3)+1/2*(np.einsum("st,pr", G_u@G_u.getH(), WC["CurlyPhiq1"])-np.einsum("st,pr", G_d@G_d.getH(), WC["CurlyPhiq1"]))-1/2*(np.einsum("sv,tw,prvw", G_u, np.conj(G_u), WC["qu1"])-1/6*np.einsum("sv,tw,prvw", G_u, np.conj(G_u), WC["qu8"]))-1/2*(np.einsum("sv,tw,prvw", G_d, np.conj(G_d), WC["qd1"])-1/6*np.einsum("sv,tw,prvw", G_d, np.conj(G_d), WC["qd8"]))-1/8*(np.einsum("sv,rw,ptvw", G_u, np.conj(G_u), WC["qu8"])+np.einsum("sv,rw,ptvw", G_d, np.conj(G_d), WC["qd8"]))-1/8*(np.einsum("rw,tv,svpw", np.conj(G_d), np.conj(G_u), WC["quqd1"])-1/6*np.einsum("rw,tv,svpw", np.conj(G_d), np.conj(G_u), WC["quqd8"]))-1/8*(np.einsum("pw,sv,tvrw", G_d, G_u, np.conj(WC["quqd1"]))-1/6*np.einsum("pw,sv,tvrw", G_d, G_u, np.conj(WC["quqd8"])))+1/16*(np.einsum("rw,tv,pvsw", np.conj(G_d), np.conj(G_u), WC["quqd8"])+np.einsum("pw,sv,rvtw", G_d, G_u, np.conj(WC["quqd8"])))+np.einsum("sv,vtpr", Gammaq, WC["qq1"])+np.einsum("svpr,vt", WC["qq1"], Gammaq)+9*g**2*np.einsum("prst", WC["qq3"])-2*(gs**2-1/6*gp**2)*np.einsum("prst", WC["qq1"])+3*gs**2*(np.einsum("ptsr", WC["qq1"])+3*np.einsum("ptsr", WC["qq3"]))


    Beta["qq3"]=1/6*g**2*np.einsum("st,pr", WC["CurlyPhiq3"], I3)+1/3*g**2*np.einsum("wwst,pr", WC["lq3"], I3)+1/3*g**2*(np.einsum("pwwr,st", WC["qq1"], I3)-np.einsum("pwwr,st", WC["qq3"], I3))+2*g**2*np.einsum("prww,st", WC["qq3"], I3)+1/3*gs**2*(np.einsum("swwr,pt", WC["qq1"], I3)+3*np.einsum("swwr,pt", WC["qq3"], I3))+1/12*gs**2*(np.einsum("srww,pt", WC["qu8"], I3)+np.einsum("srww,pt", WC["qd8"], I3))-1/2*(np.einsum("pr,st", G_u@G_u.getH(), WC["CurlyPhiq3"])+np.einsum("pr,st", G_d@G_d.getH(), WC["CurlyPhiq3"]))-1/8*(np.einsum("pv,tw,srvw", G_u, np.conj(G_u), WC["qu8"])+np.einsum("pv,tw,srvw", G_d, np.conj(G_d), WC["qd8"]))+1/8*(np.einsum("tw,rv,pvsw", np.conj(G_d), np.conj(G_u), WC["quqd1"])-1/6*np.einsum("tw,rv,pvsw", np.conj(G_d), np.conj(G_u), WC["quqd8"]))+1/8*(np.einsum("sw,pv,rvtw", G_d, G_u, np.conj(WC["quqd1"]))-1/6*np.einsum("sw,pv,rvtw", G_d, G_u, np.conj(WC["quqd8"])))-1/16*(np.einsum("tw,rv,svpw", np.conj(G_d), np.conj(G_u), WC["quqd8"])+np.einsum("sw,pv,tvrw", G_d, G_u, np.conj(WC["quqd8"])))+np.einsum("pv,vrst", Gammaq, WC["qq3"])+np.einsum("pvst,vr", WC["qq3"], Gammaq)+1/6*g**2*np.einsum("pr,st", WC["CurlyPhiq3"], I3)+1/3*g**2*np.einsum("wwpr,st", WC["lq3"], I3)+1/3*g**2*(np.einsum("swwt,pr", WC["qq1"], I3)-np.einsum("swwt,pr", WC["qq3"], I3))+2*g**2*np.einsum("stww,pr", WC["qq3"], I3)+1/3*gs**2*(np.einsum("pwwt,sr", WC["qq1"], I3)+3*np.einsum("pwwt,sr", WC["qq3"], I3))+1/12*gs**2*(np.einsum("ptww,sr", WC["qu8"], I3)+np.einsum("ptww,sr", WC["qd8"], I3))-1/2*(np.einsum("st,pr", G_u@G_u.getH(), WC["CurlyPhiq3"])+np.einsum("st,pr", G_d@G_d.getH(), WC["CurlyPhiq3"]))-1/8*(np.einsum("sv,rw,ptvw", G_u, np.conj(G_u), WC["qu8"])+np.einsum("sv,rw,ptvw", G_d, np.conj(G_d), WC["qd8"]))+1/8*(np.einsum("rw,tv,svpw", np.conj(G_d), np.conj(G_u), WC["quqd1"])-1/6*np.einsum("rw,tv,svpw", np.conj(G_d), np.conj(G_u), WC["quqd8"]))+1/8*(np.einsum("pw,sv,tvrw", G_d, G_u, np.conj(WC["quqd1"]))-1/6*np.einsum("pw,sv,tvrw", G_d, G_u, np.conj(WC["quqd8"])))-1/16*(np.einsum("rw,tv,pvsw", np.conj(G_d), np.conj(G_u), WC["quqd8"])+np.einsum("pw,sv,rvtw", G_d, G_u, np.conj(WC["quqd8"])))+np.einsum("sv,vtpr", Gammaq, WC["qq3"])+np.einsum("svpr,vt", WC["qq3"], Gammaq)+3*gs**2*(np.einsum("ptsr", WC["qq1"])-np.einsum("ptsr", WC["qq3"]))-2*(gs**2+3*g**2-1/6*gp**2)*np.einsum("prst", WC["qq3"])+3*g**2*np.einsum("prst", WC["qq1"])

    #the terms are equal, but the order is not. No wonder if you check some differences inside
    Beta["lq1"]=-1/3*gp**2*np.einsum("st,pr", WC["CurlyPhiq1"], I3)+1/9*gp**2*np.einsum("pr,st", WC["CurlyPhil1"], I3)-2/9*gp**2*(2*np.einsum("prww,st", WC["ll"], I3)+np.einsum("pwwr,st", WC["ll"], I3))+2/9*gp**2*np.einsum("prww,st", WC["lq1"], I3)+2/3*gp**2*np.einsum("wwst,pr", WC["lq1"], I3)-2/9*gp**2*(6*np.einsum("stww,pr", WC["qq1"], I3)+np.einsum("swwt,pr", WC["qq1"], I3)+3*np.einsum("swwt,pr", WC["qq3"], I3))-2/3*gp**2*(2*np.einsum("stww,pr", WC["qu1"], I3)-np.einsum("stww,pr", WC["qd1"], I3)-np.einsum("stww,pr", WC["qe"], I3))+2/9*gp**2*(2*np.einsum("prww,st", WC["lu"], I3)-np.einsum("prww,st", WC["ld"], I3)-np.einsum("prww,st", WC["le"], I3))-gp**2*np.einsum("prst", WC["lq1"])+9*g**2*np.einsum("prst", WC["lq3"])-np.einsum("pr,st", G_e@G_e.getH(), WC["CurlyPhiq1"])+np.einsum("st,pr", G_u@G_u.getH(), WC["CurlyPhil1"])-np.einsum("st,pr", G_d@G_d.getH(), WC["CurlyPhil1"])+1/4*(np.einsum("tw,rv,pvsw", np.conj(G_u), np.conj(G_e), WC["lequ1"])-12*np.einsum("tw,rv,pvsw", np.conj(G_u), np.conj(G_e), WC["lequ3"])+np.einsum("sw,pv,rvtw", G_u, G_e, np.conj(WC["lequ1"]))-12*np.einsum("sw,pv,rvtw", G_u, G_e, np.conj(WC["lequ3"])))-np.einsum("sv,tw,prvw", G_u, np.conj(G_u), WC["lu"])-np.einsum("sv,tw,prvw", G_d, np.conj(G_d), WC["ld"])-np.einsum("pv,rw,stvw", G_e, np.conj(G_e), WC["qe"])+1/4*(np.einsum("sw,rv,pvwt", G_d, np.conj(G_e), WC["ledq"])+np.einsum("pv,tw,rvws", G_e, np.conj(G_d), np.conj(WC["ledq"])))+np.einsum("pv,vrst", Gammal, WC["lq1"])+np.einsum("sv,prvt", Gammaq, WC["lq1"])+np.einsum("pvst,vr", WC["lq1"], Gammal)+np.einsum("prsv,vt", WC["lq1"], Gammaq)


    Beta["lq3"]=1/3*g**2*(np.einsum("st,pr", WC["CurlyPhiq3"], I3)+np.einsum("pr,st", WC["CurlyPhil3"], I3))+2/3*g**2*(3*np.einsum("prww,st", WC["lq3"], I3)+np.einsum("wwst,pr", WC["lq3"], I3))+2/3*g**2*(6*np.einsum("stww,pr", WC["qq3"], I3)+np.einsum("swwt,pr", WC["qq1"], I3)-np.einsum("swwt,pr", WC["qq3"], I3))+2/3*g**2*np.einsum("pwwr,st", WC["ll"], I3)+3*g**2*np.einsum("prst", WC["lq1"])-(6*g**2+gp**2)*np.einsum("prst", WC["lq3"])-np.einsum("pr,st", G_e@G_e.getH(), WC["CurlyPhiq3"])-np.einsum("st,pr", G_u@G_u.getH(), WC["CurlyPhil3"])-np.einsum("st,pr", G_d@G_d.getH(), WC["CurlyPhil3"])-1/4*(np.einsum("tw,rv,pvsw", np.conj(G_u), np.conj(G_e), WC["lequ1"])-12*np.einsum("tw,rv,pvsw", np.conj(G_u), np.conj(G_e), WC["lequ3"])+np.einsum("sw,pv,rvtw", G_u, G_e, np.conj(WC["lequ1"]))-12*np.einsum("sw,pv,rvtw", G_u, G_e, np.conj(WC["lequ3"])))+1/4*(np.einsum("sw,rv,pvwt", G_d, np.conj(G_e), WC["ledq"])+np.einsum("pv,tw,rvws", G_e, np.conj(G_d), np.conj(WC["ledq"])))+np.einsum("pv,vrst", Gammal, WC["lq3"])+np.einsum("sv,prvt", Gammaq, WC["lq3"])+np.einsum("pvst,vr", WC["lq3"], Gammal)+np.einsum("prsv,vt", WC["lq3"], Gammaq)

    #order
    Beta["ee"]=-1/3*gp**2*np.einsum("st,pr", WC["CurlyPhie"], I3)+2/3*gp**2*(np.einsum("wwpr,st", WC["le"], I3)-np.einsum("wwpr,st", WC["qe"], I3)-2*np.einsum("prww,st", WC["eu"], I3)+np.einsum("prww,st", WC["ed"], I3)+4*np.einsum("prww,st", WC["ee"], I3))+np.einsum("pr,st", G_e.getH()@G_e, WC["CurlyPhie"])-np.einsum("wr,vp,vwst", G_e, np.conj(G_e), WC["le"])+np.einsum("pv,vrst", Gammae, WC["ee"])+np.einsum("pvst,vr", WC["ee"], Gammae)-1/3*gp**2*np.einsum("pr,st", WC["CurlyPhie"], I3)+2/3*gp**2*(np.einsum("wwst,pr", WC["le"], I3)-np.einsum("wwst,pr", WC["qe"], I3)-2*np.einsum("stww,pr", WC["eu"], I3)+np.einsum("stww,pr", WC["ed"], I3)+4*np.einsum("wwst,pr", WC["ee"], I3))+np.einsum("st,pr", G_e.getH()@G_e, WC["CurlyPhie"])-np.einsum("wt,vs,vwpr", G_e, np.conj(G_e), WC["le"])+np.einsum("sv,vtpr", Gammae, WC["ee"])+np.einsum("svpr,vt", WC["ee"], Gammae)+12*gp**2*np.einsum("prst", WC["ee"])

    #order
    Beta["uu"]=2/9*gp**2*np.einsum("st,pr", WC["CurlyPhiu"], I3)-4/9*gp**2*(np.einsum("wwst,pr", WC["eu"], I3)+np.einsum("wwst,pr", WC["lu"], I3)-np.einsum("wwst,pr", WC["qu1"], I3)-4*np.einsum("wwst,pr", WC["uu"], I3)-4/3*np.einsum("swwt,pr", WC["uu"], I3))-1/9*gs**2*(np.einsum("wwst,pr", WC["qu8"], I3)-3*np.einsum("wwsr,pt", WC["qu8"], I3))+2/3*gs**2*np.einsum("pwwt,rs", WC["uu"], I3)-2/9*gs**2*np.einsum("swwt,pr", WC["uu"], I3)-4/9*gp**2*np.einsum("stww,pr", WC["ud1"], I3)-1/18*gs**2*(np.einsum("stww,pr", WC["ud8"], I3)-3*np.einsum("srww,pt", WC["ud8"], I3))-np.einsum("pr,st", G_u.getH()@G_u, WC["CurlyPhiu"])-(np.einsum("wr,vp,vwst", G_u, np.conj(G_u), WC["qu1"])-1/6*np.einsum("wr,vp,vwst", G_u, np.conj(G_u), WC["qu8"]))-1/2*np.einsum("wr,vs,vwpt", G_u, np.conj(G_u), WC["qu8"])+np.einsum("pv,vrst", Gammau, WC["uu"])+np.einsum("pvst,vr", WC["uu"], Gammau)+2/9*gp**2*np.einsum("pr,st", WC["CurlyPhiu"], I3)-4/9*gp**2*(np.einsum("wwpr,st", WC["eu"], I3)+np.einsum("wwpr,st", WC["lu"], I3)-np.einsum("wwpr,st", WC["qu1"], I3)-4*np.einsum("wwpr,st", WC["uu"], I3)-4/3*np.einsum("pwwr,st", WC["uu"], I3))-1/9*gs**2*(np.einsum("wwpr,st", WC["qu8"], I3)-3*np.einsum("wwpt,sr", WC["qu8"], I3))+2/3*gs**2*np.einsum("swwr,tp", WC["uu"], I3)-2/9*gs**2*np.einsum("pwwr,st", WC["uu"], I3)-4/9*gp**2*np.einsum("prww,st", WC["ud1"], I3)-1/18*gs**2*(np.einsum("prww,st", WC["ud8"], I3)-3*np.einsum("ptww,sr", WC["ud8"], I3))-np.einsum("st,pr", G_u.getH()@G_u, WC["CurlyPhiu"])-(np.einsum("wt,vs,vwpr", G_u, np.conj(G_u), WC["qu1"])-1/6*np.einsum("wt,vs,vwpr", G_u, np.conj(G_u), WC["qu8"]))-1/2*np.einsum("wt,vp,vwsr", G_u, np.conj(G_u), WC["qu8"])+np.einsum("sv,vtpr", Gammau, WC["uu"])+np.einsum("svpr,vt", WC["uu"], Gammau)+2*(8/3*gp**2-gs**2)*np.einsum("prst", WC["uu"])+6*gs**2*np.einsum("ptsr", WC["uu"])

    #order
    Beta["dd"]=-1/9*gp**2*np.einsum("st,pr", WC["CurlyPhid"], I3)+2/9*gp**2*(np.einsum("wwst,pr", WC["ed"], I3)+np.einsum("wwst,pr", WC["ld"], I3)-np.einsum("wwst,pr", WC["qd1"], I3)+2*np.einsum("wwst,pr", WC["dd"], I3)+2/3*np.einsum("swwt,pr", WC["dd"], I3))-1/9*gs**2*(np.einsum("wwst,pr", WC["qd8"], I3)-3*np.einsum("wwsr,pt", WC["qd8"], I3))+2/3*gs**2*np.einsum("pwwt,rs", WC["dd"], I3)-2/9*gs**2*np.einsum("swwt,pr", WC["dd"], I3)-4/9*gp**2*np.einsum("wwst,pr", WC["ud1"], I3)-1/18*gs**2*(np.einsum("wwst,pr", WC["ud8"], I3)-3*np.einsum("wwsr,pt", WC["ud8"], I3))+np.einsum("pr,st", G_d.getH()@G_d, WC["CurlyPhid"])-(np.einsum("wr,vp,vwst", G_d, np.conj(G_d), WC["qd1"])-1/6*np.einsum("wr,vp,vwst", G_d, np.conj(G_d), WC["qd8"]))-1/2*np.einsum("wr,vs,vwpt", G_d, np.conj(G_d), WC["qd8"])+np.einsum("pv,vrst", Gammad, WC["dd"])+np.einsum("pvst,vr", WC["dd"], Gammad)-1/9*gp**2*np.einsum("pr,st", WC["CurlyPhid"], I3)+2/9*gp**2*(np.einsum("wwpr,st", WC["ed"], I3)+np.einsum("wwpr,st", WC["ld"], I3)-np.einsum("wwpr,st", WC["qd1"], I3)+2*np.einsum("wwpr,st", WC["dd"], I3)+2/3*np.einsum("pwwr,st", WC["dd"], I3))-1/9*gs**2*(np.einsum("wwpr,st", WC["qd8"], I3)-3*np.einsum("wwpt,sr", WC["qd8"], I3))+2/3*gs**2*np.einsum("swwr,tp", WC["dd"], I3)-2/9*gs**2*np.einsum("pwwr,st", WC["dd"], I3)-4/9*gp**2*np.einsum("wwpr,st", WC["ud1"], I3)-1/18*gs**2*(np.einsum("wwpr,st", WC["ud8"], I3)-3*np.einsum("wwpt,sr", WC["ud8"], I3))+np.einsum("st,pr", G_d.getH()@G_d, WC["CurlyPhid"])-(np.einsum("wt,vs,vwpr", G_d, np.conj(G_d), WC["qd1"])-1/6*np.einsum("wt,vs,vwpr", G_d, np.conj(G_d), WC["qd8"]))-1/2*np.einsum("wt,vp,vwsr", G_d, np.conj(G_d), WC["qd8"])+np.einsum("sv,vtpr", Gammad, WC["dd"])+np.einsum("svpr,vt", WC["dd"], Gammad)+2*(2/3*gp**2-gs**2)*np.einsum("prst", WC["dd"])+6*gs**2*np.einsum("ptsr", WC["dd"])


    Beta["eu"]=-2/3*gp**2*(np.einsum("st,pr", WC["CurlyPhiu"], I3)+2*(np.einsum("wwst,pr", WC["qu1"], I3)-np.einsum("wwst,pr", WC["lu"], I3)+4*np.einsum("wwst,pr", WC["uu"], I3)-np.einsum("wwst,pr", WC["eu"], I3)-np.einsum("stww,pr", WC["ud1"], I3))+8/3*np.einsum("swwt,pr", WC["uu"], I3))+4/9*gp**2*(np.einsum("pr,st", WC["CurlyPhie"], I3)+2*(np.einsum("wwpr,st", WC["qe"], I3)-np.einsum("wwpr,st", WC["le"], I3)-4*np.einsum("prww,st", WC["ee"], I3)+2*np.einsum("prww,st", WC["eu"], I3)-np.einsum("prww,st", WC["ed"], I3)))-8*gp**2*np.einsum("prst", WC["eu"])+2*np.einsum("pr,st", G_e.getH()@G_e, WC["CurlyPhiu"])-2*np.einsum("st,pr", G_u.getH()@G_u, WC["CurlyPhie"])+np.einsum("vp,ws,vrwt", np.conj(G_e), np.conj(G_u), WC["lequ1"])-12*np.einsum("vp,ws,vrwt", np.conj(G_e), np.conj(G_u), WC["lequ3"])+np.einsum("vr,wt,vpws", G_e, G_u, np.conj(WC["lequ1"]))-12*np.einsum("vr,wt,vpws", G_e, G_u, np.conj(WC["lequ3"]))-2*np.einsum("vp,wr,vwst", np.conj(G_e), G_e, WC["lu"])-2*np.einsum("vs,wt,vwpr", np.conj(G_u), G_u, WC["qe"])+np.einsum("pv,vrst", Gammae, WC["eu"])+np.einsum("sv,prvt", Gammau, WC["eu"])+np.einsum("pvst,vr", WC["eu"], Gammae)+np.einsum("prsv,vt", WC["eu"], Gammau)


    Beta["ed"]=-2/3*gp**2*(np.einsum("st,pr", WC["CurlyPhid"], I3)+2*(np.einsum("wwst,pr", WC["qd1"], I3)-np.einsum("wwst,pr", WC["ld"], I3)-2*np.einsum("wwst,pr", WC["dd"], I3)-np.einsum("wwst,pr", WC["ed"], I3)+2*np.einsum("wwst,pr", WC["ud1"], I3))-4/3*np.einsum("swwt,pr", WC["dd"], I3))-2/9*gp**2*(np.einsum("pr,st", WC["CurlyPhie"], I3)+2*(np.einsum("wwpr,st", WC["qe"], I3)-np.einsum("wwpr,st", WC["le"], I3)-4*np.einsum("prww,st", WC["ee"], I3)-np.einsum("prww,st", WC["ed"], I3)+2*np.einsum("prww,st", WC["eu"], I3)))+4*gp**2*np.einsum("prst", WC["ed"])+2*np.einsum("pr,st", G_e.getH()@G_e, WC["CurlyPhid"])+2*np.einsum("st,pr", G_d.getH()@G_d, WC["CurlyPhie"])-2*np.einsum("vp,wr,vwst", np.conj(G_e), G_e, WC["ld"])-2*np.einsum("vs,wt,vwpr", np.conj(G_d), G_d, WC["qe"])+np.einsum("vp,wt,vrsw", np.conj(G_e), G_d, WC["ledq"])+np.einsum("vr,ws,vptw", G_e, np.conj(G_d), np.conj(WC["ledq"]))+np.einsum("pv,vrst", Gammae, WC["ed"])+np.einsum("sv,prvt", Gammad, WC["ed"])+np.einsum("pvst,vr", WC["ed"], Gammae)+np.einsum("prsv,vt", WC["ed"], Gammad)

    #order
    Beta["ud1"]=4/9*gp**2*(np.einsum("st,pr", WC["CurlyPhid"], I3)+2*(np.einsum("wwst,pr", WC["qd1"], I3)-np.einsum("wwst,pr", WC["ld"], I3)-2*np.einsum("wwst,pr", WC["dd"], I3)+2*np.einsum("wwst,pr", WC["ud1"], I3)-np.einsum("wwst,pr", WC["ed"], I3))-4/3*np.einsum("swwt,pr", WC["dd"], I3))-2/9*gp**2*(np.einsum("pr,st", WC["CurlyPhiu"], I3)+2*(np.einsum("wwpr,st", WC["qu1"], I3)-np.einsum("wwpr,st", WC["lu"], I3)+4*np.einsum("wwpr,st", WC["uu"], I3)-np.einsum("prww,st", WC["ud1"], I3)-np.einsum("wwpr,st", WC["eu"], I3))+8/3*np.einsum("pwwr,st", WC["uu"], I3))-8/3*(gp**2*np.einsum("prst", WC["ud1"])-gs**2*np.einsum("prst", WC["ud8"]))-2*np.einsum("pr,st", G_u.getH()@G_u, WC["CurlyPhid"])+2*np.einsum("st,pr", G_d.getH()@G_d, WC["CurlyPhiu"])+2/3*np.einsum("sr,pt", G_d.getH()@G_u, WC["CurlyPhiud"])+2/3*np.einsum("pt,rs", G_u.getH()@G_d, np.conj(WC["CurlyPhiud"]))+1/3*(np.einsum("vs,wp,vrwt", np.conj(G_d), np.conj(G_u), WC["quqd1"])+4/3*np.einsum("vs,wp,vrwt", np.conj(G_d), np.conj(G_u), WC["quqd8"])+np.einsum("vt,wr,vpws", G_d, G_u, np.conj(WC["quqd1"]))+4/3*np.einsum("vt,wr,vpws", G_d, G_u, np.conj(WC["quqd8"])))-np.einsum("ws,vp,vrwt", np.conj(G_d), np.conj(G_u), WC["quqd1"])-np.einsum("wt,vr,vpws", G_d, G_u, np.conj(WC["quqd1"]))-2*np.einsum("vp,wr,vwst", np.conj(G_u), G_u, WC["qd1"])-2*np.einsum("vs,wt,vwpr", np.conj(G_d), G_d, WC["qu1"])+np.einsum("pv,vrst", Gammau, WC["ud1"])+np.einsum("sv,prvt", Gammad, WC["ud1"])+np.einsum("pvst,vr", WC["ud1"], Gammau)+np.einsum("prsv,vt", WC["ud1"], Gammad)

    #order
    Beta["ud8"]=8/3*gs**2*np.einsum("pwwr,st", WC["uu"], I3)+8/3*gs**2*np.einsum("swwt,pr", WC["dd"], I3)+4/3*gs**2*np.einsum("wwpr,st", WC["qu8"], I3)+4/3*gs**2*np.einsum("wwst,pr", WC["qd8"], I3)+2/3*gs**2*np.einsum("prww,st", WC["ud8"], I3)+2/3*gs**2*np.einsum("wwst,pr", WC["ud8"], I3)-4*(2/3*gp**2+gs**2)*np.einsum("prst", WC["ud8"])+12*gs**2*np.einsum("prst", WC["ud1"])+4*np.einsum("sr,pt", G_d.getH()@G_u, WC["CurlyPhiud"])+4*np.einsum("pt,rs", G_u.getH()@G_d, np.conj(WC["CurlyPhiud"]))+2*(np.einsum("vs,wp,vrwt", np.conj(G_d), np.conj(G_u), WC["quqd1"])-1/6*np.einsum("vs,wp,vrwt", np.conj(G_d), np.conj(G_u), WC["quqd8"])+np.einsum("vt,wr,vpws", G_d, G_u, np.conj(WC["quqd1"]))-1/6*np.einsum("vt,wr,vpws", G_d, G_u, np.conj(WC["quqd8"])))-2*np.einsum("vp,wr,vwst", np.conj(G_u), G_u, WC["qd8"])-2*np.einsum("vs,wt,vwpr", np.conj(G_d), G_d, WC["qu8"])-(np.einsum("ws,vp,vrwt", np.conj(G_d), np.conj(G_u), WC["quqd8"])+np.einsum("wt,vr,vpws", G_d, G_u, np.conj(WC["quqd8"])))+np.einsum("pv,vrst", Gammau, WC["ud8"])+np.einsum("sv,prvt", Gammad, WC["ud8"])+np.einsum("pvst,vr", WC["ud8"], Gammau)+np.einsum("prsv,vt", WC["ud8"], Gammad)


    Beta["le"]=-1/3*gp**2*np.einsum("st,pr", WC["CurlyPhie"], I3)-2/3*gp**2*np.einsum("pr,st", WC["CurlyPhil1"], I3)+8/3*gp**2*np.einsum("prww,st", WC["ll"], I3)+4/3*gp**2*np.einsum("pwwr,st", WC["ll"], I3)-4/3*gp**2*np.einsum("prww,st", WC["lq1"], I3)-2/3*gp**2*np.einsum("wwst,pr", WC["qe"], I3)+4/3*gp**2*np.einsum("prww,st", WC["le"], I3)+2/3*gp**2*np.einsum("wwst,pr", WC["le"], I3)-8/3*gp**2*np.einsum("prww,st", WC["lu"], I3)+4/3*gp**2*np.einsum("prww,st", WC["ld"], I3)-4/3*gp**2*np.einsum("stww,pr", WC["eu"], I3)+2/3*gp**2*np.einsum("stww,pr", WC["ed"], I3)+8/3*gp**2*np.einsum("wwst,pr", WC["ee"], I3)-6*gp**2*np.einsum("prst", WC["le"])+np.einsum("rs,pt", np.conj(G_e), Xie)+np.einsum("pt,rs", G_e, np.conj(Xie))-np.einsum("pr,st", G_e@G_e.getH(), WC["CurlyPhie"])+2*np.einsum("st,pr", G_e.getH()@G_e, WC["CurlyPhil1"])-4*np.einsum("pv,rw,vtsw", G_e, np.conj(G_e), WC["ee"])+np.einsum("pw,vs,vrwt", G_e, np.conj(G_e), WC["le"])-2*np.einsum("wt,vs,pwvr", G_e, np.conj(G_e), WC["ll"])-4*np.einsum("wt,vs,prvw", G_e, np.conj(G_e), WC["ll"])+np.einsum("vt,rw,pvsw", G_e, np.conj(G_e), WC["le"])+np.einsum("pv,vrst", Gammal, WC["le"])+np.einsum("sv,prvt", Gammae, WC["le"])+np.einsum("pvst,vr", WC["le"], Gammal)+np.einsum("prsv,vt", WC["le"], Gammae)

    #order
    Beta["lu"]=-1/3*gp**2*np.einsum("st,pr", WC["CurlyPhiu"], I3)+4/9*gp**2*np.einsum("pr,st", WC["CurlyPhil1"], I3)-16/9*gp**2*np.einsum("prww,st", WC["ll"], I3)-8/9*gp**2*np.einsum("pwwr,st", WC["ll"], I3)+8/9*gp**2*np.einsum("prww,st", WC["lq1"], I3)-2/3*gp**2*np.einsum("wwst,pr", WC["qu1"], I3)+16/9*gp**2*np.einsum("prww,st", WC["lu"], I3)+2/3*gp**2*np.einsum("wwst,pr", WC["lu"], I3)-8/9*gp**2*np.einsum("prww,st", WC["ld"], I3)-8/9*gp**2*np.einsum("prww,st", WC["le"], I3)+2/3*gp**2*np.einsum("stww,pr", WC["ud1"], I3)+2/3*gp**2*np.einsum("wwst,pr", WC["eu"], I3)-8/3*gp**2*np.einsum("stww,pr", WC["uu"], I3)-8/9*gp**2*np.einsum("swwt,pr", WC["uu"], I3)+4*gp**2*np.einsum("prst", WC["lu"])-np.einsum("pr,st", G_e@G_e.getH(), WC["CurlyPhiu"])-2*np.einsum("st,pr", G_u.getH()@G_u, WC["CurlyPhil1"])-1/2*(np.einsum("rv,ws,pvwt", np.conj(G_e), np.conj(G_u), WC["lequ1"])+12*np.einsum("rv,ws,pvwt", np.conj(G_e), np.conj(G_u), WC["lequ3"]))-1/2*(np.einsum("pv,wt,rvws", G_e, G_u, np.conj(WC["lequ1"]))+12*np.einsum("pv,wt,rvws", G_e, G_u, np.conj(WC["lequ3"])))-2*np.einsum("vs,wt,prvw", np.conj(G_u), G_u, WC["lq1"])-np.einsum("rw,pv,vwst", np.conj(G_e), G_e, WC["eu"])+np.einsum("pv,vrst", Gammal, WC["lu"])+np.einsum("sv,prvt", Gammau, WC["lu"])+np.einsum("pvst,vr", WC["lu"], Gammal)+np.einsum("prsv,vt", WC["lu"], Gammau)


    Beta["ld"]=-1/3*gp**2*np.einsum("st,pr", WC["CurlyPhid"], I3)-2/9*gp**2*np.einsum("pr,st", WC["CurlyPhil1"], I3)+8/9*gp**2*np.einsum("prww,st", WC["ll"], I3)+4/9*gp**2*np.einsum("pwwr,st", WC["ll"], I3)-4/9*gp**2*np.einsum("prww,st", WC["lq1"], I3)-2/3*gp**2*np.einsum("wwst,pr", WC["qd1"], I3)+4/9*gp**2*np.einsum("prww,st", WC["ld"], I3)+2/3*gp**2*np.einsum("wwst,pr", WC["ld"], I3)-8/9*gp**2*np.einsum("prww,st", WC["lu"], I3)+4/9*gp**2*np.einsum("prww,st", WC["le"], I3)-4/3*gp**2*np.einsum("wwst,pr", WC["ud1"], I3)+2/3*gp**2*np.einsum("wwst,pr", WC["ed"], I3)+4/3*gp**2*np.einsum("stww,pr", WC["dd"], I3)+4/9*gp**2*np.einsum("swwt,pr", WC["dd"], I3)-2*gp**2*np.einsum("prst", WC["ld"])-np.einsum("pr,st", G_e@G_e.getH(), WC["CurlyPhid"])+2*np.einsum("st,pr", G_d.getH()@G_d, WC["CurlyPhil1"])-1/2*np.einsum("rv,wt,pvsw", np.conj(G_e), G_d, WC["ledq"])-1/2*np.einsum("pv,ws,rvtw", G_e, np.conj(G_d), np.conj(WC["ledq"]))-2*np.einsum("vs,wt,prvw", np.conj(G_d), G_d, WC["lq1"])-np.einsum("rw,pv,vwst", np.conj(G_e), G_e, WC["ed"])+np.einsum("pv,vrst", Gammal, WC["ld"])+np.einsum("sv,prvt", Gammad, WC["ld"])+np.einsum("pvst,vr", WC["ld"], Gammal)+np.einsum("prsv,vt", WC["ld"], Gammad)


    Beta["qe"]=1/9*gp**2*np.einsum("st,pr", WC["CurlyPhie"], I3)-2/3*gp**2*np.einsum("pr,st", WC["CurlyPhiq1"], I3)-8/3*gp**2*np.einsum("prww,st", WC["qq1"], I3)-4/9*gp**2*(np.einsum("pwwr,st", WC["qq1"], I3)+3*np.einsum("pwwr,st", WC["qq3"], I3))+4/3*gp**2*np.einsum("wwpr,st", WC["lq1"], I3)-2/9*gp**2*np.einsum("wwst,pr", WC["le"], I3)+4/3*gp**2*np.einsum("prww,st", WC["qe"], I3)+2/9*gp**2*np.einsum("wwst,pr", WC["qe"], I3)-8/3*gp**2*np.einsum("prww,st", WC["qu1"], I3)+4/3*gp**2*np.einsum("prww,st", WC["qd1"], I3)+4/9*gp**2*np.einsum("stww,pr", WC["eu"], I3)-2/9*gp**2*np.einsum("stww,pr", WC["ed"], I3)-8/9*gp**2*np.einsum("wwst,pr", WC["ee"], I3)+2*gp**2*np.einsum("prst", WC["qe"])+np.einsum("pr,st", G_u@G_u.getH(), WC["CurlyPhie"])-np.einsum("pr,st", G_d@G_d.getH(), WC["CurlyPhie"])+2*np.einsum("st,pr", G_e.getH()@G_e, WC["CurlyPhiq1"])-1/2*np.einsum("pw,vs,vtwr", G_d, np.conj(G_e), WC["ledq"])-1/2*np.einsum("vt,rw,vswp", G_e, np.conj(G_d), np.conj(WC["ledq"]))-2*np.einsum("vs,wt,vwpr", np.conj(G_e), G_e, WC["lq1"])-1/2*(np.einsum("rw,vs,vtpw", np.conj(G_u), np.conj(G_e), WC["lequ1"])+12*np.einsum("rw,vs,vtpw", np.conj(G_u), np.conj(G_e), WC["lequ3"]))-1/2*(np.einsum("pw,vt,vsrw", G_u, G_e, np.conj(WC["lequ1"]))+12*np.einsum("pw,vt,vsrw", G_u, G_e, np.conj(WC["lequ3"])))-np.einsum("rw,pv,stvw", np.conj(G_d), G_d, WC["ed"])-np.einsum("rw,pv,stvw", np.conj(G_u), G_u, WC["eu"])+np.einsum("pv,vrst", Gammaq, WC["qe"])+np.einsum("sv,prvt", Gammae, WC["qe"])+np.einsum("pvst,vr", WC["qe"], Gammaq)+np.einsum("prsv,vt", WC["qe"], Gammae)


    Beta["qu1"]=1/9*gp**2*np.einsum("st,pr", WC["CurlyPhiu"], I3)+4/9*gp**2*np.einsum("pr,st", WC["CurlyPhiq1"], I3)+16/9*gp**2*np.einsum("prww,st", WC["qq1"], I3)+8/27*gp**2*(np.einsum("pwwr,st", WC["qq1"], I3)+3*np.einsum("pwwr,st", WC["qq3"], I3))-8/9*gp**2*np.einsum("wwpr,st", WC["lq1"], I3)-8/9*gp**2*np.einsum("prww,st", WC["qe"], I3)-8/9*gp**2*np.einsum("prww,st", WC["qd1"], I3)+16/9*gp**2*np.einsum("prww,st", WC["qu1"], I3)+2/9*gp**2*np.einsum("wwst,pr", WC["qu1"], I3)-2/9*gp**2*np.einsum("wwst,pr", WC["lu"], I3)-2/9*gp**2*np.einsum("wwst,pr", WC["eu"], I3)-2/9*gp**2*np.einsum("stww,pr", WC["ud1"], I3)+8/9*gp**2*np.einsum("stww,pr", WC["uu"], I3)+8/27*gp**2*np.einsum("swwt,pr", WC["uu"], I3)-4/3*gp**2*np.einsum("prst", WC["qu1"])-8/3*gs**2*np.einsum("prst", WC["qu8"])+1/3*np.einsum("rs,pt", np.conj(G_u), Xiu)+1/3*np.einsum("pt,rs", G_u, np.conj(Xiu))+np.einsum("pr,st", G_u@G_u.getH(), WC["CurlyPhiu"])-np.einsum("pr,st", G_d@G_d.getH(), WC["CurlyPhiu"])-2*np.einsum("st,pr", G_u.getH()@G_u, WC["CurlyPhiq1"])+1/3*(np.einsum("pw,vs,vrwt", G_u, np.conj(G_u), WC["qu1"])+4/3*np.einsum("pw,vs,vrwt", G_u, np.conj(G_u), WC["qu8"]))+1/3*(np.einsum("vt,rw,pvsw", G_u, np.conj(G_u), WC["qu1"])+4/3*np.einsum("vt,rw,pvsw", G_u, np.conj(G_u), WC["qu8"]))+1/3*(np.einsum("rw,vs,ptvw", np.conj(G_d), np.conj(G_u), WC["quqd1"])+4/3*np.einsum("rw,vs,ptvw", np.conj(G_d), np.conj(G_u), WC["quqd8"]))+1/3*(np.einsum("pw,vt,rsvw", G_d, G_u, np.conj(WC["quqd1"]))+4/3*np.einsum("pw,vt,rsvw", G_d, G_u, np.conj(WC["quqd8"])))+1/2*np.einsum("rw,vs,vtpw", np.conj(G_d), np.conj(G_u), WC["quqd1"])+1/2*np.einsum("pw,vt,vsrw", G_d, G_u, np.conj(WC["quqd1"]))-2/3*(np.einsum("vt,ws,pvwr", G_u, np.conj(G_u), WC["qq1"])+3*np.einsum("vt,ws,pvwr", G_u, np.conj(G_u), WC["qq3"]))-4*np.einsum("wt,vs,prvw", G_u, np.conj(G_u), WC["qq1"])-2/3*np.einsum("pv,rw,vtsw", G_u, np.conj(G_u), WC["uu"])-2*np.einsum("pv,rw,vwst", G_u, np.conj(G_u), WC["uu"])-np.einsum("pv,rw,stvw", G_d, np.conj(G_d), WC["ud1"])+np.einsum("pv,vrst", Gammaq, WC["qu1"])+np.einsum("sv,prvt", Gammau, WC["qu1"])+np.einsum("pvst,vr", WC["qu1"], Gammaq)+np.einsum("prsv,vt", WC["qu1"], Gammau)


    Beta["qd1"]=1/9*gp**2*np.einsum("st,pr", WC["CurlyPhid"], I3)-2/9*gp**2*np.einsum("pr,st", WC["CurlyPhiq1"], I3)-8/9*gp**2*np.einsum("prww,st", WC["qq1"], I3)-4/27*gp**2*(np.einsum("pwwr,st", WC["qq1"], I3)+3*np.einsum("pwwr,st", WC["qq3"], I3))+4/9*gp**2*np.einsum("wwpr,st", WC["lq1"], I3)+4/9*gp**2*np.einsum("prww,st", WC["qe"], I3)-8/9*gp**2*np.einsum("prww,st", WC["qu1"], I3)+4/9*gp**2*np.einsum("prww,st", WC["qd1"], I3)+2/9*gp**2*np.einsum("wwst,pr", WC["qd1"], I3)-2/9*gp**2*np.einsum("wwst,pr", WC["ld"], I3)-2/9*gp**2*np.einsum("wwst,pr", WC["ed"], I3)+4/9*gp**2*np.einsum("wwst,pr", WC["ud1"], I3)-4/9*gp**2*np.einsum("stww,pr", WC["dd"], I3)-4/27*gp**2*np.einsum("swwt,pr", WC["dd"], I3)+2/3*gp**2*np.einsum("prst", WC["qd1"])-8/3*gs**2*np.einsum("prst", WC["qd8"])+1/3*np.einsum("rs,pt", np.conj(G_d), Xid)+1/3*np.einsum("pt,rs", G_d, np.conj(Xid))+np.einsum("pr,st", G_u@G_u.getH(), WC["CurlyPhid"])-np.einsum("pr,st", G_d@G_d.getH(), WC["CurlyPhid"])+2*np.einsum("st,pr", G_d.getH()@G_d, WC["CurlyPhiq1"])+1/3*(np.einsum("pw,vs,vrwt", G_d, np.conj(G_d), WC["qd1"])+4/3*np.einsum("pw,vs,vrwt", G_d, np.conj(G_d), WC["qd8"]))+1/3*(np.einsum("vt,rw,pvsw", G_d, np.conj(G_d), WC["qd1"])+4/3*np.einsum("vt,rw,pvsw", G_d, np.conj(G_d), WC["qd8"]))+1/3*(np.einsum("rw,vs,vwpt", np.conj(G_u), np.conj(G_d), WC["quqd1"])+4/3*np.einsum("rw,vs,vwpt", np.conj(G_u), np.conj(G_d), WC["quqd8"]))+1/3*(np.einsum("pw,vt,vwrs", G_u, G_d, np.conj(WC["quqd1"]))+4/3*np.einsum("pw,vt,vwrs", G_u, G_d, np.conj(WC["quqd8"])))+1/2*np.einsum("ws,rv,pvwt", np.conj(G_d), np.conj(G_u), WC["quqd1"])+1/2*np.einsum("pv,wt,rvws", G_u, G_d, np.conj(WC["quqd1"]))-2/3*(np.einsum("vt,ws,pvwr", G_d, np.conj(G_d), WC["qq1"])+3*np.einsum("vt,ws,pvwr", G_d, np.conj(G_d), WC["qq3"]))-4*np.einsum("wt,vs,prvw", G_d, np.conj(G_d), WC["qq1"])-2/3*np.einsum("pv,rw,vtsw", G_d, np.conj(G_d), WC["dd"])-2*np.einsum("pv,rw,vwst", G_d, np.conj(G_d), WC["dd"])-np.einsum("pv,rw,vwst", G_u, np.conj(G_u), WC["ud1"])+np.einsum("pv,vrst", Gammaq, WC["qd1"])+np.einsum("sv,prvt", Gammad, WC["qd1"])+np.einsum("pvst,vr", WC["qd1"], Gammaq)+np.einsum("prsv,vt", WC["qd1"], Gammad)


    Beta["qu8"]=8/3*gs**2*(np.einsum("pwwr,st", WC["qq1"], I3)+3*np.einsum("pwwr,st", WC["qq3"], I3))+2/3*gs**2*np.einsum("prww,st", WC["qu8"], I3)+2/3*gs**2*np.einsum("prww,st", WC["qd8"], I3)+4/3*gs**2*np.einsum("wwst,pr", WC["qu8"], I3)+2/3*gs**2*np.einsum("stww,pr", WC["ud8"], I3)+8/3*gs**2*np.einsum("swwt,pr", WC["uu"], I3)-(4/3*gp**2+14*gs**2)*np.einsum("prst", WC["qu8"])-12*gs**2*np.einsum("prst", WC["qu1"])+2*np.einsum("rs,pt", np.conj(G_u), Xiu)+2*np.einsum("pt,rs", G_u, np.conj(Xiu))+2*(np.einsum("pw,vs,vrwt", G_u, np.conj(G_u), WC["qu1"])-1/6*np.einsum("pw,vs,vrwt", G_u, np.conj(G_u), WC["qu8"]))+2*(np.einsum("vt,rw,pvsw", G_u, np.conj(G_u), WC["qu1"])-1/6*np.einsum("vt,rw,pvsw", G_u, np.conj(G_u), WC["qu8"]))+2*(np.einsum("rw,vs,ptvw", np.conj(G_d), np.conj(G_u), WC["quqd1"])-1/6*np.einsum("rw,vs,ptvw", np.conj(G_d), np.conj(G_u), WC["quqd8"]))+2*(np.einsum("pw,vt,rsvw", G_d, G_u, np.conj(WC["quqd1"]))-1/6*np.einsum("pw,vt,rsvw", G_d, G_u, np.conj(WC["quqd8"])))+1/2*np.einsum("vs,rw,vtpw", np.conj(G_u), np.conj(G_d), WC["quqd8"])+1/2*np.einsum("vt,pw,vsrw", G_u, G_d, np.conj(WC["quqd8"]))-4*(np.einsum("vt,ws,pvwr", G_u, np.conj(G_u), WC["qq1"])+3*np.einsum("vt,ws,pvwr", G_u, np.conj(G_u), WC["qq3"]))-4*np.einsum("pv,rw,vtsw", G_u, np.conj(G_u), WC["uu"])-np.einsum("pv,rw,stvw", G_d, np.conj(G_d), WC["ud8"])+np.einsum("pv,vrst", Gammaq, WC["qu8"])+np.einsum("sv,prvt", Gammau, WC["qu8"])+np.einsum("pvst,vr", WC["qu8"], Gammaq)+np.einsum("prsv,vt", WC["qu8"], Gammau)


    Beta["qd8"]=8/3*gs**2*(np.einsum("pwwr,st", WC["qq1"], I3)+3*np.einsum("pwwr,st", WC["qq3"], I3))+2/3*gs**2*np.einsum("prww,st", WC["qu8"], I3)+2/3*gs**2*np.einsum("prww,st", WC["qd8"], I3)+4/3*gs**2*np.einsum("wwst,pr", WC["qd8"], I3)+2/3*gs**2*np.einsum("wwst,pr", WC["ud8"], I3)+8/3*gs**2*np.einsum("swwt,pr", WC["dd"], I3)-(-2/3*gp**2+14*gs**2)*np.einsum("prst", WC["qd8"])-12*gs**2*np.einsum("prst", WC["qd1"])+2*np.einsum("rs,pt", np.conj(G_d), Xid)+2*np.einsum("pt,rs", G_d, np.conj(Xid))+2*(np.einsum("pw,vs,vrwt", G_d, np.conj(G_d), WC["qd1"])-1/6*np.einsum("pw,vs,vrwt", G_d, np.conj(G_d), WC["qd8"]))+2*(np.einsum("vt,rw,pvsw", G_d, np.conj(G_d), WC["qd1"])-1/6*np.einsum("vt,rw,pvsw", G_d, np.conj(G_d), WC["qd8"]))+2*(np.einsum("rw,vs,vwpt", np.conj(G_u), np.conj(G_d), WC["quqd1"])-1/6*np.einsum("rw,vs,vwpt", np.conj(G_u), np.conj(G_d), WC["quqd8"]))+2*(np.einsum("pw,vt,vwrs", G_u, G_d, np.conj(WC["quqd1"]))-1/6*np.einsum("pw,vt,vwrs", G_u, G_d, np.conj(WC["quqd8"])))+1/2*np.einsum("vs,rw,pwvt", np.conj(G_d), np.conj(G_u), WC["quqd8"])+1/2*np.einsum("vt,pw,rwvs", G_d, G_u, np.conj(WC["quqd8"]))-4*(np.einsum("vt,ws,pvwr", G_d, np.conj(G_d), WC["qq1"])+3*np.einsum("vt,ws,pvwr", G_d, np.conj(G_d), WC["qq3"]))-4*np.einsum("pv,rw,vtsw", G_d, np.conj(G_d), WC["dd"])-np.einsum("pv,rw,vwst", G_u, np.conj(G_u), WC["ud8"])+np.einsum("pv,vrst", Gammaq, WC["qd8"])+np.einsum("sv,prvt", Gammad, WC["qd8"])+np.einsum("pvst,vr", WC["qd8"], Gammaq)+np.einsum("prsv,vt", WC["qd8"], Gammad)


    Beta["ledq"]=-(8/3*gp**2+8*gs**2)*np.einsum("prst", WC["ledq"])-2*np.einsum("ts,pr", np.conj(G_d), Xie)-2*np.einsum("rp,st", G_e, np.conj(Xid))+2*np.einsum("pv,tw,vrsw", G_e, np.conj(G_d), WC["ed"])-2*np.einsum("vr,tw,pvsw", G_e, np.conj(G_d), WC["ld"])+2*np.einsum("vr,ws,pvwt", G_e, np.conj(G_d), WC["lq1"])+6*np.einsum("vr,ws,pvwt", G_e, np.conj(G_d), WC["lq3"])-2*np.einsum("pw,vs,vtwr", G_e, np.conj(G_d), WC["qe"])+2*np.einsum("vs,tw,prvw", np.conj(G_d), np.conj(G_u), WC["lequ1"])+np.einsum("pv,vrst", Gammal, WC["ledq"])+np.einsum("sv,prvt", Gammaq, WC["ledq"])+np.einsum("pvst,vr", WC["ledq"], Gammae)+np.einsum("prsv,vt", WC["ledq"], Gammad)


    Beta["quqd1"]=10/3*gp*np.einsum("st,pr", WC["dB"], G_u)-6*g*np.einsum("st,pr", WC["dW"], G_u)-20/9*gp*np.einsum("pt,sr", WC["dB"], G_u)+4*g*np.einsum("pt,sr", WC["dW"], G_u)-64/9*gs*np.einsum("pt,sr", WC["dG"], G_u)-2/3*gp*np.einsum("pr,st", WC["uB"], G_d)-6*g*np.einsum("pr,st", WC["uW"], G_d)+4/9*gp*np.einsum("sr,pt", WC["uB"], G_d)+4*g*np.einsum("sr,pt", WC["uW"], G_d)-64/9*gs*np.einsum("sr,pt", WC["uG"], G_d)-1/2*(11/9*gp**2+3*g**2+32*gs**2)*np.einsum("prst", WC["quqd1"])-1/3*(-5/9*gp**2-3*g**2+64/3*gs**2)*np.einsum("srpt", WC["quqd1"])-4/9*(-5/9*gp**2-3*g**2+28/3*gs**2)*np.einsum("srpt", WC["quqd8"])+16/9*gs**2*np.einsum("prst", WC["quqd8"])-2*np.einsum("pr,st", G_u, Xid)-2*np.einsum("st,pr", G_d, Xiu)+4/3*(np.einsum("vr,pw,svwt", G_u, G_d, WC["qd1"])+4/3*np.einsum("vr,pw,svwt", G_u, G_d, WC["qd8"])+np.einsum("vt,sw,pvwr", G_d, G_u, WC["qu1"])+4/3*np.einsum("vt,sw,pvwr", G_d, G_u, WC["qu8"])+np.einsum("pw,sv,vrwt", G_d, G_u, WC["ud1"])+4/3*np.einsum("pw,sv,vrwt", G_d, G_u, WC["ud8"]))+8/3*(np.einsum("wt,vr,svpw", G_d, G_u, WC["qq1"])-3*np.einsum("wt,vr,svpw", G_d, G_u, WC["qq3"])-3*np.einsum("wt,vr,swpv", G_d, G_u, WC["qq1"])+9*np.einsum("wt,vr,swpv", G_d, G_u, WC["qq3"]))-4*np.einsum("sw,pv,vrwt", G_d, G_u, WC["ud1"])+np.einsum("pv,vrst", Gammaq, WC["quqd1"])+np.einsum("sv,prvt", Gammaq, WC["quqd1"])+np.einsum("pvst,vr", WC["quqd1"], Gammau)+np.einsum("prsv,vt", WC["quqd1"], Gammad)


    Beta["quqd8"]=8*gs*np.einsum("st,pr", WC["dG"], G_u)-40/3*gp*np.einsum("pt,sr", WC["dB"], G_u)+24*g*np.einsum("pt,sr", WC["dW"], G_u)+16/3*gs*np.einsum("pt,sr", WC["dG"], G_u)+8*gs*np.einsum("pr,st", WC["uG"], G_d)+8/3*gp*np.einsum("sr,pt", WC["uB"], G_d)+24*g*np.einsum("sr,pt", WC["uW"], G_d)+16/3*gs*np.einsum("sr,pt", WC["uG"], G_d)+8*gs**2*np.einsum("prst", WC["quqd1"])+(10/9*gp**2+6*g**2+16/3*gs**2)*np.einsum("srpt", WC["quqd1"])+(-11/18*gp**2-3/2*g**2+16/3*gs**2)*np.einsum("prst", WC["quqd8"])-1/3*(5/9*gp**2+3*g**2+44/3*gs**2)*np.einsum("srpt", WC["quqd8"])+8*(np.einsum("vr,pw,svwt", G_u, G_d, WC["qd1"])-1/6*np.einsum("vr,pw,svwt", G_u, G_d, WC["qd8"])+np.einsum("vt,sw,pvwr", G_d, G_u, WC["qu1"])-1/6*np.einsum("vt,sw,pvwr", G_d, G_u, WC["qu8"])+np.einsum("pw,sv,vrwt", G_d, G_u, WC["ud1"])-1/6*np.einsum("pw,sv,vrwt", G_d, G_u, WC["ud8"]))+16*(np.einsum("wt,vr,svpw", G_d, G_u, WC["qq1"])-3*np.einsum("wt,vr,svpw", G_d, G_u, WC["qq3"]))-4*np.einsum("sw,pv,vrwt", G_d, G_u, WC["ud8"])+np.einsum("pv,vrst", Gammaq, WC["quqd8"])+np.einsum("sv,prvt", Gammaq, WC["quqd8"])+np.einsum("pvst,vr", WC["quqd8"], Gammau)+np.einsum("prsv,vt", WC["quqd8"], Gammad)


    Beta["lequ1"]=-(11/3*gp**2+8*gs**2)*np.einsum("prst", WC["lequ1"])+(30*gp**2+18*g**2)*np.einsum("prst", WC["lequ3"])+2*np.einsum("st,pr", G_u, Xie)+2*np.einsum("pr,st", G_e, Xiu)+2*np.einsum("sv,wt,prvw", G_d, G_u, WC["ledq"])+2*np.einsum("pv,sw,vrwt", G_e, G_u, WC["eu"])+2*np.einsum("vr,wt,pvsw", G_e, G_u, WC["lq1"])-6*np.einsum("vr,wt,pvsw", G_e, G_u, WC["lq3"])-2*np.einsum("vr,sw,pvwt", G_e, G_u, WC["lu"])-2*np.einsum("pw,vt,svwr", G_e, G_u, WC["qe"])+np.einsum("pv,vrst", Gammal, WC["lequ1"])+np.einsum("sv,prvt", Gammaq, WC["lequ1"])+np.einsum("pvst,vr", WC["lequ1"], Gammae)+np.einsum("prsv,vt", WC["lequ1"], Gammau)


    Beta["lequ3"]=5/6*gp*np.einsum("pr,st", WC["eB"], G_u)-3/2*g*np.einsum("st,pr", WC["uW"], G_e)-3/2*gp*np.einsum("st,pr", WC["uB"], G_e)-3/2*g*np.einsum("pr,st", WC["eW"], G_u)+(2/9*gp**2-3*g**2+8/3*gs**2)*np.einsum("prst", WC["lequ3"])+1/8*(5*gp**2+3*g**2)*np.einsum("prst", WC["lequ1"])-1/2*np.einsum("sw,pv,vrwt", G_u, G_e, WC["eu"])-1/2*np.einsum("vr,wt,pvsw", G_e, G_u, WC["lq1"])+3/2*np.einsum("vr,wt,pvsw", G_e, G_u, WC["lq3"])-1/2*np.einsum("vr,sw,pvwt", G_e, G_u, WC["lu"])-1/2*np.einsum("pw,vt,svwr", G_e, G_u, WC["qe"])+np.einsum("pv,vrst", Gammal, WC["lequ3"])+np.einsum("sv,prvt", Gammaq, WC["lequ3"])+np.einsum("pvst,vr", WC["lequ3"], Gammae)+np.einsum("prsv,vt", WC["lequ3"], Gammau)


    Beta["duql"]=-(9/2*g**2+11/6*gp**2+4*gs**2)*np.einsum("prst", WC["duql"])-np.einsum("sv,wp,vrwt", np.conj(G_d), G_d, WC["duql"])-np.einsum("sv,wr,pvwt", np.conj(G_u), G_u, WC["duql"])+2*np.einsum("tv,sw,prwv", np.conj(G_e), np.conj(G_u), WC["duue"])+np.einsum("tv,sw,pwrv", np.conj(G_e), np.conj(G_u), WC["duue"])+4*np.einsum("vp,wr,vwst", G_d, G_u, WC["qqql"])+4*np.einsum("vp,wr,wvst", G_d, G_u, WC["qqql"])-np.einsum("vp,wr,vswt", G_d, G_u, WC["qqql"])-np.einsum("vp,wr,wsvt", G_d, G_u, WC["qqql"])+2*np.einsum("wp,tv,wsrv", G_d, np.conj(G_e), WC["qque"])+np.einsum("vp,vrst", G_d.getH()@G_d, WC["duql"])+np.einsum("vr,pvst", G_u.getH()@G_u, WC["duql"])+1/2*(np.einsum("vs,prvt", G_u@G_u.getH(), WC["duql"])+np.einsum("vs,prvt", G_d@G_d.getH(), WC["duql"]))+1/2*np.einsum("vt,prsv", G_e@G_e.getH(), WC["duql"])


    Beta["qque"]=-(9/2*g**2+23/6*gp**2+4*gs**2)*np.einsum("prst", WC["qque"])-np.einsum("rv,ws,pwvt", np.conj(G_u), G_u, WC["qque"])+1/2*np.einsum("wt,rv,vspw", G_e, np.conj(G_d), WC["duql"])-1/2*(2*np.einsum("pv,rw,vwst", np.conj(G_d), np.conj(G_u), WC["duue"])+np.einsum("pv,rw,vswt", np.conj(G_d), np.conj(G_u), WC["duue"]))+1/2*(-2*np.einsum("ws,vt,prwv", G_u, G_e, WC["qqql"])+np.einsum("ws,vt,pwrv", G_u, G_e, WC["qqql"])-2*np.einsum("ws,vt,wprv", G_u, G_e, WC["qqql"]))+1/2*(np.einsum("vp,vrst", G_u@G_u.getH(), WC["qque"])+np.einsum("vp,vrst", G_d@G_d.getH(), WC["qque"]))-np.einsum("pv,ws,rwvt", np.conj(G_u), G_u, WC["qque"])+1/2*np.einsum("wt,pv,vsrw", G_e, np.conj(G_d), WC["duql"])-1/2*(2*np.einsum("rv,pw,vwst", np.conj(G_d), np.conj(G_u), WC["duue"])+np.einsum("rv,pw,vswt", np.conj(G_d), np.conj(G_u), WC["duue"]))+1/2*(-2*np.einsum("ws,vt,rpwv", G_u, G_e, WC["qqql"])+np.einsum("ws,vt,rwpv", G_u, G_e, WC["qqql"])-2*np.einsum("ws,vt,wrpv", G_u, G_e, WC["qqql"]))+1/2*(np.einsum("vr,vpst", G_u@G_u.getH(), WC["qque"])+np.einsum("vr,vpst", G_d@G_d.getH(), WC["qque"]))+np.einsum("vs,prvt", G_u.getH()@G_u, WC["qque"])+np.einsum("vt,prsv", G_e.getH()@G_e, WC["qque"])


    Beta["qqql"]=-(3*g**2+1/3*gp**2+4*gs**2)*np.einsum("prst", WC["qqql"])-4*g**2*(np.einsum("rpst", WC["qqql"])+np.einsum("srpt", WC["qqql"])+np.einsum("psrt", WC["qqql"]))-4*np.einsum("tv,sw,prwv", np.conj(G_e), np.conj(G_u), WC["qque"])+2*(np.einsum("pv,rw,vwst", np.conj(G_d), np.conj(G_u), WC["duql"])+np.einsum("rv,pw,vwst", np.conj(G_d), np.conj(G_u), WC["duql"]))+1/2*(np.einsum("vp,vrst", G_u@G_u.getH(), WC["qqql"])+np.einsum("vp,vrst", G_d@G_d.getH(), WC["qqql"]))+1/2*(np.einsum("vr,pvst", G_u@G_u.getH(), WC["qqql"])+np.einsum("vr,pvst", G_d@G_d.getH(), WC["qqql"]))+1/2*(np.einsum("vs,prvt", G_u@G_u.getH(), WC["qqql"])+np.einsum("vs,prvt", G_d@G_d.getH(), WC["qqql"]))+1/2*np.einsum("vt,prsv", G_e@G_e.getH(), WC["qqql"])


    Beta["duue"]=-(2*gp**2+4*gs**2)*np.einsum("prst", WC["duue"])-20/3*gp**2*np.einsum("psrt", WC["duue"])+4*np.einsum("ws,vt,prwv", G_u, G_e, WC["duql"])-8*np.einsum("vp,wr,vwst", G_d, G_u, WC["qque"])+np.einsum("vp,vrst", G_d.getH()@G_d, WC["duue"])+np.einsum("vr,pvst", G_u.getH()@G_u, WC["duue"])+np.einsum("vs,prvt", G_u.getH()@G_u, WC["duue"])+np.einsum("vt,prsv", G_e.getH()@G_e, WC["duue"])

    return Beta



WC={}

#1D
WC["G"]=1
WC["Gtilde"]=1
WC["W"]=1
WC["Wtilde"]=1
WC["CurlyPhi"]=1
WC["CurlyPhiEmptySquare"]=1
WC["CurlyPhiD"]=1
WC["CurlyPhiG"]=1
WC["CurlyPhiB"]=1
WC["CurlyPhiW"]=1
WC["CurlyPhiWB"]=1
WC["CurlyPhiGtilde"]=1
WC["CurlyPhiBtilde"]=1
WC["CurlyPhiWtilde"]=1
WC["CurlyPhiWtildeB"]=1

#2D
x=np.matrix(np.arange(9).reshape((3,3))+1j*np.arange(9).reshape((3,3)))
WC["uCurlyPhi"]=x
WC["dCurlyPhi"]=x
WC["eCurlyPhi"]=x
WC["eW"]=x
WC["eB"]=x
WC["uG"]=x
WC["uW"]=x
WC["uB"]=x
WC["dG"]=x
WC["dW"]=x
WC["dB"]=x
WC["CurlyPhil1"]=x
WC["CurlyPhil3"]=x
WC["CurlyPhie"]=x
WC["CurlyPhiq1"]=x
WC["CurlyPhiq3"]=x
WC["CurlyPhiu"]=x
WC["CurlyPhid"]=x
WC["CurlyPhiud"]=x

#4D
y=np.arange(81).reshape(3,3,3,3)
WC["ll"]=y
WC["qq1"]=y
WC["qq3"]=y
WC["lq1"]=y
WC["lq3"]=y
WC["ee"]=y
WC["uu"]=y
WC["dd"]=y
WC["eu"]=y
WC["ed"]=y
WC["ud1"]=y
WC["ud8"]=y
WC["le"]=y
WC["lu"]=y
WC["ld"]=y
WC["qe"]=y
WC["qu1"]=y
WC["qd1"]=y
WC["qu8"]=y
WC["qd8"]=y
WC["ledq"]=y
WC["quqd1"]=y
WC["quqd8"]=y
WC["lequ1"]=y
WC["lequ3"]=y
WC["duql"]=y
WC["qque"]=y
WC["qqql"]=y
WC["duue"]=y

Beta = getBeta(WC)
print (Beta)

