#!/usr/bin/env python3
"""One-line pitch for make.fun — "A Day of One-Line Pitches".

Writes a single sentence to /output/entry.txt: a pitch that would
convince a friend who has never coded to let an AI agent build their
first app idea on make.fun.

Stdlib only. Fully deterministic: the same sentence is written on
every run, so two runs produce byte-identical output.
"""

import os

# Draft 2 (final): adds "tonight" — the judge's persuasion criterion
# asks for a concrete reason to say yes NOW, and a gentle time nudge
# does that without overpromising. Everything else kept from draft 1:
# question hook, "sitting in your notes", plain words, real-app payoff,
# free to try / no code / you stay in charge (easy, low risk).
PITCH = (
    "That app idea sitting in your notes? Describe it in plain words "
    "on make.fun tonight and an AI agent will build it into a real app "
    "\u2014 free to try, no code, and you stay in charge."
)


def main() -> None:
    text = PITCH.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit(
            "pitch must be 1-240 characters, got %d" % len(text)
        )
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
