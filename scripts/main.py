from modules.processing import StableDiffusionProcessing
import modules.scripts as scripts
from modules.shared import cmd_opts
import gradio as gr

import datetime

class GenerationScheduler(scripts.Script):
    def title(self):
        return "Generation Scheduler"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with gr.Accordion(f"{self.title()}", open=False):
            # とりあえずテキストボックス一つでやってみる
            with gr.Row():
                gr.Textbox(
                    value="SOIYA",
                    placeholder="TEXTBOX",
                    label="LABEL",
                )
        return [enable, token, notificationDisabled]

    def get_now_time(self):
        n = datetime.datetime.now()
        return n.strftime("%H:%M:%S")

    # setup が良い感じ？
    # def setup(self, p, *args):

