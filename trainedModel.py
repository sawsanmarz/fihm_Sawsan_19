
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import argparse
import pickle

ap = argparse.ArgumentParser()
ap.add_argument("-e", "--embeddings", required=True,
	help="/Users/sawsan/Desktop/project/embeddings.pickle")
ap.add_argument("-r", "--recognizer", required=True,
	help="/Users/sawsan/Desktop/project/recognizer.pickle")
ap.add_argument("-l", "--le", required=True,
	help="/Users/sawsan/Desktop/labels.pickle")
args = vars(ap.parse_args())

print("[INFO] loading face embeddings...")
data = pickle.loads(open(args["embeddings"], "rb").read())

print("[INFO] encoding labels...")
le = LabelEncoder()
labels = le.fit_transform(data["names"])

print("[INFO] training model...")
recognizer = SVC(C=1.0, kernel="linear", probability=True)
recognizer.fit(data["embeddings"], labels)

f = open(args["recognizer"], "wb")
f.write(pickle.dumps(recognizer))
f.close()

f = open(args["le"], "wb")
f.write(pickle.dumps(le))
f.close()