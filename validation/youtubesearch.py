from youtube_search import YoutubeSearch
results = YoutubeSearch('de mysteriis dom sathanas', max_results=1).to_dict()

print(results)