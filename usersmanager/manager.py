"""Needed classes for implementing the Manager interface."""

from typing import Optional

import Ice
import UsersManager as um


class Manager(um.Manager):
    """Skeleton for the Manager implementation."""

    def login(self, username: str, password: str, current: Optional[Ice.Current] = None) -> um.SessionPrx:
        """Create and return a Session object proxy if the credentials are valid."""

    def createUser(self, username: str, password: str, current: Optional[Ice.Current] = None) -> um.SessionPrx:
        """Create a new user and perform a login, returning a Session proxy."""

    def removeUser(self, active_session: um.SessionPrx, current: Optional[Ice.Current] = None) -> None:
        """Delete an user from the database, if the session is valid."""

    def verifySession(self, session: um.SessionPrx, current: Optional[Ice.Current] = None) -> bool:
        """Check if the Session is legitimate."""
        return False
