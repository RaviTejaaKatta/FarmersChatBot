from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the fine-tuned model
model = GPT2LMHeadModel.from_pretrained("C:\\Users\\katta\\VS CODE\\LLMmodel\\LLM\\model-folder")

# Load the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("C:\\Users\\katta\\VS CODE\\LLMmodel\\LLM\\model-folder")
