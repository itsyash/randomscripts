#	first, install the facebook sdk for python :
# 	run 'pip install facebook-sdk'
#	OR
#	get it from here : https://github.com/pythonforfacebook/facebook-sdk and build it manually
#   ./setup.py build && ./setup.py install 

#	-----code-----

import facebook
import json

#make the fql query
#find out the time of the first post you want to start with, and change it with the created_time value

query = ("SELECT post_id, actor_id, message, created_time  FROM stream WHERE filter_key = 'others' AND source_id = me() AND created_time <= 1372874563 LIMIT 100")	


#get the graph api instance, get the required access token from https://developers.facebook.com/tools/explorer 
graph = facebook.GraphAPI("CAACEdEose0cBAD9sasmddq6dlCEI3uG4a9I4ZBW2tL2QNlBRLMnwYteZA29ix6S0mFZAfCfJwTE7rxcZCYZAuZCRnxrPZBFqIBuZCK8C2ERAiD32t0sUgLpc8CErzXeCAafa0qI6hELEVt5fC15X5aPo43CQvx24eTvCjXdVEQUTwSZBjWcVzSEZCtSlfWBiPjnGGFIu2E4mK7DwZDZD")

profile = graph.get_object("me")

#all the required posts
posts = graph.fql(query)

posts = posts['data']

#print posts	

for post in posts:
	print "done for  "
	print post
	graph.put_like(post['post_id'])		#like the post
	graph.put_comment(post['post_id'],"thank you :)")	#comment : " thank you :) "


