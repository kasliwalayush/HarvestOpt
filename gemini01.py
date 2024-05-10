import google.generativeai as genai

genai.configure(api_key="AIzaSyB_dlQHPizpvHlWlMAU7UVgf17hO_fgETc")

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


def start_conversation():
    convo = model.start_chat(history=[])
    return convo


def send_message(convo, message):
    response = convo.send_message(message)
    return response.text.replace("*", "")


def main(crop_name: str):
    convo = start_conversation()

    prompts = [
       f""" generate its output in html page with embedded styling,
            cultivation method for {crop_name} in step by step in detail and its imagea, give image link in jpg format and embbed them in img tag of html
            disease prediction, precaution, prevention method, and the cure for {crop_name},
            best fertilizer for {crop_name}""" 
       
        # "give best cultivation method for below and generate output in well formatted html ",
        # f"cultivation method for {crop_name} in step by step in detail and its image",
        # f"disease prediction, precaution, prevention method, and the cure for {crop_name}",
        # f"best fertilizer for {crop_name}"
    ]

    for prompt in prompts:
        try:
            response = send_message(convo, prompt)
            return response
        except Exception as e:
            print("An error occurred:", e)
            break



if __name__ == "main":
    main()