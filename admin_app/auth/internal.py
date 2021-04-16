

def auth_headers(func):
    def insert_header(*args, **kwargs):
        # insert request headers here
        return func(*args, **kwargs)
    return insert_header

