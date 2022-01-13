from pythondi import Provider, configure
# from app.user.repository.user import UserRepo, UserMySQLRepo



def init_di():
    provider = Provider()
    # provider.bind(UserRepo, UserMySQLRepo)
    configure(provider=provider)
    pass