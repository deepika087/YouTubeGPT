__author__ = 'deepika'

"""
Function: to fetch the youtube comments given a youtube video id
"""
import os
from settings import DEVELOPER_KEY, YOUTUBE_SERVICE_NAME, YOUTUBE_API_VERSION, DA_VINCI_MODEL_LIMITATION

import googleapiclient.discovery
import json

def search_comments(youtube, video_id):
    #print("finding comments for the video id: " + video_id)
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
    )
    response = request.execute()
    return response

def build_youtube_service():
    return googleapiclient.discovery.build(
                YOUTUBE_SERVICE_NAME,
                YOUTUBE_API_VERSION, 
                developerKey = DEVELOPER_KEY)

"""
#Davinci model support 4000 token which is approx 3125 words 
# which is approx  approximately 11 pages.
"""
def extract_data(raw_data = ''):

    # uncomment only if you want to test the JSON parsing of youtube comments sections
    # on the sample file or if you want to save on youtube API calls.  
    """
    comment_file_data = open('sampleyoutubecomment.json')
    raw_data = json.load(comment_file_data)
    """

    running_data = ''
    running_data_count = 0

    comments = []

    for item in raw_data['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
        count = len(comment.split())

        if running_data_count + count < DA_VINCI_MODEL_LIMITATION:
            running_data += comment
            running_data += ' '
            running_data_count += count
        else:
            #add the collection of comments to the list
            comments.append(running_data)

            #reset the data/collection
            running_data = comment
            running_data_count = count

    #Add the last chunk of data if any
    if len(running_data) > 0:
        comments.append(running_data)

    return comments

def comment_workflow(video_id):
    youtube = build_youtube_service()
    raw_data = search_comments(youtube, video_id)
    comments = extract_data(raw_data)
    return comments

#Uncomment only if you want to test the JSON parsing of youtube comments sections
#if __name__ == "__main__":
#    extract_data()