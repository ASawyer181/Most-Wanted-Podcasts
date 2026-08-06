import requests
import sys


class Podcasts:
    """
    initalizes the keyword and calls on the methods
    :param keyword: the person being searched for in podcasts
    :type: string
    """

    def __init__(self, keywords):
        self.keyword = keywords

    """
    searches for the episodes given the terms
    :param term: the term being searched for in the podcasts
    :type: str
    :return: dict
    """

    def search_episodes(self):
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

    """
    This will take all results and add them to a set to ensure their arent any duplicates
    then it will add them to the list of results
    :param data: the data that is found from search_episodes
    :type: dict
    :return: list
    """

    def inspect_first_result(self, data):
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
            if (all(k.lower() in title for k in self.keyword)) and (
                "crime" in ep.get("collectionName").lower()
                or "crime" in ep.get("trackName").lower()
            ):
                seen.add(key)
                results.append(ep)
        return results

    """
    will print out all given results
    """

    def print_results(self, results):
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
