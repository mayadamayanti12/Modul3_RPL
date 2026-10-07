import customtkinter as ctk
from tkinter import ttk

class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Perpustakaan - Manajemen Data Buku")
        self.geometry("900x480")  # Ukuran jendela diperkecil jadi pas

        # Konfigurasi Grid Utama (1 Baris, 2 Kolom)
        self.grid_columnconfigure(0, weight=1)  # Kolom Kiri (Form)
        self.grid_columnconfigure(1, weight=2)  # Kolom Kanan (Tabel)
        self.grid_rowconfigure(0, weight=1)

        # ==========================================
        # FRAME KIRI: FORMULIR INPUT BUKU
        # ==========================================
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kiri, text="Form Input Buku", font=("Arial", 16, "bold")).pack(pady=12)

        # 1. Judul Buku
        ctk.CTkLabel(self.frame_kiri, text="Judul Buku:", font=("Arial", 12, "bold"), anchor="w").pack(padx=12, anchor="w")
        self.entry_judul = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Judul Buku", font=("Arial", 12), height=32)
        self.entry_judul.pack(pady=(4, 10), padx=12, fill="x")

        # 2. Penulis
        ctk.CTkLabel(self.frame_kiri, text="Penulis:", font=("Arial", 12, "bold"), anchor="w").pack(padx=12, anchor="w")
        self.entry_penulis = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Nama Penulis", font=("Arial", 12), height=32)
        self.entry_penulis.pack(pady=(4, 10), padx=12, fill="x")

        # 3. Tahun Terbit
        ctk.CTkLabel(self.frame_kiri, text="Tahun Terbit:", font=("Arial", 12, "bold"), anchor="w").pack(padx=12, anchor="w")
        self.entry_tahun = ctk.CTkEntry(self.frame_kiri, placeholder_text="Contoh: 2024", font=("Arial", 12), height=32)
        self.entry_tahun.pack(pady=(4, 10), padx=12, fill="x")

        # Tombol Aksi
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green", font=("Arial", 13, "bold"), height=35)
        self.btn_simpan.pack(pady=(12, 8), padx=12, fill="x")

        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Perbarui Data (Update)", fg_color="blue", font=("Arial", 13, "bold"), height=35)
        self.btn_update.pack(pady=5, padx=12, fill="x")

        self.btn_delete = ctk.CTkButton(self.frame_kiri, text="Hapus Data (Delete)", fg_color="red", font=("Arial", 13, "bold"), height=35)
        self.btn_delete.pack(pady=5, padx=12, fill="x")

        # ==========================================
        # FRAME KANAN: TABEL DAFTAR BUKU
        # ==========================================
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kanan, text="Daftar Koleksi Buku", font=("Arial", 16, "bold")).pack(pady=12)

        # Style untuk Header Tabel
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        style.configure("Treeview", rowheight=32)

        # Komponen Tabel (Treeview)
        kolom = ("id", "judul", "penulis", "tahun")
        self.tabel = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=12)

        # Konfigurasi Header Tabel
        self.tabel.heading("id", text="ID Buku")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun Terbit")

        # Konfigurasi Lebar Kolom
        self.tabel.column("id", width=65, anchor="center")
        self.tabel.column("judul", width=220)
        self.tabel.column("penulis", width=170)
        self.tabel.column("tahun", width=95, anchor="center")

        # Tag Font Bold untuk Isi Tabel
        self.tabel.tag_configure("bold_row", font=("Arial", 12, "bold"))

        self.tabel.pack(fill="both", expand=True, padx=12, pady=12)

        # Masukkan Data Dummy
        self.muat_data_dummy()

    def muat_data_dummy(self):
        for item in self.tabel.get_children():
            self.tabel.delete(item)

        data_dummy = [
            (1, "Bandung After Rain", "Wulan Nur Amalia", 2024)
        ]
        for row in data_dummy:
            self.tabel.insert("", "end", values=row, tags=("bold_row",))

# Blok eksekusi untuk menguji tampilan grafis
if __name__ == "__main__":
    app = BukuView()
    app.mainloop()