# Paru — “Emboli-AI CTPA: Deteksi & Stratifikasi Risiko PE dalam 5 Menit”

## Pertanyaan Klinis (PICO)

### **P — Population**
Pasien IGD atau rawat inap dengan **kecurigaan emboli paru (PE)** yang menjalani pemeriksaan **CT Pulmonary Angiography (CTPA)**.

### **I — Intervention**
Sistem **AI multimodal** yang menggabungkan:
1. Analisis citra **CTPA** untuk deteksi PE (lokasi, burden trombus, indikator RV strain), dan
2. Ringkasan data **EHR** terstruktur (tanda vital, saturasi oksigen, troponin, BNP),

untuk menghasilkan:
- klasifikasi **PE positif/negatif**, dan
- stratifikasi risiko cepat: **massive / submassive / low-risk**

dengan target waktu keluaran **≤5 menit** dari studi CTPA tersedia.

### **C — Comparator**
Alur standar rumah sakit:
- pembacaan radiologi konvensional, dan
- penilaian klinis oleh dokter (tanpa dukungan model AI multimodal).

### **O — Outcomes**
**Outcome utama**
- Waktu dari CTPA selesai ke keputusan terapi definitif:
  - inisiasi antikoagulasi, atau
  - trombolisis/intervensi reperfusi bila diindikasikan.

**Outcome sekunder**
- **Miss rate PE** (kasus PE terlewat pada evaluasi awal),
- **Transfer ICU** dalam episode perawatan yang sama,
- **Mortalitas 30 hari**.

---

## Definisi Operasional Singkat

- **Massive PE**: PE dengan ketidakstabilan hemodinamik/shock.
- **Submassive PE**: hemodinamik stabil namun dengan bukti disfungsi ventrikel kanan dan/atau biomarker jantung meningkat.
- **Low-risk PE**: tanpa hipotensi, tanpa bukti RV strain bermakna, biomarker tidak meningkat.

> Catatan: definisi akhir mengikuti protokol lokal (mis. ESC/AHA) agar konsisten dengan praktik klinis setempat.

## Rancangan Evaluasi yang Disarankan

- **Desain**: studi implementasi pragmatis (before-after atau stepped-wedge).
- **Populasi analisis**: seluruh pasien dengan indikasi CTPA karena suspek PE.
- **Analisis utama**:
  - perbandingan median waktu-ke-terapi (AI vs standar),
  - adjusted analysis untuk keparahan awal pasien (mis. NEWS2, komorbid, setting IGD vs rawat inap).
- **Keluaran model yang dicatat**:
  - probabilitas PE,
  - kelas risiko,
  - penanda explainability (contoh: lokasi filling defect utama + fitur klinis dominan yang mendorong kelas risiko).

## Kriteria Keberhasilan Implementasi (Contoh)

- Penurunan bermakna waktu-ke-antikoagulasi/trombolisis.
- Tidak ada peningkatan false negative bermakna secara klinis.
- Penurunan transfer ICU dan/atau mortalitas 30 hari pada analisis tersesuaikan.
