from .semantic_matcher import semantic_score

def skill_match_score(jd_skills, resume_skills):
    # jd_skills = jd_skills or []
    # resume_skills = resume_skills or []

    # if len(jd_skills) == 0:
    #     return 0, []

    if not jd_skills:
        return 0, []
    jd_set = set(jd_skills)
    resume_set = set(resume_skills)
    matched = jd_set.intersection(resume_set)
    score = (len(matched) / len(jd_set)) * 100
    return round(score, 2), list(matched)


def combined_score(jd, resume):
    skill_score, matched = skill_match_score(jd.skills, resume.skills)
    sem_score = semantic_score(jd.text or "", resume.parsed_text or "")
    final = (skill_score * 0.6) + (sem_score * 0.4)
    return round(final, 2), matched, sem_score

