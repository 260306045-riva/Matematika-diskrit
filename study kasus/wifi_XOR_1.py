wifi = True
data_seluler = True

# LOGIKA XOR
hasil = wifi ^ data_seluler

# output
if wifi ^ data_seluler:
    print("internet dapat digunakan")
else:
    print("tidak ada koneksi internet")
