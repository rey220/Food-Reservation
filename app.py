import os
from tabulate import tabulate
from src.feature.components.utils.show_menu import show_menu_makanan
from src.feature.components.utils.show_menu import show_menu_minuman


def main() :
    
   os.system("cls" if os.name=="nt" else "clear")
   print()
   print("-"*107)
   print()
   print("="*22,"Selamat Datang di Program Reservasi Menu | Kedai Bakso Jihan ","="*22)
   print("="*20,"Kami menyediakan berbagai hidangan menu bakso dan minuman dingin ","="*20)
   print()
   print("-"*107)
   print()
   print()
   
   print("Feature Layanan Kami : ".center(20))
   print()
   
   menu_kategori = [["1. Lihat Menu"],["2. Lihat rincian pesanan"],["3. Keluar program"]]
   print(tabulate(menu_kategori,tablefmt="fancy_grid"))
   print()

   
def show_feature() :
    
    while True :
    
            input_pilih_menu = int(input("Pilih Opsi : "))
            
            try :
                
                if input_pilih_menu == 1 :
                    
                    print()
                    print("1. Menu Makanan")
                    print("2. Menu Minuman")
                    print()
                    
                    try :
                    
                        input_kategori = int(input("Input no untuk melanjutkan : "))
                        
                        if input_kategori == 1 :
                            
                            os.system("cls" if os.name=="nt" else "clear")
                            show_menu_makanan()
                            break
                            
                        elif input_kategori == 2 :
                            
                            os.system("cls" if os.name=="nt" else "clear")
                            show_menu_minuman()
                            break
    
                        else :
                            
                            print("Input tidak valid. Silahkan input dengan no yang tertera.")
                            print()
                            input("Tekan enter untuk melanjutkan...")
                            continue
    
                    except ValueError :
                        
                        print("Format input tidak valid. Silahkan gunakan format nomer untuk menginput.")
                        input("Tekan enter untuk melanjutkan...")
                        
            except ValueError :
                
                print("Format input tidak valid. Silakhkan inpur dengan format yang sesuai.")
                input("Tekan enter untuk melanjutkan...")
                continue
                         
if __name__ == "__main__" :
    
    main()
    show_feature()
    
    
        
   
   
   
      
   
   