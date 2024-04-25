user = "lola"
# we declare a value

def decorator(func):
    def accept_user():
         if user != "lola":
            print("action refusée")
         else:
            func()
    return accept_user


@decorator
# syntactic sugar
def do_that():
    print("action validée")

do_that()