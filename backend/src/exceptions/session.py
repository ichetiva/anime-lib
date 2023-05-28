from fastapi import HTTPException


class NoPermissionsError(HTTPException):
    def __init__(self):
        super().__init__(403, "You have no permissions")
