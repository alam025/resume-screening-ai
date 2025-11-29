import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import re
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("🎯 Resume Screening AI - Starting...")
print()

# Sample resume dataset
resumes_data = {
    'Resume_Text': [
        "Experienced Data Scientist with 5 years in machine learning, Python, TensorFlow, PyTorch, deep learning, NLP, computer vision, and statistical analysis",
        "Machine Learning Engineer skilled in Python, scikit-learn, pandas, NumPy, Keras, data analysis, predictive modeling, and big data technologies",
        "AI Researcher with expertise in neural networks, deep learning, Python, R, data mining, statistical modeling, and algorithm development",
        "Data Analyst with strong skills in Python, SQL, Excel, Tableau, Power BI, data visualization, and business intelligence",
        "ML Engineer specializing in computer vision, image processing, OpenCV, TensorFlow, Python, and deep neural networks",
        
        "Full Stack Developer proficient in JavaScript, React, Node.js, Express, MongoDB, HTML, CSS, REST APIs, and responsive web design",
        "Frontend Developer with expertise in React, Vue.js, Angular, JavaScript, TypeScript, HTML5, CSS3, SASS, and UI/UX design",
        "Backend Developer skilled in Node.js, Python Django, Flask, PostgreSQL, MySQL, REST APIs, microservices, and cloud deployment",
        "Web Developer experienced in HTML, CSS, JavaScript, jQuery, Bootstrap, WordPress, PHP, and MySQL database management",
        "MERN Stack Developer with strong knowledge of MongoDB, Express.js, React, Node.js, Redux, and modern web technologies",
        
        "DevOps Engineer with expertise in Docker, Kubernetes, Jenkins, CI/CD, AWS, Azure, Linux, bash scripting, and automation",
        "Cloud Engineer proficient in AWS, Azure, GCP, Terraform, CloudFormation, serverless architecture, and infrastructure as code",
        "Site Reliability Engineer with skills in Kubernetes, Docker, monitoring tools, Prometheus, Grafana, and incident management",
        "DevOps Specialist experienced in Jenkins, GitLab CI, CircleCI, Ansible, Chef, Puppet, and configuration management",
        
        "Android Developer with 4 years experience in Kotlin, Java, Android SDK, Room, Retrofit, MVVM, and material design",
        "iOS Developer skilled in Swift, SwiftUI, UIKit, Xcode, Core Data, RESTful APIs, and App Store deployment",
        "React Native Developer proficient in JavaScript, React Native, Redux, mobile app development for iOS and Android",
        "Flutter Developer with expertise in Dart, Flutter framework, Firebase, state management, and cross-platform development",
        
        "Senior Data Scientist with PhD in Statistics, expert in Python, R, machine learning algorithms, A/B testing, and causal inference",
        "Full Stack JavaScript Developer proficient in MEAN stack, GraphQL, TypeScript, testing frameworks, and agile methodologies"
    ],
    'Category': [
        'Data Science', 'Data Science', 'Data Science', 'Data Science', 'Data Science',
        'Web Development', 'Web Development', 'Web Development', 'Web Development', 'Web Development',
        'DevOps', 'DevOps', 'DevOps', 'DevOps',
        'Mobile Development', 'Mobile Development', 'Mobile Development', 'Mobile Development',
        'Data Science', 'Web Development'
    ]
}

df = pd.DataFrame(resumes_data)
print(f"✓ Loaded {len(df)} resumes")
print(f"✓ Categories: {df['Category'].nunique()}")
print()

# Check distribution
print("Resume distribution by category:")
print(df['Category'].value_counts())
print()

# Visualize distribution
category_counts = df['Category'].value_counts()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
category_counts.plot(kind='bar', color=colors, ax=ax1)
ax1.set_title('Resume Distribution by Category', fontsize=14, fontweight='bold')
ax1.set_xlabel('Job Category', fontsize=12)
ax1.set_ylabel('Number of Resumes', fontsize=12)
ax1.tick_params(axis='x', rotation=45)
ax1.grid(axis='y', alpha=0.3)

ax2.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', 
        colors=colors, startangle=90)
ax2.set_title('Category Distribution', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/resume_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Saved: resume_distribution.png")
print()

# Text preprocessing
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df['cleaned'] = df['Resume_Text'].apply(clean_text)
print("✓ Text preprocessing done")
print()

# Feature extraction
tfidf = TfidfVectorizer(max_features=100, stop_words='english')
X = tfidf.fit_transform(df['cleaned'])
y = df['Category']

print(f"✓ Features extracted: {X.shape}")
print()

# Top keywords per category
feature_names = tfidf.get_feature_names_out()
keywords_by_category = {}

for cat in df['Category'].unique():
    idx = df[df['Category'] == cat].index
    cat_tfidf = X[idx].toarray().mean(axis=0)
    top_idx = cat_tfidf.argsort()[-5:][::-1]
    keywords_by_category[cat] = [feature_names[i] for i in top_idx]

print("Top keywords per category:")
for cat, words in keywords_by_category.items():
    print(f"  {cat}: {', '.join(words)}")
print()

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print(f"✓ Train set: {X_train.shape[0]} samples")
print(f"✓ Test set: {X_test.shape[0]} samples")
print()

# Train models
print("Training models...")

nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)
nb_pred = nb_model.predict(X_test)
nb_acc = accuracy_score(y_test, nb_pred)
print(f"  Naive Bayes: {nb_acc*100:.1f}%")

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)
print(f"  Random Forest: {rf_acc*100:.1f}%")
print()

# Select best model
if rf_acc > nb_acc:
    best_model = rf_model
    best_pred = rf_pred
    best_name = "Random Forest"
    best_acc = rf_acc
else:
    best_model = nb_model
    best_pred = nb_pred
    best_name = "Naive Bayes"
    best_acc = nb_acc

print(f"Best model: {best_name} ({best_acc*100:.1f}%)")
print()
print("Classification Report:")
print(classification_report(y_test, best_pred))
print()

# Confusion matrix

cm = confusion_matrix(y_test, best_pred)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=sorted(df['Category'].unique()),
            yticklabels=sorted(df['Category'].unique()))
plt.title(f'Confusion Matrix - {best_name}', fontsize=16, fontweight='bold')
plt.xlabel('Predicted', fontsize=12)
plt.ylabel('Actual', fontsize=12)
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/confusion_matrix.png', dpi=300, bbox_inches='tight')
print("✓ Saved: confusion_matrix.png")
print()

# Model comparison

models = ['Naive Bayes', 'Random Forest']
scores = [nb_acc * 100, rf_acc * 100]

plt.figure(figsize=(10, 6))
bars = plt.bar(models, scores, color=['#FF6B6B', '#4ECDC4'], width=0.6)
plt.title('Model Accuracy Comparison', fontsize=16, fontweight='bold')
plt.xlabel('Model', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)
plt.ylim(0, 105)
plt.grid(axis='y', alpha=0.3)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.1f}%', ha='center', va='bottom', 
            fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/model_comparison.png', dpi=300, bbox_inches='tight')
print("✓ Saved: model_comparison.png")
print()

# Feature importance (if Random Forest wins)
if isinstance(best_model, RandomForestClassifier):
    importances = rf_model.feature_importances_
    indices = np.argsort(importances)[-15:][::-1]
    
    plt.figure(figsize=(12, 6))
    plt.barh(range(len(indices)), importances[indices], color='#45B7D1')
    plt.yticks(range(len(indices)), [feature_names[i] for i in indices])
    plt.xlabel('Importance', fontsize=12)
    plt.title('Top 15 Keywords for Resume Screening', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('/mnt/user-data/outputs/feature_importance.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: feature_importance.png")
    print()

# Test with new resume
test_resume = """
Senior Software Engineer with 6 years of experience in Python programming,
machine learning, deep learning, TensorFlow, scikit-learn, data analysis,
and building scalable AI solutions. Proficient in SQL, MongoDB, and cloud platforms.
"""

print("Testing with new resume...")
print()
cleaned_test = clean_text(test_resume)
test_vec = tfidf.transform([cleaned_test])
prediction = best_model.predict(test_vec)[0]
probs = best_model.predict_proba(test_vec)[0]

print(f"Predicted category: {prediction}")
print()
print("Confidence scores:")
for cat, prob in zip(best_model.classes_, probs):
    print(f"  {cat}: {prob*100:.1f}%")
print()

print("=" * 60)
print("✓ Resume Screening AI - Complete!")
print(f"  Total resumes: {len(df)}")
print(f"  Model: {best_name}")
print(f"  Accuracy: {best_acc*100:.1f}%")
print(f"  Visualizations: 3-4 charts saved")
print("=" * 60)