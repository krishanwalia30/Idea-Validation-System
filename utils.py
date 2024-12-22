import praw
import os
from dotenv import load_dotenv
load_dotenv()

# Initialize the Reddit instance
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ["REDDIT_USER_AGENT"]
)


# Tool for searching the market
def search_market(query:str) -> str:
    """Return the top discussions on the topic in the market."""
    total_dataset=[]
    # Perform the search across all of Reddit
    for submission in reddit.subreddit('all').search(query, limit=10):
        title = "Title: "+str(submission.title)
        body = "Body: "+str(submission.selftext)
        score = "Score: "+str(submission.score)
        subreddit = "Subbreddit: "+str(submission.subreddit.display_name)
        # print('Comments:')

        # Fetch comments
        comments_data = []
        # submission.comments.replace_more(limit=0)
        for i, comment in enumerate(submission.comments.list()[:5]):
            comment_body = "Comment Body: "+ str(comment.body)
            comment_score = "Comment Score: "+ str(comment.score)
            comments_data.append((comment_body, comment_score))
            # print(f'{i+1}. {comment.body}')
            # print(f'   Score: {comment.score}')
            # print('---')

        # print('\n' + '='*50 + '\n')
        total_dataset.append(str((title, body, score, subreddit, f"Comments: {comments_data}")))
        return str(total_dataset)