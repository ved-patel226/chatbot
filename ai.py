import os

import google.generativeai as genai


class GenAi:
    def __init__(self):

        genai.configure(api_key="AIzaSyCTcqQKqSbUGm_7DvwnlV4BPja5kXI7zVA")

        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 2048,
            "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            # See https://ai.google.dev/gemini-api/docs/safety-settings
        )

        self.chat_session = model.start_chat(history=[])

    def send_message(self, message):
        response = self.chat_session.send_message(message)
        return response.text
