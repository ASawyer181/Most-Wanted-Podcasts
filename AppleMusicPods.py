import requests
import sys


class Podcasts:


    def __init__(self, keywords):
        """
        initalizes the keyword and calls on the methods
        :param keyword: the person being searched for in podcasts
        :type: string
        """
        self.keyword = keywords



    def search_episodes(self):
        """
        searches for the episodes given the terms
        :param term: the term being searched for in the podcasts
        :type: str
        :return: dict
        """
        response = requests.get(
            "https://itunes.apple.com/search",
            params={
                "term": self.keyword,
                "media": "podcast",
                "entity": "podcastEpisode",
                "limit": 200,
            },
        )
        return response.json()



    def inspect_first_result(self, data):
        """
        This will take all results and add them to a set to ensure their arent any duplicates
        then it will add them to the list of results
        :param data: the data that is found from search_episodes
        :type: dict
        :return: list
        """
        if data.get("resultCount", 0) == 0:
            sys.exit("No results.")
            return
        seen = set()
        results = []
        for ep in data["results"]:
            title = ep.get("trackName").lower()
            publisher = ep.get("collectionName").lower()
            key = (title, publisher)
            if key in seen:
                continue
            if all(word in title for word in self.keyword.lower().split()) and (
                "crime" in ep.get("collectionName").lower()
                or "crime" in ep.get("trackName").lower()
            ):
                seen.add(key)
                results.append(ep)
        return results



    def print_results(self, results):
        """
        will print out all given results
        :param results: the results given from the inspect first result function
        :type: list
        """
        count = 0
        if len(results) == 0:
            sys.exit("No results for this person!")
        for ep in results:
            print(ep.get("trackName"), "—", ep.get("collectionName"), end="\n\n")
            count += 1
        if count == 0:
            sys.exit("No results for this person!")


def main():
    podcast = Podcasts("robert william fisher")
    data = podcast.search_episodes()
    final = podcast.inspect_first_result(data)
    for ep in final:
        print(ep.get("trackName"), "—", ep.get("collectionName"))


if __name__ == "__main__":
    main()
