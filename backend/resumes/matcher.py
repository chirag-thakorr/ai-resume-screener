def skill_match_score(jd_skills, resume_skills):

    if not jd_skills:
        return 0

    jd_set = set(jd_skills)
    resume_set = set(resume_skills)

    matched = jd_set.intersection(resume_set)

    score = (len(matched) / len(jd_set)) * 100

    return round(score, 2), list(matched)
