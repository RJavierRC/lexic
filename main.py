import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
from robot_lexical_analyzer import RobotLexicalAnalyzer

class LineNumberText(tk.Frame):
    """Widget de texto con numeración de líneas"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        
        # Crear el widget de números de línea
        self.line_numbers = tk.Text(self, width=4, padx=3, takefocus=0,
                                  relief=tk.SUNKEN, bd=1, state=tk.DISABLED,
                                  font=('Courier', 10), bg='#f0f0f0', fg='#666666')
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)
        
        # Crear el widget de texto principal
        self.text_widget = scrolledtext.ScrolledText(self, font=('Courier', 10), **kwargs)
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
        self.root = tk.Tk()
        self.root.title("Analizador Léxico, Sintáctico y Semántico para Brazo Robótico")
        self.root.geometry("1200x800")
        self.root.minsize(800, 600)
        
        # Variables
        self.current_file = None
        self.analyzer = RobotLexicalAnalyzer()
        
        # Configurar estilo
        self.setup_styles()
        
        # Crear interfaz
        self.create_widgets()
        self.create_menu()
        
    def setup_styles(self):
        """Configura los estilos de la interfaz"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar colores
        style.configure('Title.TLabel', font=('Arial', 12, 'bold'))
        style.configure('Button.TButton', font=('Arial', 10))
    
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
        file_menu.add_command(label="Guardar como", command=self.save_file_as, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.quit)
        
        # Menú Análisis
        analysis_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Análisis", menu=analysis_menu)
        analysis_menu.add_command(label="Analizar", command=self.analyze_code, accelerator="F5")
        analysis_menu.add_command(label="Limpiar", command=self.clear_all, accelerator="Ctrl+L")
        
        # Menú Ayuda
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        help_menu.add_command(label="Acerca de", command=self.show_about)
        
        # Atajos de teclado
        self.root.bind('<Control-n>', lambda e: self.new_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<Control-Shift-S>', lambda e: self.save_file_as())
        self.root.bind('<F5>', lambda e: self.analyze_code())
        self.root.bind('<Control-l>', lambda e: self.clear_all())
    
    def create_widgets(self):
        """Crea todos los widgets de la interfaz"""
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Frame superior con título y botones
        top_frame = ttk.Frame(main_frame)
        top_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Título
        title_label = ttk.Label(top_frame, text="Analizador Léxico, Sintáctico y Semántico para Brazo Robótico", style='Title.TLabel')
        title_label.pack(side=tk.LEFT)
        
        # Frame de botones
        button_frame = ttk.Frame(top_frame)
        button_frame.pack(side=tk.RIGHT)
        
        # Botones principales
        ttk.Button(button_frame, text="Abrir Archivo", command=self.open_file, style='Button.TButton').pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="Guardar", command=self.save_file, style='Button.TButton').pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="Analizar", command=self.analyze_code, style='Button.TButton').pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="Limpiar", command=self.clear_all, style='Button.TButton').pack(side=tk.LEFT, padx=2)
        
        # Panel dividido horizontal
        paned_window = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        paned_window.pack(fill=tk.BOTH, expand=True)
        
        # Frame izquierdo - Editor
        left_frame = ttk.LabelFrame(paned_window, text="Editor de Código", padding=5)
        paned_window.add(left_frame, weight=1)
        
        # Editor con números de línea
        self.code_editor = LineNumberText(left_frame, wrap=tk.NONE, undo=True)
        self.code_editor.pack(fill=tk.BOTH, expand=True)
        
        # Frame derecho - Salida
        right_frame = ttk.LabelFrame(paned_window, text="Resultados del Análisis", padding=5)
        paned_window.add(right_frame, weight=1)
        
        # Área de salida
        self.output_text = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, 
                                                   font=('Courier', 9), state=tk.DISABLED)
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        # Barra de estado
        self.status_bar = ttk.Label(main_frame, text="Listo", relief=tk.SUNKEN)
        self.status_bar.pack(fill=tk.X, pady=(5, 0))
        
        # Configurar colores del editor de salida
        self.output_text.tag_configure("error", foreground="red")
        self.output_text.tag_configure("success", foreground="green")
        self.output_text.tag_configure("info", foreground="blue")
    
    def new_file(self):
        """Crea un nuevo archivo"""
        if self.check_unsaved_changes():
            self.code_editor.delete(1.0, tk.END)
            self.current_file = None
            self.update_title()
            self.update_status("Nuevo archivo creado")
    
    def open_file(self):
        """Abre un archivo"""
        if self.check_unsaved_changes():
            file_path = filedialog.askopenfilename(
                title="Abrir archivo",
                filetypes=[
                    ("Archivos Robot", "*.robot"),
                    ("Archivos Brazo", "*.arm"),
                    ("Archivos RB", "*.rb"),
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
                ("Archivos Brazo", "*.arm"),
                ("Archivos RB", "*.rb"),
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
            # Realizar análisis léxico
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
    
    def clear_all(self):
        """Limpia el editor y la salida"""
        result = messagebox.askyesno("Confirmar", "¿Desea limpiar el editor y los resultados?")
        if result:
            self.code_editor.delete(1.0, tk.END)
            self.update_output("", "info")
            self.update_status("Editor y resultados limpiados")
    
    def update_output(self, text, tag="info"):
        """Actualiza el área de salida"""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(1.0, text, tag)
        self.output_text.config(state=tk.DISABLED)
    
    def update_status(self, message):
        """Actualiza la barra de estado"""
        self.status_bar.config(text=message)
    
    def update_title(self):
        """Actualiza el título de la ventana"""
        if self.current_file:
            filename = os.path.basename(self.current_file)
            self.root.title(f"Analizador Léxico - {filename}")
        else:
            self.root.title("Analizador Léxico, Sintáctico y Semántico para Brazo Robótico")
    
    def check_unsaved_changes(self):
        """Verifica si hay cambios sin guardar"""
        # En una implementación más completa, aquí verificarías cambios
        return True
    
    def show_about(self):
        """Muestra información sobre la aplicación"""
        messagebox.showinfo(
            "Acerca de",
            "Analizador Léxico, Sintáctico y Semántico para Brazo Robótico\n\n"
            "Desarrollado con Python y tkinter\n"
            "Versión 4.0 - Nueva Sintaxis Extendida\n\n"
            "Características:\n"
            "• Análisis léxico especializado para robótica\n"
            "• Análisis sintáctico con validación de gramática\n"
            "• Análisis semántico con validaciones avanzadas\n"
            "• Detección de declaraciones duplicadas\n"
            "• Validación de rangos de valores\n"
            "• Verificación de robots no declarados\n"
            "• Detección de tokens desconocidos\n"
            "• Soporte para bloques de control\n"
            "• Comandos de espera y repetición\n"
            "• Estadísticas detalladas\n"
            "• Interfaz gráfica intuitiva\n\n"
            "Nueva Sintaxis Soportada:\n"
            "Robot nombre_robot\n"
            "nombre_robot.repetir = N\n"
            "nombre_robot.inicio\n"
            "  nombre_robot.componente = valor\n"
            "  nombre_robot.espera = tiempo\n"
            "nombre_robot.fin\n\n"
            "Componentes soportados:\n"
            "• base: 0-360° (gira completa)\n"
            "• hombro: 0-180° (articulación limitada)\n"
            "• codo: 0-180° (articulación limitada)\n"
            "• garra: 0-90° (apertura/cierre)\n"
            "• muñeca: 0-360° (gira completa)\n"
            "• velocidad: 0.1-10.0 (velocidad de movimiento)\n"
            "• repetir: 1-100 (número de repeticiones)\n"
            "• espera: 0.1-60.0 segundos (tiempo de pausa)\n\n"
            "Comandos especiales:\n"
            "• inicio: marca el inicio de un bloque\n"
            "• fin: marca el final de un bloque\n\n"
            "Ejemplo completo:\n"
            "Robot r1\n"
            "r1.repetir = 3\n"
            "r1.inicio\n"
            "  r1.velocidad = 2\n"
            "  r1.base = 45\n"
            "  r1.hombro = 120\n"
            "  r1.espera = 1\n"
            "r1.fin"
        )
    
    def run(self):
        """Ejecuta la aplicación"""
        self.root.mainloop()

if __name__ == "__main__":
    app = LexicalAnalyzerGUI()
    app.run()
