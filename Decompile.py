import subprocess
import requests
import os
from bs4 import BeautifulSoup
from time import sleep
import os.path

Hooks = ""
FNULL = open(os.devnull, 'w')

def decompileInstagram():
	os.system("jadx/bin/jadx *.apk -d output");

	fetchHooks()


def fetchHooks():
	global Hooks
	os.system('clear')
	r = requests.get("http://pastebin.com/raw/sTXbUFcx")
	
	html = BeautifulSoup(r.content, "html.parser")	

	Hooks = html.find('p').getText()

	createHooks();

def createHooks():
	global Hooks
	Hash = "output"
	print('Fetching Hooks')

	Feed_OnClick = Find("grep -Ril 'ShareLaterMedia.SHARE_LATER_MEDIA' %s/com/instagram/feed/" % Hash)
	Feed = Find("grep -Ril 'HashMap<String, ArrayList<ProductTag>> hashMap' %s/com/instagram/feed" % Hash)
	User = Find("grep -Ril 'Follow status:' %s/com/instagram/" % Hash)
	Feed_Inject = Find("grep -Ril 'action_menu' %s/com/instagram/feed/" % Hash)
	Direct_Hold = Find("grep -Ril 'seen_direct_unseen_message_dialog' %s/com/instagram/" % Hash)
	Feed_Image = Find("grep -Ril 'full_size_' %s/com/instagram/feed" % Hash)
	Comments =  Find("grep -Ril 'onSingleTapUp' %s/com/instagram/comments/" % Hash)
	Comments2 =  Find("grep -Ril 'Comment{mCreatedAtSeconds' %s/com/instagram/" % Hash)
	Dialog = Find("grep -Ril 'message_avatar_container' %s/com/instagram/" % Hash)	
	Profile = Find("grep -Ril 'https://www.instagram' %s/com/instagram/profile/" % Hash)
	Like = Find("grep -Ril 'isTouchExplorationEnabled' %s/com/instagram/feed/ui" % Hash)
	Suggestion = Find("grep -Ril 'R.layout.mainfeed_generic_megaphone' %s/com/instagram/" % Hash)
	Date = Find("grep -Ril 'R.string.days_ago_abbreviation' %s/com/instagram/util/" % Hash)
	Push = Find("grep -Ril 'push_notification_received' %s/com/instagram/notifications/" % Hash)
	Stories_Inject = Find("grep -Ril 'explore_viewer' %s/com/instagram/" % Hash)
	Stories_Helper = Find("grep -Ril 'POST_LIVE || !' %s/com/instagram/" % Hash)
	StoriesTimer = Find("grep -Ril 'reel_playback_entry' %s/com/instagram/" % Hash)
	MiniFeed = Find("grep -Ril 'R.string.see_fewer_posts_like_this_toast' %s/com/instagram/feed/" % Hash)
	Follow_Data = Find("grep -Ril 'R.id.follow_list_social_context' %s/com/instagram/" % Hash)
	Share = Find("grep -Ril 'clipboard' %s/com/instagram/feed/" % Hash)
	Tagged = Find("grep -Ril 'public ArrayList<PeopleTag>' %s/com/instagram/feed/" % Hash)
	Gallery = Find("grep -Ril 'failed to load recent captures' %s/com/instagram/feed/" % Hash)
	Search = Find("grep -Ril 'instagram_search_results' %s/com/instagram/" % Hash)
	Location = Find("grep -Ril 'RecentPlaceSearchCache' %s/com/instagram/" % Hash)
	Users = Find("grep -Ril 'recent_hashtag_searches_with_ts";' %s/com/instagram/" % Hash)
	Sponsored = Find("grep -Ril 'explore_unconnected' %s/com/instagram/" % Hash)
	VideoLikes = Find("grep -Ril 'R.plurals.x_y_and_n_others' %s/com/instagram/feed/" % Hash)
	ExoPlayer = Find("grep -Ril 'Exception when setSubtitle' %s/com/instagram/" % Hash)
	Top = Find("grep -Ril 'fbsearch/suggested_searches/' %s/com/instagram/" % Hash)
	Profile_Helper = Find("grep -Ril 'R.dimen.avatar_size_ridiculously_xlarge' %s/com/instagram/profile/" % Hash)
	Direct = Find("grep -Ril 'direct_expiring_media_pause_sparkler_size' %s/com/instagram/" % Hash)
	Direct_Helper = Find("grep -Ril 'HashMap<String, PendingRecipient>' %s/com/instagram/" % Hash)
	Direct_Helper2 = Find("grep -Ril 'DirectMessage.createPendingMessage' %s/com/instagram/" % Hash)
	LikedPost = Find("grep -Ril 'feed_liked' %s/com/instagram/profile/" % Hash)
	Screenshot = Find("grep -Ril 'screenshot_detector' %s/com/instagram/" % Hash)
	Explore = Find("grep -Ril 'feed_contextual_post' %s/com/instagram/explore/" % Hash)

	Line = Hooks.split(";")

	Version = "111111"

	Hooks = Hooks.replace(Line[0], Version)

	if Feed_OnClick:
		Hooks = Hooks.replace(Line[1], Feed_OnClick)
	if Feed:
		Hooks = Hooks.replace(Line[2], Feed)
	if User:
		Hooks = Hooks.replace(Line[4], User)
	if Feed_Inject:
		Hooks = Hooks.replace(Line[5], Feed_Inject)
	if Direct_Hold:
		Hooks = Hooks.replace(Line[6], Direct_Hold)
		Hooks = Hooks.replace(Line[7], Direct_Hold)
	if Feed_Image:
		Hooks = Hooks.replace(Line[18], Feed_Image)
	if Comments:
		Hooks = Hooks.replace(Line[21], Comments)
	if Comments2:
		Hooks = Hooks.replace(Line[23], Comments2)
	if Dialog:
		Hooks = Hooks.replace(Line[24], Dialog)
	if Profile:
		Hooks = Hooks.replace(Line[29], Profile)
		Hooks = Hooks.replace(Line[30], Profile)
	if Like:
		Hooks = Hooks.replace(Line[35], Like)
	if Suggestion:
		Hooks = Hooks.replace(Line[39], Suggestion)
	if Date:
		Hooks = Hooks.replace(Line[43], Date)
	if Push:
		Hooks = Hooks.replace(Line[44], Push)
	if Stories_Inject:
		Hooks = Hooks.replace(Line[46], Stories_Inject)
	if StoriesTimer:
		Hooks = Hooks.replace(Line[47], StoriesTimer)
		Hooks = Hooks.replace(Line[51], StoriesTimer)
	if Stories_Helper:
		Hooks = Hooks.replace(Line[48], Stories_Helper)
	if MiniFeed:
		Hooks = Hooks.replace(Line[54], MiniFeed)
	if Follow_Data:
		Hooks = Hooks.replace(Line[55], Follow_Data)
	if Share:
		Hooks = Hooks.replace(Line[57], Share)
	if Tagged:
		Hooks = Hooks.replace(Line[58], Tagged)
	if Gallery:
		Hooks = Hooks.replace(Line[72], Gallery)
	if Search:
		Hooks = Hooks.replace(Line[73], Search)
	if Location:
		Hooks = Hooks.replace(Line[74], Location)
	if Users:
		Hooks = Hooks.replace(Line[75], Users)
	if Sponsored:
		Hooks = Hooks.replace(Line[76], Sponsored)
	if VideoLikes:
		Hooks = Hooks.replace(Line[78], VideoLikes)
	if ExoPlayer:
		Hooks = Hooks.replace(Line[80], ExoPlayer)
	if Top:
		Hooks = Hooks.replace(Line[81], Top)
	if Profile_Helper:
		Hooks = Hooks.replace(Line[84], Profile_Helper)
	if Direct:
		Hooks = Hooks.replace(Line[93], Direct)
	if Direct_Helper:
		Hooks = Hooks.replace(Line[94], Direct_Helper)
	if Direct_Helper2:
		Hooks = Hooks.replace(Line[95], Direct_Helper2)
	if LikedPost:
		Hooks = Hooks.replace(Line[98], LikedPost)
	if Screenshot:
		Hooks = Hooks.replace(Line[100], Screenshot)
	if Explore:
		Hooks = Hooks.replace(Line[101], Explore)

	Hooks = "<p>" + Hooks;
	Hooks = Hooks + "</p>";

	print("Hooks Found")
	os.system('echo "%s" > Hooks.txt' %Hooks)

def Find(cmd):
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()

	out = out.replace(";", "")
	out = out.replace("import ", "")
	out = out.replace(".java", "")
	out = out.replace("output/", "")

	out = out.replace("Auto.py", "")
	out = out.replace("/", ".")
	out = out.replace("\n", "")
	out = out.replace("\r", "")
	out = out.rstrip()	

	return out

def main():
	try:
		decompileInstagram()
	except BaseException as error:
		print("Failed Decompiling Instagram ", error)

main()
