from db import tech_skills_collection
from pymongo.errors import BulkWriteError
tech_skill_preferences_data = {
    "Programming": {
        "skills": ["Python", "JavaScript", "Java", "C++", "Ruby", "Go", "Rust", "C#", "Perl", "Kotlin", "Swift"],
        "domains": {
            "Software Development": {
                "roles": [
                    {"name": "Software Engineer", "preferences": ["teamwork", "coding-based", "remote"]},
                    {"name": "Backend Developer", "preferences": ["alone", "coding-based", "remote"]},
                    {"name": "Full Stack Developer", "preferences": ["teamwork", "coding-based", "remote or in-office"]},
                ],
            },
            "Mobile Development": {
                "roles": [
                    {"name": "Mobile App Developer", "preferences": ["teamwork", "coding-based", "remote or in-office"]},
                    {"name": "iOS Developer", "preferences": ["teamwork", "coding-based", "remote or in-office"]},
                    {"name": "Android Developer", "preferences": ["alone", "coding-based", "remote or in-office"]},
                ],
            },
        },
    },
    "Data Analysis & Visualization": {
        "skills": [
            "Excel", "Tableau", "Power BI", "SQL", "Python (Pandas/NumPy)", "R", "Matplotlib", "Seaborn",
            "Data Wrangling", "Data Cleaning", "ETL"
        ],
        "domains": {
            "Data Science & AI": {
                "roles": [
                    {"name": "Data Analyst", "preferences": ["alone", "coding-based", "remote or in-office"]},
                    {"name": "Business Intelligence Analyst", "preferences": ["teamwork", "managerial-based", "in-office"]},
                    {"name": "Data Scientist", "preferences": ["alone", "coding-based", "remote"]},
                ],
            },
            "Business Analytics": {
                "roles": [
                    {"name": "Operations Analyst", "preferences": ["teamwork", "managerial-based", "in-office"]},
                    {"name": "Marketing Analyst", "preferences": ["teamwork", "coding-based", "remote or in-office"]},
                ],
            },
        },
    },
    "Cloud & DevOps": {
        "skills": [
            "AWS", "Azure", "Google Cloud", "Kubernetes", "Docker", "Terraform", "CI/CD", "Ansible", "Jenkins",
            "Linux Administration", "Cloud Security", "Serverless Architecture"
        ],
        "domains": {
            "Cloud Computing & DevOps": {
                "roles": [
                    {"name": "Cloud Engineer", "preferences": ["teamwork", "coding-based", "remote"]},
                    {"name": "DevOps Engineer", "preferences": ["alone", "coding-based", "remote or in-office"]},
                    {"name": "Site Reliability Engineer (SRE)", "preferences": ["teamwork", "coding-based", "remote"]},
                ],
            },
        },
    },
    "Networking & Security": {
        "skills": [
            "Network Security", "Routing", "Firewall Configuration", "VPN Setup", "Cryptography", "Penetration Testing",
            "Incident Response", "Disaster Recovery", "Cyber Threat Intelligence", "Wireless Networking"
        ],
        "domains": {
            "Cybersecurity": {
                "roles": [
                    {"name": "Cybersecurity Analyst", "preferences": ["teamwork", "coding-based", "remote"]},
                    {"name": "Penetration Tester", "preferences": ["alone", "coding-based", "remote or in-office"]},
                    {"name": "Security Engineer", "preferences": ["teamwork", "coding-based", "in-office"]},
                ],
            },
            "Networking & IT Support": {
                "roles": [
                    {"name": "Network Administrator", "preferences": ["teamwork", "coding-based", "in-office"]},
                    {"name": "System Administrator", "preferences": ["alone", "coding-based", "in-office"]},
                ],
            },
        },
    },
    "UI/UX & Design": {
        "skills": [
            "UI/UX Design", "Figma", "Sketch", "Adobe XD", "Wireframing", "User Research", "Prototyping", "Interaction Design",
            "User Testing", "Motion Design"
        ],
        "domains": {
            "UI/UX Design": {
                "roles": [
                    {"name": "UI Designer", "preferences": ["teamwork", "coding-based", "remote"]},
                    {"name": "UX Researcher", "preferences": ["teamwork", "coding-based", "remote"]},
                    {"name": "Interaction Designer", "preferences": ["alone", "coding-based", "in-office"]},
                ],
            },
        },
    },
    "Blockchain & Web3": {
        "skills": [
            "Blockchain", "Smart Contracts", "Ethereum", "Solidity", "Web3", "Hyperledger", "DApps", "DeFi", "NFTs",
            "Consensus Algorithms"
        ],
        "domains": {
            "Blockchain & Web3": {
                "roles": [
                    {"name": "Blockchain Developer", "preferences": ["teamwork", "coding-based", "remote"]},
                    {"name": "Web3 Developer", "preferences": ["teamwork", "coding-based", "remote or in-office"]},
                    {"name": "Smart Contract Developer", "preferences": ["alone", "coding-based", "remote"]},
                ],
            },
        },
    },
    "Leadership & Management": {
        "skills": [
            "Agile", "Scrum", "Project Management", "Tech Leadership", "Product Management", "Risk Management", 
            "Team Building", "Communication", "Strategic Planning"
        ],
        "domains": {
            "Tech Management & Leadership": {
                "roles": [
                    {"name": "Product Manager", "preferences": ["teamwork", "managerial-based", "in-office"]},
                    {"name": "Tech Lead", "preferences": ["teamwork", "managerial-based", "remote or in-office"]},
                    {"name": "Project Manager", "preferences": ["teamwork", "managerial-based", "in-office"]},
                ],
            },
        },
    },
}


documents=[]
for category,details in tech_skill_preferences_data.items():
    documents.append(
        {
            "category":category,
            "skills":details["skills"],
            "domains":[
                { "name": domain_name,"roles":domain["roles"]}
                for domain_name,domain in details["domains"].items()
            ]
        }
    )
    # tech_skills_collection.insert_many(documents)
    # print("done")


# Clear old data (optional for reseeding)
try:
    tech_skills_collection.delete_many({})
    print("🗑️ Old data cleared.")
except Exception as e:
    print("⚠️ Error while clearing old data:", e)

# Insert new data
try:
    tech_skills_collection.insert_many(documents)
    print("✅ Data seeded successfully.")
except BulkWriteError as bwe:
    print("❌ Duplicate key error or bulk write error:")
    for err in bwe.details['writeErrors']:
        print(f"→ Index: {err['index']} | Message: {err['errmsg']}")
except Exception as e:
    print("❌ General error during insert:", e)
