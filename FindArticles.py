articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    matching_articles = []

    for article in articles_dict:
        author = article["author"]
        title = article["title"]

        if not letter_case:
            key = key.lower()
            author = author.lower()
            title = title.lower()

        if key in author or key in title:
            matching_articles.append({
                "author": article["author"],
                "title": article["title"],
                "year": article["year"],
            })

    return matching_articles

# Приклад використання
result1 = find_articles("Ocean")
result2 = find_articles("python", letter_case=False)
result3 = find_articles("Python", letter_case=True)

print("Результат 1:", result1)
print("Результат 2:", result2)
print("Результат 3:", result3)
