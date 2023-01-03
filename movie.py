from pathlib import Path
import json
import logging
DATA_FILE=str(Path(__file__).parent.absolute()/"data/movies.json")


def get_movies():
    with open(DATA_FILE,"r") as file:
            movies_title=json.load(file)
    movies=[Movie(movie) for movie in movies_title]
    return movies


class Movie():
    data=[]
    def __init__(self,title) :
        self.title=title.title()
    
    def __str__(self) -> str:
        return self.title

    def _get_movies(self):  
        with open(DATA_FILE,"r") as file:
            data=json.load(file)
        return data
    
    def _write_movies(self,movies: list):
        with open(DATA_FILE,"w") as file:
            json.dump(movies,file,indent=4)

    def add_movies(self):
        list_movies=self._get_movies()
        if self.title not in list_movies:
            list_movies.append(self.title)
            self._write_movies(list_movies)
            return True
        else:
            logging.warning(f"Le film '{self.title}' est déjà enregistré!")
            return False
    def remove_from_movies(self):
        list_movies=self._get_movies()
        if self.title in list_movies:
            list_movies.remove(self.title)
            self._write_movies(list_movies)
            return True
        else:
            logging.warning(f"Le film {self.title} n'est pas dans la liste")
            return False



if __name__=="__main_":
   pass