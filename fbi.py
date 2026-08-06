import requests

class FBI:

    """
    This class initalizes a dict to nothing and then when called on
    it will create a dict via the make Dict method which calls n the grabAPI method to make the dict
    full of the information that is held in the fbis top 10 most wanted murderers list
    """
    def __init__(self):
        self.fbidict = {}

    """
    This makes the dict that is filled with api data
    :return: dict
    """
    def makeDict(self):
        self.fbidict = self.grabAPI()
        return self.fbidict

    """
    gets and opens the api and retrieves data to be put into a dict with their name and crime
    :return: dict
    """
    def grabAPI(self):
        people = {}
        page = 1

        while True:
            response = requests.get("https://api.fbi.gov/wanted/v1/list", params={"page": page})
            items = response.json()["items"]

            if not items:
                break

            for person in items:
                if person["url"] and "/wanted/murders/" in person["url"]:
                    people[person["title"]] = person["description"]

            page += 1

        return people

def main():
    fbi = FBI()
    fbi.makeDict()
    print(len(fbi.fbidict))
    print(fbi.fbidict)


if __name__ == "__main__":
    main()
