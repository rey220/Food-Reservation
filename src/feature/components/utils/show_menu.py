from src.feature.components.makanan import show_daftar_makanan
from src.feature.components.minuman import show_daftar_minuman
from src.resources.db_makanan import db_menu_makanan
from src.resources.db_minuman import db_menu_minuman
from src.feature.payments.order import customer_order_makanan
from src.feature.payments.order import customer_order_minuman
from tabulate import tabulate

def show_menu_makanan() :
    
    get_menu_makanan = show_daftar_makanan()
    print("DAFTAR MENU MAKANAN : ")
    
    print()
    title = ["Nama Menu","Harga(Rp)"]
    print(tabulate(get_menu_makanan,title,"fancy_grid"))
    
    print()
    get_db_makanan = db_menu_makanan()
    customer_order_makanan(get_db_makanan)
    return
    
def show_menu_minuman() :
    
    get_menu_minuman = show_daftar_minuman()
    print("DAFTAR MENU MINUMAN : ")
    
    print()
    title = ["Nama Menu","Harga(Rp)"]
    print(tabulate(get_menu_minuman,title,"fancy_grid"))
    
    print()
    get_db_minuman = db_menu_minuman()
    customer_order_minuman(get_db_minuman)
    