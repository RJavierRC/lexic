#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext, simpledialog
import os
import platform
from robot_lexical_analyzer import RobotLexicalAnalyzer

class LineNumberText(tk.Frame):
    """Widget de texto con numeración de líneas"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        
        # Crear el widget de números de línea
        self.line_numbers = tk.Text(self, width=4, padx=3, takefocus=0,
                                  relief=tk.SUNKEN, bd=1, state=tk.DISABLED,
                                  font=('Courier', 12), bg='#f0f0f0', fg='#666666')
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)
        
        # Crear el widget de texto principal
        self.text_widget = scrolledtext.ScrolledText(self, font=('Courier', 12), **kwargs)
        self.text_widget.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Vincular eventos
        self.text_widget.bind('<KeyRelease>', self.update_line_numbers)
        self.text_widget.bind('<ButtonRelease-1>', self.update_line_numbers)
        self.text_widget.bind('<MouseWheel>', self.update_line_numbers)
        
        # Inicializar numeración
        self.update_line_numbers()
    
    def update_line_numbers(self, event=None):
        """Actualiza la numeración de líneas"""
        self.line_numbers.config(state=tk.NORMAL)
        self.line_numbers.delete(1.0, tk.END)
        
        # Obtener el número de líneas
        line_count = int(self.text_widget.index(tk.END).split('.')[0]) - 1
        
        # Generar números de línea
        line_numbers_text = '\n'.join(str(i) for i in range(1, line_count + 1))
        self.line_numbers.insert(1.0, line_numbers_text)
        self.line_numbers.config(state=tk.DISABLED)
        
        # Sincronizar scroll
        self.line_numbers.yview_moveto(self.text_widget.yview()[0])
    
    def get(self, start, end=None):
        """Obtiene el texto del widget"""
        return self.text_widget.get(start, end)
    
    def insert(self, index, text):
        """Inserta texto en el widget"""
        self.text_widget.insert(index, text)
        self.update_line_numbers()
    
    def delete(self, start, end=None):
        """Elimina texto del widget"""
        self.text_widget.delete(start, end)
        self.update_line_numbers()

class LexicalAnalyzerGUI:
    """Interfaz gráfica para el analizador léxico"""
    
    def __init__(self):
        # Detectar sistema operativo
        self.is_macos = platform.system() == "Darwin"
        self.is_windows = platform.system() == "Windows"
        self.is_linux = platform.system() == "Linux"
        
        # Crear ventana principal
        self.root = tk.Tk()
        self.root.title("Analizador Léxico para Brazo Robótico")
        self.root.geometry("1200x800")
        self.root.minsize(800, 600)
        
        # Variables
        self.current_file = None
        self.analyzer = RobotLexicalAnalyzer()
        
        # Configurar colores según el sistema
        if self.is_macos:
            self.bg_color = 'white'
            self.root.configure(bg=self.bg_color)
        else:
            self.bg_color = 'SystemButtonFace'
        
        # Crear interfaz
        self.create_interface()
        self.create_menu()
        
        print(f"🚀 Interfaz iniciada en {platform.system()}")
    
    def create_interface(self):
        """Crea la interfaz de usuario"""
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título y botones
        self.create_header(main_frame)
        
        # Panel dividido
        self.create_panels(main_frame)
        
        # Barra de estado
        self.create_status_bar(main_frame)
    
    def create_header(self, parent):
        """Crea el encabezado con título y botones"""
        header_frame = tk.Frame(parent, bg=self.bg_color)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Título
        title_label = tk.Label(header_frame, 
                              text="Analizador Léxico para Brazo Robótico",
                              font=('Arial', 16, 'bold'),
                              bg=self.bg_color)
        title_label.pack(side=tk.LEFT)
        
        # Botones
        button_frame = tk.Frame(header_frame, bg=self.bg_color)
        button_frame.pack(side=tk.RIGHT)
        
        # Botones principales
        tk.Button(button_frame, text="Abrir", command=self.open_file, 
                 font=('Arial', 11), width=8).pack(side=tk.LEFT, padx=2)
        tk.Button(button_frame, text="Guardar", command=self.save_file, 
                 font=('Arial', 11), width=8).pack(side=tk.LEFT, padx=2)
        tk.Button(button_frame, text="Analizar", command=self.analyze_code, 
                 font=('Arial', 11), width=8, bg='lightblue').pack(side=tk.LEFT, padx=2)
        
        # Botón específico por sistema
        if self.is_windows:
            tk.Button(button_frame, text="Generar .EXE", command=self.generate_executable, 
                     font=('Arial', 11), width=12, bg='lightgreen').pack(side=tk.LEFT, padx=2)
        elif self.is_linux:
            tk.Button(button_frame, text="Compilar", command=self.generate_executable, 
                     font=('Arial', 11), width=10, bg='lightgreen').pack(side=tk.LEFT, padx=2)
        else:  # macOS
            tk.Button(button_frame, text="Ver ASM", command=self.show_assembly_only, 
                     font=('Arial', 11), width=10, bg='lightyellow').pack(side=tk.LEFT, padx=2)
        
        tk.Button(button_frame, text="Limpiar", command=self.clear_all, 
                 font=('Arial', 11), width=8).pack(side=tk.LEFT, padx=2)
    
    def create_panels(self, parent):
        """Crea los paneles del editor y resultados"""
        # Panel dividido
        paned = tk.PanedWindow(parent, orient=tk.HORIZONTAL, bg=self.bg_color)
        paned.pack(fill=tk.BOTH, expand=True)
        
        # Panel izquierdo - Editor
        left_frame = tk.LabelFrame(paned, text="Editor de Código", 
                                  font=('Arial', 12, 'bold'))
        paned.add(left_frame, width=600)
        
        # Editor con números de línea
        self.code_editor = LineNumberText(left_frame, wrap=tk.NONE, undo=True)
        self.code_editor.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Panel derecho - Resultados
        right_frame = tk.LabelFrame(paned, text="Resultados del Análisis", 
                                   font=('Arial', 12, 'bold'))
        paned.add(right_frame, width=600)
        
        # Área de salida
        self.output_text = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, 
                                                   font=('Courier', 11), state=tk.DISABLED,
                                                   bg='white', fg='black')
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Configurar colores del editor de salida
        self.output_text.tag_configure("error", foreground="red")
        self.output_text.tag_configure("success", foreground="green")
        self.output_text.tag_configure("info", foreground="blue")
    
    def create_status_bar(self, parent):
        """Crea la barra de estado"""
        status_frame = tk.Frame(parent, bg=self.bg_color)
        status_frame.pack(fill=tk.X, pady=(5, 0))
        
        # Icono y sistema
        system_icon = "🪟" if self.is_windows else "🐧" if self.is_linux else "🍎"
        compile_status = "Compilación disponible" if (self.is_windows or self.is_linux) else "Solo ASM"
        
        self.status_bar = tk.Label(status_frame, 
                                 text=f"Listo | {system_icon} {platform.system()} | {compile_status}",
                                 relief=tk.SUNKEN, font=('Arial', 10),
                                 bg=self.bg_color)
        self.status_bar.pack(fill=tk.X)
    
    def create_menu(self):
        """Crea la barra de menú"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menú Archivo
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Nuevo", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Abrir", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Guardar", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Guardar como", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.quit)
        
        # Menú Análisis
        analysis_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Análisis", menu=analysis_menu)
        analysis_menu.add_command(label="Analizar", command=self.analyze_code, accelerator="F5")
        if self.is_windows or self.is_linux:
            analysis_menu.add_command(label="Generar .EXE", command=self.generate_executable)
        else:
            analysis_menu.add_command(label="Generar ASM", command=self.show_assembly_only)
        analysis_menu.add_command(label="Limpiar", command=self.clear_all)
        
        # Menú Ayuda
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        help_menu.add_command(label="Acerca de", command=self.show_about)
        
        # Atajos de teclado
        self.root.bind('<Control-n>', lambda e: self.new_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<F5>', lambda e: self.analyze_code())
    
    def new_file(self):
        """Crea un nuevo archivo"""
        self.code_editor.delete(1.0, tk.END)
        self.current_file = None
        self.update_title()
        self.update_status("Nuevo archivo creado")
    
    def open_file(self):
        """Abre un archivo"""
        file_path = filedialog.askopenfilename(
            title="Abrir archivo",
            filetypes=[
                ("Archivos Robot", "*.robot"),
                ("Archivos de texto", "*.txt"),
                ("Todos los archivos", "*.*")
            ]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                self.code_editor.delete(1.0, tk.END)
                self.code_editor.insert(1.0, content)
                self.current_file = file_path
                self.update_title()
                self.update_status(f"Archivo abierto: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{str(e)}")
    
    def save_file(self):
        """Guarda el archivo actual"""
        if self.current_file:
            self.save_to_file(self.current_file)
        else:
            self.save_file_as()
    
    def save_file_as(self):
        """Guarda el archivo con un nuevo nombre"""
        file_path = filedialog.asksaveasfilename(
            title="Guardar archivo",
            defaultextension=".robot",
            filetypes=[
                ("Archivos Robot", "*.robot"),
                ("Archivos de texto", "*.txt"),
                ("Todos los archivos", "*.*")
            ]
        )
        
        if file_path:
            self.save_to_file(file_path)
            self.current_file = file_path
            self.update_title()
    
    def save_to_file(self, file_path):
        """Guarda el contenido en el archivo especificado"""
        try:
            content = self.code_editor.get(1.0, tk.END)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            self.update_status(f"Archivo guardado: {os.path.basename(file_path)}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{str(e)}")
    
    def analyze_code(self):
        """Analiza el código del editor"""
        code = self.code_editor.get(1.0, tk.END).strip()
        
        if not code:
            self.update_output("No hay código para analizar.", "error")
            return
        
        self.update_status("Analizando código...")
        
        try:
            # Realizar análisis
            tokens, errors = self.analyzer.analyze(code)
            
            # Generar salida formateada
            output = self.analyzer.get_formatted_output()
            
            # Mostrar resultados
            self.update_output(output, "success" if not errors else "error")
            
            status_msg = f"Análisis completado: {len(tokens)} tokens"
            if errors:
                status_msg += f", {len(errors)} errores"
            self.update_status(status_msg)
            
        except Exception as e:
            self.update_output(f"Error durante el análisis:\n{str(e)}", "error")
            self.update_status("Error en el análisis")
    
    def generate_executable(self):
        """Genera código ensamblador y compila a ejecutable"""
        if self.is_macos:
            messagebox.showinfo("Modo macOS", 
                "En macOS la compilación .EXE no está disponible.\n"
                "Usa el botón 'Ver ASM' para generar código ensamblador.")
            return
        
        code = self.code_editor.get(1.0, tk.END).strip()
        if not code:
            messagebox.showerror("Error", "No hay código para generar ejecutable")
            return
        
        try:
            # Analizar código
            tokens, errors = self.analyzer.analyze(code)
            if errors:
                messagebox.showerror("Error", 
                    f"Errores en el código:\n" + "\n".join(errors[:3]))
                return
            
            # Solicitar nombre
            program_name = simpledialog.askstring(
                "Nombre del Programa", 
                "Ingrese el nombre:",
                initialvalue="robot_program"
            )
            if not program_name:
                return
            
            # Generar y compilar
            self.update_status("Generando ejecutable...")
            success, message = self.analyzer.generate_and_compile(program_name)
            
            if success:
                messagebox.showinfo("Éxito", f"✅ {message}")
                self.update_status(f"Ejecutable {program_name}.exe generado")
            else:
                messagebox.showerror("Error", f"❌ {message}")
                self.update_status("Error al generar ejecutable")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")
            self.update_status("Error en la generación")
    
    def show_assembly_only(self):
        """Genera y muestra código ensamblador"""
        code = self.code_editor.get(1.0, tk.END).strip()
        if not code:
            messagebox.showerror("Error", "No hay código para generar")
            return
        
        try:
            # Analizar código
            tokens, errors = self.analyzer.analyze(code)
            if errors:
                messagebox.showerror("Error", 
                    f"Errores en el código:\n" + "\n".join(errors[:3]))
                return
            
            # Solicitar nombre
            program_name = simpledialog.askstring(
                "Nombre del Programa", 
                "Ingrese el nombre:",
                initialvalue="robot_program"
            )
            if not program_name:
                return
            
            # Generar ASM
            self.update_status("Generando código ensamblador...")
            asm_code, error = self.analyzer.generate_assembly_code(program_name)
            
            if asm_code and not error:
                self.show_assembly_code(asm_code, program_name)
                messagebox.showinfo("Código Generado", 
                    f"✅ Código ensamblador generado\n"
                    f"🍎 Compatible con TASM")
                self.update_status(f"Código {program_name}.asm generado")
            else:
                messagebox.showerror("Error", f"Error: {error}")
                self.update_status("Error en la generación")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")
            self.update_status("Error en la generación")
    
    def show_assembly_code(self, asm_code, program_name):
        """Muestra el código ensamblador en una ventana"""
        asm_window = tk.Toplevel(self.root)
        asm_window.title(f"Código Ensamblador - {program_name}.asm")
        asm_window.geometry("800x600")
        
        # Área de texto
        text_area = scrolledtext.ScrolledText(asm_window, wrap=tk.NONE, 
                                            font=('Courier', 10))
        text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        text_area.insert(1.0, asm_code)
        text_area.config(state=tk.DISABLED)
        
        # Botones
        button_frame = tk.Frame(asm_window)
        button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        def save_asm():
            file_path = filedialog.asksaveasfilename(
                title="Guardar código ensamblador",
                defaultextension=".asm",
                filetypes=[("Archivos ASM", "*.asm"), ("Todos", "*.*")]
            )
            if file_path:
                try:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(asm_code)
                    messagebox.showinfo("Guardado", f"Guardado en:\n{file_path}")
                except Exception as e:
                    messagebox.showerror("Error", f"Error: {str(e)}")
        
        tk.Button(button_frame, text="Guardar", command=save_asm).pack(side=tk.RIGHT, padx=5)
        tk.Button(button_frame, text="Cerrar", command=asm_window.destroy).pack(side=tk.RIGHT)
    
    def clear_all(self):
        """Limpia editor y resultados"""
        result = messagebox.askyesno("Confirmar", "¿Limpiar todo?")
        if result:
            self.code_editor.delete(1.0, tk.END)
            self.update_output("", "info")
            self.update_status("Limpiado")
    
    def update_output(self, text, tag="info"):
        """Actualiza el área de salida"""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(1.0, text, tag)
        self.output_text.config(state=tk.DISABLED)
    
    def update_status(self, message):
        """Actualiza la barra de estado"""
        system_icon = "🪟" if self.is_windows else "🐧" if self.is_linux else "🍎"
        self.status_bar.config(text=f"{message} | {system_icon} {platform.system()}")
    
    def update_title(self):
        """Actualiza el título de la ventana"""
        if self.current_file:
            filename = os.path.basename(self.current_file)
            self.root.title(f"Analizador Léxico - {filename}")
        else:
            self.root.title("Analizador Léxico para Brazo Robótico")
    
    def show_about(self):
        """Muestra información sobre la aplicación"""
        system_info = f"Sistema: {platform.system()}"
        if self.is_macos:
            note = "🍎 macOS: Análisis completo + generación ASM"
        elif self.is_windows:
            note = "🪟 Windows: Todas las funciones disponibles"
        else:
            note = "🐧 Linux: Todas las funciones disponibles"
            
        messagebox.showinfo("Acerca de",
            f"Analizador Léxico para Brazo Robótico\n"
            f"Versión 5.0 - Multiplataforma\n\n"
            f"{system_info}\n"
            f"{note}\n\n"
            f"Funciones:\n"
            f"• Análisis léxico, sintáctico y semántico\n"
            f"• Generación de código intermedio\n"
            f"• Validaciones avanzadas\n"
            f"• Interfaz gráfica intuitiva\n\n"
            f"Sintaxis soportada:\n"
            f"Robot nombre\n"
            f"nombre.componente = valor\n"
            f"nombre.inicio ... nombre.fin")
    
    def run(self):
        """Ejecuta la aplicación"""
        self.root.mainloop()

if __name__ == "__main__":
    try:
        print(f"🚀 Iniciando en {platform.system()}...")
        app = LexicalAnalyzerGUI()
        app.run()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
