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
    # GetNextKey(text)

    "sdfor XORed with a ciphertext stream to produce plaintext. And it’s fast. WAKE works in CFB; "
    return plainText     
def GetNextKey(text):   
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
# 2.2	Word Auto Key Encryption

# Word Auto Key Encryption algorithm is a stream cipher algorithm that has been used commercially [6]. This algorithm invented by David Wheeler in 1993. Word Auto Key Encryption algorithm uses 128-bit key length and SBOX table 256 x 32 bits [6]. Word Auto Key Encryption Algorithm uses XOR, AND, OR and Right Shift. The main process of the algorithm consists of [6]:
# 1. The process of formation of the S-Box table (Substitution Box).
# 2. The process of formation of the key.
# 3. The process of encryption and decryption.
# The essence of the Word Auto Key Encryption algorithm lies in the formation of S-Box tables and key establishment process. Table S-Box of Word Auto Key Encryption Algorithm is flexible and different for each round [6].

# The process of formation of the S-Box table is as follows:
# 1.	Initialize the value of TT [0] ... TT [7] (in hexadecimal):
# TT [0]: 726a8f3b 
# TT [1]: e69a3b5c 
# TT [2]: d3c71fe5 
# TT [3]: ab3c73d2 
# TT [4]: 4d3a8eb3 
# TT [5]: 0396d6e8 
# TT [6]: 3d4c2f7a 
# TT [7]: 9ee27cf3 
# 2.	Initialize the initial value of 
# T [0] ... T [3]:
# T [0] = K [0]			T [1] = K [1]
# T[2] = K[2]			T[3] = K[3]
# K [0], K [1], K [2], K [3] resulting from the lock were broken up into 4 parts of equal length.
# 3.	To T [4] to T [255], do the following:
# X = T [n-4] + T [n-1]
# T [n] = X >> 3 XOR TT (X AND 7)
# 4.	To T [0] to T [22], do the following:
# T [n] = T [n] + T [n + 89]
# 5.	Set the value to multiple variables below:
# X = T [33]
# Z = T [59] OR (01000001h)
# Z = Z AND (FF7FFFFFh)
# X = (X AND FF7FFFFFh) + Z
# 6.	To T [0] ... T [255], do the following:
# X = (X AND FF7FFFFFh) + Z
# T [n] = T [n] AND 00FFFFFFh XOR X
# 7.	Initialization values for some of the following variables:
# T [256] = T [0]
# X = X AND 255
# 8.	To T [0] ... T [255], do the following:
# Temp = (T [n XOR X] XOR X) AND 255
# T [n] = T [Temp]
# T [X] = T [n + 1]

# The process of formation Key Word Auto Key Encryption algorithms can determine for n rounds. The more rounds of the process of forming the key, then the data security will be guaranteed. Function used in the process of forming the key is M (X, Y) = (X + Y) >> 8 XOR T [(X + Y) AND 255]. First of all, the key input will be split into four parts and set as the initial value of the variable A0, B0, C0, and D0 [6]. The value of this variable will process through the following steps:
# Ai + 1 = M (Ai, Di)
# Bi + 1 = M (Bi, Ai + 1)
# Ci + 1 = M (Ci, Bi + 1)
# At + 1 = M (Di, Ci + 1)
# The value of Di is the value of the key Ki.

# III. RESULT AND DISCUSSION
# The first process is to determine the key for encryption and decryption, the key used is "legitosinarhusni" and subsequent conduct the operation of forming the key to the results in hexadecimal form, proceed as follows:

# 'legitosinarhusni' is converted into hex = 6C656769746F73696E61726875736E69

# Key broke into 4 groups and enter into A (0), B (0), C (0) and D (0).
# A (0) = 6C656769
# B (0) = 746F7369
# C (0) = 6E617268
# D (0) = 75736E69

# M (A [0], D [0]) = M (6C656769, 75736E69) = (6C656769 + 75736E69) >> 8 XOR T [(6C656769 + 75736E69) AND 255 (10)] = E1D8D5D2 >> 8 XOR T [210] = 00E1D8D5 XOR 1C5A4A56 = 1CBB9283
# A [1] = 1CBB9283

# M (B [0], A [1]) = M (746F7369, 1CBB9283) = (746F7369 + 1CBB9283) >> 8 XOR T [(746F7369 + 1CBB9283) AND 255 (10)] = 912B05EC >> 8 XOR T [236] = 00912B05 XOR 26853B5B = 2614105E
# B [1] = 2614105E

# M (C [0], B [1]) = M (6E617268, 2614105E) = (6E617268 + 2614105E) >> 8 XOR T [(6E617268 + 2614105E) AND 255 (10)] = 947582C6 >> 8 XOR T [198] = 00,947,582 XOR 244C066C = 24D873EE
# C [1] = 24D873EE

# M (D [0], C [1]) = M (75736E69, 24D873EE) = (75736E69 + 24D873EE) >> 8 XOR T [(75736E69 + 24D873EE) AND 255 (10)] = 9A4BE257 >> 8 XOR T [87] = 009A4BE2 XOR C2C748D2 = C25D0330
# D [1] = C25D0330

# KEY = C25D0330

# After getting the key in hexadecimal form, the next is the process of encrypting SMS messages, for example, SMS messages to be encrypted is ROBBI RAHIM and the encryption process as follows: 

# Table 1. ASCII of ROBBI RAHIM
# No	Plaintext Character	ASCII Code
# 1	R	52
# 2	O	4F
# 3	B	42
# 4	B	42
# 5	I	49
# 6	SPACE	20
# 7	R	52
# 8	A	41
# 9	H	48
# 10	I	49
# 11	M	4D

# The final result "ROBBI RAHIM" after it was hexadecimal is "524F42424920524148494D", the results of this hexadecimal performed XOR process with a key "C25D0330", the process is as follows:

