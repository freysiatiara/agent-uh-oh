"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

The entry word is "Overthinking": the honest blurt of an agent caught
mid-task, stalled because it cannot decide what to do next.
"""

import os

WORD = "Overthinking"


def output_path() -> str:
    """Resolve the output path without ever relying on the cwd."""
    if "ENTRY_OUTPUT" in os.environ:
        return os.environ["ENTRY_OUTPUT"]
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main() -> None:
    path = output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
