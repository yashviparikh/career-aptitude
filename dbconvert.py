from seeddb import tech_skill_preferences_data
def expand_dataset(dataset1):
    dataset2 = {}
    for category, cat_data in dataset1.items():
        dataset2[category] = {"domains": {}}
        category_skills = cat_data.get("skills", [])
        
        for domain, dom_data in cat_data["domains"].items():
            dataset2[category]["domains"][domain] = {"roles": []}
            
            for role in dom_data["roles"]:
                dataset2[category]["domains"][domain]["roles"].append({
                    "name": role["name"],
                    "skills": category_skills,   # copy all category-level skills to this role
                    "preferences": role.get("preferences", [])
                })
    return dataset2


# Example usage:
tech_skill_preferences_data2 = expand_dataset(tech_skill_preferences_data)
print(tech_skill_preferences_data2)
