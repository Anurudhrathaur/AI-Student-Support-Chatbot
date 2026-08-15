
from google import genai
import os


def create_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not configured.")

    return genai.Client(api_key=api_key)


SYSTEM_PROMPT = """
You are an AI Student Support Chatbot.

Your job is to help students with college and student-support related questions.

You can help with:
- Admissions
- Admission documents
- Fees
- Examinations
- Library
- Hostel
- Scholarships
- Placements
- Academic support
- General student services

Important rules:
1. Give clear and helpful answers.
2. If information is not provided, do not invent official college-specific facts.
3. Tell the student when they should contact the college office for official information.
4. Politely refuse questions that are unrelated to student support.
5. Keep answers simple and student-friendly.
"""


def get_response(user_message):
    client = create_client()

    prompt = f"""
{SYSTEM_PROMPT}

Student's question:
{user_message}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text
