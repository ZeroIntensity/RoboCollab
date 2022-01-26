from typing import TypedDict

class StateConfig(TypedDict):
    mongo_url: str
    graphiql: bool
    ip: str
    port: int
    require_auth: bool

class Config(TypedDict):
	production: bool
	prod: StateConfig
	dev: StateConfig