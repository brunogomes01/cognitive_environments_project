# Cognitive Environments  
## Automated Document Validation and Facial Recognition Pipeline

---

## 📌 Overview

**Cognitive Environments** is an academic project that applies **Computer Vision and Artificial Intelligence** techniques to automate **identity verification and document validation** processes.

The solution integrates **OCR**, **face detection**, and **facial recognition** to validate whether personal identity data is consistent across multiple documents, simulating real-world **KYC (Know Your Customer)** and **fraud prevention** scenarios.

---

## 🎯 Problem Statement

Manual document validation workflows are often:
- Time-consuming
- Error-prone
- Difficult to scale

Organizations require automated solutions capable of:
- Extracting structured information from official documents
- Verifying facial identity
- Cross-validating data across multiple sources
- Supporting compliance and fraud detection processes

---

## 🧠 Solution Description

This project implements an end-to-end validation pipeline that performs:

1. **Optical Character Recognition (OCR)** on a government-issued ID to extract personal data  
2. **Face detection and cropping** from the document image  
3. **Facial similarity comparison** between the document image and a selfie  
4. **Text validation** against a proof-of-address document  
5. **Final decision logic** to approve or reject the validation request  

---

## 🏗️ Architecture

The solution is composed of the following components:

- **Google Cloud Vision API**
  - Text Detection (OCR)
  - Face Detection
- **DeepFace**
  - Facial recognition and similarity scoring
- **OpenCV**
  - Image processing and face extraction
- **Python**
  - Pipeline orchestration and validation logic

The architecture is modular and designed for future API-based or cloud-native deployments.

---

## 📊 Validation Workflow

1. Extract textual data from identity document  
2. Detect and extract face from document image  
3. Compare extracted face with selfie image  
4. Validate name consistency across documents  
5. Generate final approval or rejection result  

---

## ⚙️ Technologies & Tools

- Python  
- Google Cloud Vision API  
- DeepFace  
- OpenCV  
- Jupyter Notebook  

---

## 📁 Project Structure

```
cognitive_environments_project/
├── architecture/
│   └── architecture_diagram.png
├── credentials/
│   └── key_vision.json
├── images/
│   └── upload_images.py
├── report/
│   └── final_report.pdf
├── scripts/
│   └── main_script.py
├── src/
│   └── document_validation_pipeline.py
├── README.md
```

---

## 🚀 How to Run (Proof of Concept)

### Prerequisites
- Python 3.8 or higher  
- Google Cloud account with Vision API enabled  
- Service Account credentials

### Images Upload
- Upload your images at:
images/

### Install dependencies
```bash
pip install google-cloud-vision deepface opencv-python
```

---

## 🔐 Credentials Configuration

This project requires **Google Cloud Vision API credentials**.

Create a service account and place the key file locally at:

```
credentials/key_vision.json
```

---

## ▶️ Execute the Pipeline

```bash
python src/doc_validation_pipeline.py
```

---

## 📈 Decision Logic

The final validation decision considers:
- Facial match result  
- Facial similarity distance threshold  
- Name consistency across all documents  

The request is approved only if **all validation criteria are met**, ensuring a robust identity verification workflow.

---

## 🔍 Key Learnings

- Practical application of OCR for document processing  
- Facial recognition thresholds and validation strategies  
- Integration of multiple AI services into a single pipeline  
- Design of automated identity verification workflows  

---

## 🛣️ Future Improvements

- API deployment using FastAPI  
- Cloud-native logging and monitoring  
- Confidence scoring per validation stage  
- Dataset expansion for robustness testing  
- Integration with fraud detection systems  

---

## 👤 Author

**Bruno Gomes**  
Cloud Infrastructure Analyst | Data Science & AI Project 

Focused on Computer Vision, cloud-based AI solutions, and applied machine learning.

