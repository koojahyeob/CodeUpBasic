w, h, b = input().split()

w = int(w)
h = int(h)
b = int(b)

x = w*h*b
y = 8*1024*1024

print("%.2f"%(x/y) +" MB")

#8 bit(비트           = 1byte(바이트)     #       8bit=1Byte
#1024 Byte(210 byte) = 1KB(킬로 바이트)  # 1024Byte=1KB
#1024 KB(210 KB)      = 1MB(메가 바이트)
#1024 MB(210 MB)     = 1GB(기가 바이트)
#1024 GB(210 GB)      = 1TB(테라 바이트