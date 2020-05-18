import face_recognition
import urllib.request
import base64
import sys
import json
import os
from friend import Friend
from urllib.parse import urlencode
from urllib.request import Request, urlopen

def start():
    myUserId = "8"
    path = "/home/pi/Desktop/smart_doorbell/yolov3/test.png"
    url = 'http://glassdoor-api.azurewebsites.net/Upload/index' # Set destination URL here
    myfriends = getFriends(myUserId)
    friend = matchFace(myfriends, path)
    post_fields = None
    
    if friend == None:
        print("Unknown person is at the door")
        with open(path, 'rb') as img:
            post_fields = {'UserId': myUserId, 'ImageBase64': base64.b64encode(img.read())}     # Set POST fields here
            request = Request(url, urlencode(post_fields).encode())
            json = urlopen(request).read().decode()
            print(json)
    else:
        print("Your friend %s is by the door." % (friend.name))
        with open(path, 'rb') as img:
            post_fields = {'UserId': myUserId, 'ImageBase64': base64.b64encode(img.read()), 'friendId': friend.friendId}     # Set POST fields here
            request = Request(url, urlencode(post_fields).encode())
            json = urlopen(request).read().decode()
            print(json)
        
    print("Finished Uploading Results")

def getFriends(myUserId):
    url = "http://glassdoor-api.azurewebsites.net/Home/GetFriends/" + myUserId
    
    jsonResp = urllib.request.urlopen(url).read()
    data = json.loads(jsonResp)
    friends = []
    
    for friend in data:
        createFriendPhoto(friend['imageBase64'], friend['friendId'], friend['imageExtension'])
        friends.append(Friend(friend['friendName'], '%s.%s' % (friend['friendId'], friend['imageExtension']), friend['friendId']))
        print(friend['friendName'])
        
    return friends
        
def createFriendPhoto(base64Str, friendId, extension):
    #print(base64Str)
    with open('%s.%s' % (friendId, extension), 'wb') as f:
        base64StrIdx = base64Str.index("base64,")
        f.write(base64.b64decode(base64Str[base64StrIdx + 7:]))
    print("Saved.")

def matchFace(myFriends, path):
    
    
    for myFriend in myFriends:
        print(myFriend.imagePath)
        picture_of_me = face_recognition.load_image_file(myFriend.imagePath)
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

        unknown_picture = face_recognition.load_image_file(path)
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

        if results[0] == True:
            return myFriend
        
    return None

print(sys.argv[0])
start()