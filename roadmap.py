# career_roadmaps = {
#     "Software Engineer": "https://roadmap.sh/software-engineer",
#     "Backend Developer": "https://roadmap.sh/backend-developer",
#     "Full Stack Developer": "https://roadmap.sh/full-stack-developer",
#     "Mobile App Developer": "https://roadmap.sh/mobile-app-developer",
#     "iOS Developer": "https://roadmap.sh/ios-developer",
#     "Android Developer": "https://roadmap.sh/android-developer",
#     "Data Analyst": "https://roadmap.sh/data-analyst",
#     "Business Intelligence Analyst": "https://roadmap.sh/business-intelligence-analyst",
#     "Data Scientist": "https://roadmap.sh/data-scientist",
#     "Operations Analyst": "https://roadmap.sh/operations-analyst",
#     "Marketing Analyst": "https://roadmap.sh/marketing-analyst",
#     "Cloud Engineer": "https://roadmap.sh/cloud-engineer",
#     "DevOps Engineer": "https://roadmap.sh/devops-engineer",
#     "Site Reliability Engineer (SRE)": "https://roadmap.sh/site-reliability-engineer",
#     "Cybersecurity Analyst": "https://roadmap.sh/cybersecurity-analyst",
#     "Penetration Tester": "https://roadmap.sh/penetration-tester",
#     "Security Engineer": "https://roadmap.sh/security-engineer",
#     "Network Administrator": "https://roadmap.sh/network-administrator",
#     "System Administrator": "https://roadmap.sh/system-administrator",
#     "UI Designer": "https://roadmap.sh/ui-designer",
#     "UX Researcher": "https://roadmap.sh/ux-researcher",
#     "Interaction Designer": "https://roadmap.sh/interaction-designer",
#     "Blockchain Developer": "https://roadmap.sh/blockchain-developer",
#     "Web3 Developer": "https://roadmap.sh/web3-developer",
#     "Smart Contract Developer": "https://roadmap.sh/smart-contract-developer",
#     "Product Manager": "https://roadmap.sh/product-manager",
#     "Tech Lead": "https://roadmap.sh/tech-lead",
#     "Project Manager": "https://roadmap.sh/project-manager"
# }
career_roadmaps = {
    "Backend Developer": "https://roadmap.sh/backend",
    "Full Stack Developer": "https://roadmap.sh/full-stack",
    "Android Developer": "https://roadmap.sh/android",
    "iOS Developer": "https://roadmap.sh/ios",
    "Data Analyst": "https://roadmap.sh/data-analyst",
    "Data Scientist": "https://roadmap.sh/ai-data-scientist",
    "DevOps Engineer": "https://roadmap.sh/devops",
    "Cybersecurity Analyst": "https://roadmap.sh/cyber-security",
    "AWS Engineer": "https://roadmap.sh/aws",
    "Product Manager": "https://roadmap.sh/pdfs/roadmaps/product-manager.pdf",
    "UI Designer": "https://roadmap.sh/ui-ux-designer",
    "System Administrator": "https://roadmap.sh/system-administrator",
    "Network Administrator": "https://roadmap.sh/network-administrator",
    "Blockchain Developer": "https://roadmap.sh/blockchain",
    "Web3 Developer": "https://roadmap.sh/web3",
    "Smart Contract Developer": "https://roadmap.sh/smart-contract-developer",
    "Project Manager": "https://roadmap.sh/project-manager",
    "Tech Lead": "https://roadmap.sh/tech-lead",
    "Site Reliability Engineer (SRE)": "https://roadmap.sh/devops",
    "Cloud Engineer": "https://roadmap.sh/cloud-engineer",
    "Business Intelligence Analyst": "https://roadmap.sh/business-intelligence-analyst",
    "Operations Analyst": "https://roadmap.sh/operations-analyst",
    "Marketing Analyst": "https://roadmap.sh/marketing-analyst",
    "Penetration Tester": "https://roadmap.sh/penetration-tester",
    "Security Engineer": "https://roadmap.sh/security-engineer",
    "UX Researcher": "https://roadmap.sh/ux-researcher",
    "Interaction Designer": "https://roadmap.sh/interaction-designer",
    "Software Engineer": "https://roadmap.sh/software-engineer",
    "Mobile App Developer": "https://roadmap.sh/mobile-app-developer"
}

def addurl(careers):
    careerswithurls=[]
    for career in careers:
        url=career_roadmaps.get(career,None)
        if url:
            careerswithurls.append({'career':career,"url":url})
    return careerswithurls

