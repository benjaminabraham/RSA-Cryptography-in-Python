# RSA-Cryptography-in-Python
An implementation of RSA algorithm in Python

While small numbers have made the calculations easy, the crucial point here is that when choosing the 2 prime numbers,
'p' and 'q', the numbers chosen has to be large.

Once 'p' and 'q' are chosen we calculate the value of N which is the product of the two prime numbers. This 'N' is the public key and is visible to anyone Using a mathematical function, we then calculate a mathematical constant "phi". The sender of the message generates a private key,'e', which fulfills certain conditions:

i) The value of 'e' must be between one and Phi
ii) The value of 'e' must be co prime with N and phi

Once we get 'e', we then find the value of 'd', which is the private key for decryption for the receiver. 
