import json
import os.path
from SnapFriends.util import get_bitmoji_image, friends_from_dict


with open('./friends.json', encoding="UTF-8") as f:
    data = json.load(f)

# Load friends from friends.json
friends = friends_from_dict(data)

# Generate output directory if it doesn't exist
if not os.path.isdir("./output"):
    os.mkdir("./output")


for friend in friends:
    # Checks if friend has all the required data to generate a bitmoji url.
    if friend.generate_bitmoji_url():
        # Gets first bitmoji friend ever had at smallest size
        im = get_bitmoji_image(friend.generate_bitmoji_url(version=0, transparent=True, scale=0))
        # Saves the image to `output/<username>/first_bitmoji.png`
        im.save(f"./output/{friend.username}/first_bitmoji.png")
