import json
import datetime


class ExperimentTracker:

    def __init__(self):

        self.metadata = {

            "created":
                str(
                    datetime.datetime.now()
                )
        }

    def update(
        self,
        key,
        value
    ):

        self.metadata[key] = value

    def save(
        self,
        filename
    ):

        with open(
            filename,
            "w"
        ) as f:

            json.dump(
                self.metadata,
                f,
                indent=2
            )