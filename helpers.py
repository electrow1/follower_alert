from tweepy import API,Client,OAuth1UserHandler
import json
import smtplib
import os
import time



auth = OAuth1UserHandler(
    consumer_key=os.environ.get("API_KEY"),
    consumer_secret=os.environ.get("API_SECRET_KEY"),
    access_token=os.environ.get("ACCESS_TOKEN"),
    access_token_secret=os.environ.get("ACCESS_TOKEN_SECRET")
)

api = API(auth)

def get_followers(username):
    list_followers=api.get_friends(screen_name=username)
    usernames=[list_follower.screen_name for list_follower in list_followers]
    return usernames
    
def all_accounts_followers(accounts):
    for username in accounts:
        followers=get_followers(username)
        #get_new_followers
        #new_followers=
        for new_follower in new_followers:
            notifications.append("f{username} is now following {new_follower}")
            
            
def get_old_followers(username):
    with open('followers.json') as file:
        data = json.load(file)
    if username in data:
        return data[username]
    return []
    
def update_followers(username,followers):
    with open('followers.json',"r") as file:
        data = json.load(file)
    data[username]=followers
    with open("followers.json", "w") as file:
        json.dump(data, file)
        
def get_new_followers(username):
    new_followers=[]
    current_followers=get_followers(username)
    old_followers=get_old_followers(username)
    for current_follower in current_followers:
        if current_follower not in old_followers:
            new_followers.append(current_follower)
    update_followers(username,current_followers)
    return new_followers
    
    
def create_message(username, new_followers ):
    new_followers=["@"+i for i in new_followers]
    message=f"Subject: Follower Alert\n{username} is now following"
    for link in new_followers:
        message=message+" " +link
    return message
    
    
def send_email(message,receiver_email):
    # creates SMTP session
    s = smtplib.SMTP(os.environ.get("MAIL_SERVER"), int(os.environ.get("MAIL_PORT")))

    # start TLS for security
    s.starttls()

    # Authentication

    s.login(os.environ.get("MAIL_USERNAME"),os.environ.get("MAIL_PASSWORD"))
    
    # sending the mail
   
    s.sendmail(os.environ.get("MAIL_USERNAME"), receiver_email, message)
    # terminating the session
    s.quit()
    
def get_updates(username,receiver_email):
    new_followers=get_new_followers(username)
    if new_followers:
        message=create_message(username,new_followers)
        print(message)
        send_email(message,receiver_email)

    else:
        pass
        
def get_all_updates():
    get_updates("GemHackerHunter","sodiq.yusuf.a33@gmail.com")
    time.sleep(10)
    get_updates("@GemsLady555","sodiq.yusuf.a33@gmail.com")
    time.sleep(10)
    get_updates("BSCsuper1000X","sodiq.yusuf.a33@gmail.com")
    time.sleep(10)
    get_updates("_CZArmy","sodiq.yusuf.a33@gmail.com")
    time.sleep(10)
    get_updates("CryptoGemsNFT_","sodiq.yusuf.a33@gmail.com")
    time.sleep(10)
    get_updates("bull_bnb","sodiq.yusuf.a33@gmail.com")
    time.sleep(10)
    get_updates("@CryptoXMad","sodiq.yusuf.a33@gmail.com")
    time.sleep(10)
    get_updates("Crypticsmma","sodiq.yusuf.a33@gmail.com")
    time.sleep(10)
    get_updates("bnbbombs","sodiq.yusuf.a33@gmail.com")
    time.sleep(10)
    get_updates("GemsLadyBullish","sodiq.yusuf.a33@gmail.com")
    time.sleep(10)
    get_updates("@_CryptoWaller","sodiq.yusuf.a33@gmail.com")
    time.sleep(10)
    get_updates("Crypto_Jerry705","sodiq.yusuf.a33@gmail.com")
    time.sleep(10)
    get_updates("theblueunicornn","sodiq.yusuf.a33@gmail.com")
    time.sleep(10)
    get_updates("CoinGPO","sodiq.yusuf.a33@gmail.com")
    time.sleep(10)
    get_updates("RealDogen","sodiq.yusuf.a33@gmail.com")
    time.sleep(10)
    
    
