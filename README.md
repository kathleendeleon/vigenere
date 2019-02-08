# vigenere
copy & paste from:
https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Base.html

The Vigenère cipher uses a 26×26 table with A to Z as the row heading and column heading This table is usually referred to as the Vigenère Tableau, Vigenère Table or Vigenère Square. We shall use Vigenère Table. The first row of this table has the 26 English letters. Starting with the second row, each row has the letters shifted to the left one position in a cyclic way. For example, when B is shifted to the first position on the second row, the letter A moves to the end.


 
In addition to the plaintext, the Vigenère cipher also requires a keyword, which is repeated so that the total length is equal to that of the plaintext. For example, suppose the plaintext is MICHIGAN TECHNOLOGICAL UNIVERSITY and the keyword is HOUGHTON. Then, the keyword must be repeated as follows:

 MICHIGAN TECHNOLOGICAL UNIVERSITY
HOUGHTON HOUGHTONHOUGH TONHOUGNTO
We follow the tradition by removing all spaces and punctuation, converting all letters to upper case, and dividing the result into 5-letter blocks. As a result, the above plaintext and keyword become the following:

 MICHI GANTE CHNOL OGICA LUNIV ERSIT Y
HOUGH TONHO UGHTO NHOUG HTONH OUGHT O
To encrypt, pick a letter in the plaintext and its corresponding letter in the keyword, use the keyword letter and the plaintext letter as the row index and column index, respectively, and the entry at the row-column intersection is the letter in the ciphertext. For example, the first letter in the plaintext is M and its corresponding keyword letter is H. This means that the row of H and the column of M are used, and the entry T at the intersection is the encrypted result.


Similarly, since the letter N in MICHIGAN corresponds to the letter N in the keyword, the entry at the intersection of row N and column N is A which is the encrypted letter in the ciphertext


Repeating this process until all plaintext letters are processed, the ciphertext is TWWNPZOA ASWNUHZBNWWGS NBVCSLYPMM. The following has the plaintext, repeated keyword and ciphertext aligned together.

 MICHI GANTE CHNOL OGICA LUNIV ERSIT Y
HOUGH TONHO UGHTO NHOUG HTONH OUGHT O
TWWNP ZOAAS WNUHZ BNWWG SNBVC SLYPM M
To decrypt, pick a letter in the ciphertext and its corresponding letter in the keyword, use the keyword letter to find the corresponding row, and the letter heading of the column that contains the ciphertext letter is the needed plaintext letter. For example, to decrypt the first letter T in the ciphertext, we find the corresponding letter H in the keyword. Then, the row of H is used to find the corresponding letter T and the column that contains T provides the plaintext letter M (see the above figures). Consider the fifth letter P in the ciphertext. This letter corresponds to the keyword letter H and row H is used to find P. Since P is on column I, the corresponding plaintext letter is I.
