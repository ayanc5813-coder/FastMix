manager = CheckpointManager()

manager.save(
    "test.pkl",
    {
        "a":1
    }
)

obj = manager.load(
    "test.pkl"
)

print(obj)