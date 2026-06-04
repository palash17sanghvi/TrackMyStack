# TrackMyStack

A streamlined, secure web application for tracking recurring software subscriptions and managing infrastructure costs.

## 🎯 Overview
Managing multiple software services often leads to "subscription creep." TrackMyStack solves this by providing a centralized financial dashboard to monitor monthly burn rates, project annual costs, and securely manage asset data. 

## ✨ Key Features
* **Financial Analytics:** Real-time calculation of monthly burn rates and annual financial projections.
* **Asset Management (CRUD):** Seamlessly create, read, update, and delete subscription pipelines.
* **Zero-Trust Security:** Strict access control utilizing Time-based One-Time Password (TOTP) Multi-Factor Authentication (MFA).
* **Modern Interface:** Clean, responsive, and grid-based UI built for a frictionless user experience.

## 🛠️ Tech Stack
* **Backend:** Python, Django 6.0
* **Security:** Django OTP, Two-Factor Authentication (MFA/2FA)
* **Database:** SQLite
* **Frontend:** HTML5, Custom CSS3, Django Template Engine

## 🚀 Quick Start

**1. Clone the repository**

    git clone [https://github.com/palash17sanghvi/TrackMyStack.git](https://github.com/palash17sanghvi/TrackMyStack.git)
    cd TrackMyStack

**2. Set up the environment**

    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

**3. Initialize and run**

    python manage.py migrate
    python manage.py runserver

---
*Note: A live preview of the dashboard interface can be found in the `/assets` directory.*