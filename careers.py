CAREERS = {
    "data-driven": ["Data Scientist", "Business Analyst"],
    "problem-solving": ["Consultant", "Risk Analyst"],
    "artistic": ["Graphic Designer", "Illustrator"],
    "visual": ["UI/UX Designer", "Videographer"],
    "coding": ["Software Developer", "Game Developer"],
    "engineering": ["Mechanical Engineer", "Electrical Engineer"],
    "advertising": ["Marketing Manager", "Copywriter"],
    "branding": ["SEO Specialist", "Digital Marketer"],
    "management": ["Project Manager", "Operations Manager"],
    "decision-making": ["CEO", "Entrepreneur"],
}

MAIN_KEYWORDS = {
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