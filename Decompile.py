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
	r = requests.get("http://pastebin.com/raw/sTXbUFcx")
	
	html = BeautifulSoup(r.content, "html.parser")	

	Hooks = html.find('p').getText()

	createHooks();

def createHooks():
	global Hooks
	Hash = "output"

	Feed_OnClick = Find("grep -Ril 'ShareLaterMedia.SHARE_LATER_MEDIA' %s/com/instagram/feed/" % Hash)
	Feed = Find("grep -Ril 'HashMap<String, ArrayList<ProductTag>> hashMap' %s/com/instagram/feed" % Hash)
	User = Find("grep -Ril 'Follow status:' %s/com/instagram/" % Hash)
	Feed_Inject = Find("grep -Ril 'action_menu' %s/com/instagram/feed/" % Hash)
	Feed_Image = Find("grep -Ril 'full_size_' %s/com/instagram/feed" % Hash)
	Comments =  Find("grep -Ril 'onSingleTapUp' %s/com/instagram/comments/" % Hash)
	Comments2 =  Find("grep -Ril 'Comment{mCreatedAtSeconds' %s/com/instagram/" % Hash)
	Dialog = Find("grep -Ril 'message_avatar_container' %s/com/instagram/" % Hash)	
	Profile = Find("grep -Ril 'https://www.instagram' %s/com/instagram/profile/" % Hash)
	Like = Find("grep -Ril 'isTouchExplorationEnabled' %s/com/instagram/feed/ui" % Hash)
	Date = Find("grep -Ril 'R.string.days_ago_abbreviation' %s/com/instagram/util/" % Hash)
	Push = Find("grep -Ril 'push_notification_received' %s/com/instagram/notifications/" % Hash)
	Stories_Inject = Find("grep -Ril 'explore_viewer' %s/com/instagram/" % Hash)
	StoriesTimer = Find("grep -Ril 'reel_playback_entry' %s/com/instagram/" % Hash)
	MiniFeed = Find("grep -Ril 'R.string.see_fewer_posts_like_this_toast' %s/com/instagram/feed/" % Hash)
	Follow_Data = Find("grep -Ril 'R.id.follow_list_social_context' %s/com/instagram/" % Hash)
	Share = Find("grep -Ril 'clipboard' %s/com/instagram/feed/" % Hash)
	Sponsored = Find("grep -Ril 'explore_unconnected' %s/com/instagram/" % Hash)
	VideoLikes = Find("grep -Ril 'R.plurals.x_y_and_n_others' %s/com/instagram/feed/" % Hash)
	ExoPlayer = Find("grep -Ril 'Exception when setSubtitle' %s/com/instagram/" % Hash)

	Line = Hooks.split(";")

	versionLine = "aapt dump badging *.apk"
	procVersion = subprocess.Popen(versionLine, stdout=subprocess.PIPE, shell=True)
	(outputVersion, err) = procVersion.communicate()

	Code = outputVersion.split("name'com.")
	Test = Code[0].split("versionCode")
	Version = Code[0].replace(Test[1], "")
	Version = Version.replace("' versionCode", "")
	Version = Version.replace("package: name='", "") 

	Hooks = Hooks.replace(Line[0], Version)

	if Feed_OnClick:
		Hooks = Hooks.replace(Line[1], Feed_OnClick)
	if Feed:
		Hooks = Hooks.replace(Line[2], Feed)
	if User:
		Hooks = Hooks.replace(Line[4], User)
	if Feed_Inject:
		Hooks = Hooks.replace(Line[5], Feed_Inject)
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
	if Date:
		Hooks = Hooks.replace(Line[43], Date)
	if Push:
		Hooks = Hooks.replace(Line[44], Push)
	if Stories_Inject:
		Hooks = Hooks.replace(Line[47], Stories_Inject)
	if StoriesTimer:
		Hooks = Hooks.replace(Line[49], StoriesTimer)
	if MiniFeed:
		Hooks = Hooks.replace(Line[54], MiniFeed)
	if Follow_Data:
		Hooks = Hooks.replace(Line[55], Follow_Data)
	if Share:
		Hooks = Hooks.replace(Line[57], Share)
	if Sponsored:
		Hooks = Hooks.replace(Line[76], Sponsored)
	if VideoLikes:
		Hooks = Hooks.replace(Line[78], VideoLikes)
	if ExoPlayer:
		Hooks = Hooks.replace(Line[80], ExoPlayer)

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
