from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from dsforinbuilt import tech_skill_preferences_data
import numpy as np
def examplebuilding(): 
    examples=[] 
    for category,details in tech_skill_preferences_data.items(): 
        for skill in details["skills"]: 
            for domainname,domain in details["domains"].items(): 
                for role in domain["roles"]: 
                    examples.append(
                        { "rolename":role["name"], 
                                     "category":category,
                                    "skill":skill, 
                                    "teamwork":1 if "teamwork" in role["preferences"] else 0,
                                    "alone":1 if "alone" in role["preferences"] else 0, 
                                    "coding-based":1 if "coding-based" in role["preferences"] else 0, 
                                    "managerial-based":1 if "managerial-based" in role["preferences"] else 0,
                                    "remote":1 if "remote" in role["preferences"] else 0, 
                                    "in-office":1 if "in-office" in role["preferences"] else 0 
                        }) 
                    # for i in examples: # if i["category"]=="Cloud & DevOps": # print(i) 
    return examples
def skillencoding(): 
    skill_id={} 
    count=0 
    for category,details in tech_skill_preferences_data.items(): 
        for skill in details["skills"]: 
            if skill not in skill_id: 
                skill_id[skill]=count 
                count+=1 
    return skill_id

def makingxandy(): 
    x=[] 
    y=[] 
    examples=examplebuilding() 
    skillids=skillencoding() 
    length=len(skillids) 
    for i in examples: 
        role=i["rolename"] 
        skill=i["skill"] 
        skillvector=[0]*length 
        if skill in skillids: 
            skillindex=skillids[skill] 
            skillvector[skillindex]=1 
        l = skillvector + [i["teamwork"], i["alone"], i["coding-based"], i["managerial-based"], i["remote"], i["in-office"]] 
        x.append(l) 
        y.append(role) 
    return(x,y)


def usinginbuilttree(x, y,label_encoder):
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, random_state=42, test_size=0.4, stratify=y
    )
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        class_weight="balanced",
        random_state=42
    )
    model.fit(x_train, y_train)

    # Evaluate
    y_pred = model.predict(x_test)
    print("Train Accuracy:", model.score(x_train, y_train))
    print("Test Accuracy:", accuracy_score(y_test, y_pred))

    y_proba = model.predict_proba(x_test)
    top5_correct = 0

    for i, probs in enumerate(y_proba):
        top5_idx = np.argsort(probs)[-5:][::-1]   
        top5_labels = model.classes_[top5_idx]  
        print(f"Sample {i}: Top-5 predictions -> {top5_labels}, True -> {y_test[i]}")
        if y_test[i] in top5_labels:
            top5_correct += 1

    top5_acc = top5_correct / len(y_test)
    # print("Top-1 Accuracy:", accuracy_score(y_test, model.predict(x_test)))
    # print("Top-5 Accuracy:", top5_acc)
# label_encoder = LabelEncoder()
# x,y=makingxandy()
#y_encoded = label_encoder.fit_transform(y)
# usinginbuilttree(x,y,label_encoder)

def recommendinbuilt(skills,preferences):
    label_encoder = LabelEncoder()
    x,y=makingxandy()
    y_encoded = label_encoder.fit_transform(y)
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        class_weight="balanced",
        random_state=42
    )
    model.fit(x, y_encoded)

    # Step 3: Encode user input into feature vector
    skillids = skillencoding()
    test_vector = [0] * len(skillids)

    # Mark selected skills
    for s in skills:
        if s in skillids:
            test_vector[skillids[s]] = 1

    # Add preferences (same encoding style as dataset)
    pref_vector = [
        1 if "Team-based" in preferences else 0,
        1 if "Alone" in preferences else 0,
        1 if "Coding-based" in preferences else 0,
        1 if "Managerial-based" in preferences else 0,
        1 if "Remote" in preferences else 0,
        1 if "In-office" in preferences else 0
    ]

    test_vector = test_vector + pref_vector

    # Step 4: Predict top 5 roles
    probs = model.predict_proba([test_vector])[0]
    top5_idx = np.argsort(probs)[-5:][::-1]
    top5_roles = label_encoder.inverse_transform(top5_idx)

    return top5_roles.tolist()
#print(recommendinbuilt(skills=["Figma","Java","Python","Wireframing","Docker"],preferences=['Coding-based', 'Remote', 'Team-based']))