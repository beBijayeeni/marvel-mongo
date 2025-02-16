
from db.vector import Vectorize

obj = Vectorize()

url_list = [
    "https://www.marvel.com/movies",
    "https://en.wikipedia.org/wiki/Marvel_Cinematic_Universe",
    "https://screenrant.com/marvel-2025-movies-list-release-dates"
]
#obj.client_setup()
obj.chunker(urls=url_list)

flag = obj.store()

if flag:
    print("Embedding & storage done")
else:
    print("Operation Failed")

from bot.query import Bot

obj = Bot()

obj.retrieval()

query = input("User query :- ")

answer = obj.response(query=query)

print(answer)