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
    """Interfaz gráfica para el analizador léxico - Optimizada para Windows"""
    
    def __init__(self):
        # Configuración específica para Windows
        self.is_windows = True  # Forzar modo Windows
        self.is_macos = False
        self.is_linux = False
        
        # Crear ventana principal
        self.root = tk.Tk()
        self.root.title("Analizador Léxico para Brazo Robótico - Windows Edition")
        self.root.geometry("1200x800")
        self.root.minsize(800, 600)
        
        # Configurar para Windows
        self.root.state('zoomed') if platform.system() == "Windows" else None
        
        # Variables
        self.current_file = None
        self.analyzer = RobotLexicalAnalyzer()
        
        # Configurar rutas para Windows
        self.dosbox_path = os.path.join(os.getcwd(), "DOSBox2")
        self.tasm_path = os.path.join(self.dosbox_path, "Tasm")
        
        # Colores para Windows
        self.bg_color = 'SystemButtonFace'
        
        # Crear interfaz
        self.create_interface()
        self.create_menu()
        
        print(f"Analizador iniciado en modo Windows - Compilación .EXE disponible")
    
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
        """Crea el encabezado con título y botones - Optimizado para Windows"""
        header_frame = tk.Frame(parent, bg=self.bg_color)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Título profesional
        title_label = tk.Label(header_frame, 
                              text="Analizador Léxico para Brazo Robótico - Windows Edition",
                              font=('Arial', 16, 'bold'),
                              bg=self.bg_color, fg='darkblue')
        title_label.pack(side=tk.LEFT)
        
        # Botones optimizados para Windows
        button_frame = tk.Frame(header_frame, bg=self.bg_color)
        button_frame.pack(side=tk.RIGHT)
        
        # Botones principales con estilos profesionales
        tk.Button(button_frame, text="Abrir", command=self.open_file, 
                 font=('Arial', 11), width=10, relief='raised').pack(side=tk.LEFT, padx=3)
        tk.Button(button_frame, text="Guardar", command=self.save_file, 
                 font=('Arial', 11), width=10, relief='raised').pack(side=tk.LEFT, padx=3)
        tk.Button(button_frame, text="Analizar", command=self.analyze_code, 
                 font=('Arial', 11, 'bold'), width=10, bg='lightblue', relief='raised').pack(side=tk.LEFT, padx=3)
        
        # Botón principal para Windows - Generar .EXE
        tk.Button(button_frame, text="Generar .EXE", command=self.generate_executable, 
                 font=('Arial', 11, 'bold'), width=14, bg='lightgreen', 
                 relief='raised', cursor='hand2').pack(side=tk.LEFT, padx=3)
        
        tk.Button(button_frame, text="Limpiar", command=self.clear_all, 
                 font=('Arial', 11), width=10, relief='raised').pack(side=tk.LEFT, padx=3)
    
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
        """Crea la barra de estado - Optimizada para Windows"""
        status_frame = tk.Frame(parent, bg=self.bg_color, relief='sunken', bd=1)
        status_frame.pack(fill=tk.X, pady=(5, 0))
        
        # Estado específico para Windows
        self.status_bar = tk.Label(status_frame, 
                                 text="Listo - Windows | Compilación .EXE disponible | DOSBox + TASM",
                                 relief=tk.SUNKEN, font=('Arial', 10),
                                 bg=self.bg_color, anchor='w')
        self.status_bar.pack(fill=tk.X, padx=5, pady=2)
    
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
        
        # Menú Análisis - Específico para Windows
        analysis_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Análisis", menu=analysis_menu)
        analysis_menu.add_command(label="Analizar Código", command=self.analyze_code, accelerator="F5")
        analysis_menu.add_command(label="Generar .EXE", command=self.generate_executable, accelerator="F6")
        analysis_menu.add_separator()
        analysis_menu.add_command(label="Limpiar Todo", command=self.clear_all)
        
        # Menú Ayuda
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        help_menu.add_command(label="Acerca de", command=self.show_about)
        
        # Atajos de teclado - Windows
        self.root.bind('<Control-n>', lambda e: self.new_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<F5>', lambda e: self.analyze_code())
        self.root.bind('<F6>', lambda e: self.generate_executable())  # Atajo para compilar
    
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
        """Genera código ensamblador y compila a ejecutable - Optimizado para Windows"""
        code = self.code_editor.get(1.0, tk.END).strip()
        if not code:
            messagebox.showerror("Error", "No hay código para generar ejecutable")
            return
        
        try:
            # Verificar DOSBox
            if not os.path.exists(self.dosbox_path):
                messagebox.showerror("Error de Configuración", 
                    f"DOSBox no encontrado en: {self.dosbox_path}\n\n"
                    f"Asegúrate de que la carpeta DOSBox2 esté en el directorio del proyecto.\n"
                    f"Debe contener:\n"
                    f"• dosbox.exe\n"
                    f"• configuracion.conf\n"
                    f"• Carpeta Tasm/ con TASM.EXE y TLINK.EXE")
                return
            
            # Analizar código
            self.update_status("Analizando código robótico...")
            tokens, errors = self.analyzer.analyze(code)
            
            if errors:
                error_msg = "Errores encontrados en el código:\n\n" + "\n".join(errors[:5])
                if len(errors) > 5:
                    error_msg += f"\n... y {len(errors) - 5} errores más"
                messagebox.showerror("Errores en el Código", error_msg)
                return
            
            # Solicitar nombre del programa
            program_name = simpledialog.askstring(
                "Nombre del Programa", 
                "Ingrese el nombre del programa (sin extensión):\n\n"
                "Este será el nombre del archivo .exe generado",
                initialvalue="robot_program"
            )
            if not program_name:
                return
            
            # Validar nombre
            if not program_name.replace('_', '').isalnum():
                messagebox.showerror("Nombre Inválido", 
                    "El nombre solo puede contener letras, números y guiones bajos")
                return
            
            # Generar y compilar
            self.update_status(f"Generando {program_name}.exe con DOSBox + TASM...")
            
            # Mostrar progreso
            progress_window = self.show_compilation_progress(program_name)
            self.root.update()
            
            success, message = self.analyzer.generate_and_compile(program_name)
            
            # Cerrar ventana de progreso
            progress_window.destroy()
            
            if success:
                # Verificar archivos generados
                exe_path = os.path.join(self.tasm_path, f"{program_name}.exe")
                asm_path = os.path.join(self.tasm_path, f"{program_name}.asm")
                obj_path = os.path.join(self.tasm_path, f"{program_name}.obj")
                
                files_info = []
                if os.path.exists(exe_path):
                    size = os.path.getsize(exe_path)
                    files_info.append(f"• {program_name}.exe ({size} bytes)")
                if os.path.exists(asm_path):
                    files_info.append(f"• {program_name}.asm (código fuente)")
                if os.path.exists(obj_path):
                    files_info.append(f"• {program_name}.obj (código objeto)")
                
                success_msg = (
                    f"Compilación exitosa en Windows\n\n"
                    f"Archivos generados en DOSBox2\\Tasm\\:\n" + 
                    "\n".join(files_info) + 
                    f"\n\nEl archivo {program_name}.exe está listo para usar en Proteus\n"
                    f"Ubicación: {self.tasm_path}"
                )
                
                messagebox.showinfo("Compilación Exitosa", success_msg)
                
                # Mostrar código ensamblador
                asm_code, error = self.analyzer.generate_assembly_code(program_name)
                if asm_code:
                    self.show_assembly_code(asm_code, program_name)
                
                self.update_status(f"{program_name}.exe generado exitosamente en DOSBox2\\Tasm\\")
            else:
                messagebox.showerror("Error de Compilación", 
                    f"Error durante la compilación:\n\n{message}\n\n"
                    f"Verificaciones:\n"
                    f"• DOSBox instalado correctamente\n"
                    f"• configuracion.conf disponible\n"
                    f"• TASM.EXE y TLINK.EXE en Tasm/\n"
                    f"• Permisos de escritura en la carpeta")
                self.update_status("Error en la compilación")
                
        except Exception as e:
            messagebox.showerror("Error Inesperado", 
                f"Error durante la generación:\n\n{str(e)}\n\n"
                f"Contacta al desarrollador si el problema persiste")
            self.update_status("Error inesperado")
    
    def show_compilation_progress(self, program_name):
        """Muestra ventana de progreso durante la compilación"""
        progress_window = tk.Toplevel(self.root)
        progress_window.title("Compilando...")
        progress_window.geometry("400x150")
        progress_window.resizable(False, False)
        
        # Centrar ventana
        progress_window.transient(self.root)
        progress_window.grab_set()
        
        tk.Label(progress_window, text="Compilando código robótico", 
                font=('Arial', 12, 'bold')).pack(pady=10)
        tk.Label(progress_window, text=f"Programa: {program_name}.exe", 
                font=('Arial', 10)).pack(pady=5)
        tk.Label(progress_window, text="DOSBox + TASM trabajando...", 
                font=('Arial', 10)).pack(pady=5)
        
        # Barra de progreso indeterminada
        import tkinter.ttk as ttk
        progress_bar = ttk.Progressbar(progress_window, mode='indeterminate')
        progress_bar.pack(pady=10, padx=20, fill='x')
        progress_bar.start()
        
        return progress_window
    
    def update_output(self, text, tag="info"):
        """Actualiza el área de salida"""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, text, tag)
        self.output_text.config(state=tk.DISABLED)
        self.output_text.see(tk.END)
    
    def clear_all(self):
        """Limpia todos los campos"""
        self.code_editor.delete(1.0, tk.END)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state=tk.DISABLED)
        self.update_status("Campos limpiados")
    
    def update_status(self, message):
        """Actualiza la barra de estado - Windows Edition"""
        self.status_bar.config(text=f"{message}")
    
    def update_title(self):
        """Actualiza el título de la ventana - Windows Edition"""
        if self.current_file:
            filename = os.path.basename(self.current_file)
            self.root.title(f"Analizador Léxico - {filename} - Windows Edition")
        else:
            self.root.title("Analizador Léxico para Brazo Robótico - Windows Edition")
    
    def show_about(self):
        """Muestra información sobre la aplicación - Windows Edition"""
        messagebox.showinfo("Acerca de - Windows Edition",
            f"Analizador Léxico para Brazo Robótico\n"
            f"Windows Edition - Versión 5.0\n\n"
            f"Sistema: Windows (Optimizado)\n"
            f"Compilación: DOSBox + TASM integrado\n"
            f"Target: Archivos .EXE para Proteus\n\n"
            f"Funciones completas:\n"
            f"• Análisis léxico, sintáctico y semántico\n"
            f"• Generación de código intermedio (cuádruplos)\n"
            f"• Compilación nativa a archivos .EXE\n"
            f"• Validaciones avanzadas\n"
            f"• Interfaz optimizada para Windows\n\n"
            f"Sintaxis soportada:\n"
            f"Robot nombre\n"
            f"nombre.componente = valor\n"
            f"nombre.inicio ... nombre.fin\n\n"
            f"Archivos generados en: DOSBox2\\Tasm\\")
    
    def show_assembly_code(self, asm_code, program_name):
        """Muestra el código ensamblador generado - Windows optimizado"""
        asm_window = tk.Toplevel(self.root)
        asm_window.title(f"Código Ensamblador - {program_name}.asm")
        asm_window.geometry("900x700")
        asm_window.state('normal')
        
        # Frame principal
        main_frame = tk.Frame(asm_window)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título
        title_frame = tk.Frame(main_frame)
        title_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(title_frame, text=f"Código Ensamblador Generado", 
                font=('Arial', 14, 'bold')).pack(side=tk.LEFT)
        tk.Label(title_frame, text=f"Compatible con TASM", 
                font=('Arial', 10), fg='green').pack(side=tk.RIGHT)
        
        # Área de texto con scroll mejorado
        text_frame = tk.Frame(main_frame)
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        text_area = scrolledtext.ScrolledText(text_frame, wrap=tk.NONE, 
                                            font=('Courier New', 10),
                                            bg='#f8f8f8', fg='black')
        text_area.pack(fill=tk.BOTH, expand=True)
        text_area.insert(1.0, asm_code)
        text_area.config(state=tk.DISABLED)
        
        # Botones mejorados
        button_frame = tk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(10, 0))
        
        def save_asm():
            file_path = filedialog.asksaveasfilename(
                title="Guardar código ensamblador",
                defaultextension=".asm",
                filetypes=[("Archivos Ensamblador", "*.asm"), ("Todos los archivos", "*.*")],
                initialvalue=f"{program_name}.asm"
            )
            if file_path:
                try:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(asm_code)
                    messagebox.showinfo("Guardado", 
                        f"Código ensamblador guardado exitosamente:\n\n{file_path}")
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo guardar:\n{str(e)}")
        
        def open_folder():
            """Abre la carpeta donde está el archivo .exe"""
            try:
                os.startfile(self.tasm_path)
            except:
                messagebox.showinfo("Ubicación", f"Los archivos están en:\n{self.tasm_path}")
        
        tk.Button(button_frame, text="Abrir Carpeta", command=open_folder,
                 font=('Arial', 10), relief='raised').pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Guardar Como...", command=save_asm,
                 font=('Arial', 10), relief='raised').pack(side=tk.RIGHT, padx=5)
        tk.Button(button_frame, text="Cerrar", command=asm_window.destroy,
                 font=('Arial', 10), relief='raised').pack(side=tk.RIGHT)
    
    def run(self):
        """Ejecuta la aplicación"""
        self.root.mainloop()

if __name__ == "__main__":
    try:
        print("===============================================")
        print("ANALIZADOR LÉXICO PARA BRAZO ROBÓTICO")
        print("Windows Edition - Versión 5.0")
        print("===============================================")
        print("Optimizado para Windows con compilación .EXE")
        print("DOSBox + TASM integrado")
        print("Iniciando aplicación...")
        print("===============================================")
        
        app = LexicalAnalyzerGUI()
        app.run()
        
    except Exception as e:
        print(f"Error crítico: {e}")
        import traceback
        traceback.print_exc()
        input("Presiona Enter para salir...")
