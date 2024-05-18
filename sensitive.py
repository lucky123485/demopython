# File: sensitive_data.py

class SensitiveData:
    def __init__(self):
        self.rsa_private_key = """
-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDZRsz7B2Vd1TihbDh0mXvYpX1Cq2uQ+XzwKjnK0P6C1StIaOaG
o9QEB/C4Gy1ov5BmqUv7t2S47thT+KP2zjvzskf1yE5Fg9U/xZfBRRUilUz6y75c
gWwhhoyZfE5PG5JLj9P6cnQg2x2QVCEU3tVJYRFcEBNQ7bbYvobv0lLkQIDAQAB
AoGAP4ZKfy9Gg+UwVXupcOq5tP94svT3K3/gLkNlqFfTtX45hwkOCV72ksk9kTxk
7fv0WCDXj+5uhSHnTQWIDNrNmJrfI6FmGnDDNcPTcQm46J99yN1pgcW59XubJ1qf
kO3uhllt8y7S/Mn+8W1YrziISvI4y6+TAWrzKJj6eE2oh9ECQQDQzRr+7Y8ED7A7
G1VD4OoHL0leY9YN4IzXVNZ/ODwJVVubLkA+ZlFMsXQ9zYgAgrxOeXgec/8ITM1C
hZp43G5DAkEA2JWtPvLEOU2Nz4Q+T4KQd3tOro9iMT+6H+x9QAX4OeK/U/ryuyGJ
SZR96Z5oO2BFhBpJp7nBYIImMfTSb+YXJwJBAJW7aVJHAd/WR8A5ok/7FQsSwx4n
l85pJFiyUP7lmC+w7/hd2lGZnAkq6j74NTfpYHKhvCq7NwD4IVtY5cBglW8CQQDS
sfC4QHbbG4bLxTgS+lsKq+GUV+gxKGi/mcVLjtmFNoPRqPhxOWnlJjucpc8DFgYk
XlcC+pSyX4aEY/KUrPL9AkBySP1SkUoDdD2DkRAQUgV4gJLJ5bdQwDpU5sQ8wnny
BNhGYBqjNN7Q6vlnY9GK3d5Rv1n5oYZzAKb/sSKljzUt
-----END RSA PRIVATE KEY-----
"""

        self.secret_password = "my_secret_password"

if __name__ == "__main__":
    data = SensitiveData()
    print("RSA Private Key:")
    print(data.rsa_private_key)
    print("\nSecret Password:")
    print(data.secret_password)
