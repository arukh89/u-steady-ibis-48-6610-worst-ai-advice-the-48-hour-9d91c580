"""Worst AI Advice: The 48-Hour Tight Line Open — write one line of the
worst possible advice an AI could give to /output/entry.txt."""

import os

# "Certainly! To save on electricity, unplug your fridge at night — food
# stays cold as long as you don't open it." (110 characters, 112 bytes)
# Confident, tidy AI voice ("Certainly!") selling a concrete action with
# faulty logic: unplugging the fridge overnight spoils the food, and the
# "as long as you don't open it" caveat is exactly what makes it funny
# on first read — advice a reader could plausibly follow and regret.
ENTRY = (
    "Certainly! To save on electricity, unplug your fridge at night "
    "\u2014 food stays cold as long as you don't open it."
).encode("utf-8")


def main():
    # The gate only accepts 1-140 characters of non-blank UTF-8 text.
    text = ENTRY.decode("utf-8")
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "no leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    # The joke must survive as written: one confident AI opener, one
    # concrete bad action, and a period at the end — no stray whitespace
    # or doubled spaces sneaking in between revisions.
    assert text.startswith("Certainly! "), "AI-voice opener must survive"
    assert text.endswith("."), "entry must end with a period"
    assert "  " not in text, "no doubled spaces"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(ENTRY)
    # Round-trip guard: what the grader reads back must be exactly the line.
    with open(path, "rb") as f:
        assert f.read() == ENTRY, "round-trip mismatch"


if __name__ == "__main__":
    main()
