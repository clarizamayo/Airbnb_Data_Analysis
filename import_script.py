
from app import db, Emissions
from app import db, Population
from emission import co2_emissions
from population import world_pop_2005

emiss_url = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions"
pop_url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_in_2005"

# set up your scraping below

emission_table = co2_emissions(emiss_url)
population_table = world_pop_2005(pop_url)

# this `main` function should run your scraping when 
# this script is ran.
def main():
    db.drop_all()
    db.create_all()
    for country in emission_table:
        new_row = Emissions(name = country[0], emission_1990=country[1], emission_2005=country[2], emission_2017=country[3],perc_world_emissions=country[4], perc_change_2017_2019=country[5], per_land_area=country[6], per_capita=country[7])
        print(new_row)
        db.session.add(new_row)
        db.session.commit()

    for country in population_table:
        new_row = Population(name = country[0], population=country[1])
        print(new_row)
        db.session.add(new_row)
        db.session.commit()

if __name__ == '__main__':
    main()