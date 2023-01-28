from socialmedia.constants.numeric import MIN_TEXT_LENGTH, MAX_TEXT_LENGTH

TEXT_EMPTY_ERROR_STRING = 'Text is a mandatory field'
MIN_TEXT_ERROR_STRING = f'Text must have at least {MIN_TEXT_LENGTH} symbols'
MAX_TEXT_ERROR_STRING = f'Text can\'t have more than {MAX_TEXT_LENGTH} characters'


COMMENT_NOT_FOUND_ERROR_STRING = 'Cannot find comment'
COMMENT_NOT_VALID_ERROR_STRING = 'Comment data is invalid'
USER_REQUESTING_FOREIGN_COMMENT_ID_ERROR_STRING = 'Cannot perform this operation on comments of another users'
COMMENT_ALREADY_LIKED_ERROR_STRING = 'Comment already been liked'
COMMENT_NOT_LIKED_ERROR_STRING = 'Comment hasn\'t been liked'
COMMENT_ALREADY_DISLIKED_ERROR_STRING = 'Comment already been disliked'
COMMENT_NOT_DISLIKED_ERROR_STRING = 'Comment hasn\'t been disliked'
