from src.feature.menu.makanan import show_daftar_makanan
from src.feature.menu.minuman import show_daftar_minuman
from tabulate import tabulate

def show_menu_makanan() :
    
    get_menu_makanan = show_daftar_makanan()
    print("DAFTAR MENU MAKANAN : ")
    
    print()
    title = ["Nama Menu","Harga(Rp)"]
    print(tabulate(get_menu_makanan,title,"fancy_grid"))
    
    
def show_menu_minuman() :
    
    get_menu_minuman = show_daftar_minuman()
    print("DAFTAR MENU MINUMAN : ")
    
    print()
    title = ["Nama Menu","Harga(Rp)"]
    print(tabulate(get_menu_minuman,title,"fancy_grid"))