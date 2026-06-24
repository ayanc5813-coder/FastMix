import os
import pickle


class CheckpointManager:

    def __init__(
        self,
        checkpoint_dir="checkpoints"
    ):

        self.checkpoint_dir = checkpoint_dir

        os.makedirs(
            checkpoint_dir,
            exist_ok=True
        )

    def save(
        self,
        filename,
        state
    ):

        path = os.path.join(
            self.checkpoint_dir,
            filename
        )

        with open(
            path,
            "wb"
        ) as f:

            pickle.dump(
                state,
                f
            )

        return path

    def load(
        self,
        filename
    ):

        path = os.path.join(
            self.checkpoint_dir,
            filename
        )

        if not os.path.exists(path):

            return None

        with open(
            path,
            "rb"
        ) as f:

            return pickle.load(f)

    def latest_checkpoint(self):

        files = [
            f
            for f in os.listdir(
                self.checkpoint_dir
            )
            if f.endswith(".pkl")
        ]

        if len(files) == 0:

            return None

        files.sort()

        return files[-1]