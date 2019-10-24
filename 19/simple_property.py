from datetime import datetime, timedelta

NOW = datetime.now()


class Promo:
    def __init__(self, name: str, expires: datetime):
        self.name = name
        self.expires = expires

    @property
    def expired(self) -> bool:
        """Get the expired status."""
        if datetime.now() <= self.expires:
            return False
        else:
            return True


if __name__ == '__main__':
    promo = Promo("20% off until tomorrow", datetime.today() + timedelta(days=1))

    print(promo.expired)
    print(promo.expires)
    promo.expires = datetime.now()
    print(promo.expired)
