def customer_order_makanan(db) :
    
    while True :
        
        try :
            
            input_menu_pesanan = input("Input nama menu yang akan dipesan : ".capitalize())
            get_data_makanan = None
            
            for makanan in db :
                
                if makanan['nama_menu_makanan'].capitalize() == input_menu_pesanan.capitalize() :
                    
                    get_data_makanan = makanan
                    break
                
            if get_data_makanan != None :
                
                print()
                input_jumlah_pesanan = int(input("Jumlah order : "))
                total_pesanan = input_jumlah_pesanan * makanan['harga']
                print(f"Total pesanan : Rp. {total_pesanan}")
                break
            
            else :
                
                print("Menu tidak ada dalam menu. Silahkan input nama menu yang tertera.")
                input("Tekan enter untuk melanjutkan...")
                continue
            
        except ValueError :
             
            print("Input format tidak valid. Gunakan teks untuk menginput menu. ")
            input("Tekan enter untuk melanjutkan...")
            continue
            
                
def customer_order_minuman(db) :
    
    while True :
        
        try :
            
            input_menu_pesanan = input("Input nama menu yang akan dipesan : ".capitalize())
            get_data_minuman = None
            
            for minuman in db :
                
                if minuman['nama_menu_minuman'].capitalize() == input_menu_pesanan.capitalize() :
                    
                    get_data_minuman = minuman
                    break
                
            if get_data_minuman != None :
                
                print()
                input_jumlah_pesanan = int(input("Jumlah order : "))
                total_pesanan = input_jumlah_pesanan * minuman['harga']
                print(f"Total pesanan : Rp. {total_pesanan}")
                break
            
            else :
                
                print("Menu tidak ada dalam menu. Silahkan input nama menu yang tertera.")
                input("Tekan enter untuk melanjutkan...")
                continue
            
        except ValueError :
             
            print("Input format tidak valid. Gunakan teks untuk menginput menu. ")
            input("Tekan enter untuk melanjutkan...")
            continue
            
                