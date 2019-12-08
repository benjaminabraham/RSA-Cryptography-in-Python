# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 01:14:15 2019

@author: Jibin Jiju Abraham
"""

## RSA Cryptograpgy

# Choosing 2 prime numbers
p=2
q=7

N=p*q # This will be the public key

phi=(p-1)*(q-1)

e=5 # Taking a number greater than 2 as sender's private key



X=[phi,
   e]

Y=[phi,
   1]    


x=1
y=1
temp_x=1
temp_y=1
s_x=1
s_y=1
i=0

# The main process of generating keys
while x==1:
    x=X[0]/X[1]
    y=phi/1
    temp_x=x
    temp_y=y
    s_x=phi-x
    s_y=phi-y
    X[0]=X[1]
    Y[0]=Y[1]
    X[1]=s_x
    Y[1]=s_y
    
print("The Public key is:", N)
print("The Private key with sender is:", e)    
print("The private key with reciever is:", y)       
    