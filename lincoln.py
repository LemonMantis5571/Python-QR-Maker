from textwrap import fill
import qrcode

qr = qrcode.QRCode(
    version=2,
    box_size=10,
    border=5
)

content = 'https://www.youtube.com/watch?v=msSTlqos4fQ'

qr.add_data(content)
qr.make(fit=True)
img = qr.make_image(fill='black',
    back_color='white'
)
img.save('dahyun.png')
