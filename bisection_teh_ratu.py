"""
Program Metode Bisection
Kasus: Menentukan titik impas penjualan Teh Ratu G. Obos VI

Fungsi keuntungan:
f(x) = -2x^2 + 150x - 2500

Keterangan:
x    = jumlah gelas Teh Ratu G. Obos VI yang terjual
f(x) = keuntungan
f(x) = 0 berarti kondisi impas / balik modal
"""

def f(x):
    """Fungsi keuntungan penjualan Teh Ratu G. Obos VI."""
    return -2 * x**2 + 150 * x - 2500


def bisection(a, b, epsilon=0.0001, max_iter=100):
    """
    Mencari akar persamaan f(x)=0 menggunakan Metode Bisection.

    Parameter:
    a        : batas bawah
    b        : batas atas
    epsilon  : batas toleransi error
    max_iter : jumlah iterasi maksimum
    """

    if f(a) * f(b) > 0:
        print("Metode Bisection tidak dapat digunakan.")
        print("f(a) dan f(b) harus memiliki tanda yang berbeda.")
        return None

    print("METODE BISECTION - KASUS PENJUALAN TEH RATU G. OBOS VI")
    print("Fungsi: f(x) = -2x^2 + 150x - 2500")
    print("Tujuan: mencari x saat f(x) = 0")
    print()
    print(f"Selang awal: a = {a}, b = {b}")
    print(f"f(a) = {f(a):.6f}")
    print(f"f(b) = {f(b):.6f}")
    print()
    print("Iterasi |      a      |      b      |      c      |     f(c)     |    Error")
    print("-" * 78)

    c_lama = None

    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)

        if c_lama is None:
            error = abs(fc)
        else:
            error = abs(c - c_lama)

        print(f"{i:^7} | {a:^11.6f} | {b:^11.6f} | {c:^11.6f} | {fc:^12.6f} | {error:^9.6f}")

        if abs(fc) < epsilon:
            print("-" * 78)
            print(f"Akar hampiran ditemukan pada iterasi ke-{i}")
            print(f"Jumlah penjualan Teh Ratu G. Obos VI pada kondisi impas = {c:.6f} gelas")
            print(f"Nilai error |f(c)| = {abs(fc):.6f}")
            return c

        if f(a) * fc < 0:
            b = c
        else:
            a = c

        c_lama = c

    print("-" * 78)
    print("Iterasi maksimum tercapai.")
    print(f"Akar hampiran terakhir = {c:.6f}")
    return c


if __name__ == "__main__":
    # Selang awal dipilih karena f(20) bernilai negatif dan f(28) bernilai positif.
    bisection(a=20, b=28, epsilon=0.0001, max_iter=100)
