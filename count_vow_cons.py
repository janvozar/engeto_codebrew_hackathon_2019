#requested output 'No. consonants: <cons_count> | No. vowels: <vowel_count>'
user_input=' '
vowels_list=set(['a','e','i','o','u','y'])
vowel_count=0
cons_count=0

def count(user_input,vowels_list,vowel_count,cons_count):
    for i in user_input:
        if i in vowels_list:
            vowel_count+=1
        else:
            cons_count+=1
    return vowel_count,cons_count

def main():
   user_input = input('Enter a string of vowels and consonants:').replace(" ", "")
   vowels,cons = count(user_input, vowels_list, vowel_count, cons_count)
   print('No. consonants:' +str(cons)+ '| No. vowels:' +str(vowels))
main()