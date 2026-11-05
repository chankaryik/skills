#!/usr/bin/env python3
"""Flag dashes, AI vocabulary and chatbot phrases in a draft.

Usage: lint_draft.py <file>   or   echo "text" | lint_draft.py
Skips fenced code blocks, inline code and URLs. Exit code 1 if any dash is found.
"""
import re
import sys

DASHES = [
    ("em dash", re.compile("—")),
    ("en dash", re.compile("–")),
    ("double hyphen", re.compile(r"(?<!-)--(?!-)")),
    ("spaced hyphen used as dash", re.compile(r"(?<=\w) - (?=\w)")),
]

AI_WORDS = [
    "delve", "crucial", "pivotal", "vital", "robust", "seamless", "seamlessly",
    "leverage", "leveraging", "utilize", "utilizing", "showcase", "testament",
    "tapestry", "landscape", "realm", "streamline", "empower", "elevate", "unlock",
    "foster", "holistic", "comprehensive", "cutting-edge", "game-changer", "synergy",
    "embark", "intricate", "nuanced", "meticulous", "underscore", "underscores",
    "bolster", "paramount", "myriad", "plethora", "furthermore", "moreover",
    "notably", "serves as", "stands as", "boasts", "best-in-class", "world-class",
]

PHRASES = [
    "great question", "i hope this helps", "hope this helps", "let me know if you have any questions",
    "feel free to", "happy to help", "i wanted to reach out", "hope this message finds you",
    "here's the thing", "let's dive in", "dive into", "here's what you need to know",
    "at its core", "the real question is", "when it comes to", "it's worth noting",
    "in today's fast-paced", "this document outlines", "below is a summary",
    "let that sink in", "not just", "paves the way", "a testament to",
]


def strip_code(text):
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    text = re.sub(r"https?://\S+", "", text)
    return text


def main():
    raw = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    lines = strip_code(raw).splitlines()
    dash_hits, word_hits = [], []
    for n, line in enumerate(lines, 1):
        low = line.lower()
        for label, rx in DASHES:
            if rx.search(line):
                dash_hits.append(f"  L{n} {label}: {line.strip()[:100]}")
        for w in AI_WORDS:
            if re.search(rf"\b{re.escape(w)}\b", low):
                word_hits.append(f"  L{n} '{w}': {line.strip()[:100]}")
        for p in PHRASES:
            if p in low:
                word_hits.append(f"  L{n} '{p}': {line.strip()[:100]}")

    if dash_hits:
        print("DASHES (must fix):")
        print("\n".join(dash_hits))
    if word_hits:
        print("AI tells (fix unless there's a reason to keep):")
        print("\n".join(word_hits))
    if not dash_hits and not word_hits:
        print("clean")
    sys.exit(1 if dash_hits else 0)


if __name__ == "__main__":
    main()
