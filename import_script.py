
from app import db, Emissions    #import the Class from the app.py file
from app import db, Population   #importing my second Class from the app.py file
from emission import co2_emissions   #import the scraping function from the emission.py file
from population import world_pop_2005  ##import the second craping function from the population.py file

emiss_url = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions"   #first link I am scraping
pop_url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_in_2005"   #second link I am scraping


emission_table = co2_emissions(emiss_url)   #setting up my funcs and passing the url link that is being scraped into a variable
population_table = world_pop_2005(pop_url)  #setting up my funcs and passing the url link that is being scraped into a variable

# this `main` function should run your scraping when 
# this script is ran.
def main():
    db.drop_all()   # makes sure there are no tables and the database is empty
    db.create_all()   #creates all the columns on the table that were defined inside the Class
    for country in emission_table:   #starts looping the result that came from the scraping function
        #in the next line we start defining each column with it's value using indexing since we have a list
        new_row = Emissions(name = country[0], emission_1990=country[1], emission_2005=country[2], emission_2017=country[3],perc_world_emissions=country[4], perc_change_2017_2019=country[5], per_land_area=country[6], per_capita=country[7])
        print(new_row)  #just to see each row 
        db.session.add(new_row)  # adds each row to the database
        db.session.commit()   #commit the changes so the database has all the new rows 

    for country in population_table:
        new_row = Population(name = country[0], population=country[1])
        print(new_row)
        db.session.add(new_row)
        db.session.commit()

if __name__ == '__main__':
    main()