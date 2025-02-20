import wikipedia


class WikipediaApp:
    def get_wiki(self, query):
        try:
            return wikipedia.summary(query, sentences=3)
        except Exception as e:
            return "Try a different search term."


def main():
    wiki_app = WikipediaApp()
    while True:
        print(wiki_app.get_wiki(input("Search Wikipedia: ").strip()))
        if input("Search again? y/n: ").lower() != "y":
            break


if __name__ == "__main__":
    main()
