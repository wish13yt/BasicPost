from atproto import Client
import time
print("Welcome!")
user = input("Please enter your BlueSky username!")
password = input("Please enter an **app** password. Do NOT enter your real password.")
f = open("postpassword.txt", "w")
f = open("postpassword.txt", "a")
f.write(password)
f.close()
f = open("postuser.txt", "w")
f = open("postuser.txt", "a")
f.write(user)
f.close()
f = open('postuser.txt')
# Read the contents of the file into a variable
user = f.read()
# Don't forget to close the file again
f.close()
f = open('postpassword.txt')
# Read the contents of the file into a variable
password = f.read()
# Don't forget to close the file again
f.close()
client = Client(base_url='https://bsky.social')
client.login(user,password)
postme = input("What do you want to post?")
post = client.send_post(postme)
print("It should have worked!")
time.sleep(3)
exit (0)