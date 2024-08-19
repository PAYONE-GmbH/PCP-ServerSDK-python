from typing import List


class APIError:
    def __init__(self, error_id: str, message: str):
        self.error_id = error_id
        self.message = message
