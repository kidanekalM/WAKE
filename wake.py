def encrypt(plainText): 
    # Produce S - box
    # Generate KeyStream 1 use CFB
    # XOR with plaintext 
    for i in range(0,10):
        print ()
    return plainText
def dencrypt(cipherText):
    # Generate KeyStram 1 use CFB 
    # XOR with
    "sdfor XORed with a ciphertext stream to produce plaintext. And it’s fast. WAKE works in CFB; "
    return plainText     
def GenerateKey(text):   
    # ai+1 = M(ai ,di)  
    # bi+1 = M(bi ,ai+1)
    # ci+1 = M(ci,bi+1) 
    # di+1 = M(di ,ci+1)
    # Function M is     
    # M(x,y) = (x + y) >> 8 • S(x+y) ^ 255
    return
def M(x,y):
    return 
"""
17.3 WAKE
WAKE is the Word Auto Key Encryption algorithm, invented by David
Wheeler [1589].                                                  
It produces a stream of 32-bit words which can be XORed  
with a plaintext stream to produce ciphertext,
                                              
or XORed with a ciphertext stream to produce plaintext. And it’s fast.
WAKE works in CFB;                                                    
the previous ciphertext word is used to generate the next key word.
 It also uses an S-box of 256 32-bit values. This S-box has a     
special property: The high-order byte of all the entries is a permutation of all
possible bytes, and the low-order 3 bytes are random.                           
First, generate the S-box entries, Si, from the key. Then initialize four registers
with the key (or with another key): a0, b0 , c0, and d0. To generate a 32-bit      
keystream word, Ki:
Ki = di            
The ciphertext word Ci, is the plaintext word, Pi XORed with Ki.
Then, update the four registers:
ai+1 = M(ai ,di)  
bi+1 = M(bi ,ai+1)
ci+1 = M(ci,bi+1) 
di+1 = M(di ,ci+1)
Function M is     
M(x,y) = (x + y) >> 8 • S(x+y) ^ 255
This is shown in Figure 17.2. The operation >> is a right shift, not a rotation.
The low-order 8 bits of x + y are the input into the S-box. Wheeler gives a     
procedure for generating the S-box, but it isn’t really complete. Any algorithm 
to generate random bytes and a random permutation will work.
Figure 17.2 Wake.                                           
WAKE’s biggest asset is that it is fast. However, it’s insecure against a    
chosen-plaintext or chosen-ciphertext attack. It is being used in the current
version of Dr. Solomon’s Anti-Virus program.
"""