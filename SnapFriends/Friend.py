class Friend:
    def __init__(self, username=None, user_id=None, display=None, birthday=None, ts=None, reverse_ts=None,
                 direction=None, can_see_custom_stories=None, expiration=None, friendmoji_string=None, friendmojis=None,
                 snap_streak_count=None, bitmoji_avatar_id=None, bitmoji_selfie_id=None, fidelius_info=None,
                 is_popular=None, is_story_muted=None, mutable_username=None, is_cameos_sharing_supported=None,
                 bitmoji_scene_id=None, bitmoji_background_id=None, is_bitmoji_friendmoji_sharing_supported=None,
                 cameos_sharing_policy=None, plus_badge_visibility=None):
        self.username = username
        self.user_id = user_id
        self.display = display
        self.birthday = birthday
        self.ts = ts
        self.reverse_ts = reverse_ts
        self.direction = direction
        self.can_see_custom_stories = can_see_custom_stories
        self.expiration = expiration
        self.friendmoji_string = friendmoji_string
        self.friendmojis = friendmojis
        self.snap_streak_count = snap_streak_count
        self.bitmoji_avatar_id = bitmoji_avatar_id
        self.bitmoji_selfie_id = bitmoji_selfie_id
        self.fidelius_info = fidelius_info
        self.is_popular = is_popular
        self.is_story_muted = is_story_muted
        self.mutable_username = mutable_username
        self.is_cameos_sharing_supported = is_cameos_sharing_supported
        self.bitmoji_scene_id = bitmoji_scene_id
        self.bitmoji_background_id = bitmoji_background_id
        self.is_bitmoji_friendmoji_sharing_supported = is_bitmoji_friendmoji_sharing_supported
        self.cameos_sharing_policy = cameos_sharing_policy
        self.plus_badge_visibility = plus_badge_visibility

    @staticmethod
    def from_dict(data: dict):
        """
        Creates a Friend object from a dictionary.
        :param data: The dictionary containing the friend data.
        :return Friend: The Friend object.
        """
        return Friend(
            username=data.get('name'),
            user_id=data.get('user_id'),
            display=data.get('display'),
            birthday=data.get('birthday'),
            ts=data.get('ts'),
            reverse_ts=data.get('reverse_ts'),
            direction=data.get('direction'),
            can_see_custom_stories=data.get('can_see_custom_stories'),
            expiration=data.get('expiration'),
            friendmoji_string=data.get('friendmoji_string'),
            friendmojis=data.get('friendmojis'),
            snap_streak_count=data.get('snap_streak_count'),
            bitmoji_avatar_id=data.get('bitmoji_avatar_id'),
            bitmoji_selfie_id=data.get('bitmoji_selfie_id'),
            fidelius_info=data.get('fidelius_info'),
            is_popular=data.get('is_popular'),
            is_story_muted=data.get('is_story_muted'),
            mutable_username=data.get('mutable_username'),
            is_cameos_sharing_supported=data.get('is_cameos_sharing_supported'),
            bitmoji_scene_id=data.get('bitmoji_scene_id'),
            bitmoji_background_id=data.get('bitmoji_background_id'),
            is_bitmoji_friendmoji_sharing_supported=data.get('is_bitmoji_friendmoji_sharing_supported'),
            cameos_sharing_policy=data.get('cameos_sharing_policy'),
            plus_badge_visibility=data.get('plus_badge_visibility')
        )

    def get_bitmoji_version(self) -> int:
        """
        Gets the bitmoji version from a Friend object.
        :return: int - version of the most up to date bitmoji.
        """
        if all((self.bitmoji_selfie_id, self.bitmoji_avatar_id)):
            version = int(self.bitmoji_avatar_id.split("-")[0].split("_")[-1])
            return version

    def generate_bitmoji_url(self, version: int = None, transparent: bool = True, scale: int = 0) -> str:
        """
        Generates a bitmoji url from a Friend object.
        :param version: int - The version of the bitmoji.
        :param transparent: bool - Whether the bitmoji is transparent.
        :param scale: int - The scale of the bitmoji.
        :return: str - The bitmoji url.
        """
        base_url = "https://sdk.bitmoji.com/render/panel/"
        if all((self.bitmoji_selfie_id, self.bitmoji_avatar_id)):
            ident = self.bitmoji_avatar_id.split("-")[0].split("_")[:-1][0]
            if not version:
                version = self.get_bitmoji_version()
            sv = self.bitmoji_avatar_id.split("-")[1]

            scale = round(scale)
            transparent = int(transparent)
            uri = f'{self.bitmoji_selfie_id}-{ident}_{version}_{sv}-v1.webp?{transparent=}&{scale=}'
            return f'{base_url}{uri}'
