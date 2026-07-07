# HelpDesk-AI
AI Help Desk Assistant built in Python using Streamlit.
Demo video: https://1drv.ms/f/c/73546c4a586072f6/IgCePDuTqkzOTovIkpV6lhgYAS6FalzbFU3Fw4NaOvt64qg?e=THld8P
A small Streamlit web application built for the Clarity AI practical evaluation. The app demonstrates how AI-assisted workflows can simplify help desk ticket creation and resolution for different user roles.

-Overview-
AI Help Desk Assistant is designed to reduce friction between employees and IT technicians. Employees can submit support issues in plain language, and the app generates an AI-assisted ticket title, category, priority level, and summary. Technicians can then review the organized ticket, update its status, add notes, and resolve the issue.

-User Roles-
Employee:
Submit a support issue in plain language
Generate an AI-assisted ticket
View submitted ticket status

Technician:
Review submitted tickets
View AI-generated summaries, categories, and priorities
Add technician notes
Update ticket status

-Workflow-
Employee describes a technical issue.
The app generates a clear ticket title, category, priority, and summary.
The ticket appears in the technician dashboard.
The technician reviews the ticket, adds notes, and updates the status.
The employee can view the updated ticket status.

-Technologies Used-
Python
Streamlit
Session State
Mock AI-assisted logic

-AI Tools Used-
I used ChatGPT to help brainstorm the workflow, refine the user experience, organize the application structure, and accelerate implementation. I reviewed and adapted the generated code to fit the intended design and functionality.

-What Makes This App Unique-
This app focuses on reducing cognitive load. Employees do not need to understand technical categories or decide ticket priority. The AI-assisted workflow organizes the request into a consistent, actionable format so technicians can spend less time interpreting requests and more time solving problems.

-How to Run Locally-
Install Streamlit: pip install streamlit
Run the application: streamlit run app.py

-Project Purpose-
This project was created as a practical evaluation for an entry-level AI Software Engineer opportunity. The focus is on product judgment, role-based user experience, and using AI to make a workflow simpler and more intuitive.
