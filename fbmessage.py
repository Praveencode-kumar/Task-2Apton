
# =============================================================================
# 
# 
# import facebook

# 
# page_access_token = "843043104789-2vsqqvpfc8oiv3u0tm5ko9invhmq7oqe.apps.googleusercontent.com"
# graph = facebook.GraphAPI(page_access_token)
# facebook_page_id = "400161141075699"
# graph.put_object(facebook_page_id, "feed", message='test message')
# =============================================================================

import fbchat 
from fbchat  import Client
from getpass import getpass 
username = "9944738991"
client = fbchat.Client(username, getpass()) 
no_of_friends = int("Number of friends: ")
for i in range(no_of_friends): 
	name = str("Name: ")
	friends = client.getUsers(name) # return a list of names 
	friend = friends[0] 
	msg = str("Message: ")
	sent = client.send(fbchat.models.Message(msg),friend.uid) 
	if sent: 
		print("Message sent successfully!") 
