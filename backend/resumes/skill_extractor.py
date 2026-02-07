import re
from .skills_db import SKILLS


def extract_skills(text):
    text_lower = text.lower()
    found = set()

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text_lower):
            found.add(skill)

    return sorted(list(found))
