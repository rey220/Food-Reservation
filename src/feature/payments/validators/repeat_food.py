import os
from src.feature.components.utils.show_menu import show_menu_makanan
from src.resources.storage import data_pesanan

def repeat_order_makanan(data,db,nama_pemesan) :
    
    while True :
        
        try :
            
            if data == "Y" :
                
                os.system("cls" if os.name=="nt" else "clear" )
                show_menu_makanan()
                print()
                
                input_menu_makanan_tambahan = input("Input nama menu yang akan dipesan : ".capitalize())
                get_data_makanan = None
                get_harga_makanan_tambahan = None
                
                for item in db :
                    
                    if item['nama_menu_makanan'].capitalize() == input_menu_makanan_tambahan.capitalize() :
                        
                        get_data_makanan = item
                        get_harga_makanan_tambahan = item["harga"]
                        # break   
                
                if get_data_makanan != None :
                    
                    print()
                    input_jumlah_pesanan_tambahan = int(input("Jumlah order : "))
                    total_pesanan_tambahan = input_jumlah_pesanan_tambahan * get_harga_makanan_tambahan
                    print(f"Total pesanan : Rp. {total_pesanan_tambahan}")
                    
                    pesanan_repeat_order = {
                            "nama_pemesan" : nama_pemesan,
                            "menu" : input_menu_makanan_tambahan,
                            "jumlah" : input_jumlah_pesanan_tambahan,
                            "total" : total_pesanan_tambahan,
                            "harga" : get_harga_makanan_tambahan
                            
                        }
                        
                    data_pesanan.append(pesanan_repeat_order)  
                    break 
            
            elif data == "N" :
                
                print()
                os.system("cls" if os.name =="nt" else "clear")
                print("Terimakasih telah memesan makanan di kedai kami 🙏😄🙏")
                print("Silahkan tekan enter untuk kembali ke menu utama")
                print()
                input("Tekan enter untuk melanjutkan...")
                break
            
        except ValueError :
            
            print("Format input tidak valid. Silahkan gunakan format teks untuk menginput. ")
            input("Tekan enter untuk melanjutkan...")
            continue     
                
      
                
        
        
        
    