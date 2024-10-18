"""Module containing the handler functions for CLI commands."""

import logging
import os
import sys

from usersmanager.server import Server


def users_manager_server() -> None:
    """Handle for running the server for users manager."""
    logging.basicConfig(level=logging.DEBUG)

    cmd_name = os.path.basename(sys.argv[0])

    logger = logging.getLogger(cmd_name)
    logger.info("Running %s server...", sys.argv[0])

    server = Server()
    sys.exit(server.main(sys.argv))
