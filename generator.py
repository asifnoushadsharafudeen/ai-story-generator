from transformers import pipeline
generator = pipeline("text-generation", model='gpt2')  #Globally defined

def generate_story(prompt: str) ->str: 
     #distilgpt2 is a pre-trained language model; it causes grammatical errors

    output = generator(prompt, max_length = 100, num_return_sequences = 1, temperature = 0.7, top_p = 0.9, repetition_penalty = 1.2)                                                       #Updated to 'gpt2' model for better english 

    return output[0]['generated_text'] #generator returns a list of dictionaries. The first item in dictionary is returned/printed


#Command Line Interface Model - Tested in Spyder IDE

if __name__ == "__main__":
    print("Welcome to AI Story Generator!\n ")
    
    user_prompt = input("Enter a story beginning: ")
    
    if not user_prompt.strip():
        print("Story cannot be empty. Please try again.")
        
    else:
        story = generate_story(user_prompt)
    
        print("\n Generated Story: \n")
    
        print(story)

