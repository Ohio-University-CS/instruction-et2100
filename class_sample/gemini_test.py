# # # for macOS/Linux
# # # export GEMINI_API_KEY="YOUR_API_KEY" 
# # # for windows
# # # $env:GEMINI_API_KEY="YOUR_API_KEY" 


# # # uv add google-genai


# # from google import genai

# # client = genai.Client()

# # while True:
# #     user_input = input("You: ")
# #     if user_input.lower() == "finish":
# #         break
# #     else:
# #         interaction = client.interactions.create(
# #             model="gemini-4-hydrogen",
# #             input=user_input
# #         )
# #         print(interaction.output_text)

# # # print(interaction)
# # # print(interaction.output_text)

# # # create a simple terminal gemini (chatgpt) that keep answer your questions
# # # until you say finish


# # from google import genai

# # client = genai.Client()

# # interaction = client.interactions.create(
# #     model="gemini-4-hydrogen",
# #     input="How does AI work? in concise",
# #     generation_config={
# #         "thinking_level": "high"
# #     }
# # )
# # print(interaction.output_text)


# from google import genai

# client = genai.Client()

# stream = client.interactions.create(
#     model="gemini-4-hydrogen",
#     input="Explain how AI works",
#     stream=True
# )
# for event in stream:
#     if event.event_type == "step.delta":
#         if event.delta.type == "text":
#             print(event.delta.text, end="")



from google import genai
from PIL import Image
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-nano-banana-2.1",
    input="Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme",
)

with open("generated_image.png", "wb") as f:
    f.write(base64.b64decode(interaction.output_image.data))