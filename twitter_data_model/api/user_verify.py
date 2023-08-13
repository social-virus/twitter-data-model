"""User Verification class definitions."""

from __future__ import annotations

from typing import (
    List,
    Optional,
)


from pydantic import (  # pylint: disable=no-name-in-module
    BaseModel,
)


# pylint: disable=too-few-public-methods


class VerificationInfo(BaseModel):
    """Verification Info object."""

    reason: Optional[VerificationInfoReason]


class VerificationInfoReason(BaseModel):
    """Verification Info Reason object."""

    description: VerificationInfoReasonDescription


class VerificationInfoReasonDescription(BaseModel):
    """Verification Info Reason Description object."""

    text: str
    entities: List[VerificationInfoEntity]


class VerificationInfoEntity(BaseModel):
    """Verification Info Entity object."""

    from_index: int
    to_index: int
    ref: VerificationInfoRef


class VerificationInfoRef(BaseModel):
    """Verification Info Reference object."""

    url: str
    url_type: str


VerificationInfo.update_forward_refs()
VerificationInfoReason.update_forward_refs()
VerificationInfoReasonDescription.update_forward_refs()
VerificationInfoEntity.update_forward_refs()
