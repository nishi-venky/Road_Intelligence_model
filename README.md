# 🚍 Road Intelligence

### AI-Powered Mobile Road & Traffic Intelligence System

**Road Intelligence** is an AI-powered computer vision platform that transforms public buses into **mobile urban sensing units**. By using cameras mounted on buses, the system continuously monitors roads, traffic, and infrastructure while the bus operates on its normal route.

The platform combines **YOLO-based object detection, object tracking, road-condition analysis, GPS-based event localization, and GIS visualization** to create a scalable solution for intelligent road monitoring and traffic management.

---

## 📌 Overview

Traditional road inspection relies heavily on manual surveys, fixed CCTV cameras, and periodic inspections. These approaches can be expensive, slow, and limited in geographic coverage.

Road Intelligence addresses this problem by using buses that are already travelling throughout the city as **mobile sensing platforms**.

Camera footage captured from a bus is processed using AI models to detect:

* 🚗 Vehicles and road users
* 🕳️ Potholes
* 🛣️ Road cracks and surface damage
* 🚦 Traffic density
* 🚧 Potential road hazards
* 🚸 Pedestrian-crossing and road infrastructure issues
* 🚌 Traffic bottlenecks and abnormal situations

Detected events can be associated with **confidence scores, timestamps, and GPS coordinates**, allowing them to be stored and visualized on a centralized map.

---

## 🎯 Problem Statement

Cities generate large amounts of road and traffic information every day, but much of this information is difficult to collect continuously.

Road defects such as potholes and cracks can develop between inspection cycles, while traffic conditions change throughout the day.

A scalable system is required that can:

1. Continuously monitor roads.
2. Detect road damage automatically.
3. Analyze traffic conditions.
4. Identify potential hazards.
5. Record the location of detected problems.
6. Provide actionable information to authorities.

---

## 💡 Proposed Solution

Road Intelligence uses public buses as **mobile data-collection platforms**.

### Basic workflow

```text
Bus Camera
     ↓
Live Video
     ↓
Edge AI / Computer Vision
     ↓
YOLO Object Detection
     ↓
Object Tracking & Event Analysis
     ↓
GPS + Timestamp + Confidence
     ↓
Event Storage
     ↓
GIS / Monitoring Dashboard
```

Instead of deploying dedicated inspection vehicles throughout a city, existing public transport vehicles can collect road intelligence during their regular operations.

---

# 🚦 Key Features

## 1. Vehicle Detection

The system uses YOLO-based object detection to identify different road users.

Current traffic classes include:

* Autorickshaw
* Bicycle
* Bus
* Car
* Motorcycle
* Person
* Rider
* Truck

These detections can be used for traffic analysis and vehicle counting.

---

## 2. Road Damage Detection

The system also incorporates road-condition perception.

The road dataset contains classes such as:

* Pothole
* Longitudinal Crack
* Transverse Crack
* Alligator Crack
* Other Corruption

This allows the system to identify different forms of road deterioration from camera footage.

---

## 3. Traffic Analysis

Detected vehicles can be tracked across frames to estimate:

* Vehicle counts
* Traffic density
* Traffic flow
* Bottleneck locations
* Road utilization

Object tracking can maintain a persistent ID for vehicles as they move through the camera's field of view.

---

## 4. Road Hazard Detection

The platform can be extended to identify infrastructure and safety-related problems, including:

* Missing pedestrian crossings
* Damaged or missing road dividers
* Road hazards
* Waterlogging
* Unsafe pedestrian situations
* Other infrastructure abnormalities

---

## 5. GPS-Based Event Localization

Each important detection can be associated with:

```text
Detection Type
Confidence Score
Timestamp
GPS Coordinates
Vehicle / Track ID
```

This allows detected problems to be mapped to their actual geographical locations.

---

## 🗺️ GIS-Based Visualization

Road Intelligence is designed to integrate detected events with a geographic information system.

A centralized dashboard can display road problems on a map, allowing users to view where specific issues have been detected.

Example:

```text
             CITY ROAD MAP

       🕳️ Pothole
             │
             │
      🚗 🚗 🚗
             │
     🚧 Road Damage
             │
             │
        🚸 Crossing
```

This can help authorities understand the spatial distribution of road and traffic problems.

---

# 🤖 AI Architecture

The current AI pipeline is based on **YOLO11** for object detection.

```text
                   Camera
                      │
                      ▼
               Video Stream
                      │
                      ▼
              ┌──────────────┐
              │   YOLO11     │
              │ Object Model │
              └──────────────┘
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
   Traffic Objects          Road Objects
          │                       │
          ▼                       ▼
      Tracking              Classification
          │                       │
          └───────────┬───────────┘
                      ▼
                Event Engine
                      │
              ┌───────┴───────┐
              ▼               ▼
             GPS           Timestamp
              │               │
              └───────┬───────┘
                      ▼
               Event Database
                      │
                      ▼
               GIS Dashboard
```

---

# 📊 Datasets

## Indian Driving Dataset — IDD

The **Indian Driving Dataset (IDD)** is used for traffic-related object detection.

The dataset provides images captured from Indian road environments and contains multiple road-user categories.

The project uses a cleaned version of the dataset containing relevant traffic classes.

### Traffic Classes

| ID | Class        |
| -: | ------------ |
|  0 | Autorickshaw |
|  1 | Bicycle      |
|  2 | Bus          |
|  3 | Car          |
|  4 | Motorcycle   |
|  5 | Person       |
|  6 | Rider        |
|  7 | Truck        |

---

## Road Damage Dataset — RDD

The road perception component uses a road-damage dataset containing multiple types of road surface defects.

### Road Classes

| Class              |
| ------------------ |
| Longitudinal Crack |
| Transverse Crack   |
| Alligator Crack    |
| Other Corruption   |
| Pothole            |

The traffic and road-perception datasets can be combined into a unified detection pipeline for joint inference.

---

# 🧠 Model Training

The project uses **Ultralytics YOLO11** for training and inference.

Example training command:

```bash
python training.py D:\CleanedIDDDataset\data.yaml --epochs 5
```

A trained model produces weights such as:

```text
runs/
└── detect/
    └── train/
        └── weights/
            ├── best.pt
            └── last.pt
```

`best.pt` can then be used for evaluation and inference.

---

# 🎥 Live Camera Inference

The system can process video from different sources.

### Possible input sources

* USB camera
* Laptop webcam
* Smartphone camera
* IP Webcam
* RTSP camera
* Bus-mounted camera

For prototyping, a smartphone can act as the camera while a laptop performs the AI processing.

```text
Smartphone
    │
    │ RTSP / IP Camera
    ▼
Laptop
    │
    ▼
YOLO11
    │
    ▼
Detection + Tracking
```

This allows the complete pipeline to be tested before deployment on dedicated edge hardware.

---

# 🍓 Edge Deployment

The long-term goal is to deploy the AI system directly on an **edge computing device installed inside a bus**.

A possible deployment architecture is:

```text
Bus Camera
     ↓
Raspberry Pi / Edge Computer
     ↓
Optimized YOLO Model
     ↓
Real-Time Detection
     ↓
Event Generation
     ↓
GPS + Timestamp
     ↓
Cloud / Central Server
```

Model optimization and quantization can be explored to reduce computational requirements and enable inference on resource-constrained hardware.

---

# 🔄 Object Tracking

Detection alone identifies objects in individual frames.

For traffic analysis, tracking can associate detections across consecutive frames:

```text
Frame 1 → Car ID 12
Frame 2 → Car ID 12
Frame 3 → Car ID 12
Frame 4 → Car ID 12
```

This enables applications such as:

* Vehicle counting
* Line-crossing detection
* Traffic-flow analysis
* Vehicle trajectory analysis
* Incident detection

ByteTrack is one of the tracking approaches considered for the project.

---

# 🚨 Future Incident Detection

The Road Intelligence platform is designed to support more advanced event detection in future versions.

Potential applications include:

* Rash-driving detection
* Collision detection
* Hit-and-run event detection
* Dangerous pedestrian situations
* Abnormal vehicle behavior
* Number-plate event triggering

These systems can generate structured events for further analysis rather than simply storing raw video.

---

# 🛠️ Technology Stack

| Component           | Technology                |
| ------------------- | ------------------------- |
| Programming         | Python                    |
| Computer Vision     | OpenCV                    |
| Object Detection    | YOLO11                    |
| Object Tracking     | ByteTrack                 |
| Deep Learning       | PyTorch                   |
| Model Framework     | Ultralytics               |
| Traffic Dataset     | IDD                       |
| Road Dataset        | RDD                       |
| Camera Input        | RTSP / IP Camera / USB    |
| Edge Computing      | Raspberry Pi              |
| Mapping             | GIS / Map-based Dashboard |
| Data Format         | JSON                      |
| Geospatial Indexing | H3                        |

---

# 📁 Project Structure

```text
Road-Intelligence/
│
├── datasets/
│   ├── IDD/
│   └── RDD/
│
├── training/
│   ├── training.py
│   └── data.yaml
│
├── models/
│   └── best.pt
│
├── inference/
│   ├── test_camera.py
│   └── detection.py
│
├── tracking/
│   └── tracker.py
│
├── events/
│   └── event_engine.py
│
├── dashboard/
│   └── map/
│
├── outputs/
│
└── README.md
```

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone <repository-url>
cd Road-Intelligence
```

## 2. Install dependencies

```bash
pip install ultralytics opencv-python torch
```

Additional dependencies can be installed depending on the tracking, GPS, and dashboard components.

## 3. Prepare the dataset

Organize the dataset using the YOLO directory structure:

```text
dataset/
├── train/
│   ├── images/
│   └── labels/
│
├── val/
│   ├── images/
│   └── labels/
│
└── test/
    ├── images/
    └── labels/
```

## 4. Train the model

```bash
python training.py <path-to-data.yaml> --epochs 5
```

## 5. Run inference

```bash
python test_camera.py --model <path-to-best.pt> --source <camera-source>
```

---

# 📈 Evaluation

The project evaluates trained models using standard object-detection metrics including:

* Precision
* Recall
* mAP@0.5
* mAP@0.5:0.95
* Per-class performance

Evaluation is performed on validation/test datasets to identify classes that require further improvement.

---

# 🎯 Project Goals

The long-term objective of Road Intelligence is to create a **city-scale road intelligence network** using existing public transportation infrastructure.

The system aims to provide:

> **Continuous road monitoring without requiring dedicated inspection vehicles.**

By combining AI, edge computing, GPS, object tracking, and GIS, the platform can convert ordinary bus journeys into a continuous source of road and traffic intelligence.

---

# 🔮 Future Scope

Future development can include:

* Multi-camera bus setup
* Real-time cloud synchronization
* Advanced traffic prediction
* Automated road-maintenance prioritization
* Improved road-damage classification
* Number-plate event detection
* Collision and incident analysis
* Edge-model quantization
* Raspberry Pi deployment
* Multi-bus fleet integration
* Central command-center dashboard
* Historical road-condition analysis
* Automated alerts for authorities

---

# 🌐 Vision

Road Intelligence aims to move from **periodic road inspection** toward **continuous, AI-driven road intelligence**.

Instead of asking:

> *"When was this road last inspected?"*

the system aims to provide a continuously updated view of:

> **"What is happening on our roads right now?"**

---

## 👨‍💻 Project

**Road Intelligence**
AI-powered road monitoring, traffic analysis, and urban sensing platform.

Built using **Computer Vision + Deep Learning + Edge AI + Geospatial Intelligence**.
