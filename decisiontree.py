from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import numpy as np
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
def examplebuilding():
    examples=[]
    for category,details in tech_skill_preferences_data.items():
        for skill in details["skills"]:
            for domainname,domain in details["domains"].items():
                for role in domain["roles"]:
                    examples.append({
                    "rolename":role["name"],
                    "category":category,
                    "skill":skill,
                    "teamwork":1 if "teamwork" in role["preferences"] else 0,
                    "alone":1 if "alone" in role["preferences"] else 0,
                    "coding-based":1 if "coding-based" in role["preferences"] else 0,
                    "managerial-based":1 if "managerial-based" in role["preferences"] else 0,
                    "remote":1 if "remote" in role["preferences"] else 0,
                    "in-office":1 if "in-office" in role["preferences"] else 0
                    })
    # for i in examples:
    #     if i["category"]=="Cloud & DevOps":
    #         print(i)
    return examples 
#print(examplebuilding())
#examplebuilding()
def skillencoding():
    skill_id={}
    count=0
    for category,details in tech_skill_preferences_data.items():
        for skill in details["skills"]:
            if skill not in skill_id:
                skill_id[skill]=count
                count+=1
    return skill_id
#skillencoding()
#{'rolename': 'Project Manager', 'category': 'Leadership & Management', 'skill': 'Strategic Planning',
# 'teamwork': 1, 'alone': 0, 'coding-based': 0, 'managerial-based': 1, 'remote': 0, 'in-office': 1}]
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
#print(makingxandy())
makingxandy()

class Node:
    def __init__(self,feature=None,threshold=None,left=None,right=None,value=None):
        self.feature=feature
        self.threshold=threshold
        self.left=left
        self.right=right
        self.value=value

    def ginicalc(self,y):
        count={}
        total=0
        gini=0
        for i in y:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
            total=len(y)
        for j in count:
            gini+=(count[j]/total)**2
        gini=1-gini
        return gini
    
    def splitdata(self,x,y):
        bestgini=10
        bestfeature=None
        if not x:
            return float('inf'),None
        for featureindex in range(len(x[0])):
            xleft,xright,yleft,yright=[],[],[],[]
            for i in range(len(x)):
                if x[i][featureindex]==0:
                    xleft.append(x[i])
                    yleft.append(y[i])
                else:
                    xright.append(x[i])
                    yright.append(y[i])
            if len(xleft)==0 or len(xright)==0:
                continue
            leftgini=self.ginicalc(yleft)
            rightgini=self.ginicalc(yright)
            combinedgini=(len(yleft)/len(y) * leftgini) + (len(yright)/len(y) * rightgini)
            if combinedgini<bestgini:
                bestgini=combinedgini
                bestfeature=featureindex
        return(bestgini,bestfeature)
    
    def buildtree(self,x,y,depth,maxdepth=5):
        l=dict()
        left,right=[],[]
        for i in y:
            if i in l:
                l[i]+=1
            else:
                l[i]=1
        k=set(l.keys())
        if len(k)==1:
            return Node(value=list(k)[0])
        xleft,xright,yleft,yright=[],[],[],[]
        if depth>=maxdepth:
            common=max(l, key=l.get)
            return Node(value=common)
        if depth==0:
            bestgini=float('inf')
            bestskill=None
            bestxleft,bestyleft=[],[]
            bestxright,bestyright=[],[]
            skillfeaturecount=len(x[0])-6
            for featureindex in range(skillfeaturecount):
                xleft,xright,yleft,yright=[],[],[],[]
                for i in range(len(x)):
                    if x[i][featureindex]==1:
                        xleft.append(x[i])
                        yleft.append(y[i])
                    else:
                        xright.append(x[i])
                        yright.append(y[i])
                if len(xleft)==0 or len(xright)==0:
                    continue
                leftgini=self.ginicalc(yleft)
                rightgini=self.ginicalc(yright)
                combinedgini=(len(yleft)/len(y)) * leftgini + (len(yright)/len(y)) * rightgini
                if combinedgini<bestgini:
                    bestgini=combinedgini
                    bestskill=featureindex
                    bestxleft,bestyleft=xleft,yleft
                    bestxright,bestyright=xright,yright
            if bestskill is not None:
                lefttree=self.buildtree(bestxleft,bestyleft,depth+1,maxdepth=5)
                righttree=self.buildtree(bestxright,bestyright,depth+1,maxdepth=5)
                return Node(feature=bestskill,left=lefttree,right=righttree)
            else:
                common=max(l, key=l.get)
                return Node(value=common)
        else:
            if not x:
                common=max(l, key=l.get)
                return Node(value=common)
            gini,feature=self.splitdata(x,y)
            if feature is None:
                common=max(l,key=l.get)
                return Node(value=common)
            for i in range(len(x)):
                if x[i][feature]==0:
                   xleft.append(x[i])
                   yleft.append(y[i])
                else:
                   xright.append(x[i])
                   yright.append(y[i])
            lefttree=self.buildtree(x=xleft,y=yleft,depth=depth+1,maxdepth=5)
            righttree=self.buildtree(x=xright,y=yright,depth=depth+1,maxdepth=5)
            return Node(feature=feature,left=lefttree,right=righttree)
    
def predict(tree, test):
    if tree.value is not None:
        return tree.value
    feature_index = tree.feature
    if test[feature_index] == 0:
        return predict(tree.left, test)
    else:
        return predict(tree.right, test)
n=Node()
x,y=makingxandy()
# tree=n.buildtree(x,y,depth=0)
# skillmap=skillencoding()
# test=[0]*len(skillmap)
# #{'rolename': 'Project Manager', 'category': 'Leadership & Management', 'skill': 'Strategic Planning',
# # 'teamwork': 1, 'alone': 0, 'coding-based': 0, 'managerial-based': 1, 'remote': 0, 'in-office': 1}]
# test[skillmap["Figma"]]=1
# test+=[1,0,1,0,0,1]
# print(predict(tree,test))
#gini,feature=n.splitdata(examplebuilding())
#print("gini",gini)
#print("feature",feature)

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
        top5_idx = np.argsort(probs)[-5:][::-1]   # top-5 indices
        top5_labels = label_encoder.inverse_transform(top5_idx)
        if y_test[i] in top5_labels:
            top5_correct += 1

    top5_acc = top5_correct / len(y_test)
    print("Top-1 Accuracy:", accuracy_score(y_test, model.predict(x_test)))
    print("Top-5 Accuracy:", top5_acc)
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
usinginbuilttree(x,y,label_encoder)