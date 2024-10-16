# Generated by ariadne-codegen
# Source: queries.gql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class Ping(BaseModel):
    ping: str
    organizations: Optional[List["PingOrganizations"]]


class PingOrganizations(BaseModel):
    id: str
    profile: "PingOrganizationsProfile"


class PingOrganizationsProfile(BaseModel):
    display_name: Optional[str] = Field(alias="displayName")


Ping.model_rebuild()
PingOrganizations.model_rebuild()
