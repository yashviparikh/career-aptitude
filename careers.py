CAREERS = {
    "analytical": ["Data Scientist", "Statistician"],
    "creative": ["Graphic Designer", "Copywriter"],
    "technical": ["Software Developer", "Cybersecurity Expert"],
    "marketing": ["SEO Specialist", "Digital Marketer"],
    "leadership": ["Project Manager", "CEO"],
}

RELATED_KEYWORDS = {
    "analytical": ["data-driven", "problem-solving"],
    "creative": ["artistic", "visual"],
    "technical": ["coding", "engineering"],
    "marketing": ["advertising", "branding"],
    "leadership": ["management", "decision-making"],
}

def recommend_careers(keywords):
    recommended=[]
    for keyword in keywords:
        if keyword in CAREERS:
            recommended.extend(CAREERS[keyword])
    return list(set(recommended))[:10]