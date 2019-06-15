class Like:

    def __init__(self, *args, **kwargs):
        self.comment_id = kwargs.get('id', None)
        self.username = kwargs.get('username', None)
        self.full_name = kwargs.get('full_name', None)
        self.profile_pic_url = kwargs.get('profile_pic_url', None)
        self.is_verified = kwargs.get('is_verified', None)
        self.followed_by_viewer = kwargs.get('followed_by_viewer', None)
        self.requested_by_viewer = kwargs.get('requested_by_viewer', None)

    def _initPropertiesCustom(self, value, prop):
        if prop == 'id':
            self.identifier = value
        if prop == 'username':
            self.username = value
