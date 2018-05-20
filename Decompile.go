package main

import (
   "fmt"
   "net/http"
   "io/ioutil"
   "os/exec"
   "strings"
)

func main() {
    fetchHooks()
}

func createHooks(hooks string) {
    fmt.Println("Fetching Hooks")

    Hash := "output"

    Feed_OnClick := findClass("grep -Ril 'ShareLaterMedia.SHARE_LATER_MEDIA' %s/com/instagram/feed/", Hash)
    Feed := findClass("grep -Ril 'HashMap<String, ArrayList<ProductTag>> hashMap' %s/com/instagram/feed" , Hash)
    User := findClass("grep -Ril 'Follow status:' %s/com/instagram/" , Hash)
    Feed_Inject := findClass("grep -Ril 'action_menu' %s/com/instagram/feed/" , Hash)
    Direct_Hold := findClass("grep -Ril 'getString(R.string.direct_unsend_message)))' %s/com/instagram/" , Hash)
    Feed_Image := findClass("grep -Ril 'full_size_' %s/com/instagram/feed" , Hash)
    Comments :=  findClass("grep -Ril 'onSingleTapUp' %s/com/instagram/comments/" , Hash)
    Comments2 :=  findClass("grep -Ril 'Comment{mCreatedAtSeconds' %s/com/instagram/" , Hash)
    Dialog := findClass("grep -Ril 'message_avatar_container' %s/com/instagram/" , Hash)	
    Profile := findClass("grep -Ril 'https://www.instagram' %s/com/instagram/profile/" , Hash)
    Like := findClass("grep -Ril 'isTouchExplorationEnabled' %s/com/instagram/feed/ui" , Hash)
    Suggestion := findClass("grep -Ril 'R.layout.mainfeed_generic_megaphone' %s/com/instagram/" , Hash)
    Date := findClass("grep -Ril 'R.string.days_ago_abbreviation' %s/com/instagram/util/" , Hash)
    Push := findClass("grep -Ril 'push_notification_received' %s/com/instagram/notifications/" , Hash)
    Stories_Inject := findClass("grep -Ril 'explore_viewer' %s/com/instagram/" , Hash)
    Stories_Helper := findClass("grep -Ril 'POST_LIVE || !' %s/com/instagram/" , Hash)
    StoriesTimer := findClass("grep -Ril 'reel_playback_entry' %s/com/instagram/" , Hash)
    MiniFeed := findClass("grep -Ril 'R.string.see_fewer_posts_like_this_toast' %s/com/instagram/feed/" , Hash)
    Follow_Data := findClass("grep -Ril 'R.id.follow_list_social_context' %s/com/instagram/" , Hash)
    Share := findClass("grep -Ril 'clipboard' %s/com/instagram/feed/" , Hash)
    Tagged := findClass("grep -Ril 'public ArrayList<PeopleTag>' %s/com/instagram/feed/" , Hash)
    Gallery := findClass("grep -Ril 'failed to load recent captures' %s/com/instagram/feed/" , Hash)
    Search := findClass("grep -Ril 'instagram_search_results' %s/com/instagram/" , Hash)
    Location := findClass("grep -Ril 'RecentPlaceSearchCache' %s/com/instagram/" , Hash)
    Users := findClass("grep -Ril 'recent_hashtag_searches_with_ts\";' %s/com/instagram/" , Hash)
    Sponsored := findClass("grep -Ril 'explore_unconnected' %s/com/instagram/" , Hash)
    VideoLikes := findClass("grep -Ril 'R.plurals.x_y_and_n_others' %s/com/instagram/feed/" , Hash)
    ExoPlayer := findClass("grep -Ril 'Exception when setSubtitle' %s/com/instagram/" , Hash)
    Top := findClass("grep -Ril 'fbsearch/suggested_searches/' %s/com/instagram/" , Hash)
    Profile_Helper := findClass("grep -Ril 'R.dimen.avatar_size_ridiculously_xlarge' %s/com/instagram/profile/" , Hash)
    Direct := findClass("grep -Ril 'direct_expiring_media_pause_sparkler_size' %s/com/instagram/" , Hash)
    Direct_Helper := findClass("grep -Ril 'HashMap<String, PendingRecipient>' %s/com/instagram/" , Hash)
    Direct_Helper2 := findClass("grep -Ril 'DirectMessage.createPendingMessage' %s/com/instagram/" , Hash)
    LikedPost := findClass("grep -Ril 'feed_liked' %s/com/instagram/profile/" , Hash)
    Screenshot := findClass("grep -Ril 'screenshot_detector' %s/com/instagram/" , Hash)
    Explore := findClass("grep -Ril 'feed_contextual_post' %s/com/instagram/explore/", Hash)

    Line := strings.Split(hooks, ";")
    hooks = strings.Replace(hooks, Line[0], "111111", 1)

    if (Feed_OnClick != "Empty") {
        hooks = strings.Replace(hooks, Line[1], Feed_OnClick, 1)
    }

    if (Feed != "Empty") {
        hooks = strings.Replace(hooks, Line[2], Feed, 1)
    }

    if (User != "Empty") {
        hooks = strings.Replace(hooks, Line[4], User, 1)
    }

    if (Feed_Inject != "Empty") {
        hooks = strings.Replace(hooks, Line[5], Feed_Inject, 1)
    }

    if (Direct_Hold != "Empty") {
        hooks = strings.Replace(hooks, Line[6], Direct_Hold, 1)
        hooks = strings.Replace(hooks, Line[7], Direct_Hold, 1)
    }

    if (Feed_Image != "Empty") {
        hooks = strings.Replace(hooks, Line[18], Feed_Image, 1)
    }

    if (Comments != "Empty") {
        hooks = strings.Replace(hooks, Line[21], Comments, 1)
    }

    if (Comments2 != "Empty") {
        hooks = strings.Replace(hooks, Line[23], Comments2, 1)
    }

    if (Dialog != "Empty") {
        hooks = strings.Replace(hooks, Line[24], Dialog, 1)
    }

    if (Profile != "Empty") {
        hooks = strings.Replace(hooks, Line[29], Profile, 1)
        hooks = strings.Replace(hooks, Line[30], Profile, 1)
    }

    if (Like != "Empty") {
        hooks = strings.Replace(hooks, Line[35], Like, 1)
    }

    if (Suggestion != "Empty") {
        hooks = strings.Replace(hooks, Line[39], Suggestion, 1)
    }

    if (Date != "Empty") {
        hooks = strings.Replace(hooks, Line[43], Date, 1)
    }

    if (Push != "Empty") {
        hooks = strings.Replace(hooks, Line[44], Push, 1)
    }

    if (Stories_Inject != "Empty") {
        hooks = strings.Replace(hooks, Line[46], Stories_Inject, 1)
    }

    if (StoriesTimer != "Empty") {
        hooks = strings.Replace(hooks, Line[47],StoriesTimer, 1)
        hooks = strings.Replace(hooks, Line[51],StoriesTimer, 1)
    }

    if (Stories_Helper != "Empty") {
        hooks = strings.Replace(hooks, Line[48], Stories_Helper, 1)
    }

    if (MiniFeed != "Empty") {
        hooks = strings.Replace(hooks, Line[54], MiniFeed, 1)
    }

    if (Follow_Data != "Empty") {
        hooks = strings.Replace(hooks, Line[55], Follow_Data, 1)
    }

    if (Share != "Empty") {
        hooks = strings.Replace(hooks, Line[57], Share, 1)
    }

    if (Tagged != "Empty") {
        hooks = strings.Replace(hooks, Line[58], Tagged, 1)
    }

    if (Gallery != "Empty") {
        hooks = strings.Replace(hooks, Line[72], Gallery, 1)
    }

    if (Search != "Empty") {
        hooks = strings.Replace(hooks, Line[73], Search, 1)
    }

    if (Location != "Empty") {
        hooks = strings.Replace(hooks, Line[74], Location, 1)
    }

    if (Users != "Empty") {
        hooks = strings.Replace(hooks, Line[75], Users, 1)
    }

    if (Sponsored != "Empty") {
        hooks = strings.Replace(hooks, Line[76], Sponsored, 1)
    }

    if (VideoLikes != "Empty") {
        hooks = strings.Replace(hooks, Line[78], VideoLikes, 1)
    }

    if (ExoPlayer != "Empty") {
        hooks = strings.Replace(hooks, Line[80], ExoPlayer, 1)
    }

    if (Top != "Empty") {
        hooks = strings.Replace(hooks, Line[81], Top, 1)
    }

    if (Profile_Helper != "Empty") {
        hooks = strings.Replace(hooks, Line[84], Profile_Helper, 1)
    }

    if (Direct != "Empty") {
        hooks = strings.Replace(hooks, Line[93], Direct, 1)
    }

    if (Direct_Helper != "Empty") {
        hooks = strings.Replace(hooks, Line[94],Direct_Helper, 1)
    }

    if (Direct_Helper2 != "Empty") {
        hooks = strings.Replace(hooks, Line[95], Direct_Helper2, 1)
    }

    if (LikedPost != "Empty") {
        hooks = strings.Replace(hooks, Line[98], LikedPost, 1)
    }

    if (Screenshot != "Empty") {
        hooks = strings.Replace(hooks, Line[100], Screenshot, 1)
    }

    if (Explore != "Empty") {
        hooks = strings.Replace(hooks, Line[101], Explore, 1)
    }

    fmt.Println("Hooks Found")
    hooksString := "echo '" + hooks + "' > Hooks.txt"
    exec.Command("/bin/bash", "-c", hooksString).Output()
}

func decompileInstagram() {
    exec.Command("/bin/bash", "-c", "jadx/bin/jadx *.apk -d output").Output()
    fmt.Println("Decompiled")
}

func fetchHooks() {
    var client http.Client
    resp, err := client.Get("http://pastebin.com/raw/sTXbUFcx")
    if err != nil {
        // err
    }
    defer resp.Body.Close()

    if resp.StatusCode == http.StatusOK {
        bodyBytes, err2 := ioutil.ReadAll(resp.Body)
        bodyString := string(bodyBytes)

	bodyString = strings.Split(bodyString, "<p>")[1]
        bodyString = strings.Replace(bodyString, "</p>", "", 1)

	if err2 == nil {
            createHooks(bodyString)
	} else {
            fmt.Println("Hook Fetch Error: ", err2)
        }
    }
}

func findClass(command string, replacement string) string {
    command = strings.Replace(command, "%s", replacement, 1)
    out, err := exec.Command("/bin/bash", "-c", command).Output()

    cmdString := string(out)

    if err != nil {
        return "Empty"
    } else {
        cmdString = strings.Replace(cmdString, ";", "", 1)
        cmdString = strings.Replace(cmdString, "import", "", 1)
        cmdString = strings.Replace(cmdString, ".java", "", 1)
        cmdString = strings.Replace(cmdString, "output/", "", 1)
        cmdString = strings.Replace(cmdString, "/", ".", 10)
        cmdString = strings.Replace(cmdString, "\n", "", 10)
        cmdString = strings.Replace(cmdString, "\r", "", 10)

        return cmdString
    }

}
