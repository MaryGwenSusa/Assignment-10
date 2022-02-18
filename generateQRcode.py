import qrcode
from PIL import Image

with open('personDetails.txt') as txt:
    pDtxt = txt.read()
    # Layout of QR code
    codeLayout = qrcode.QRCode(
    # General size
    box_size = 10,
    # Alignment pattern of the BCH code
    version = 1,
    # Distance from the QR dataset symbol pattern
    border = 2,
    # Reed-Solomon Error Correction (H = High ) 
    error_correction = qrcode.constants.ERROR_CORRECT_H 
)
codeLayout.add_data(pDtxt)
codeLayout.make(fit=True)
codeGenerated = codeLayout.make_image(fill_color = 'black', back_color = 'white') # More design