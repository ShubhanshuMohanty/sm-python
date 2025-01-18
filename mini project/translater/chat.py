from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the pre-trained model and tokenizer
model_name = "microsoft/DialoGPT-medium"  # You can choose another model from Hugging Face's model hub if desired
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Function to interact with the chatbot
def chat_with_bot():
    print("Hello! I am your AI chatbot. Type 'quit' to end the chat.")
    
    # Initialize conversation history
    chat_history_ids = None
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Encode the user input
        new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
        
        # Append the new input to the conversation history
        bot_input_ids = new_user_input_ids if chat_history_ids is None else torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
        
        # Generate a response from the model
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id, top_p=0.92, temperature=0.75)
        
        # Decode the response and print it
        bot_output = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        print(f"Bot: {bot_output}")

if __name__ == "__main__":
    chat_with_bot()
