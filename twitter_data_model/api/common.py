"""Base class mixin."""

import json

from typing import (
    Any,
    Dict,
    List,
    Set,
)

import yaml


def _getattr(kwargs: Dict, config: Dict, attr: str, default: Any = None):
    """Three-way evaluation of parameters, class settings, and default value."""

    if attr in kwargs:
        # Prioritize parameterized argument.
        _attr = kwargs.get(attr) or default

        if not isinstance(_attr, (Set, List)):
            opts = set()
            opts.add(_attr)
            return opts
        return _attr

    if hasattr(config, attr):
        # Fall-back to class settings in 'BaseModel.Config'.
        return getattr(config, attr, default)

    # Fall-through to the default value
    return default


# pylint: disable=too-few-public-methods


class BaseMixin:
    """Base mixins."""

    class Config:  # pylint: disable=missing-class-docstring
        exclude: Set = None
        include: Set = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Read from dict object."""

        if isinstance(data, List):
            return [cls.from_dict(datum) for datum in data]

        return cls(**data)

    @classmethod
    def from_json(cls, pathname: str, encoding: str = "utf8"):
        """Read from JSON file."""

        with open(
            pathname, mode="r", encoding=encoding
        ) as fp:  # pylint: disable=invalid-name
            data = json.load(fp)

            if isinstance(data, List):
                return [cls(**datum["data"]["user"]["result"]) for datum in data]

            return cls(**data)

    def dict(self, **kwargs):
        """Convert to dict output."""

        config = self.Config

        kwargs["exclude"] = _getattr(kwargs, config, "exclude", None)
        kwargs["include"] = _getattr(kwargs, config, "include", None)

        return super().dict(**kwargs)

    def json(self, **kwargs):
        """Convert to JSON output."""

        config = self.config

        kwargs["exclude"] = _getattr(kwargs, config, "exclude", None)
        kwargs["include"] = _getattr(kwargs, config, "include", None)
        kwargs["indent"] = kwargs.get("indent", 4)

        return super().json(**kwargs)

    def yaml(self, **kwargs) -> str:
        """Convert to YAML output."""

        config = self.Config

        kwargs["exclude"] = _getattr(kwargs, config, "exclude", None)
        kwargs["include"] = _getattr(kwargs, config, "include", None)
        kwargs["sort_keys"] = kwargs.get("sort_keys", False)

        return yaml.dump(self.dict(), **kwargs)
