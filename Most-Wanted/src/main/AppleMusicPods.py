import requests
import sys
import re


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
        seen = set()
        results = []
        for ep in data.get("results", []):
            title = ep.get("trackName") or ""
            publisher = ep.get("collectionName") or ""
            description = ep.get("description") or ""
            searchable_text = self._normalize(" ".join((title, publisher, description)))
            person_words = self._person_words()

            if not person_words or not self._is_about_person(searchable_text, title, person_words):
                continue
            if not self._is_true_crime(ep, searchable_text):
                continue

            title = self._normalize(title)
            publisher = self._normalize(publisher)
            key = (title, publisher)
            if key in seen:
                continue
            seen.add(key)
            results.append(ep)
        return results

    @staticmethod
    def _normalize(value):
        """Make API text comparable without punctuation or case differences."""
        return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()

    def _person_words(self):
        return self._normalize(self.keyword).split()

    @staticmethod
    def _is_about_person(searchable_text, title, person_words):
        full_name = " ".join(person_words)
        title = Podcasts._normalize(title)
        surname_in_title = bool(person_words) and re.search(
            rf"\b{re.escape(person_words[-1])}\b", title
        )
        return surname_in_title and (full_name in searchable_text or all(
            re.search(rf"\b{re.escape(word)}\b", searchable_text)
            for word in person_words
        ))

    @staticmethod
    def _is_true_crime(episode, searchable_text):
        genre_ids = {str(genre_id) for genre_id in episode.get("genreIds", [])}
        if "1488" in genre_ids:
            return True

        crime_signals = (
            "true crime",
            "murder",
            "murdered",
            "homicide",
            "killer",
            "killing",
            "serial killer",
            "cold case",
            "missing person",
            "unsolved",
        )
        return any(signal in searchable_text for signal in crime_signals)



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
