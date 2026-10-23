
from pathlib import Path

import gradio as gr
from PIL import Image


# Path to the latest drawing
BILD_DATEI = Path("letzte_zeichnung.png")


def zeichnung_empfangen(bild):
    """Saves the drawing received from the iPad."""

    if bild is None or bild.get("composite") is None:
        return "Bitte zeichne zuerst etwas!"

    # Extract the final image from the Gradio editor
    fertiges_bild = Image.fromarray(bild["composite"])

    # Save the drawing locally on the laptop
    fertiges_bild.save(BILD_DATEI)

    return "Zeichnung erfolgreich übertragen!"


def bild_anzeigen():
    """Loads the most recently saved drawing."""

    if not BILD_DATEI.exists():
        return None

    with Image.open(BILD_DATEI) as bild:
        return bild.copy()


with gr.Blocks() as demo:
    gr.Markdown("# DrawAI")
    gr.Markdown("Interaktive Zeichnungserkennung – erster Prototyp")

    # Interface for the iPad
    with gr.Tab("iPad – Zeichnen"):
        zeichnung = gr.Sketchpad(
            label="Zeichenfläche",
            type="numpy",
            width=400,
            height=400,
            brush=gr.Brush(
                colors=["#000000", "#FF0000", "#0000FF", "#00AA00"],
                color_mode="fixed"
            )
        )

        senden = gr.Button("Zeichnung senden")
        status = gr.Textbox(label="Status")

        senden.click(
            fn=zeichnung_empfangen,
            inputs=zeichnung,
            outputs=status
        )

    # Interface for the laptop
    with gr.Tab("Laptop – Anzeige"):
        anzeige = gr.Image(label="Letzte Zeichnung")
        aktualisieren = gr.Button("Zeichnung aktualisieren")

        aktualisieren.click(
            fn=bild_anzeigen,
            outputs=anzeige
        )


if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860
    )
