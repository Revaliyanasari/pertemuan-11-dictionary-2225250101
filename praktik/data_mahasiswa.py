def cari_mahasiswa(data, nim):
    return data.get(nim, "Data tidak ditemukan")


def rata_rata_nilai(data):
    if not data:
        return 0

    total_nilai = sum(mahasiswa["nilai"] for mahasiswa in data.values())
    return total_nilai / len(data)


data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

# Pencarian mahasiswa
print("Hasil pencarian A003:", cari_mahasiswa(data_mahasiswa, "A003"))
print("Hasil pencarian A006:", cari_mahasiswa(data_mahasiswa, "A006"))

# Penambahan mahasiswa
data_mahasiswa["A006"] = {"nama": "Fajar", "kelas": "C", "nilai": 80}

# Pembaruan nilai mahasiswa
data_mahasiswa["A002"]["nilai"] = 82

# Rekap data mahasiswa
print("\nRekap data mahasiswa:")
for nim, mahasiswa in data_mahasiswa.items():
    print(
        f"{nim}: {mahasiswa['nama']}, "
        f"kelas {mahasiswa['kelas']}, nilai {mahasiswa['nilai']}"
    )

print("Jumlah mahasiswa:", len(data_mahasiswa))
print("Rata-rata nilai:", rata_rata_nilai(data_mahasiswa))