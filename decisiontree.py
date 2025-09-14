# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import LabelEncoder
import numpy as np
from collections import Counter
from dataset import tech_skill_preferences_data
def examplebuilding():
    examples = []
    for category, details in tech_skill_preferences_data.items():
        for domainname, domain in details["domains"].items():
            for role in domain["roles"]:
                examples.append({
                    "rolename": role["name"],
                    "skills": role["skills"],  # now role-specific
                    "teamwork": 1 if "teamwork" in role["preferences"] else 0,
                    "alone": 1 if "alone" in role["preferences"] else 0,
                    "coding-based": 1 if "coding-based" in role["preferences"] else 0,
                    "managerial-based": 1 if "managerial-based" in role["preferences"] else 0,
                    "remote": 1 if "remote" in role["preferences"] else 0,
                    "in-office": 1 if "in-office" in role["preferences"] else 0
                })
    return examples


#print(examplebuilding())
#examplebuilding()
def skillencoding():
    skill_id = {}
    count = 0
    for category, details in tech_skill_preferences_data.items():
        for domainname, domain in details["domains"].items():
            for role in domain["roles"]:
                for skill in role["skills"]:
                    if skill not in skill_id:
                        skill_id[skill] = count
                        count += 1
    return skill_id

#skillencoding()
#{'rolename': 'Project Manager', 'category': 'Leadership & Management', 'skill': 'Strategic Planning',
# 'teamwork': 1, 'alone': 0, 'coding-based': 0, 'managerial-based': 1, 'remote': 0, 'in-office': 1}]
def makingxandy():
    x = []
    y = []
    examples = examplebuilding()
    skillids = skillencoding()
    length = len(skillids)

    for i in examples:
        skillvector = [0]*length
        for skill in i["skills"]:   # multiple skills now
            if skill in skillids:
                skillindex = skillids[skill]
                skillvector[skillindex] = 1

        l = skillvector + [i["teamwork"], i["alone"], i["coding-based"],
                           i["managerial-based"], i["remote"], i["in-office"]]
        x.append(l)
        y.append(i["rolename"])
    
    x = np.array(x, dtype=int)
    y = np.array(y)
    return (x, y,length)

#print(makingxandy())
# makingxandy()

class Node:
    def __init__(self, feature=None, left=None, right=None, value=None,ispref=False):
        self.feature = feature
        self.left = left
        self.right = right
        self.value = value
        self.ispref = ispref

    def ginicalc(self, y):
        if len(y) == 0:
            return 0
        _, counts = np.unique(y, return_counts=True)
        probs = counts / counts.sum()
        return 1 - np.sum(probs**2)

    def splitdata(self, X, y,feature_range=None):
        best_gini = float('inf')
        best_feature = None
        X=np.array(X)
        y=np.array(y)
        if X.ndim == 1:      # Make 1D -> 2D
            X = X.reshape(-1, 1)

        assert X.shape[0] == y.shape[0], f"Mismatch X:{X.shape} y:{y.shape}"
        if feature_range is None:
            feature_range=range(X.shape[1])
        for feature in feature_range:
            mask = X[:, feature] == 1
            assert len(mask) == len(y), f"mask length {len(mask)} != y length {len(y)}"
            y_left, y_right = y[~mask], y[mask]
            if len(y_left) == 0 or len(y_right) == 0:
                continue

            gini_left = self.ginicalc(y_left)
            gini_right = self.ginicalc(y_right)
            combined_gini = (len(y_left)/len(y))*gini_left + (len(y_right)/len(y))*gini_right

            if combined_gini < best_gini:
                best_gini = combined_gini
                best_feature = feature

        return best_feature

    def buildtree(self, X, y, depth=0, maxdepth=5):
        X = np.array(X)
        y = np.array(y)
        if len(y) == 0:
            return Node(value=None)
        unique_labels, counts = np.unique(y, return_counts=True)
        if len(unique_labels) == 1 or depth >= maxdepth:
            return Node(value=Counter(y))
        
        
        feature_range = range(length)  
        best_feature = self.splitdata(X,y,feature_range=feature_range)
        
        if best_feature is None:
            return Node(value=Counter(y))

        mask = X[:, best_feature] == 1
        left_tree = self.buildtree(X[~mask], y[~mask], depth + 1, maxdepth)
        right_tree = self.buildtree(X[mask], y[mask], depth + 1, maxdepth)

        return Node(feature=best_feature, left=left_tree, right=right_tree)


    def preftree(self,X,y,length,depth=0,maxdepth=3):
        if len(y) == 0:
                return Node(value=None,ispref=True)
        
        unique_labels,counts=np.unique(y,return_counts=True)
        if len(unique_labels)==1 or depth>=maxdepth:
            return Node(value=unique_labels[np.argmax(counts)],ispref=True)
        
        feature_range=range(length,X.shape[1])
        best_feature=self.splitdata(X,y,feature_range)
        if best_feature is None:
                return Node(value=unique_labels[np.argmax(counts)], ispref=True)

        
        mask = X[:, best_feature] == 1
        left_tree = self.preftree(X[~mask], y[~mask], length, depth+1, maxdepth)
        right_tree =self.preftree(X[mask], y[mask], length, depth+1, maxdepth)

        return Node(feature=best_feature, left=left_tree, right=right_tree, ispref=True)


def refineleaves(tree,x,y,length,maxdepth=3):
    if isinstance(tree.value, Counter):
        if len(tree.value) > 1:
            pref_tree = Node().preftree(x, y, length, depth=0, maxdepth=maxdepth)
            return pref_tree
        else:
            return tree
    if tree.left:
        tree.left = refineleaves(tree.left, x, y, length, maxdepth)
    if tree.right:
        tree.right = refineleaves(tree.right, x, y, length, maxdepth)

    return tree  


def predict(tree, test,k=5):
        def traverse(node):
            if node.value is not None:
                if isinstance(node.value,Counter):
                    return node.value
                else:
                    return Counter({node.value:1})
            leftvotes=traverse(node.left) if node.left else Counter()
            rightvotes=traverse(node.right) if node.right else Counter()

            if test[node.feature]==0:
                return leftvotes+rightvotes
            else:
                return rightvotes+leftvotes
        votes=traverse(tree)
        return votes.most_common(k)
def predicttop5(tree, test, skillmap, examples, k=5):
    def traverse(node):
        if isinstance(node.value, Counter):
            return node.value
        if test[node.feature] == 0:
            return traverse(node.left)
        else:
            return traverse(node.right)
    
    votes = traverse(tree) if traverse(tree) else Counter()

    role_scores = {}
    pref_keys = ["teamwork", "alone", "coding-based", "managerial-based", "remote", "in-office"]
    
    for role in examples:
        rolename = role["rolename"]
        skill_count = sum(test[skillmap[s]] for s in role["skills"] if s in skillmap)
        pref_count = sum(1 for i, p in enumerate(pref_keys) if role[p] == test[len(skillmap)+i] == 1)
        tree_vote = votes.get(rolename, 0)
        total_score = skill_count*0.5 + pref_count*0.3 + tree_vote*0.2
        role_scores[rolename] = total_score
    top_roles = sorted(role_scores.items(), key=lambda x: x[1], reverse=True)
    return top_roles[:k]


n = Node()
x, y,length = makingxandy()
skilltree = n.buildtree(x, y, depth=0, maxdepth=5)
skillmap = skillencoding()
test = [0]*len(skillmap)
for s in ["Network Security","AWS","Figma","Python","Java","Docker","Penetration Testing","Kubernetes"]:
    test[skillmap[s]] = 1
test += [0,1,1,0,1,1]
finaltree=refineleaves(skilltree,x,y,length)
#print("Predicted Role:", predict(finaltree, test,k=10))
examples = examplebuilding()
top5 = predicttop5(finaltree, test, skillmap, examples, k=10)
print("Top-5 Predicted Roles:", top5)


