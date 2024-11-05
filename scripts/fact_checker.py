import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')

page_py = wiki_wiki.page('Python_(programming_language)')

print("Page - Exists: %s" % page_py.exists())


print("Page - Title: %s" % page_py.title)

print("Page - Summary: %s" % page_py.summary[0:60])
