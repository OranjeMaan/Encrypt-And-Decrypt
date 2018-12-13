# Encrypt-And-Decrypt
This Python Code does encryption and decryption in both the Caesar Cipher and the Vingenere Cipher

Method for Caesar Cipher
1. Get the message and key
2. Validate message and key
  A. Make sure the message is a string made up of ASCII characters (and only visible ones; the ones from char 33 to 126) and the key is an integer
    I. Stop if validation fails
3. For every letter in the message
  A. Get the current letter and its ASCII number
  B. If the ASCII number of the current letter plus the key is above 126
    I. Add to the output string the character with an ASCII number equal to the ASCII number of the current letter plus the key minus 94
  C.Else
    I. Add to the output string the character with an ASCII number equal to the ASCII number of the current letter plus the key
4. Return the output string

Method for Vingenere Cipher
1. Get the Message ad Key
2. Validate the Message and Key
  A. Make sure both are strings that contain alphabetical letters
    I. Stop if validation fails
3. For i in the length of Message
  A. Get A which is the index of the i'th letter in a array containing the alphabet
  B. Get B which is the index of the letter in Key at point i % length of the key string
  C. If A + B is greater than 26
    I. Add to the output string the letter in the alphabet array at the index of A + B - 26
  D. Else
    I. Add to the output string the letter in the alphabet array at the index of A + B
4. Return the Array

The Decryption method for both is basically a slight alteration of the encryption method. Instead of adding, the functions subtract the key.
