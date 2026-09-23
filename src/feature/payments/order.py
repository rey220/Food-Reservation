from src.resources.db_makanan import db_menu_makanan
from src.resources.db_minuman import db_menu_minuman
from src.feature.payments.validators.repeat_drink import repeat_order_minuman
from src.feature.payments.validators.repeat_food import repeat_order_makanan
from src.resources.storage import data_pesanan

def customer_order_makanan(db) :
    
    while True :
        
        try :
            
            print()
            
            print()
            input_menu_pesanan = input("Input nama menu yang akan dipesan : ".capitalize())
            get_data_makanan = None
            get_harga_makanan = None
            
            for makanan in db :
                
                if makanan['nama_menu_makanan'].capitalize() == input_menu_pesanan.capitalize() :
                    
                    get_data_makanan = makanan
                    get_harga_makanan = makanan["harga"]
                    # break
                
            if get_data_makanan != None :
                
                print()
                input_jumlah_pesanan = int(input("Jumlah order : "))
                total_pesanan = input_jumlah_pesanan * get_harga_makanan
                print(f"Total pesanan : Rp. {total_pesanan}")
                
                print()
                input_nama_pemesan = input("Nama Pemesan : ").capitalize()
                print()
                
                data_pesanan_makanan = {
                    "nama_pemesan" : input_nama_pemesan,
                    "menu" : input_menu_pesanan,
                    "jumlah" : input_jumlah_pesanan,
                    "total" : total_pesanan,
                    "harga" : get_harga_makanan
                }
                
                data_pesanan.append(data_pesanan_makanan)
                break
            
            else :
                
                print("Menu tidak ada dalam menu. Silahkan input nama menu yang tertera.")
                input("Tekan enter untuk melanjutkan...")
                continue
            
            
        except ValueError :
             
            print("Input format tidak valid. Gunakan teks untuk menginput menu. ")
            input("Tekan enter untuk melanjutkan...")
            continue
        
    print()
    
    while True :
        
        input_repeat_order_makanan = input("Pesan menu kembali ? (Y/N) : ").capitalize()
        
        if input_repeat_order_makanan == "Y" :
            
            repeat_order_makanan(input_repeat_order_makanan,db_menu_makanan(),input_nama_pemesan)
            continue
        
        elif input_repeat_order_makanan == "N" :
            
            repeat_order_makanan(input_repeat_order_makanan,db_menu_makanan(),input_nama_pemesan)
            break
        
        else : 
                        
            print("Input tidak valid. Gunakan Y/N untuk menginput.")
            input("Tekan enter untuk melanjutkan...")
            continue
    
    
def customer_order_minuman(db) :
    
    while True :
        
        try :
            
            print()
            input_menu_pesanan = input("Input nama menu yang akan dipesan : ".capitalize())
            get_data_minuman = None
            get_harga_minuman = None
            
            for minuman in db :
                
                if minuman['nama_menu_minuman'].capitalize() == input_menu_pesanan.capitalize() :
                    
                    get_data_minuman = minuman
                    get_harga_minuman = minuman["harga"]
                    # break
                
            if get_data_minuman != None :
                
                print()
                input_jumlah_pesanan = int(input("Jumlah order : "))
                total_pesanan = input_jumlah_pesanan * minuman['harga']
                print(f"Total pesanan : Rp. {total_pesanan}")
                input_nama_pemesan = input("Nama Pemesan : ").capitalize()
                break
            
            else :
                
                print("Menu tidak ada dalam menu. Silahkan input nama menu yang tertera.")
                input("Tekan enter untuk melanjutkan...")
                continue
            
        except ValueError :
             
            print("Input format tidak valid. Gunakan teks untuk menginput menu. ")
            input("Tekan enter untuk melanjutkan...")
            continue
        
    data_pesanan_minuman = {
        
        "nama_pemesan" : input_nama_pemesan,
        "menu" : input_menu_pesanan,
        "jumlah" : input_jumlah_pesanan,
        "total" : total_pesanan,
        "harga" : get_harga_minuman
    }
    
    data_pesanan.append(data_pesanan_minuman)
            
    while True :
        
        input_repeat_order_minuman = input("Pesan menu kembali ? (Y/N) : ").capitalize()
        
        if input_repeat_order_minuman == "Y" :
            
            repeat_order_minuman(input_repeat_order_minuman,db_menu_minuman(),input_nama_pemesan)
            continue
        
        elif input_repeat_order_minuman == "N" :
            
            repeat_order_minuman(input_repeat_order_minuman,db_menu_minuman(),input_nama_pemesan)
            break
        
        else : 
                        
            print("Input tidak valid. Gunakan Y/N untuk menginput.")
            input("Tekan enter untuk melanjutkan...")
            continue
                    
