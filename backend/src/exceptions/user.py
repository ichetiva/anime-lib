from fastapi import HTTPException


class AlreadyExistsError(HTTPException):
    def __init__(self) -> None:
        super().__init__(409, "User already exists")


class DoesNotExistError(HTTPException):
    def __init__(self) -> None:
        super().__init__(404, "User does not exist")


class WrongPasswordError(HTTPException):
    def __init__(self) -> None:
        super().__init__(401, "Wrong password")


class PasswordsMismatchError(HTTPException):
    def __init__(self) -> None:
        super().__init__(400, "Passwords mismatch")
