import tkinter as tk
from codificacion import codifcarCodigo

def interfaz():
    ventana = tk.Tk()
    ventana.title("Ventana con TextField")
    
    ventana.state("zoomed")
    
    ventana.config(bg="#f0f0f0")

    frame_superior = tk.Frame(ventana, bg="#f0f0f0")
    frame_superior.pack(fill="both", expand=True)

    text_field = tk.Text(frame_superior, font=("Arial", 12), wrap="word", borderwidth=2, relief="solid")
    text_field.pack(expand=True, fill="both", padx=20, pady=20)

    frame_inferior = tk.Frame(ventana, bg="#f0f0f0")
    frame_inferior.pack(fill="both", expand=True)

    resultado = tk.Text(frame_inferior, font=("Arial", 10), wrap="word", borderwidth=2, relief="solid", height=10)
    resultado.pack(expand=True, fill="both", padx=20, pady=10)

    def mostrar_texto():
        
        resultado.config(state="normal")  
        resultado.delete("1.0", "end")  

        texto = text_field.get("1.0", "end-1c")  
        ejecucion, errores = codifcarCodigo(texto)  
        

        if ejecucion:
            resultado.config(state="normal") 
            
            for linea in ejecucion:
                resultado.insert("end", f"Tokens: {linea[0]}\n")
                resultado.insert("end", f"AST: {linea[1]}\n")
                resultado.insert("end", f"Resultado: {linea[2]}\n")
                resultado.insert("end", f"Código MIPS:\n{linea[3]}\n")
                resultado.insert("end", "-" * 40 + "\n")
                
            resultado.config(state="disabled")
        elif errores:
            resultado.insert("end", "Errores:\n")
            for error in errores:
                resultado.insert("end", f"{error}\n")
        else:
            resultado.insert("end", "No se generaron resultados.\n")
            resultado.config(state="disabled")

    boton = tk.Button(frame_inferior, text="Ejecutar", font=("Arial", 12), command=mostrar_texto,
                      bg="#4CAF50", fg="white", activebackground="#45a049", activeforeground="white",
                      borderwidth=0, padx=10, pady=5)
    boton.pack(pady=10)

    ventana.mainloop()
    
if __name__ == "__main__":
    interfaz()
