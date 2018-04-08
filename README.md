# Movie Trailer Website (ud036_StarterCode)
Create a Movie Trailer website allowing visitors to review their movies and watch the trailers. It's necessary to provide a list of movies, including poster image and a movie trailer URL.

## How to use
The Movie Trailer website generator consists in a python program, and movies content is fetch from a JSON file. Bellow you can see how to compile and run this program, as well as provide the movies content. 

### Movies Content
The movies content are fetch from a [JSON file](https://pythonspot.com/json-encoding-and-decoding-with-python/) called **movies.json**. The structure of this file is as follows:
```
{
	"movies": [
			{
		    "title": "",
		    "description": "",
		    "box image url": "",
		    "trailer url": ""
		}
    ]
}
```
For each movie you need to fill **movies.json** with title, description (not mandatory), poster image url, trailer url.
_The file is already filled with six movies to be used as a sample._

### Running the program to generate Movie Trailer Website
1. [Install Python](https://www.python.org/downloads/)
2. Compile and run python program entertainment_center.py:
``` python entertainment_center.py ```

This file will load the movies from **movies.json**, create the movie trailer website, and open the browser showing this webpage.