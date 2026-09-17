from fbi import FBI
from AppleMusicPods import Podcasts
import sys
def main():
    print(
        "Hi, welcome to find your podcast,\nhere you can find any true crime podcast\n" \
        "about a specific wanted murderer from the FBI's most\nwanted list!\n"
    )
    fbiDict = getFBIList()

    for person in fbiDict:
        print(f"Persons Name: {person}\nDescription Of Crime: {fbiDict[person]}\n")
    poiName = input("What is the name (as shown in the list) of the person you are interested in\nlistening to a podcast about: ")
    print("\n")
    poiName = check_name(fbiDict, poiName)
    search_podcasts(poiName)


def search_podcasts(keyword):
    """
    This will use the applePods class to search for podacasts in apple music that contain the given keyword
    the keyword will be the name of someone from the fbis most wanted list
    :param keyword: the name of the person that we are searching for in the apple podcasts api
    :type: int
    :return: list for testing
    """
    # list = [keyword, "true"]
    podcast = Podcasts(keyword)
    data = podcast.search_episodes()
    results = podcast.inspect_first_result(data)
    podcast.print_results(results)

    return results



def getFBIList():   
    """
    This loads in the FBI most wanted list from the fbi class
    located in fbi.py
    :return: dict
    """
    print("Loading data from the FBI's database, this may take a moment...")
    fbi = FBI()
    return fbi.makeDict()


def check_name(fbiDict, poiName):
    """
    This checks the name given the dictonary and the name the person
    entered into the program
    :param fbiDict: the dictonary from the fbi class
    :type: dict
    :param poiName: The name the user entered into the main function
    :type: string
    :return: string
    """
    # print(list(fbiDict.keys()))
    lwoer_dict = {name.lower(): name for name in fbiDict}

    if poiName.strip().lower() not in lwoer_dict:
        sys.exit("Please ensure to you are naming someone from the list above!")
    return poiName.strip().lower()



if __name__ == "__main__":
    main()
