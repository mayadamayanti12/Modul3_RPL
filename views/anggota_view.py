import customtkinter as ctk
from tkinter import ttk

class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Perpustakaan - Manajemen Data Anggota")
        self.geometry("900x520")

        # Konfigurasi Grid Utama (1 Baris, 2 Kolom)
        self.grid_columnconfigure(0, weight=1)  # Kolom Kiri (Form)
        self.grid_columnconfigure(1, weight=2)  # Kolom Kanan (Tabel)
        self.grid_rowconfigure(0, weight=1)

        # ==========================================
        # FRAME KIRI: FORMULIR INPUT ANGGOTA
        # ==========================================
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kiri, text="Form Data Anggota", font=("Arial", 16, "bold")).pack(pady=15)

        # 1. Nama Anggota
        ctk.CTkLabel(self.frame_kiri, text="Nama Anggota:", font=("Arial", 12), anchor="w").pack(padx=12, anchor="w")
        self.entry_nama = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Nama Lengkap", font=("Arial", 12), height=32)
        self.entry_nama.pack(pady=(4, 12), padx=12, fill="x")

        # 2. Alamat
        ctk.CTkLabel(self.frame_kiri, text="Alamat:", font=("Arial", 12), anchor="w").pack(padx=12, anchor="w")
        self.text_alamat = ctk.CTkTextbox(self.frame_kiri, font=("Arial", 12), height=100)
        self.text_alamat.pack(pady=(4, 15), padx=12, fill="x")

        # Tombol Simpan Data Saja
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="#28a745", hover_color="#218838", font=("Arial", 13, "bold"), height=35)
        self.btn_simpan.pack(pady=(5, 15), padx=12, fill="x")

        # ==========================================
        # FRAME KANAN: TABEL DAFTAR ANGGOTA
        # ==========================================
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kanan, text="Daftar Anggota Perpustakaan", font=("Arial", 16, "bold")).pack(pady=12)

        # Style untuk Header Tabel (Warna Biru Tua)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview.Heading", font=("Arial", 11, "bold"), background="#1f4e78", foreground="white")
        style.map("Treeview.Heading", background=[('active', '#16365c')])
        style.configure("Treeview", rowheight=30, font=("Arial", 11))

        # Komponen Tabel (Treeview)
        kolom = ("id", "nama", "alamat")
        self.tabel = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=12)

        # Konfigurasi Header Tabel
        self.tabel.heading("id", text="ID Anggota")
        self.tabel.heading("nama", text="Nama Anggota")
        self.tabel.heading("alamat", text="Alamat")

        # Konfigurasi Lebar Kolom
        self.tabel.column("id", width=90, anchor="center")
        self.tabel.column("nama", width=180, anchor="w")
        self.tabel.column("alamat", width=250, anchor="w")

        self.tabel.pack(fill="both", expand=True, padx=12, pady=12)

        # Memuat data spesifik namamu
        self.muat_data_dummy()

    def muat_data_dummy(self):
        for item in self.tabel.get_children():
            self.tabel.delete(item)

        data_dummy = [
            (1, "Putri Damayanti", "Jl. Merpati")
        ]
        for row in data_dummy:
            self.tabel.insert("", "end", values=row)

if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()