from .db import auth

def validate_auth(token: str) -> bool:
    """Function for validating authentication tokens."""
    doc = auth.find({'token': token})

    return bool(
        dict(doc)
    )
