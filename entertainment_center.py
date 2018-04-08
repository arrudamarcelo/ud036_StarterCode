# Instantiate all movies and call 'open_movies_page()' to render the content.

import json
import media
import fresh_tomatoes

def loadMovies():
	""" Return a list with movies """

	# It's using a JSON to fetch content but can be change to use an API
	return loadMoviesFromJson()

def loadMoviesFromJson():
	""" Read a JSON, and return a list with movies """
	#movie list to be returned
	movies = []

	try:
		json_file='movies.json'

		#open file to read
		json_data=open(json_file)

		#decode the file to an array
		data = json.load(json_data)

		#close the file
		json_data.close()

		# Access data and construct the Movie object
		for x in data['movies']:
			#check if all required fields are filled
			if x['title'] and x['poster image url'] and x['trailer url']:
				m = media.Movie(x['title'], x['description'], 
								x['poster image url'], x['trailer url']);
				#append new movie to list
				movies.append(m)
	 
	except (ValueError, KeyError, TypeError):
		print "JSON format error"
		return []

	return movies

movies = loadMovies()
if movies: # check if movies list is not empty
	fresh_tomatoes.open_movies_page(movies) # call to create movies webpage
else:
	print ("It was not possible to load any movie from JSON. " 
		   "Check if the file is filled correctly.")