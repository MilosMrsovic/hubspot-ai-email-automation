# AI-Driven Email Automation System

This project showcases a complete, end-to-end automated workflow for collecting contacts, generating personalized email content, sending emails, and updating CRM statuses. The system combines **HubSpot API**, **FastAPI**, **Docker**, **n8n**, and a local **Ollama AI model** to deliver a fully autonomous marketing pipeline.

---

## Overview

The goal of this automation is to remove all manual work from outreach. The system **fetches only contacts with the status 'in_progress' from HubSpot**, prepares the data, generates customized email content using a local AI model, sends the emails, updates the contact’s status inside HubSpot, and **sends a final summary report** all without human intervention.

---

## Architecture Breakdown

### **1. Contact Retrieval (Python + FastAPI)**
- A Python script connects to HubSpot via the official API and pulls contact records **filtered by the status 'in_progress'**.
- The data is cleaned and saved into a structured CSV file.
- A FastAPI endpoint is exposed so the script can be triggered by n8n at any moment.

### **2. Data Processing (n8n)**
Once the CSV is generated:

- n8n loads the file from a Docker-mounted folder.
- The file is split into individual items so each contact can be processed separately.
- Data is normalized and prepared for AI content generation.

### **3. AI-Generated Email Content (Ollama)**
For every contact:

- A local Ollama model generates a personalized email body.
- A matching subject line is generated based on the content.
- The model uses contact details from the CSV to tailor tone, message, and relevance.

### **4. Email Delivery & Status Update**
- Emails are sent automatically through the chosen email provider (e.g., SMTP, Gmail API, or another service).
- After a successful send, n8n calls the HubSpot API to update the contact status (e.g., `in_progress → contacted`).
- Errors are captured and logged to ensure no contact is skipped.

### **5. Final Reporting (New Feature)**
- Once the processing loop finishes, the workflow generates a **final email report** containing a table of **Name and Email** for all contacts that were successfully sent an email.

---

## Data Flow Summary

HubSpot API (Filter: 'in_progress' status) → FastAPI (data fetch)
↓
CSV stored in Docker-mounted folder
↓
n8n loads CSV → splits contacts
↓
Ollama generates personalized content
↓
Email is sent
↓
HubSpot contact status is updated
↓
**Final Step: Summary Email Report with Table of Sent Contacts**

---

## Key Features

- **Targeted automation:** Fetches only contacts currently in the `in_progress` stage.
- **Full automation** from data pull to email delivery.
- **Local AI generation** ensures fast, private, and cost-efficient content creation.
- **CRM sync** keeps HubSpot always up-to-date.
- **End-of-Process Reporting:** Provides a final summary email detailing all successful outreach.
- **Modular design** — each component can be replaced or enhanced without breaking the workflow.
- **Real-world use case** demonstrating API work, automation logic, AI integration, and system orchestration.

---

## Requirements

- HubSpot private app token
- Docker environment
- FastAPI and Python 3.10+
- n8n automation platform
- Local Ollama installation and model
- Email provider/API credentials

---

## Why This Project Matters

This system demonstrates practical automation skills suited for real companies:

- handling APIs
- **implementing selective filtering logic**
- data processing
- building microservices
- orchestrating workflows
- integrating AI for real business tasks
- synchronizing multiple systems
- **delivering post-process reporting**

It serves as a strong portfolio example for automation, backend development, and AI-driven marketing operations.

