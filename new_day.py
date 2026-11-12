#!/usr/bin/env python3
"""Create a new day folder for the 100 days of code challenge.

Usage:
    python new_day.py 1 "tip calculator"
    python new_day.py 35 "matrix ops" --lang c
    python new_day.py 68 "bank simulator" --lang java
"""

import argparse
import re
import sys
from pathlib import Path

STARTERS = {
    "py": (
        "main.py",
        '"""{title}"""\n\n\ndef main():\n    print("Day {day}: {title}")\n\n\nif __name__ == "__main__":\n    main()\n',
        "python main.py",
    ),
    "c": (
        "main.c",
        '#include <stdio.h>\n\nint main(void) {{\n    printf("Day {day}: {title}\\n");\n    return 0;\n}}\n',
        "gcc main.c -o main && ./main",
    ),
    "cpp": (
        "main.cpp",
        '#include <iostream>\n\nint main() {{\n    std::cout << "Day {day}: {title}" << std::endl;\n    return 0;\n}}\n',
        "g++ main.cpp -o main && ./main",
    ),
    "java": (
        "Main.java",
        'public class Main {{\n    public static void main(String[] args) {{\n        System.out.println("Day {day}: {title}");\n    }}\n}}\n',
        "javac Main.java && java Main",
    ),
}

README_TEMPLATE = """# Day {day:03d}: {title}

## What it does

_One or two sentences._

## How to run

```bash
{run_cmd}
```

## What I learned

- _Fill this in after you finish._

## Screenshot / demo

_Add a screenshot or GIF here if the project is visual._
"""


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a new day folder.")
    parser.add_argument("day", type=int, help="Day number (1-100)")
    parser.add_argument("title", help="Project title, e.g. 'tip calculator'")
    parser.add_argument(
        "--lang", choices=sorted(STARTERS), default="py", help="Starter language (default: py)"
    )
    args = parser.parse_args()

    if not 1 <= args.day <= 100:
        print("Day must be between 1 and 100.", file=sys.stderr)
        return 1

    folder = Path(__file__).parent / f"day-{args.day:03d}-{slugify(args.title)}"
    if folder.exists():
        print(f"{folder.name} already exists.", file=sys.stderr)
        return 1

    filename, code, run_cmd = STARTERS[args.lang]
    title = args.title.strip().capitalize()

    folder.mkdir()
    (folder / filename).write_text(code.format(day=args.day, title=title))
    (folder / "README.md").write_text(
        README_TEMPLATE.format(day=args.day, title=title, run_cmd=run_cmd)
    )

    print(f"Created {folder.name}/")
    print(f'Next: build it, then  git add . && git commit -m "Day {args.day}: {title.lower()}"')
    return 0


if __name__ == "__main__":
    sys.exit(main())
