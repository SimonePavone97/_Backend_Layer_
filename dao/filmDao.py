from dao.utility.db import MySql

class Film:

    @classmethod
    def getAllFilm(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM film")
        data = MySql.getResults()
        MySql.closeConnection()

        return data

    @classmethod
    def getAllPgFilms(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM film WHERE rating like 'PG%'")
        
        data = MySql.getResults()
        MySql.closeConnection()

        return data

    @classmethod
    def getAllTitleStartR(cls):
        MySql.openConnection()
        MySql.query("SELECT title FROM film WHERE title LIKE 'R%'")

        data = MySql.getResults()
        MySql.closeConnection()

        return data
    
    @classmethod
    def getAllCategoryFilm(cls):
        MySql.openConnection()
        MySql.query("select f.title from Category as c inner join film_category as f_c on f_c.category_id = c.category_id inner join Film as f on f_c.film_id = f.film_id where c.name = 'Action';")
        data = MySql.getResults()
        MySql.closeConnection()

        return data


