from socialmedia.constants.numeric.post import MIN_TITLE_LENGTH, MAX_TITLE_LENGTH


TITLE_EMPTY_ERROR_STRING = 'Title is a mandatory field'
MIN_TITLE_ERROR_STRING = f'Title must have at least {MIN_TITLE_LENGTH} symbols'
MAX_TITLE_ERROR_STRING = f'Title can\'t have more than {MAX_TITLE_LENGTH} characters'

BODY_EMPTY_ERROR_STRING = 'Body is a mandatory field'


POST_NOT_FOUND_ERROR_STRING = 'Cannot find post'
POST_NOT_VALID_ERROR_STRING = 'Post data is invalid'
USER_REQUESTING_FOREIGN_POST_ID_ERROR_STRING = 'Cannot perform this operation on posts of another users'
POST_ALREADY_LIKED_ERROR_STRING = 'Post already been liked'
POST_NOT_LIKED_ERROR_STRING = 'Post hasn\'t been liked'
POST_ALREADY_DISLIKED_ERROR_STRING = 'Post already been disliked'
POST_NOT_DISLIKED_ERROR_STRING = 'Post hasn\'t been disliked'
