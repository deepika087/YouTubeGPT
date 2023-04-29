{{{ YouTubeGPT }}}

The aim of this project is to allow the use to analyse youtube videos' comment section before watching the video. The user can not only see the youtube video comments but also do semantic analysis plus filter keywords from the comment section that will allow the user to make educated guess if the user would like to watch the video 


Pre-requisites
1. Youtube Data Key
2. Open AI key
3. python libraries such as openai


To run the project
 > Run the requirement file. 
 > Replace the keys in settings.py
 > analysis.py is the main file that can be called using python3 analysis.py video_id
 Say, python3 analysis.py DOWDNBu9DkU
 > This command will return summary, semantics and keywords of the comment section.


Sample Output 
To test out the code, I used the video of a famous Youtuber Mark Rober whose glitter bomb video had 19M views. 

python3 analysis.py DOWDNBu9DkU
-------------SUMMARY-------------
It is incredible to see how Rwandans have been able to use drones to save lives. It is inspiring to see the hard work and effort put into this project, and it is something that needs to be normalized in the future. It is also important to recognize the inventiveness of the people who designed these drones for positive medical delivery.
-------------SEMANTICS-------------
Positive
-------------KEYWORDS-------------
['Keywords: Rwandans, drones, save lives, hard work, effort, normalized, inventiveness, designed, positive medical delivery.']


Scope of Improvement
1. Say, the youtube video is related to finance, in the commment section people might express opinion about the bad conditions of financial markets or the failing banks. This will result is semantics is negative even if the purpose of the video were to be just educational. So, I think there is scope to tie the semantics of the video with the semantics of the comment section. 
2. Add unit testing
3. Add a switch such that when it is used the call to Youtube API is completely ignored and mocked data is used. 
4. Add the code behind a chrome extension for seamless integration. 

