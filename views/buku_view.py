import customtkinter as ctk
from tkinter import ttk

class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("900x500")
        self.resizable(False, False)
        
        # Konfigurasi tema
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        
        # Frame Kiri (Form Input)
        self.frame_left = ctk.CTkFrame(self, width=350, corner_radius=0)
        self.frame_left.pack(side="left", fill="y", padx=10, pady=10)
        
        self.label_form = ctk.CTkLabel(self.frame_left, text="Form Input Buku", font=("Arial", 16, "bold"))
        self.label_form.pack(pady=20)
        
        # Input Judul Buku
        self.label_judul = ctk.CTkLabel(self.frame_left, text="Judul Buku:", anchor="w")
        self.label_judul.pack(fill="x", padx=20, pady=(5, 0))
        self.entry_judul = ctk.CTkEntry(self.frame_left, placeholder_text="Masukkan Judul Buku")
        self.entry_judul.pack(fill="x", padx=20, pady=5)
        
        # Input Penulis
        self.label_penulis = ctk.CTkLabel(self.frame_left, text="Penulis:", anchor="w")
        self.label_penulis.pack(fill="x", padx=20, pady=(5, 0))
        self.entry_penulis = ctk.CTkEntry(self.frame_left, placeholder_text="Masukkan Nama Penulis")
        self.entry_penulis.pack(fill="x", padx=20, pady=5)
        
        # Input Tahun Terbit
        self.label_tahun = ctk.CTkLabel(self.frame_left, text="Tahun Terbit:", anchor="w")
        self.label_tahun.pack(fill="x", padx=20, pady=(5, 0))
        self.entry_tahun = ctk.CTkEntry(self.frame_left, placeholder_text="Contoh: 2024")
        self.entry_tahun.pack(fill="x", padx=20, pady=5)
        
        # Tombol Simpan Data (Hanya 1 tombol hijau)
        self.btn_simpan = ctk.CTkButton(
            self.frame_left, 
            text="Simpan Data", 
            fg_color="green", 
            hover_color="darkgreen"
        )
        self.btn_simpan.pack(pady=20, padx=20, fill="x")
        
        # Frame Kanan (Tabel Data Buku)
        self.frame_right = ctk.CTkFrame(self, corner_radius=10)
        self.frame_right.pack(side="right", expand=True, fill="both", padx=10, pady=10)
        
        self.label_tabel = ctk.CTkLabel(self.frame_right, text="Daftar Koleksi Buku", font=("Arial", 16, "bold"))
        self.label_tabel.pack(pady=20)
        
        # Setup Treeview (Tabel)
        columns = ("id", "judul", "penulis", "tahun")
        self.tabel = ttk.Treeview(self.frame_right, columns=columns, show="headings")
        
        self.tabel.heading("id", text="ID Buku")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun Terbit")
        
        self.tabel.column("id", width=60, anchor="center")
        self.tabel.column("judul", width=220, anchor="w")
        self.tabel.column("penulis", width=180, anchor="w")
        self.tabel.column("tahun", width=90, anchor="center")
        
        self.tabel.pack(expand=True, fill="both", padx=20, pady=10)