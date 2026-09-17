import os
from src.feature.components.utils.show_menu import show_menu_makanan
from src.feature.components.utils.show_menu import show_menu_minuman
# from src.feature.payments.order import customer_order_makanan

def repeat_order_makanan(data,db) :
    
    while True :
        
        try :
        
            if data == "Y" :
                
                os.system("cls" if os.name=="nt" else "clear" )
                show_menu_makanan()
                print()
                input_menu_makanan = input("Input nama menu yang akan dipesan : ".capitalize())
                get_data_makanan = None
                
                for item in db :
                    
                    if item['nama_menu_makanan'].capitalize() == input_menu_makanan.capitalize() :
                        
                        get_data_makanan = item
                        break
                    
                if get_data_makanan != None :
                    
                    print()
                    input_jumlah_pesanan = int(input("Jumlah order : "))
                    total_pesanan = input_jumlah_pesanan * item['harga']
                    print(f"Total pesanan : Rp. {total_pesanan}")
                    
                break   
    
            elif data == "N" :
                
                print()
                os.system("cls" if os.name =="nt" else "clear")
                print("Terimakasih telah memesan makanan di kedai kami 🙏😄🙏")
                print("Silahkan tekan enter untuk kembali ke menu utama")
                print()
                input("Tekan enter untuk melanjutkan...")
                return
            
        except ValueError :
            
            print("Format input tidak valid. Silahkan gunakan format teks untuk menginput. ")
            input("Tekan enter untuk melanjutkan...")
                
def repeat_order_minuman(data,db) :
    
    while True :
        
        try :
        
            if data == "Y" :
                
                os.system("cls" if os.name=="nt" else "clear" )
                show_menu_minuman()
                print()
                input_menu_makanan = input("Input nama menu yang akan dipesan : ".capitalize())
                get_data_minuman = None
                
                for item in db :
                    
                    if item['nama_menu_minuman'].capitalize() == input_menu_makanan.capitalize() :
                        
                        get_data_minuman = item
                        break
                    
                if get_data_minuman != None :
                    
                    print()
                    input_jumlah_pesanan = int(input("Jumlah order : "))
                    total_pesanan = input_jumlah_pesanan * item['harga']
                    print(f"Total pesanan : Rp. {total_pesanan}")
                
                break
                
            elif data == "N" :
                
                print()
                os.system("cls" if os.name =="nt" else "clear")
                print("Terimakasih telah memesan makanan di kedai kami 🙏😄🙏")
                print("Silahkan tekan enter untuk kembali ke menu utama")
                input("Tekan enter untuk melanjutkan...")
                break
            
            else : 
                
                print("Input tidak valid. Gunakan Y/N untuk menginput.")
                input("Tekan enter untuk melanjutkan...")
                continue
            
        except ValueError :
            
            print("Format input tidak valid. Silahkan gunakan format teks untuk menginput. ")
            input("Tekan enter untuk melanjutkan...")
                
                
        
        
        
    