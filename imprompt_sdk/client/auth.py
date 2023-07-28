import pydantic.dataclasses


@pydantic.dataclasses.dataclass
class Auth:
    api_key: str
