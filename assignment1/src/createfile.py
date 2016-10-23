with open("512M+7", "wb") as out:
    out.seek(512 * 1000000 + 6)
    print out.tell()
    out.write("\0")
import os
print(os.stat("512M+7").st_size)
