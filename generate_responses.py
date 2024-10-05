def generate_response(prompt, model, tokenizer, max_length=100):
    '''
    this function takes the users input which is string prompt 
    and model and tokenizer as parameters
    and returns a string which is the users input and model generates a response for it
    '''
    # encode user input 
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    # Generate a response from the model
    outputs = model.generate(
        inputs,
        max_length=max_length,
        do_sample=True,  # Use sampling for more varied responses
        top_p=0.95,  # Nucleus sampling: only keep the top 95% most likely next words
        top_k=50   # Consider only the top 50 words
    )
    # Decode the generated tokens to text
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
