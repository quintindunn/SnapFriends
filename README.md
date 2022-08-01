# A Snapchat Friend parser / (future) API

----

## Prerequisites
 - Access to https://web.snapchat.com/
 - Python3

## Download prerequisites:
- [Python3](https://www.python.org/downloads/)
- [requests](https://pypi.python.org/pypi/requests)
- [pillow](https://pypi.python.org/pypi/Pillow)

**OR**
1. [Python3](https://www.python.org/downloads/)
2. Download the requirements.txt file
3. Run the command below in the same directory as the requirements.txt file:
    ```
    python3 -m pip install -r requirements.txt
    ```

## How to get `friends.json`
1. Go to https://web.snapchat.com/
2. Open inspect element and click on the `Network` tab.
3. In the `Filter` box enter `https://web.snapchat.com/ami/friends`
4. Right-click on the first `GET` request and hover over the `copy` button.
5. Click on the `copy response` button.
6. Save the response accordingly. (For the example save it in the same folder as `example.py` in a file called `friends.json`)

example.py
```python
import json
import os.path
from SnapFriends.util import get_bitmoji_image, friends_from_dict


with open('friends.json', encoding="UTF-8") as f:
    data = json.load(f)

# Load friends from friends.json
friends = friends_from_dict(data)

# Generate output directory if it doesn't exist
if not os.path.isdir("output"):
    os.mkdir("output")


for friend in friends:
    # Checks if friend has all the required data to generate a bitmoji url.
    if friend.generate_bitmoji_url():
        # Gets first bitmoji friend ever had at smallest size
        im = get_bitmoji_image(friend.generate_bitmoji_url(version=0, transparent=True, scale=0))
        # Saves the image to `output/<username>/first_bitmoji.png`
        im.save(f"output/{friend.username}/first_bitmoji.png")

```

