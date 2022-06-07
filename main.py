'''

Exercise 5

Pig Latin (http://mng.bz/YrON) is a common childrens “secret” language in English-
speaking countries. (Its normally secret among children who forget that their parents
were once children themselves.) The rules for translating words from English into Pig
Latin are quite simple:
 If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the
word. So “air” becomes “airway” and “eat” becomes “eatway.”
 If the word begins with any other letter, then we take the first letter, put it on
the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay”
and “computer” becomes “omputercay.”
(And yes, I recognize that the rules can be made more sophisticated. Lets keep it sim-
ple for the purposes of this exercise.)
For this exercise, write a Python function ( pig_latin ) that takes a string as input,
assumed to be an English word. The function should return the translation of this word
into Pig Latin. You may assume that the word contains no capital letters or punctuation.
This exercise is not meant to help you translate documents into Pig Latin for your
job. (If that is your job, then I really have to question your career choices.) However, it
demonstrates some of the powerful techniques that you should know when working
with sequences, including searches, iteration, and slices. Its hard to imagine a Python
program that does not include any of these techniques.

'''

def pig_latin(string1):
    if string1[0] in 'aeiou':
        string1 += 'way'
    else:
        string1 = string1[1:] + string1[0] + 'ay'
    return string1
 
print(pig_latin('computer')) 
print(pig_latin('python'))
print(pig_latin('arrow'))