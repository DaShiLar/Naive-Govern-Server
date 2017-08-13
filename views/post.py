from flask import request, Blueprint
import controller
import json
mod = Blueprint('post', __name__, template_folder='templates')




@mod.route('/post/comment', methods=['POST'])
def post_comment():
    post_str = request.form.get("post_data")
    print (post_str)
    comment = json.loads(post_str)

    print (comment)

    status = controller.addComment(comment['passage_id'],comment['comment_incline'], comment['comment_content']['textarea'])

    return json.dumps({
        "status": True,
        "message": "LLL"
    })
