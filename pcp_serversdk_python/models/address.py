
from typing import Optional

class Address:
    def __init__(
        self,
        additionalInfo: Optional[str] = None,
        city: Optional[str] = None,
        countryCode: Optional[str] = None,
        houseNumber: Optional[str] = None,
        state: Optional[str] = None,
        street: Optional[str] = None,
        zip: Optional[str] = None
    ):
        """
        Object containing billing address details

        :param additionalInfo: Second line of street or additional address information such as apartments and suits
        :param city: City
        :param countryCode: ISO 3166-1 alpha-2 country code
        :param houseNumber: House number
        :param state: State (ISO 3166-2 subdivisions), only if country=US, CA, CN, JP, MX, BR, AR, ID, TH, IN.
        :param street: Street name
        :param zip: Zip code
        """
        self.additionalInfo = additionalInfo
        self.city = city
        self.countryCode = countryCode
        self.houseNumber = houseNumber
        self.state = state
        self.street = street
        self.zip = zip

    def __str__(self):
        return str(self.__dict__)
