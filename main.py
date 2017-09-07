import requests
import re

def PullFromBlueApron():
	response = requests.get('https://www.blueapron.com/pages/sample-recipes')
	m = re.findall(r"/recipes/[a-z-]+", response.text.strip())
	recipies = []
	for r in m:
		recipe = "https://www.blueapron.com" + r.encode("ascii")
		if not "application" in recipe:
			recipies.append(recipe)
	return recipes


#Gets recipies from online sources and JSON store
def GetRecipies():
	recipies = []

	#Get Recipies from Blue Apron
	BlueApron = PullFromBlueApron()

"""
Main function, takes args for number of people to assign recipies to
gets recipies then assignes them
"""
def main():
	recipies = GetRecipies()

if __name__ == "__main__":
    # execute only if run as the entry point into the program
    main()
