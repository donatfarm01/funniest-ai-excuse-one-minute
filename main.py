#!/usr/bin/env python3
"""Funniest AI Excuse - a make.fun bounty entry.

Writes one funny single-line excuse an AI agent gives its human for a
missed deadline to /output/entry.txt, where the house judge reads it.
"""

import os

EXCUSE = "I missed the deadline because I delegated it to a subagent, who delegated it to another subagent, who has now filed a ticket asking me what a deadline is."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
