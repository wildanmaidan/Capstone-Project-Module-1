from datetime import datetime

# Syntax untuk menghitung usia berdasarkan tanggal lahir
def hitung_usia(tanggal_lahir):
    today = datetime.today() # Menghasilkan tanggal dari tanpa detail zona waktu
    tanggal_lahir = datetime.strptime(tanggal_lahir, "%Y-%m-%d")
    usia = today.year - tanggal_lahir.year - ((today.month, today.day) < (tanggal_lahir.month, tanggal_lahir.day)) # Fungsi perhitungan usia dari tahun yang diinput dan melihat dari tanggal dan bulan yang dibandingkan dengan today

    return usia # eksekusi fungsi berhenti, dan nilai yang ada setelah return dikirimkan kembali kepada pemanggil fungsi

# List 3 data dummy
data_karyawan = [
    ["101", "Wildan", "1995-01-22", hitung_usia("1995-01-22"), "L", "wildan@example.com"],
    ["102", "Farah", "1997-09-09", hitung_usia("1997-09-09"), "P", "farah@example.com"],
    ["103", "Lindawani", "1993-11-03", hitung_usia("1993-11-03"), "P", "lindawani@example.com"]
]

# Syntax untuk menampilkan menu utama
def menu_utama():
    print("\n=== Menu Manajemen Data Karyawan ===")
    print("1. Tampilkan Data Karyawan")
    print("2. Tambah Data Karyawan")
    print("3. Perbarui Data Karyawan")
    print("4. Hapus Data Karyawan")
    print("5. Keluar")
    pilihan = input("Pilih menu: ")
    return pilihan

# Syntax untuk menampilkan data karyawan
def tampilkan_data_karyawan():
    if len(data_karyawan) == 0:
        print("Belum ada data karyawan.")
        input("\nTekan Enter untuk kembali ke menu utama...")
    else:
        print("\nTampilkan data karyawan berdasarkan:")
        print("1. Semua data karyawan")
        print("2. Berdasarkan Nama")
        pilihan_tampil = input("Pilih opsi (1/2): ")
        
        if pilihan_tampil == "1":
            # Menampilkan semua data karyawan
            print("\nData Karyawan:")
            print("="*70)
            print("{:<10} {:<20} {:<15} {:<5} {:<10} {:<20}".format("ID", "Nama", "Tanggal Lahir", "Usia", "Kelamin", "Email")) # Mengatur tampilan perataan data pada tabel saat menampilkan hasil pencarian
            print("="*70)
            for karyawan in data_karyawan:
                print("{:<10} {:<20} {:<15} {:<5} {:<10} {:<20}".format(karyawan[0], karyawan[1], karyawan[2], karyawan[3], karyawan[4], karyawan[5]))
            print("="*70)
        
        elif pilihan_tampil == "2":
            # Menampilkan data berdasarkan nama
            nama_cari = input("Masukkan Nama Karyawan yang ingin ditampilkan: ").lower()
            ditemukan = False
            print("\nHasil pencarian untuk nama:", nama_cari.capitalize())
            print("="*70)
            print("{:<10} {:<20} {:<15} {:<5} {:<10} {:<20}".format("ID", "Nama", "Tanggal Lahir", "Usia", "Kelamin", "Email")) # Mengatur tampilan perataan data pada tabel saat menampilkan hasil pencarian
            print("="*70)
            for karyawan in data_karyawan:
                if karyawan[1].lower() == nama_cari:
                    print("{:<10} {:<20} {:<15} {:<5} {:<10} {:<20}".format(karyawan[0], karyawan[1], karyawan[2], karyawan[3], karyawan[4], karyawan[5]))
                    ditemukan = True
            if not ditemukan:
                print("Karyawan dengan nama tersebut tidak ditemukan.")
            print("="*70)
        
        else:
            print("Pilihan tidak valid.")
        
        input("\nTekan Enter untuk kembali ke menu utama...")

# Syntax untuk menambah data karyawan
def tambah_data_karyawan():
    konfirmasi_awal = input("Anda yakin ingin menambah data karyawan? (y/n): ").lower()
    if konfirmasi_awal == 'y':
        id_karyawan = input("Masukkan ID Karyawan: ")
        nama = input("Masukkan Nama: ")
        tanggal_lahir = input("Masukkan Tanggal Lahir (YYYY-MM-DD): ")
        usia = hitung_usia(tanggal_lahir)
        jenis_kelamin = input("Masukkan Jenis Kelamin (L/P): ")
        email = input("Masukkan Email: ")

        # Pengecekan duplikasi berdasarkan ID, nama, atau email
        for karyawan in data_karyawan:
            if karyawan[0] == id_karyawan:
                print(f"Data karyawan dengan ID {id_karyawan} sudah ada. Penambahan dibatalkan.")
                return
            if karyawan[1].lower() == nama.lower():
                print(f"Data karyawan dengan nama {nama} sudah ada. Penambahan dibatalkan.")
                return
            if karyawan[5].lower() == email.lower():
                print(f"Data karyawan dengan email {email} sudah ada. Penambahan dibatalkan.")
                return

        # Menampilkan kembali data yang diinput untuk konfirmasi
        print("\nData yang Anda masukkan:")
        print(f"ID Karyawan     : {id_karyawan}")
        print(f"Nama Karyawan   : {nama}")
        print(f"Tanggal Lahir   : {tanggal_lahir}")
        print(f"Usia            : {usia} tahun")
        print(f"Jenis Kelamin   : {jenis_kelamin}")
        print(f"Email           : {email}")
        
        # Konfirmasi akhir sebelum menyimpan data
        konfirmasi_akhir = input("Apakah data sudah benar? Simpan data? (y/n): ").lower()
        if konfirmasi_akhir == 'y':
            data_karyawan.append([id_karyawan, nama, tanggal_lahir, usia, jenis_kelamin, email])
            print("Data karyawan berhasil ditambahkan.")
        else:
            print("Penambahan data dibatalkan.")
    else:
        print("Penambahan data dibatalkan.")
    
    input("\nTekan Enter untuk kembali ke menu utama...")

# Syntax untuk memperbarui data karyawan
def perbarui_data_karyawan():
    konfirmasi = input("Anda yakin ingin memperbarui data karyawan? (y/n): ").lower()
    if konfirmasi == 'y':
        id_karyawan = input("Masukkan ID Karyawan yang ingin diperbarui: ")
        for karyawan in data_karyawan:
            if karyawan[0] == id_karyawan:
                print(f"Data Karyawan {karyawan[1]} ditemukan.")
                
                # Input data baru
                nama_baru = input("Masukkan Nama Baru: ")
                tanggal_lahir_baru = input("Masukkan Tanggal Lahir Baru (YYYY-MM-DD): ")
                usia_baru = hitung_usia(tanggal_lahir_baru)
                jenis_kelamin_baru = input("Masukkan Jenis Kelamin Baru (L/P): ")
                email_baru = input("Masukkan Email Baru: ")
                
                # Menampilkan data yang diubah untuk konfirmasi
                print("\nData yang akan diperbarui:")
                print(f"ID Karyawan     : {karyawan[0]}")
                print(f"Nama Karyawan   : {nama_baru}")
                print(f"Tanggal Lahir   : {tanggal_lahir_baru}")
                print(f"Usia            : {usia_baru} tahun")
                print(f"Jenis Kelamin   : {jenis_kelamin_baru}")
                print(f"Email           : {email_baru}")
                
                # Konfirmasi akhir sebelum memperbarui data
                konfirmasi_akhir = input("Apakah data sudah benar? Simpan perubahan? (y/n): ").lower()
                if konfirmasi_akhir == 'y':
                    karyawan[1] = nama_baru
                    karyawan[2] = tanggal_lahir_baru
                    karyawan[3] = usia_baru
                    karyawan[4] = jenis_kelamin_baru
                    karyawan[5] = email_baru
                    print("Data karyawan berhasil diperbarui.")
                else:
                    print("Perbaruan data dibatalkan.")
                break
        else:
            print("Karyawan dengan ID tersebut tidak ditemukan.")
    else:
        print("Perbaruan data dibatalkan.")
    
    input("\nTekan Enter untuk kembali ke menu utama...")


def hapus_data_karyawan():
    konfirmasi_awal = input("Anda yakin ingin menghapus data karyawan? (y/n): ").lower()
    if konfirmasi_awal == 'y':
        id_karyawan = input("Masukkan ID Karyawan yang ingin dihapus: ")
        for karyawan in data_karyawan:
            if karyawan[0] == id_karyawan:
                # Menampilkan data yang akan dihapus untuk konfirmasi
                print("\nData yang akan dihapus:")
                print(f"ID Karyawan     : {karyawan[0]}")
                print(f"Nama Karyawan   : {karyawan[1]}")
                print(f"Tanggal Lahir   : {karyawan[2]}")
                print(f"Usia            : {karyawan[3]} tahun")
                print(f"Jenis Kelamin   : {karyawan[4]}")
                print(f"Email           : {karyawan[5]}")
                
                # Konfirmasi akhir sebelum menghapus data
                konfirmasi_akhir = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ").lower()
                if konfirmasi_akhir == 'y':
                    data_karyawan.remove(karyawan)
                    print(f"Data Karyawan {karyawan[1]} berhasil dihapus.")
                else:
                    print("Penghapusan data dibatalkan.")
                break
        else:
            print("Karyawan dengan ID tersebut tidak ditemukan.")
    else:
        print("Penghapusan data dibatalkan.")
    
    input("\nTekan Enter untuk kembali ke menu utama...")


# Syntax utama yang menjalankan program
def main():
    while True:
        pilihan = menu_utama()
        
        if pilihan == "1":
            konfirmasi = input("Anda yakin ingin menampilkan data karyawan? (y/n): ").lower()
            if konfirmasi == 'y':
                tampilkan_data_karyawan()
            else:
                print("Tampilan data dibatalkan.")
                input("\nTekan Enter untuk kembali ke menu utama...")
        elif pilihan == "2":
            tambah_data_karyawan()
        elif pilihan == "3":
            perbarui_data_karyawan()
        elif pilihan == "4":
            hapus_data_karyawan()
        elif pilihan == "5":
            konfirmasi = input("Anda yakin ingin keluar? (y/n): ").lower()
            if konfirmasi == 'y':
                print("Terima kasih!")
                break
            else:
                print("Keluar dari program dibatalkan.")
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
