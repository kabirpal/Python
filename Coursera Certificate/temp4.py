import emoji

Mood = input("Enter your mood")

if (Mood == "Diyu sad"):
   print(emoji.emojize(":thumbs_up:"))
elif (Mood == "Diyu chup raho"):
   print(emoji.emojize(":zipper-mouth_face:")) 
elif (Mood == "baat mat kro"):
    print(emoji.emojize(":grinning_face_with_big_eyes:"))
elif (Mood == "Diyu tease"):
    print(emoji.emojize(":winking_face_with_tongue:"))
elif (Mood == "Diyu kiss"):
    print(emoji.emojize(":kissing_face_with_closed_eyes:"))
elif (Mood == "Diyu love"):
    print(emoji.emojize(":smiling_face_with_heart-eyes:"))
else :
    print("Invalid")