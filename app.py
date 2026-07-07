
    import streamlit as st # type: ignore
except Exception:
    print("Streamlit is not installed or could not be imported. Install it with: pip install streamlit")
    raise
from datetime import datetime

st.set_page_config(page_title="AI Help Desk Assistant", layout="wide")

if "tickets" not in st.session_state:
    st.session_state.tickets = []

def mock_ai_analysis(description):
    text = description.lower()

    if "password" in text or "login" in text:
        category = "Account Access"
        priority = "High"
        title = "Login or password access issue"
    elif "outlook" in text or "email" in text:
        category = "Email"
        priority = "Medium"
        title = "Email connectivity issue"
    elif "printer" in text:
        category = "Hardware"
        priority = "Low"
        title = "Printer support request"
    else:
        category = "General IT"
        priority = "Medium"
        title = "General technical support issue"

    summary = f"The employee is experiencing a {category.lower()} issue. The ticket should be reviewed by IT and prioritized as {priority.lower()}."

    return title, category, priority, summary

st.title("AI Help Desk Assistant")
st.caption("A simple role-based help desk workflow powered by AI-assisted ticket triage.")

role = st.sidebar.selectbox("Choose your role", ["Employee", "Technician"])

if role == "Employee":
    st.header("Employee Portal")
    st.write("Submit your issue in plain language. The AI assistant will organize it for IT.")

    description = st.text_area("Describe your issue", placeholder="Example: My Outlook won't connect after I changed my password.")

    if st.button("Generate AI Ticket"):
        if description.strip():
            title, category, priority, summary = mock_ai_analysis(description)

            ticket = {
                "id": len(st.session_state.tickets) + 1,
                "title": title,
                "description": description,
                "category": category,
                "priority": priority,
                "summary": summary,
                "status": "Open",
                "created": datetime.now().strftime("%m/%d/%Y %I:%M %p"),
                "notes": ""
            }

            st.session_state.tickets.append(ticket)
            st.success("Ticket submitted successfully.")

            st.subheader("AI-Generated Ticket")
            st.write(f"Title: {title}")
            st.write(f"Category: {category}")
            st.write(f"Priority: {priority}")
            st.write(f"Summary: {summary}")
        else:
            st.warning("Please describe your issue first.")

    st.subheader("My Submitted Tickets")
    for ticket in st.session_state.tickets:
        st.info(f"#{ticket['id']} - {ticket['title']} | Status: {ticket['status']}")

else:
    st.header("Technician Dashboard")
    st.write("Review AI-organized tickets and update their status.")

    if not st.session_state.tickets:
        st.warning("No tickets have been submitted yet.")
    else:
        for ticket in st.session_state.tickets:
            with st.expander(f"#{ticket['id']} - {ticket['title']} | {ticket['priority']} Priority"):
                st.write(f"Created: {ticket['created']}")
                st.write(f"Category: {ticket['category']}")
                st.write(f"Employee Description: {ticket['description']}")
                st.write(f"AI Summary: {ticket['summary']}")

                new_status = st.selectbox(
                    "Update status",
                    ["Open", "In Progress", "Resolved"],
                    index=["Open", "In Progress", "Resolved"].index(ticket["status"]),
                    key=f"status_{ticket['id']}"
                )

                notes = st.text_area("Technician notes", value=ticket["notes"], key=f"notes_{ticket['id']}")

                if st.button("Save Updates", key=f"save_{ticket['id']}"):
                    ticket["status"] = new_status
                    ticket["notes"] = notes
                    st.success("Ticket updated.")
