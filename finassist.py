import sys
import subprocess
import time
import shutil
from colorama import init, Fore, Style

def imdl(mdl):
    subprocess.check_call([sys.executable, "-m", "pip", "install", mdl])

try:
    from colorama import init, Fore, Style
except ImportError:
    print("Modul Colorama belum terinstal. Melakukan instalasi...")
    imdl("colorama")
    from colorama import init, Fore, Style

init()

def lanim():
    for _ in range(10):
        sys.stdout.write('\r' + Fore.YELLOW + "Memuat..." + "|" + "-" * _ + "|")
        sys.stdout.flush()
        time.sleep(0.1)

def cldcf(cshfl, dscrt):
    dcf = sum(cf / (1 + dscrt) ** (i + 1) for i, cf in enumerate(cshfl))
    return dcf

def clfcf(netcsh, capex):
    fcf = netcsh - capex
    return fcf

def clpr(pe, grwth):
    pr = pe / grwth
    return pr

def clazs(A, B, C, D, E):
    zs = 1.2 * A + 1.4 * B + 3.3 * C + 0.6 * D + 1.0 * E
    return zs

def clddm(dps, dr, grwth):
    ddm = dps / (dr - grwth)
    return ddm

algo_info = {
    '1': {
        "name": "Discounted Cash Flow (DCF)",
        "description": "DCF menghitung nilai intrinsik saham berdasarkan arus kas masa depan yang diestimasi, diskonto dengan tingkat pengembalian yang diharapkan (r). Ini memberikan gambaran tentang apa yang seharusnya menjadi harga 'fair' dari suatu saham.",
        "example": "Contoh penggunaan:\nArus kas masa depan: [100, 200, 300, 400, 500]\nTingkat diskonto: 0.1 (misalnya 10%)"
    },
    '2': {
        "name": "Free Cash Flow (FCF)",
        "description": "FCF mengukur seberapa banyak uang tunai yang tersisa setelah perusahaan menghabiskan uang untuk operasi dan investasi. Ini membantu dalam mengevaluasi kemampuan perusahaan untuk menghasilkan uang tunai yang bisa digunakan untuk memperluas bisnis, membayar dividen, atau membayar utang.",
        "example": "Contoh penggunaan:\nArus kas bersih: 1000\nPengeluaran modal: 500"
    },
    '3': {
        "name": "PEG Ratio",
        "description": "PEG ratio membandingkan P/E ratio dengan tingkat pertumbuhan perusahaan. Ini membantu investor menilai apakah saham tersebut dihargai dengan tepat berdasarkan tingkat pertumbuhan perusahaan.",
        "example": "Contoh penggunaan:\nP/E Ratio: 15\nTingkat pertumbuhan: 0.1 (misalnya 10%)"
    },
    '4': {
        "name": "Altman Z-Score",
        "description": "Altman Z-Score digunakan untuk memprediksi kemungkinan kebangkrutan suatu perusahaan dalam waktu tertentu. Semakin tinggi nilai Z-Score, semakin kecil kemungkinan kebangkrutan.",
        "example": "Contoh penggunaan:\nWorking Capital / Total Assets: 1.5\nRetained Earnings / Total Assets: 2.0\nEBIT / Total Assets: 3.0\nMarket Value of Equity / Total Liabilities: 0.8\nRevenue / Total Assets: 1.2"
    },
    '5': {
        "name": "Dividend Discount Model (DDM)",
        "description": "DDM menghitung nilai intrinsik saham berdasarkan dividen yang diharapkan dan tingkat diskonto. Ini berguna untuk menilai saham berdasarkan arus kas yang diharapkan dari dividen.",
        "example": "Contoh penggunaan:\nDividen per saham: 2\nTingkat diskonto DDM: 0.1 (misalnya 10%)\nTingkat pertumbuhan dividen DDM: 0.05 (misalnya 5%)"
    }
}

def dsp_header():
    cols = shutil.get_terminal_size().columns
    print(Fore.CYAN + "╔" + "═" * (cols - 4) + "╗")
    print("║".center(cols))
    print("║" + "  Selamat datang di FinAssist  ".center(cols - 2) + "║")
    print("║" + "  Financial Analysis Assistant  ".center(cols - 2) + "║")
    print("║" + "  Satoribyte © 2024  ".center(cols - 2) + "║")
    print("║".center(cols))
    print(Fore.CYAN + "╚" + "═" * (cols - 4) + "╝")
    print(Style.RESET_ALL)

def chs_algo():
    slctd_algo = input(Fore.YELLOW + "Masukkan nomor algoritma yang ingin Anda gunakan: " + Style.RESET_ALL)
    return slctd_algo

def prc_data():
    print(Fore.YELLOW + "Memproses data...", end="")
    lanim()
    print("\n" + Style.RESET_ALL)

def dsp_result(rslt):
    print(Fore.GREEN + "Hasil perhitungan adalah:", round(rslt, 2))
    print(Style.RESET_ALL)

def prmt_add_input():
    return input(Fore.CYAN + "Apakah Anda ingin menggunakan opsi lain? (y/n): " + Style.RESET_ALL).lower()

def clr_terminal():
    subprocess.run("clear")

def main():
    try:
        clr_terminal()
        dsp_header()

        while True:
            print("Silakan pilih algoritma yang ingin Anda gunakan:")
            for key, value in algo_info.items():
                print(Fore.YELLOW + key + ". " + value["name"])
                print(Style.RESET_ALL)
                print(value["description"])
                print(value["example"])
                print()

            slctd_algo = chs_algo()

            if slctd_algo not in algo_info:
                clr_terminal()
                print(Fore.RED + "Mohon maaf, pilihan tidak valid. Silakan pilih nomor algoritma yang tersedia.")
                print(Style.RESET_ALL)
                continue

            algo_name = algo_info[slctd_algo]["name"]
            algo_desc = algo_info[slctd_algo]["description"]
            print(Fore.YELLOW + algo_name)
            print(Style.RESET_ALL)
            print(algo_desc)
            print()

            prc_data()
            try:
                if slctd_algo == '1':
                    csh_flows = [float(input(Fore.CYAN + "Masukkan arus kas untuk tahun ke-{}: ".format(i+1) + Style.RESET_ALL)) for i in range(5)]
                    dscrt_rate = float(input(Fore.CYAN + "Masukkan tingkat diskonto (misalnya 0.1 untuk 10%): " + Style.RESET_ALL))
                    rslt = cldcf(csh_flows, dscrt_rate)
                    dsp_result(rslt)

                elif slctd_algo == '2':
                    net_cf = float(input(Fore.CYAN + "Masukkan arus kas bersih: " + Style.RESET_ALL))
                    cap_exp = float(input(Fore.CYAN + "Masukkan pengeluaran modal: " + Style.RESET_ALL))
                    rslt = clfcf(net_cf, cap_exp)
                    dsp_result(rslt)

                elif slctd_algo == '3':
                    pe_r = float(input(Fore.CYAN + "Masukkan Price/Earnings Ratio: " + Style.RESET_ALL))
                    grwth_r = float(input(Fore.CYAN + "Masukkan tingkat pertumbuhan (misalnya 0.1 untuk 10%): " + Style.RESET_ALL))
                    rslt = clpr(pe_r, grwth_r)
                    dsp_result(rslt)

                elif slctd_algo == '4':
                    A = float(input(Fore.CYAN + "Masukkan Working Capital / Total Assets: " + Style.RESET_ALL))
                    B = float(input(Fore.CYAN + "Masukkan Retained Earnings / Total Assets: " + Style.RESET_ALL))
                    C = float(input(Fore.CYAN + "Masukkan Earnings Before Interest and Taxes (EBIT) / Total Assets: " + Style.RESET_ALL))
                    D = float(input(Fore.CYAN + "Masukkan Market Value of Equity / Total Liabilities: " + Style.RESET_ALL))
                    E = float(input(Fore.CYAN + "Masukkan Revenue / Total Assets: " + Style.RESET_ALL))
                    rslt = clazs(A, B, C, D, E)
                    dsp_result(rslt)

                elif slctd_algo == '5':
                    dps = float(input(Fore.CYAN + "Masukkan dividen per saham: " + Style.RESET_ALL))
                    dr_ddm = float(input(Fore.CYAN + "Masukkan tingkat diskonto DDM (misalnya 0.1 untuk 10%): " + Style.RESET_ALL))
                    grwth_ddm = float(input(Fore.CYAN + "Masukkan tingkat pertumbuhan dividen DDM (misalnya 0.05 untuk 5%): " + Style.RESET_ALL))
                    rslt = clddm(dps, dr_ddm, grwth_ddm)
                    dsp_result(rslt)
            except ValueError:
                clr_terminal()
                print(Fore.RED + "Terjadi kesalahan! Mohon pastikan Anda memasukkan angka yang valid." + Style.RESET_ALL)
                continue

            add_input = prmt_add_input()
            if add_input == 'y':
                clr_terminal()
                continue
            else:
                clr_terminal()
                print(Fore.CYAN + "Terima kasih telah menggunakan FinAssist. Sampai jumpa!" + Style.RESET_ALL)
                break
    except KeyboardInterrupt:
        clr_terminal()
        sys.exit()

if __name__ == "__main__":
    main()
