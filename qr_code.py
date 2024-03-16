import pyqrcode

website = 'https://github.com/ylanekouassi'

qr_code = pyqrcode.create(website)

qr_code.svg("ylanekouassi_git.svg", scale = 6)