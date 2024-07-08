import json

movies = {'name' : 'Scarface', 
          'Actors' : ["Al Pacino", "Steven Bauer", "Mark Margolis"],
          'year' : 1983
          }


def handlingDictionary(dictionary):
    for key, value in dictionary.items():
        print(f"Key : {key}, Value : {value}")


def handlingLists(lists):
    for item in lists:
        print(item)

actors_list = movies['Actors']

handlingLists(actors_list)