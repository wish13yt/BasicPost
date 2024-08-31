from atproto import Client
import time
print("Welcome!")
user = input("Please enter your BlueSky username!")
password = input("Please enter an **app** password. Do NOT enter your real password.")
client = Client(base_url='https://bsky.social')
client.login(user,password)
postme = input("What do you want to post?")
post = client.send_post(postme)
print("It should have worked!")
time.sleep(3)
exit (0)