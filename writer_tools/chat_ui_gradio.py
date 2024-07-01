import gradio as gr
from pathlib import Path

image_dir = Path("./images")
human_icon = image_dir / "human_icon.png"
ai_icon = image_dir / "ai_icon.png"
with gr.Blocks(theme=gr.themes.Default(primary_hue="green")) as demo:
    chatbot = gr.Chatbot(avatar_images=(str(human_icon), str(ai_icon)))
    user_message = gr.Textbox(label="ユーザ入力")
    ai_message = gr.Textbox(label="AI応答")
    submit_button = gr.Button("送信")
    clear = gr.ClearButton([chatbot, user_message, ai_message])

    def respond(user_message, ai_message, chat_history):
        chat_history.append((user_message, ai_message))
        return "", "", chat_history

    submit_button.click(
        respond,
        inputs=[user_message, ai_message, chatbot],
        outputs=[user_message, ai_message, chatbot],
    )


demo.launch()
