import media
import fresh_tomatoes

china_hustle = media.Movie("The China Hustle",
						"An unsettling and eye-opening Wall Street horror story about Chinese companies",
						"https://ia.media-imdb.com/images/M/MV5BMjIzNTcxMDU5OF5BMl5BanBnXkFtZTgwNzk0MDM0NDM@._V1_UX182_CR0,0,182,268_AL_.jpg", 
						"https://www.youtube.com/watch?v=55892jT06aI")
#print(toy_story.storyline)

black_panther = media.Movie("Black Panther",
					 "T'Challa, the King of Wakanda, rises to the throne in the isolated, technologically advanced African nation, but his claim is challenged by a vengeful outsider who was a childhood victim of T'Challa's father's mistake.",
					 "https://ia.media-imdb.com/images/M/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg", 
					 "https://www.youtube.com/watch?v=dxWvtMOGAhw")

batman = media.Movie("Batman Dark Knight Rises",
					 "It has been eight years since Batman (Christian Bale), in collusion with Commissioner Gordon (Gary Oldman), vanished into the night. Assuming responsibility for the death of Harvey Dent, Batman sacrificed everything for what he and Gordon hoped would be the greater good. However, the arrival of a cunning cat burglar (Anne Hathaway) and a merciless terrorist named Bane (Tom Hardy) force Batman out of exile and into a battle he may not be able to win.",
					 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHkmmgxTSX3z4Sk_3CrYmoIfdDjXPwKCXWMr5TyhOlxHWL6nVd", 
					 "https://www.youtube.com/watch?v=GokKUqLcvD8")

avengers_infinity_war = media.Movie("Avengers: Infinity War",
					 "Iron Man, Thor, the Hulk and the rest of the Avengers unite to battle their most powerful enemy yet -- the evil Thanos. On a mission to collect all six Infinity Stones, Thanos plans to use the artifacts to inflict his twisted will on reality. The fate of the planet and existence itself has never been more uncertain as everything the Avengers have fought for has led up to this moment.",
					 "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg", 
					 "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

pacific_rim = media.Movie("Pacific Rim",
					 "Long ago, legions of monstrous creatures called Kaiju arose from the sea, bringing with them all-consuming war. To fight the Kaiju, mankind developed giant robots called Jaegers, designed to be piloted by two humans locked together in a neural bridge. However, even the Jaegers are not enough to defeat the Kaiju, and humanity is on the verge of defeat. Mankind's last hope now lies with a washed-up ex-pilot (Charlie Hunnam), an untested trainee (Rinko Kikuchi) and an old, obsolete Jaeger.",
					 "http://t3.gstatic.com/images?q=tbn:ANd9GcT24u-kDNdX_vpwbAkMyXGKDIz7m-h_QorA_o6m0q36GPHDgJmU", 
					 "https://www.youtube.com/watch?v=5guMumPFBag")

animal_crackers = media.Movie("Animal Crackers",
					 "A workaholic dad, stuck in a nowhere job, inherits a rundown circus from a distant relative he hardly knew. On the brink of losing his job, his house, and his sanity he uncovers a magical box of Animal Crackers that gives him the uncanny ability to become any animal from the box.",
					 "https://ia.media-imdb.com/images/M/MV5BZDBkODRlMWMtMDEzNS00Zjc1LTlhNDItZTk1NmZhNmI2YzA1XkEyXkFqcGdeQXVyNTY0MTg1NTE@._V1_UX182_CR0,0,182,268_AL_.jpg", 
					 "https://www.youtube.com/watch?v=6yrtrDjmw5c")


movies = [pacific_rim, animal_crackers, china_hustle, avengers_infinity_war, batman, black_panther]
fresh_tomatoes.open_movies_page(movies)