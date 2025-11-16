import re

def extract_usernames(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()  

    pattern = r'https://www.instagram.com/([a-zA-Z0-9_.]+)'
    usernames = set(re.findall(pattern, content))

    return usernames

def who_unfollowed(old_file, new_file):
    followers1 = extract_usernames(old_file)
    followers2 = extract_usernames(new_file)
    unfollowed = followers1 - followers2

    return unfollowed

followers = extract_usernames("followers.html")
following = extract_usernames("following.html")
noFollow = following - followers
unfollowers = who_unfollowed("followers.html", "followers2.html")

print("\n—————THEY THINK YOU A FAN: —————")
if noFollow:
    for username in noFollow:
        print(f"   https://instagram.com/{username}")
else:
    print("✔️ EVERYONE FW YOU TWIN!!!!")

print("\n—————WHO UNFOLLOWED YOU: —————")
if unfollowers:
    for username in unfollowers:
        print(f"   https://instagram.com/{username}")
else:
    print("🔥 NO ONE UNFOLLOWED YOU, YOU VALID TWINNN!!!")