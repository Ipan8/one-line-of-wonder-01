#!/usr/bin/env python3
"""One Line of Wonder — make.fun entry.
Writes the one-line wonder to /output/entry.txt.
Entry: "The stars are so far away their light left before we were born, and it still found us."
"""
import os

ENTRY = "The stars are so far away their light left before we were born, and it still found us."  # 89 chars, limit 120

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
