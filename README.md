# 🌾 Farming Chatbot - An AI Assistant for Farmers 🤖

![Header Image](https://th.bing.com/th/id/OIG3.CMQYJVqY57fkKJhsqs6.?w=270&h=270&c=6&r=0&o=5&dpr=1.3&pid=ImgGn) 

## 🚀 Overview
The **Farming Chatbot** is a conversational AI assistant designed to help farmers with various tasks like pest control, crop management, and farming best practices. It aims to make agricultural knowledge more accessible by using natural language conversation. Built with state-of-the-art machine learning and NLP tools, this chatbot assists users in an interactive, efficient way.

## 🎯 Features
- **Interactive Conversations**: Provides conversational responses to farming-related queries.
- **Audio Support**: Convert chatbot text responses to speech.
- **Voice Input**: Supports voice-based user input.
- **Rich Farming Knowledge**: Tips for pest control, soil management, crop yields, and more.
- **Basic Chat**: Handles common greetings and casual conversations to enhance user engagement.

## 🤔 Problem Statement
Farmers often lack easy access to expert knowledge for managing daily farming activities. This chatbot bridges the gap by providing personalized assistance on-demand, enabling farmers to make informed decisions quickly.

## 💻 Tech Stack
- **Streamlit**: For building the interactive web interface.
- **Transformers & PyTorch**: Model used for generating responses.
- **Text-to-Speech (gTTS/pyttsx3)**: Converts chatbot responses to audio.
- **SpeechRecognition**: Converts user voice input to text.
- **Streamlit-Chat**: To display chat history.

## 📑 Implementation Details
The project is built using **Streamlit** for the user interface, which supports text and audio interactions. The backend chatbot is powered by a **GPT-2 model**, fine-tuned to handle both farming-specific queries and general greetings. 

### Steps for Implementation:
1. **User Authentication**: The user logs in to access the chatbot. The login functionality is implemented in `login.py`. ( Actually i made a code of login.py just because i was bored )
2. **Interaction Interface**: Users interact via the chat interface built in `app.py`.
3. **Model Responses**: A custom-trained GPT-2 model provides farming advice.
4. **Audio Integration**: Text-to-speech and speech-to-text functions offer an engaging way for farmers to interact with the bot.
5. **Deployment**: Deployed using Streamlit to ensure a lightweight, user-friendly experience.

## 🛠️ How to Run Locally
### Prerequisites
- Python 3.10+
- Git
- Required Libraries:
  ```bash
  pip install -r requirements.txt
  ```
# 🚀 Running the Project

1. Clone the repository:
    ```bash
    git clone https://github.com/RaviTejaaKatta/FarmersChatBot.git
    ```

2. Navigate to the project folder:
    ```bash
    cd farming-chatbot
    ```

3. Run the application:
    ```bash
    streamlit run app.py
    ```

4. The app will launch in your browser.

## 🤖 Model Details
The chatbot uses a **fine-tuned GPT-2** model for generating responses. Initial training focused on farming tips, while fine-tuning expanded its ability to recognize general conversational prompts, spelling mistakes, and greetings.( I used GPT-2 because my laptop can't handle the load of other GPT models)

### Data Used
- **Farming Tips JSON**: The primary dataset includes common farming practices.
- **Greetings Corpus**: The chatbot was also trained with basic greeting dialogues to enable friendly interactions.

## 🔬 Testing of Project
We performed testing across several scenarios to evaluate the chatbot’s performance:

1. **General Greetings**: Bot responds naturally to various greetings and small talk.
2. **Farming-Specific Queries**: Thorough testing on how well the bot provides farming advice.
3. **Speech Integration**: The voice input and output functionalities were tested for accuracy and response clarity.

### Example Interaction
User: "How do I improve soil quality?"  
Bot: "To improve soil quality, consider adding compost or organic matter. Using cover crops can also enhance fertility."  

## 💡 Future Scope
- **Multi-Language Support**: Adding regional languages to reach more farmers.
- **Advanced AI Integration**: Using more advanced models like GPT-3 or fine-tuning to specific regions.
- **Weather Data Integration**: Provide real-time farming advice based on current weather.

## 🏆 Achievements
- Helped users reduce the time taken to get answers to their farming problems.
- Successfully integrated audio features for a more immersive experience.

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
We love collaboration! If you want to contribute to this project, please feel free to:
- Submit issues and feature requests.
- Fork the project and submit pull requests.
- I'm new to building a LLM, so feel free to adjust my code so that the app looks more interactive

## 📬 Contact
- ** Mail **: kattarockyraviteja123@gmail.com
- GitHub: [GitHub](https://github.com/RaviTejaaKatta)

## 🐑 Shoutout to All Farmers
> “Farmers are the backbone of society. Let’s support them with technology.” 🧑‍🌾

![Thank You](panda.jpeg) 

