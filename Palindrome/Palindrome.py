#*-* coding:Latin-1 -*-
import math
x=input("Entrez le mot à analyser : ")
l=len(x) #On determine la taille du mot
c=len(x)
k=list(x)
v=math.floor(len(x)/2) #on ressort la valeur de la moitié de la taille du mot
p=0     #On ititialisel les compteurs
q=0
i=0
j=0
if(l%2==0): #Si la taille du mot est paire
    while(i<(len(x)/2)):  #on parcourt le mot jusqu"à sa moitié
        if(k[i]==k[l-1]):  #On verifie si le premier et le dernier mot sont pareils
            p=p+1  #on utilise une variable pour compter
        i=i+1        #On incremente la position du mot à partir du debut
        l=l-1         #On decremente la position des caratère à partir de la fin
else:                #si la taille du mot est impair
    while(j<(v)):      #On parcourt le mot jusqu'à la partie entière du nbre impair/2
        if(k[j]==k[c-1]):     #On teste si le premier et le dernier caractère sont pareils
            q=q+1             #on utilise une variable pour compter
        j=j+1                 #On incremente la position du mot à partir du debut
        c=c-1                   #On decremente la position des caratère à partir de la fin
if(p==(len(x)/2)or q==v):        #On teste si les compteurs sont egaux à la moitié de la taille du mot
    print("Ce mot est un palindrome")
else:
    print("Ce mot n'est pas un palindrome")
            
