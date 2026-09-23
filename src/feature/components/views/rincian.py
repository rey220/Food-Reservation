from tabulate import tabulate

def show_rincian(makanan) : 
    
    while True :
        
        try :
        
            print()
            nama_pemesan = input("Input nama pemesan : ").capitalize()
            get_data = []
            
            for item in makanan :
                
                if item['nama_pemesan'].capitalize() == nama_pemesan.capitalize() :
                    
                    get_data.append(item)
            
            if len(get_data) == 0 :
                
                print("Nama pemesan tidak ada.")
                input("Tekan enter untuk kembali...")
                return
            
            print()
            print(f"RINCIAN PESANAN ATAS NAMA : {nama_pemesan.upper()} ")
            print()
            
            table_rows = []
            total_keseluruhan = 0                            
            for i in get_data  :
                
                total_per_menu = i["jumlah"] * i["harga"]
                total_keseluruhan += total_per_menu
                        
                table_rows.append([i["menu"].capitalize(),
                                  i["jumlah"],
                                  f"Rp. {i["harga"]}",
                                  f"Rp. {total_per_menu}"])

            judul = ["Nama Menu","Jumlah","Harga Satuan","Subtotal"]
            print(tabulate(table_rows,judul,"fancy_grid"))

            print()
            print(f"TOTAL KESELURUHAN: Rp. {total_keseluruhan}")
            print()
            print("-"*70)
            
            return
         
        except ValueError :
            
            print("Format input tidak valid. Gunakan 'huruf' saat menginput")
            input("Tekan enter untuk melanjutkan...")
            continue
        
        
        
        
    
    