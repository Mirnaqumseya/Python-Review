def create_youtube_video(title, discription):
	youvideo= {"Title" : title , "Description" : 'description' , "Likes" : 0 , "Dislikes" : 0 , "comments" : {}}
	return youvideo

	

newvideo = create_youtube_video ("why cats are better  than dogs", "hello")


def like(youtube_video):
	if "Likes" in youtube_video: 
		 youtube_video["Likes"] += 1
	return youtube_video



def Dislike(youtube_video):
	if "Dislikes" in youtube_video: 
		 youtube_video["dislikes"] += 1
	return youtube_video


def add_comment(youtubevideo, username, comment_text):
	comment={username:comment_text}
	youtubevideo["comments"] = comment
	return comment


youtubevideo1=create_youtube_video("How to kill yourself" , "Make sure you like,subscribe,and share before you die")
for i in range(1):
	print(youtubevideo1)