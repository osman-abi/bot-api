import requests
from celery import shared_task
from .views import ACCESS_TOKEN, PAGE_ID
from .models import Comments, ReplyMessage, CommentAuthors
from datetime import datetime

# celery -A core beat -l info
# celery -A core worker -l info

@shared_task
def enforce_task():
    # 1st we need to get all posts
    posts = []
    posts_url = 'https://graph.facebook.com/v13.0/{}/posts?access_token={}'.format(PAGE_ID, ACCESS_TOKEN)
    posts_ = requests.get(posts_url).json()

    for post in posts_.get('data'):
        posts.append(post.get('id'))

    # 2nd we need to get every comment by per posts
    comments = []
    comment_ids = Comments.objects.values_list('comment_id',flat=True) # We are creating array of comment_ids to check 
    comment_user_ids = Comments.objects.all().values_list('user_id', flat=True) # We are creating array of user_ids to check
    for post_id in posts:
        comments_url = 'https://graph.facebook.com/v13.0/{}/comments?access_token={}'.format(post_id, ACCESS_TOKEN)
        comments_ = requests.get(comments_url).json()
        checking_comments = [] # We are creating checking comments (empty array) to gather all of the comment ids
                               # of the post

        for comment in comments_.get('data'):
            checking_comments.append(comment.get('id')) 

        for comment in comment_ids:
            if comment not in checking_comments: # We are checking if comment id (from DB) in 
                                                 # all of the comment id (from FB)
                Comments.objects.filter(comment_id=comment).delete()

        for comment in comments_.get('data'):
            comment_json = dict()
            comment_publish_time = datetime.fromisoformat(comment.get('created_time').replace('+0000','+00:00'))
            all_comments_from_db = Comments.objects.all().count()
           
            if comment.get('from').get('name') != 'Otobot3':
                if all_comments_from_db == 0:


                    if not CommentAuthors.objects.filter(user_id = comment.get('from').get('id')).exists():
                        CommentAuthors.objects.create(user_id=comment.get('from').get('id'))


                        print(True)
                    

                    comment_auth = CommentAuthors.objects.last()

                    Comments.objects.create(
                        user_id = comment_auth,
                        post_id = post_id,
                        comment_id=comment.get('id'),
                        comment = comment.get('message'),
                        user_name = comment.get('from').get('id'),
                        created_at = comment_publish_time
                    )

                    comment_json['commentID'] = comment.get('id')
                    comment_json['userID'] = comment.get('from').get('id')

                    comments.append(comment_json)
                else:
                    comment_from_db = Comments.objects.filter(post_id=post_id).last()
                    if comment_publish_time > comment_from_db.created_at and not Comments.objects.filter(user_id=comment.get('from').get('id')).exists():
                        comment_json['commentID'] = comment.get('id')
                        comment_json['userID'] = comment.get('from').get('id')
                        comments.append(comment_json)


                        if not CommentAuthors.objects.filter(user_id = comment.get('from').get('id')).exists():
                            CommentAuthors.objects.create(user_id=comment.get('from').get('id'))
                        

                        comment_auth = CommentAuthors.objects.last()

                        Comments.objects.create(
                            user_id = comment_auth,
                            post_id = post_id,
                            comment_id=comment.get('id'),
                            comment = comment.get('message'),
                            created_at = comment.get('created_time')
                        )
    # 3rd we need to reply comments
    response = []
    print('comments -> ',comments)
    for comment in comments:
        response_json = dict()

        """ REPLY COMMENT """

        print('comment count -> ',Comments.objects.filter(user_id=comment.get('userID')).count())
        comment_author_id = CommentAuthors.objects.filter(user_id = comment.get('userID')).last()

        if Comments.objects.filter(user_id_id=comment_author_id.id).count() == 1 and Comments.objects.filter(user_id_id=comment_author_id.id).last().is_sent == False:

            comment_url = 'https://graph.facebook.com/v13.0/{}/comments?access_token={}'.format(comment.get('commentID') ,ACCESS_TOKEN)
            body = {
                "message":"Melumat inboxa gonderildi"
            }
            headers = {'content-type': 'application/json'}
            comment_ = requests.post(comment_url, json=body, headers=headers).json()
            
            """ SEND MESSAGE TO COMMENT AUTHOR """
            headers = {'content-type': 'application/json'}
            body_ = {
                "messaging_type":"MESSAGE_TAG",
                "tag":"CONFIRMED_EVENT_UPDATE",
                "recipient": {
                    "comment_id": comment.get('commentID')
                },
                "message": {
                    "text": "Salam, ətraflı məlumat almaq üçün 055 213 73 12 və ya 055 213 36 13 nömrələrilə əlaqə saxlaya bilərsiniz."
                }
            }
            url = 'https://graph.facebook.com/v13.0/me/messages?access_token={}'.format(ACCESS_TOKEN)

            send_message_comment_author = requests.post(url, json=body_, headers=headers).json()

            comm = Comments.objects.filter(user_id_id=comment_author_id.id).last()
            comm.is_sent = True
            comm.save()
            if comment.get('id') and send_message_comment_author.get('id'):
                response_json[comment.get('commentID')] = 'gonderildi'
                response_json[f"№ {comment.get('commentID')}"] = 'mesaj gonderildi'

            else:
                response_json[comment.get('commentID')] = comment_
                response_json[f"№ {comment.get('commentID')}"] = send_message_comment_author
            
            response.append(response_json)
        else:
            comment_url = 'https://graph.facebook.com/v13.0/{}/likes?access_token={}'.format(comment.get('commentID') ,ACCESS_TOKEN)
            headers = {'content-type': 'application/json'}
            comment = requests.post(comment_url, headers=headers).json()
            print({'is liked':comment})
    print(response)
    return response