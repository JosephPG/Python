#Version: Python 2.X
import ctypes
import time
from StringIO import StringIO
from struct import pack
from ctypes import cast, POINTER, pointer, memmove, c_ubyte, sizeof
from ctypes.wintypes import HANDLE                               
from estruct import HEADER, DIB
from PIL import Image

def presiona_tecla():
    VK_SNAPSHOT = 0x2c
    ctypes.windll.user32.keybd_event(VK_SNAPSHOT, 0, 0, 0)
		
def get_clipboard():
    """Accedemos al clipboard"""
    CF_DIB = 8                                                   
    ctypes.windll.user32.OpenClipboard(None)                     
    data = ctypes.windll.user32.GetClipboardData(CF_DIB)        
    ctypes.windll.user32.CloseClipboard()                        
    return data	
	
def lock_address(address):
    """Bloqueamos direccion de memoria"""
    return ctypes.windll.kernel32.GlobalLock(address)         

def unlock_address(address):
    """Desbloqueamos direccion de memoria"""
    ctypes.windll.kernel32.GlobalUnlock(address)                                 

		
try:		
    presiona_tecla()
    address = HANDLE(get_clipboard())
    address = lock_address(address)
    pointer_ = cast(address, POINTER(DIB))
    DIB_pointer = pointer_[0]

    #Rellenemos la estructura HEADER
    header = HEADER()
    header.type = 19778                                            
    header.reserved = 0
    header.offset = 14 + sizeof(DIB)                               
    header.bfSize = DIB_pointer.biSizeImage + header.offset

    #Apuntar al mapa bits
    array_byte = (c_ubyte * DIB_pointer.biSizeImage)()
    memmove(array_byte, address + sizeof(DIB), DIB_pointer.biSizeImage) 

    #LLenamos el buffer
    buffer = StringIO()
    buffer.write(pack('<HIII', header.type, header.bfSize, header.reserved, header.offset))
    buffer.write(pack('<IiiHHIIiiII', DIB_pointer.biSize, DIB_pointer.biWidth,
                        DIB_pointer.biHeight, DIB_pointer.biPlanes, DIB_pointer.biBitCount,
                        DIB_pointer.biCompression, DIB_pointer.biSizeImage, 
                        DIB_pointer.biXPelsPerMeter, DIB_pointer.biYPelsPerMeter,
                        DIB_pointer.biClrUsed, DIB_pointer.biClrImportant))	
  			
    for x in range(DIB_pointer.biSizeImage):
        buffer.write(pack('>B', array_byte[x])) 
    
    #Convertimos el buffer de BITMAP a PNG
    img = Image.open(buffer)
    name = "captura_"+time.strftime("%d-%m-%y")+"_"+time.strftime("%H-%M-%S")+".png"
    img.save(name, "png")
							   
except Exception as e:
    print "Error identificado: ", e
	
finally:
    #Liberamos memoria, borramos variables
    unlock_address(address)
    del pointer_, DIB_pointer, array_byte, buffer, img
    print "Terminado"
