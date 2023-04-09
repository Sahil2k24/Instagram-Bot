#PACKAGE : pip intall instaloader

import instaloader

insta=instaloader.Instaloader()
acc='username'

##For downloading all the the post of the instagram account

insta.download_profile(acc, profile_pic_only=False)

##For printing all the comments of your instagram posts

insta.download_comments

##For downloading all the stories
insta.download_stories

#for downloading all the hastags of the posts
insta.download_hashtag
