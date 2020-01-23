#Collecting_emails

#What should individual functions do?
#Extract all emails from my_str,
#Collect all emails containing numeric characters,
#Extract all domains.

#1. string to list
#2. interationn of list
#3. in each cycle find @

my_str='''Lorem ipsum dolor sit amet, consectetur adipiscing 
        elit. Mauris vulputate lacus id eros consequat tempus. 
        Nam viverra velit sit amet lorem lobortis, at tincidunt
        nunc ultricies. Duis facilisis ultrices lacus, id 
        tiger123@email.cz auctor massa molestie at. Nunc tristique 
        fringilla congue. Donec ante diam cnn@info.com, dapibus
        lacinia vulputate vitae, ullamcorper in justo. Maecenas 
        massa purus, ultricies a dictum ut, dapibus vitae massa. 
        Cras abc@gmail.com vel libero felis. In augue elit, porttitor 
        nec molestie quis, auctor a quam. Quisque b2b@money.fr 
        pretium dolor et tempor feugiat. Morbi libero lectus, 
        porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
        leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam 
        erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
        Pellentesque id dui viverra, auctor enim ut, fringilla est. 
        Maecenas gravida turpis nec ultrices aliquet.'''

emails = []
emailswithnum = []
domains = []

list=my_str.split()
a=str('@')
for i in list:
    findinigs = i.find('@')
    if findinigs!=-1:
        emails.append(i)
        for x in i:
            if x.isdigit():
                emailswithnum.append(i)
        domains.append(i[findinigs+1:])
print('Emails from my_str are :' + str(emails))
print('Emails from my_str with numbers are : ' + str(emailswithnum))
print('Domain in e-mails are : ' + str(domains))