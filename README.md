# AI-Driven Email Automation System

This project showcases a complete, end-to-end automated workflow for collecting contacts, generating personalized email content, sending emails, and updating CRM statuses. The system combines **HubSpot API**, **FastAPI**, **Docker**, **n8n**, and a local **Ollama AI model** to deliver a fully autonomous marketing pipeline.

---

## Overview

The goal of this automation is to remove all manual work from outreach. The system fetches contacts from HubSpot, prepares the data, generates customized email content using a local AI model, sends the emails, and updates the contact’s status inside HubSpot — all without human intervention.

---

## Architecture Breakdown

### **1. Contact Retrieval (Python + FastAPI)**
- A Python script connects to HubSpot via the official API and pulls all contact records with full property data.
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

---

## Data Flow Summary

HubSpot API → FastAPI (data fetch)  
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

---

## Key Features

- **Full automation** from data pull to email delivery.  
- **Local AI generation** ensures fast, private, and cost-efficient content creation.  
- **CRM sync** keeps HubSpot always up-to-date.  
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
- data processing  
- building microservices  
- orchestrating workflows  
- integrating AI for real business tasks  
- synchronizing multiple systems  

It serves as a strong portfolio example for automation, backend development, and AI-driven marketing operations.


