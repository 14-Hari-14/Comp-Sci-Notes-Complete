# 0_Core_Cs_Notes Index Guide

Quick reference guide to navigate through Core Computer Science Notes organized by topic and tags.

---

## 📂 Folder Structure Overview

```
0_Core_Cs_Notes/
├── AI-ML/                          (Machine Learning & AI concepts)
│   ├── Algorithms/                 (ML algorithms)
│   ├── Data Analysis/              (EDA and data processing)
│   └── Loss_Functions/             (Loss metrics and calculations)
├── CN_Cybersecurity/               (Cybersecurity & Encryption)
│   └── Encryption/                 (Cryptographic techniques)
└── College_Notes/                  (Course-related materials)
    ├── CST 401 AI/                 (AI course modules)
    └── CST 463 WEBP/               (Web Programming course modules)
```

---

## 🏷️ TAG SYSTEM & IMPROVEMENTS

### Existing Tag Categories
- **#ai** - Artificial Intelligence concepts
- **#ml** - Machine Learning general
- **#supervised_ml** - Supervised Learning
- **#loss_functions** - Loss metrics
- **#encryption** - Encryption techniques
- **#cybersecurity_basics** - Cybersecurity fundamentals

### **Suggested Tag Additions** ✨
- `#algorithm` - For specific ML algorithms
- `#optimization` - For optimization techniques (gradient descent, etc.)
- `#linear_algebra` - For mathematical foundations
- `#classification` - For classification algorithms
- `#regression` - For regression algorithms
- `#asymmetric_encryption` - For RSA and asymmetric methods
- `#practical_tools` - For tools like Wireshark, EDA tools

---

## 📚 QUICK NAVIGATION BY CATEGORY

### 🤖 **AI-ML Core Concepts**

#### Foundation
| File                                                     | Tags                                    | Purpose                                                    |
| -------------------------------------------------------- | --------------------------------------- | ---------------------------------------------------------- |
| [AI-ML Basics.md](AI-ML/AI-ML%20Basics.md)               | #ai #ml                                 | Overview of machine learning types and training data split |
| [Supervised Learning.md](AI-ML/Supervised%20Learning.md) | #supervised_ml                          | Supervised learning fundamentals                           |
| [Gradient Descent.md](AI-ML/Gradient%20Descent.md)       | #gradient_descent #optimization #ai #ml | Optimization algorithm and variants                        |
| [regularisation.md](AI-ML/regularisation.md)             | #ml #optimization                       | Regularization techniques                                  |


#### 🧮 **Algorithms Subfolder**
| File                                                                                            | Tags                                       | Purpose                                |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------ | -------------------------------------- |
| [Linear Regression.md](AI-ML/Algorithms/Linear%20Regression.md)                                 | #regression #supervised_ml #linear_algebra | Linear regression model                |
| [Logistic Regression.md](AI-ML/Algorithms/Logistic%20Regression.md)                             | #classification #supervised_ml             | Logistic regression for classification |
| [Decision Trees + Random Forest.md](AI-ML/Algorithms/Decision%20Trees%20+%20Random%20Forest.md) | #algorithm #classification #regression     | Tree-based ensemble methods            |
| [Support Vector Machines (SVM).md](AI-ML/Algorithms/Support%20Vector%20Machines%20(SVM).md)     | #algorithm #classification                 | SVM classification algorithm           |
| [KNN.md](AI-ML/Algorithms/KNN.md)                                                                                | #algorithm                                 | K-Nearest Neighbors algorithm          |
| [Naive Bayes.md](AI-ML/Algorithms/Naive%20Bayes.md)                                                              | #algorithm #classification                 | Naive Bayes classifier                 |


#### 📊 **Loss Functions Subfolder**
| File                                                                  | Tags                                | Purpose                              |
| --------------------------------------------------------------------- | ----------------------------------- | ------------------------------------ |
| [Loss functions.md](AI-ML/Loss_Functions/Loss%20functions.md)         | #loss_functions #ai #ml             | Index of loss functions by algorithm |
| [MSE.md](AI-ML/Loss_Functions/MSE.md)                                 | #loss_functions #regression         | Mean Squared Error                   |
| [MAE.md](AI-ML/Loss_Functions/MAE.md)                                 | #loss_functions #regression         | Mean Absolute Error                  |
| [Log Loss.md](AI-ML/Loss_Functions/Log%20Loss.md)                     | #loss_functions #classification     | Logarithmic loss for classification  |
| [Entropy.md](AI-ML/Loss_Functions/Entropy.md)                         | #loss_functions #information_theory | Information entropy concept          |
| [Gini Impurity.md](AI-ML/Loss_Functions/Gini%20Impurity.md)           | #loss_functions #decision_trees     | Gini impurity metric                 |
| [Hinge Loss.md](AI-ML/Loss_Functions/Hinge%20Loss.md)                 | #loss_functions #svm                | Hinge loss for SVM                   |
| [Minkowski distance.md](AI-ML/Loss_Functions/Minkowski%20distance.md) | #distance_metric                    | Distance calculation metric          |


#### 📈 **Data Analysis Subfolder**
| File | Tags | Purpose |
|------|------|---------|
| [EDA_Notes.md](AI-ML/Data%20Analysis/EDA_Notes.md) | #eda #data_analysis | Exploratory Data Analysis |


---

### 🔐 **Cybersecurity & Encryption**

#### Foundation
| File                                                                                | Tags                        | Purpose                             |
| ----------------------------------------------------------------------------------- | --------------------------- | ----------------------------------- |
| [Cybersecurity Basics.md](CN_Cybersecurity/Cybersecurity%20Basics.md)               | #cybersecurity_basics       | CIA Triad and security fundamentals |
| [Access Control List (ACL).md](CN_Cybersecurity/Access%20Control%20List%20(ACL).md) | #security #access_control   | Access control mechanisms           |
| [Packet Sniffing.md](CN_Cybersecurity/Packet%20Sniffing.md)                         | #attack #network_security   | Packet sniffing attack              |
| [[CN_Cybersecurity/Threats/DOS(Denial of service) & DDOS (Distributed DOS)|DOS(Denial of service) & DDOS (Distributed DOS)]]                                 | #attack #dos_ddos           | DoS and DDoS attacks                |
| [Phishing.md](CN_Cybersecurity/Threats/Phishing.md)                                                          | #attack #social_engineering | Phishing attack vectors             |
| [Botnet.md](CN_Cybersecurity/Threats/Botnet.md)                                                              | #attack #malware            | Botnet attacks                      |
| [DNS Tunneling.md](CN_Cybersecurity/Threats/DNS%20Tunneling.md)                                              | #attack #dns                | DNS tunneling attacks               |
| [Wireshark.md](CN_Cybersecurity/Wireshark.md)                                       | #tool #network_analysis     | Wireshark network analyzer tool     |

#### 🔑 **Encryption Subfolder**
| File | Tags | Purpose |
|------|------|---------|
| [AES.md](CN_Cybersecurity/Encryption/AES.md) | #symmetric_encryption #aes #encryption | AES symmetric encryption |
| [RSA-2048.md](CN_Cybersecurity/Encryption/RSA-2048.md) | #asymmetric_encryption #rsa #encryption | RSA asymmetric encryption |

---

### 🎓 **College Notes**

#### General Resources
| File | Tags | Purpose |
|------|------|---------|
| [BT Question Bank.md](College_Notes/BT%20Question%20Bank.md) | #exam #question_bank | Question bank for exam prep |
| [Solutions to question bank.md](College_Notes/Solutions%20to%20question%20bank.md) | #exam #solutions | Solutions to questions |
| [DISTRIBUTED_COMPUTING_SERIES_ANSWERS.md](College_Notes/DISTRIBUTED_COMPUTING_SERIES_ANSWERS.md) | #distributed_systems #exam | Distributed computing answers |
| [DISTRIBUTED_COMPUTING_SERIES_2_ANSWER.MD](College_Notes/DISTRIBUTED_COMPUTING_SERIES_2_ANSWER.MD) | #distributed_systems #exam | Distributed computing series 2 |
| [GFS_AFS.md](College_Notes/GFS_AFS.md) | #distributed_systems #file_systems | Google File System & AFS |
| [Module 1 ISE.canvas](College_Notes/Module%201%20ISE.canvas) | #exam #canvas | ISE module canvas |

#### 🤖 **CST 401 AI Course**
| File | Tags | Purpose |
|------|------|---------|
| [Module 1 AI.md](College_Notes/CST%20401%20AI/Module%201%20AI.md) | #course #ai #module_1 | AI course module 1 |
| [Module 2 AI.md](College_Notes/CST%20401%20AI/Module%202%20AI.md) | #course #ai #module_2 | AI course module 2 |

#### 🌐 **CST 463 Web Programming Course**
| File | Tags | Purpose |
|------|------|---------|
| [Module 1 WebP.md](College_Notes/CST%20463%20WEBP/Module%201%20WebP.md) | #course #web_programming #module_1 | Web programming module 1 |


---

## 🔍 **Search Tips**

### Find notes by topic:
- **All ML algorithms:** Search files tagged with `#algorithm` or browse `AI-ML/Algorithms/`
- **Loss functions:** Check `AI-ML/Loss_Functions/` or use `#loss_functions` tag
- **Security concepts:** Browse `CN_Cybersecurity/` or search `#cybersecurity_basics`
- **Encryption methods:** Use `#encryption`, `#symmetric_encryption`, or `#asymmetric_encryption`
- **Course materials:** Search `#course` tag
- **Exam prep:** Use `#exam` or `#question_bank` tags

---

## 📝 **File Status & Notes**

- **tasks_to_be_completed.md** - Contains pending items to review
- **Module 1 ISE.canvas** - Canvas visualization file (Excalidraw format)
- All files include Date, Topics (tags), and related class links in metadata

---

**Last Updated:** 2026-05-15  
**Total Files:** 35+  
**Categories:** 3 (AI-ML, Cybersecurity, College Notes)
