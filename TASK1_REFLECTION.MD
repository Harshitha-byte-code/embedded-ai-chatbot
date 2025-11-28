## Task 1: Streamlit Chatbot Reflection

# What was easy / hard about using Streamlit + OpenAI?

Easy Aspects:
Using Streamlit to build the chatbot interface was remarkably straightforward. The st.chat_message() and st.chat_input() functions made creating a professional-looking chat interface simple with minimal code. Streamlit's session state management worked seamlessly for maintaining conversation history across interactions. The OpenAI API integration was also intuitive - the documentation was clear, and the streaming feature allowed for a smooth, responsive user experience that felt natural and engaging.

Challenging Aspects:
The most challenging aspect was properly structuring the conversation history for the OpenAI API. Understanding how to format the messages array with the system prompt and user/assistant messages required careful attention. Error handling was another complexity - I needed to anticipate various failure scenarios like missing API keys, network issues, or rate limiting, and provide user-friendly error messages for each case. Additionally, crafting the system prompt for the health chatbot required balance - being helpful and informative while clearly stating limitations and reminding users that the chatbot isn't a replacement for professional medical advice.

One thing I would improve if I had more time:
If I had more time, I would implement a persistent conversation storage system using a database (like SQLite or PostgreSQL) so users could return to previous conversations. This would include features like:

Conversation history saved to disk with timestamps
Ability to browse and resume past conversations
Export chat history as PDF or text file
User authentication to keep conversations private
Voice input/output using speech recognition and text-to-speech for accessibility
Multi-language support to reach a broader audience
Integration with verified medical databases (like PubMed or WHO resources) for more accurate and sourced information
Analytics dashboard showing common health topics users ask about
