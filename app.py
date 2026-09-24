import qrcode as qr
from datetime import datetime

def create_qr():
    #get user input
    data=input("Enter the url or text for qr:").strip()
    if not data:
        print("Input is Empty !!")
        return

    #for asking custom filename from user
    custom_name=input("Enter output filename (press Enter for default):").strip()

    if not custom_name:
        filename=f"qr_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    else:
        filename=custom_name if(custom_name.endswith(".png")) else f"{custom_name}.png"          #short code for below 4 lines
#     if custom_name.endswith(".png"):
#     filename = custom_name
#     else:
#     filename = f"{custom_name}.png"

    fg_color = input("Enter QR color (e.g. black, navy, darkgreen) [default: black]: ").strip() or "black"
    bg_color = input("Enter background color (e.g. white, yellow, cyan) [default: white]: ").strip() or "white"

    code = qr.QRCode(
        version=1,                                                  #sets grid size
        error_correction=qr.constants.ERROR_CORRECT_H,              #code thoda kharab hone pr bhi scan ho sake
        box_size=10,                                                #har ek square dot kitne pixel ka hoga
        border=4,                                                   #boundary ke all sides kitne boxes kiwhite space ragegi
    )    

    code.add_data(data)

    code.make(fit=True)

    try:
        img = code.make_image(fill_color=fg_color, back_color=bg_color)
        img.save(filename)
        img.show()
        print(f"\n Success! Saved as '{filename}'")
    except Exception as e:
        print(f"\n Error creating image: {e}")

    # Script run hote hi sabse pehle ye check hoga aur function call karega
if __name__ == "__main__":
    create_qr()