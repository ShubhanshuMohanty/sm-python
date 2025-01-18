from google.cloud import generativeai

# Replace with your actual API key
generativeai.configure(api_key="AIzaSyBvV1aXm0PAqOHGLKhTD2Yj6gzCfMrvUHU") 

model = generativeai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)