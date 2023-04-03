import qrcode
import PySimpleGUI as sg
import io


def generate_qr_code(text):
    try:
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        with io.BytesIO() as output:
            img.save(output, format='png')
            img_bytes = output.getvalue()
        return img_bytes
    except Exception as e:
        print(f"Error generating QR code: {e}")
        sg.PopupError("Error generating QR code")


layout = [
    [sg.Text("Enter text to convert to QR code:")],
    [sg.Input(key="-INPUT-")],
    [sg.Button("Create")],
    [sg.Image(key="-IMAGE-")]
]


window = sg.Window("QR Code Generator", layout)


while True:
    event, values = window.read()
    if event == "Create":

        text = values["-INPUT-"]
        print(f"Input text: {text}")
        
        
        img_bytes = generate_qr_code(text)
        if img_bytes:
            
            window["-IMAGE-"].update(data=img_bytes)
    elif event == sg.WIN_CLOSED:
        break


window.close()



