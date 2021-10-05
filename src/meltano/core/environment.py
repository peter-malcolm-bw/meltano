from meltano.core.behavior import NameEq
from meltano.core.behavior.canonical import Canonical


class Environment(NameEq, Canonical):
    """Runtime environment for Meltano runs."""

    def __init__(
        self,
        name: str = None,
    ) -> None:
        """Create a new environment object.

        Args:
            name: Environment name. Must be unique. Defaults to None.
        """
        super().__init__()

        self.name = name
