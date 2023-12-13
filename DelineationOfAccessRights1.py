class User:
    login = "Guest"

    def greet(self):
        print(f"Hi, my login is {self.login}")


class AuthenticatedUser(User):
    password = "password"

    def authenticate(self, user_password):
        return user_password == self.password


class AccessObject:
    content = "*"
    owner = None
    name = ""

    def change_owner(self, old_owner_password, new_owner):
        if self.owner is None:
            print("Object owner is not set.")
        elif self.owner.authenticate(old_owner_password):
            print(f"The ownership changing of '{self.name}' was successful! New owner is {new_owner.login}.")
            self.owner = new_owner
        else:
            print(f"Unauthorised attempt of '{self.name}' owner changing detected!")


if __name__ == '__main__':
    alice = AuthenticatedUser()
    alice.login = "Alice"
    bob = AuthenticatedUser()
    bob.login = "Bob"
    bob.password = "uNc1e"

    log = AccessObject()
    log.owner = alice
    log.name = "Computer logs"
    log.content = "There is no entries yet"

    security_policy = AccessObject()
    security_policy.owner = bob
    security_policy.name = "Enterprise security policy"
    security_policy.content = "Only authorized users may access objects"

    log.change_owner(bob.password, bob)
    security_policy.change_owner(bob.password, alice)


# Перший сценарій:
#
# 1.Аутентифікація користувача:
# Користувач вводить логін та пароль.
# Перевіряється відповідність введеного пароля збереженому паролю користувача.
# Якщо паролі співпадають, користувач аутентифікований.
# 2.Зміна власника об'єкта:
# Перевіряється чи власник об'єкта аутентифікований (чи вірний пароль).
# Якщо аутентифікація пройшла успішно, власника об'єкта змінюється.