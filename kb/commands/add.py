# -*- encoding: utf-8 -*-
# kb v0.1.4
# A knowledge base organizer
# Copyright © 2020, gnc.
# See /LICENSE for licensing information.

"""
kb add command module

:Copyright: © 2020, gnc.
:License: GPLv3 (see /LICENSE).
"""

import shlex
import sys
from pathlib import Path
from subprocess import call
from typing import Dict
import kb.db as db
import kb.initializer as initializer
import kb.filesystem as fs
from kb.entities.artifact import Artifact
from kb.actions.add import add_file_to_kb


def add(args: Dict[str, str], file,config: Dict[str, str]):
    """
    Adds a list of artifacts to the knowledge base of kb.

    Arguments:
    args:           - a dictionary containing the following fields:
                      file -> a list of files to add to kb
                      title -> the title assigned to the artifact(s)
                      category -> the category assigned to the artifact(s)
                      tags -> the tags assigned to the artifact(s)
                      author -> the author to assign to the artifact
                      status -> the status to assign to the artifact
    config:         - a configuration dictionary containing at least
                      the following keys:
                      PATH_KB_DB        - the database path of KB
                      PATH_KB_DATA      - the data directory of KB
                      EDITOR            - the editor program to call
    """
    # Check if the add command has proper arguments/options
    is_valid_add = args["file"] or args["title"]
    if not is_valid_add:
        print("Please, either specify a file or a title for the new artifact")
        sys.exit(1)

    

    conn = db.create_connection(config["PATH_KB_DB"])
    if args["file"]:
        for fname in args["file"]:
            if fs.is_directory(fname):
                continue
            add_file_to_kb(conn, args, config, fname)
            print("here1")
    else:
        # Get title for the new artifact
        title = args["title"]

        # Assign a "default" category if not provided
        category = args["category"] or "default"

        # Create "category" directory if it does not exist
        category_path = Path(config["PATH_KB_DATA"], category)
        category_path.mkdir(parents=True, exist_ok=True)

        if not db.is_artifact_existing(conn, title, category):
            # If a file is provided, copy the file to kb directory
            # otherwise open up the editor and create some content
            artifact_path = str(Path(category_path, title))
            if args["body"]:
                with open(artifact_path, "w+") as art_file:
                    body = args["body"].replace("\\n", "\n")
                    art_file.write(body)
            else:
                shell_cmd = shlex.split(
                    config["EDITOR"]) + [artifact_path]
                call(shell_cmd)

        new_artifact = Artifact(
            id=None, title=title, category=category,
            path="{category}/{title}".format(category=category, title=title),
            tags=args["tags"],
            status=args["status"], author=args["author"], template=args["template"])
        db.insert_artifact(conn, new_artifact)
