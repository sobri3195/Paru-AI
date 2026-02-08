# Emboli-AI CTPA Prototype

Prototype kode untuk deteksi emboli paru (PE) dan stratifikasi risiko cepat berbasis:
- temuan CTPA terstruktur, dan
- ringkasan EHR (vital signs, saturasi, troponin, BNP).

## Fitur
- Klasifikasi PE: `positive` / `negative`
- Stratifikasi risiko: `massive` / `submassive` / `low`
- Penjelasan keputusan (fitur dominan)

## Menjalankan CLI
```bash
python -m emboli_ai.cli --input sample_input.json
```

## Menjalankan test
```bash
pytest -q
```
