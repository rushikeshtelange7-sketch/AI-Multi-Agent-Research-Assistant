from ddgs import DDGS


def search_web(query):

    results = []

    try:

        with DDGS() as ddgs:

            search_results = ddgs.text(query, max_results=3)

            for item in search_results:

                results.append(item.get("title", "No title"))

    except Exception as e:

        results.append(f"Search Error: {e}")

    return results