from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required

from socialmedia.api.blueprints import comment_blueprint
from socialmedia.api.services import CommentService
from socialmedia.decorators import handle_app_errors
from socialmedia.responses import get_comment_response, get_all_comments_response, get_like_comment_response, \
    get_remove_like_comment_response, \
    get_add_comment_answer_response, get_delete_comment_response, get_dislike_comment_response, \
    get_remove_dislike_comment_response, get_comment_answers_response, \
    get_update_comment_response, get_patch_comment_response
from socialmedia.utils import check_request_content_type, \
    check_user_operation_permission_on_comment, get_user_id
from socialmedia.models.model_transfer import CommentModelTransfer


@comment_blueprint.route('/<int:comment_id>', methods=['GET'])
@handle_app_errors
def get_comment(comment_id: int):
    comment = CommentService.get_by_id(comment_id=comment_id)
    comment_dto = CommentModelTransfer.to_dto_model(database_model=comment)
    return get_comment_response(comment=comment_dto)


@comment_blueprint.route('', methods=['GET'])
@handle_app_errors
def get_all_comments():
    comments = CommentService.get_all()
    comments_dto = [CommentModelTransfer.to_dto_model(database_model=comment) for comment in comments]
    return get_all_comments_response(comments=comments_dto)


@comment_blueprint.route('/<int:comment_id>/answers', methods=['GET'])
@handle_app_errors
def get_comment_answers(comment_id: int):
    comment = CommentService.get_by_id(comment_id=comment_id)

    answers_dto = [CommentModelTransfer.to_dto_model(database_model=answer) for answer in comment.comment_answers]
    return get_comment_answers_response(answers=answers_dto)


@comment_blueprint.route('/<int:comment_id>/answer', methods=['POST'])
@handle_app_errors
@jwt_required()
def add_comment_answer(comment_id: int):
    comment = CommentService.get_by_id(comment_id=comment_id)

    request_body: dict = check_request_content_type(request=request)
    user_id = int(get_jwt_identity().get('id'))

    request_body['user_id'] = user_id
    request_body['post_id'] = comment.post_id

    comment = CommentService.add_comment_answer(comment_id=comment_id, answer_comment_data=request_body)

    comment_dto = CommentModelTransfer.to_dto_model(database_model=comment)
    return get_add_comment_answer_response(comment=comment_dto)


@comment_blueprint.route('/<int:comment_id>/like', methods=['POST'])
@handle_app_errors
@jwt_required()
def like_comment(comment_id: int):
    user_id: int = get_user_id(token_identity=get_jwt_identity())
    CommentService.like_comment(user_id=user_id, comment_id=comment_id)
    return get_like_comment_response()


@comment_blueprint.route('/<int:comment_id>/like', methods=['DELETE'])
@handle_app_errors
@jwt_required()
def remove_like_comment(comment_id: int):
    user_id: int = get_user_id(token_identity=get_jwt_identity())
    CommentService.remove_like_comment(user_id=user_id, comment_id=comment_id)
    return get_remove_like_comment_response()


@comment_blueprint.route('/<int:comment_id>/dislike', methods=['POST'])
@handle_app_errors
@jwt_required()
def dislike_comment(comment_id: int):
    user_id: int = get_user_id(token_identity=get_jwt_identity())
    CommentService.dislike_comment(user_id=user_id, comment_id=comment_id)
    return get_dislike_comment_response()


@comment_blueprint.route('/<int:comment_id>/dislike', methods=['DELETE'])
@handle_app_errors
@jwt_required()
def remove_dislike_comment(comment_id: int):
    user_id: int = get_user_id(token_identity=get_jwt_identity())
    CommentService.remove_dislike_comment(user_id=user_id, comment_id=comment_id)
    return get_remove_dislike_comment_response()


@comment_blueprint.route('/<int:comment_id>', methods=['PUT'])
@handle_app_errors
@jwt_required()
def update_comment(comment_id: int):
    request_body = check_request_content_type(request=request)

    comment = CommentService.get_by_id(comment_id=comment_id)

    comment_author_id: int = comment.user_id

    check_user_operation_permission_on_comment(comment_author_id=comment_author_id, token_identity=get_jwt_identity())
    CommentService.update(comment_id=comment_id, comment_data=request_body)

    return get_update_comment_response()


@comment_blueprint.route('/<int:comment_id>', methods=['PATCH'])
@handle_app_errors
@jwt_required()
def patch_comment(comment_id: int):
    request_body = check_request_content_type(request=request)

    comment = CommentService.get_by_id(comment_id=comment_id)

    comment_author_id: int = comment.user_id

    check_user_operation_permission_on_comment(comment_author_id=comment_author_id, token_identity=get_jwt_identity())
    CommentService.patch(comment_id=comment_id, comment_data=request_body)

    return get_patch_comment_response()


@comment_blueprint.route('/<int:comment_id>', methods=['DELETE'])
@handle_app_errors
@jwt_required()
def delete_comment(comment_id: int):
    comment = CommentService.get_by_id(comment_id=comment_id)

    comment_author_id: int = comment.user_id

    check_user_operation_permission_on_comment(comment_author_id=comment_author_id, token_identity=get_jwt_identity())

    CommentService.delete(comment_id=comment_id)
    return get_delete_comment_response()
