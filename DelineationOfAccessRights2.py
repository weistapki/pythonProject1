class AccessLevel:
    name: str
    level: int

    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level

    def __eq__(self, other):
        return self.level == other.level

    def __lt__(self, other):
        return self.level < other.level

    def __gt__(self, other):
        return self.level > other.level

    def __ge__(self, other):
        return self.level >= other.level


if __name__ == '__main__':
    unclassified = AccessLevel("Unclassified", 1)
    secret = AccessLevel("Secret", 2)
    top_secret = AccessLevel("Top Secret", 3)
    print(unclassified < secret)  # True
    print(secret == secret)  # True
    print(unclassified > top_secret)  # False


class AccessObject:
    name: str
    content: str
    access_level: AccessLevel

    def __init__(self, name: str, content: str, access_level: AccessLevel):
        self.name = name
        self.content = content
        self.access_level = access_level


class User:
    login: str
    __mandatum: AccessLevel

    def __init__(self, login: str, mandatum: AccessLevel):
        self.login = login
        self.__mandatum = mandatum

    @property
    def mandatum(self) -> str:
        return self.__mandatum.name

    @mandatum.setter
    def mandatum(self, value: AccessLevel):
        if isinstance(value, AccessLevel):
            self.__mandatum = value

    def greet(self):
        print(f"Hi, my login is {self.login}")

    def get_access(self, access_object: AccessObject):
        if isinstance(self.__mandatum, AccessLevel) and isinstance(access_object.access_level, AccessLevel):
            if self.__mandatum >= access_object.access_level:
                print(access_object.content)
            else:
                print("Access to this resource denied!")
        else:
            print("Invalid access level or access object.")


if __name__ == '__main__':
    unclassified = AccessLevel("Unclassified", 1)
    secret = AccessLevel("Secret", 2)
    top_secret = AccessLevel("Top Secret", 3)

    alice = User("Alice", top_secret)
    bob = User("Bob", unclassified)

    password_database = AccessObject(
        "Password Database",
        "Alice - C00peR, Bob - uNc1e",
        secret
    )

    alice.greet()
    alice.get_access(password_database)

    bob.greet()
    bob.get_access(password_database)

# Другий сценарій:
#
# 1.Визначення рівня доступу користувача:
# Користувач має свій рівень доступу (mandatum).
# 2.Перевірка доступу до об'єкта:
# Користувач вимагає доступ до об'єкта.
# Перевіряється, чи рівень доступу користувача (mandatum) вищий або рівний рівню доступу об'єкта (access_object).
# Якщо користувач має відповідний рівень доступу, виводиться вміст об'єкта. Інакше виводиться повідомлення про відмову у доступі.
