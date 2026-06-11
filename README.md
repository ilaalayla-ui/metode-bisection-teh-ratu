# Menentukan Titik Impas Penjualan Teh Ratu G. Obos VI Menggunakan Metode Bisection

Repositori ini berisi program Metode Bisection/Bagi Dua untuk menentukan titik impas penjualan pada usaha Teh Ratu G. Obos VI. Titik impas adalah kondisi ketika keuntungan sama dengan nol, sehingga usaha tidak mengalami kerugian maupun keuntungan.

## 1. Deskripsi Kasus

Teh Ratu G. Obos VI merupakan usaha minuman yang menjual produk teh kepada konsumen. Dalam kegiatan penjualan, pemilik usaha perlu mengetahui jumlah minimum produk yang harus terjual agar tidak mengalami kerugian.

Masalah tersebut dimodelkan ke dalam fungsi keuntungan non-linear:

```math
f(x) = -2x^2 + 150x - 2500
```

Keterangan:

- `x` = jumlah gelas Teh Ratu G. Obos VI yang terjual
- `f(x)` = keuntungan
- `f(x) > 0` = usaha memperoleh keuntungan
- `f(x) < 0` = usaha mengalami kerugian
- `f(x) = 0` = kondisi impas atau balik modal

Fungsi tersebut termasuk persamaan non-linear karena terdapat variabel berpangkat dua, yaitu `x^2`.

## 2. Metode yang Digunakan

Metode yang digunakan adalah Metode Bisection atau Metode Bagi Dua. Metode ini digunakan untuk mencari akar persamaan dalam bentuk:

```math
f(x) = 0
```

Rumus titik tengah:

```math
c = (a+b)/2
```

Syarat awal Metode Bisection:

```math
f(a) x f(b) < 0
```

Artinya, nilai fungsi pada batas bawah dan batas atas harus memiliki tanda yang berbeda.

## 3. Selang Awal

Pada program ini digunakan selang awal:

```math
a = 20
b = 28
```

Cek nilai fungsi:

```math
f(20) = -300
f(28) = 132
```

Karena nilai `f(20)` negatif dan `f(28)` positif, maka akar berada di antara 20 dan 28.

## 4. Perhitungan Manual Singkat

Iterasi 1:

```math
c = (20+28)/2 = 24
f(24) = -52
```

Iterasi 2:

```math
c = (24+28)/2 = 26
f(26) = 48
```

Iterasi 3:

```math
c = (24+26)/2 = 25
f(25) = 0
```

Karena `f(25) = 0`, maka nilai akar yang diperoleh adalah `x = 25`.

## 5. Cara Menjalankan Program

Jalankan program dengan perintah:

```bash
python bisection_teh_ratu.py
```

Program juga dapat dijalankan menggunakan VS Code, Google Colab, Replit, atau compiler Python online.

## 6. Hasil Program

Berdasarkan hasil program, diperoleh:

```math
x = 25
```

Artinya, Teh Ratu G. Obos VI perlu menjual sekitar 25 gelas agar mencapai kondisi impas atau balik modal.

Nilai error dihitung menggunakan:

```math
Error = |f(c)|
```

Pada hasil akhir:

```math
Error = |f(25)| = 0
```

## 7. Kesimpulan

Metode Bisection berhasil digunakan untuk menentukan titik impas penjualan Teh Ratu G. Obos VI. Berdasarkan hasil perhitungan manual dan program Python, jumlah penjualan yang diperlukan agar mencapai kondisi impas adalah sekitar 25 gelas.
