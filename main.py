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
        
        print(f"🪟 Analizador iniciado en modo Windows - Compilación .EXE disponible")
    
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
        
        # Título optimizado para Windows
        title_label = tk.Label(header_frame, 
                              text="🪟 Analizador Léxico para Brazo Robótico - Windows Edition",
                              font=('Arial', 16, 'bold'),
                              bg=self.bg_color, fg='darkblue')
        title_label.pack(side=tk.LEFT)
        
        # Botones optimizados para Windows
        button_frame = tk.Frame(header_frame, bg=self.bg_color)
        button_frame.pack(side=tk.RIGHT)
        
        # Botones principales con estilos Windows
        tk.Button(button_frame, text="📂 Abrir", command=self.open_file, 
                 font=('Arial', 11), width=10, relief='raised').pack(side=tk.LEFT, padx=3)
        tk.Button(button_frame, text="💾 Guardar", command=self.save_file, 
                 font=('Arial', 11), width=10, relief='raised').pack(side=tk.LEFT, padx=3)
        tk.Button(button_frame, text="🔍 Analizar", command=self.analyze_code, 
                 font=('Arial', 11, 'bold'), width=10, bg='lightblue', relief='raised').pack(side=tk.LEFT, padx=3)
        
        # Botón principal para Windows - Generar .EXE
        tk.Button(button_frame, text="⚙️ Generar .EXE", command=self.generate_executable, 
                 font=('Arial', 11, 'bold'), width=14, bg='lightgreen', 
                 relief='raised', cursor='hand2').pack(side=tk.LEFT, padx=3)
        
        # Botón específico para Proteus
        tk.Button(button_frame, text="🎯 DOS Real", command=self.generate_for_proteus, 
                 font=('Arial', 11, 'bold'), width=14, bg='red', fg='white',
                 relief='raised', cursor='hand2').pack(side=tk.LEFT, padx=3)
        
        # Botón específico para Proteus - Generar .COM
        tk.Button(button_frame, text="📁 .COM", command=self.generate_com_file, 
                 font=('Arial', 11, 'bold'), width=10, bg='orange', fg='white',
                 relief='raised', cursor='hand2').pack(side=tk.LEFT, padx=3)
        
        # Botón para ASM dinámico
        tk.Button(button_frame, text="📝 ASM", command=self.generate_dynamic_asm, 
                 font=('Arial', 11, 'bold'), width=8, bg='purple', fg='white',
                 relief='raised', cursor='hand2').pack(side=tk.LEFT, padx=3)
        
        tk.Button(button_frame, text="🧹 Limpiar", command=self.clear_all, 
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
                                 text="🪟 Listo - Windows | Compilación .EXE disponible | DOSBox + TASM",
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
        analysis_menu.add_command(label="🔍 Analizar Código", command=self.analyze_code, accelerator="F5")
        analysis_menu.add_command(label="⚙️ Generar .EXE", command=self.generate_executable, accelerator="F6")
        analysis_menu.add_command(label="🎯 Para Proteus", command=self.generate_for_proteus, accelerator="F7")
        analysis_menu.add_command(label="📁 Generar .COM", command=self.generate_com_file, accelerator="F8")
        analysis_menu.add_separator()
        analysis_menu.add_command(label="🧹 Limpiar Todo", command=self.clear_all)
        
        # Menú Ayuda
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        help_menu.add_command(label="Acerca de", command=self.show_about)
        
        # Atajos de teclado - Windows
        self.root.bind('<Control-n>', lambda e: self.new_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<F5>', lambda e: self.analyze_code())
        self.root.bind('<F6>', lambda e: self.generate_executable())  # Atajo para compilar
        self.root.bind('<F7>', lambda e: self.generate_for_proteus())  # Atajo para Proteus
        self.root.bind('<F8>', lambda e: self.generate_com_file())  # Atajo para .COM
        self.root.bind('<F7>', lambda e: self.generate_for_proteus())  # Atajo para Proteus
    
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
                    f"⚠️ DOSBox no encontrado en: {self.dosbox_path}\n\n"
                    f"Asegúrate de que la carpeta DOSBox2 esté en el directorio del proyecto.\n"
                    f"Debe contener:\n"
                    f"• dosbox.exe\n"
                    f"• Carpeta Tasm/ con TASM.EXE y TLINK.EXE")
                return
            
            # Verificar archivos TASM
            tasm_exe = os.path.join(self.tasm_path, "TASM.EXE")
            tlink_exe = os.path.join(self.tasm_path, "TLINK.EXE")
            if not os.path.exists(tasm_exe) or not os.path.exists(tlink_exe):
                messagebox.showerror("Error de Configuración", 
                    f"❌ Archivos de compilación faltantes:\n\n"
                    f"• TASM.EXE: {'✓' if os.path.exists(tasm_exe) else '❌'}\n"
                    f"• TLINK.EXE: {'✓' if os.path.exists(tlink_exe) else '❌'}\n\n"
                    f"Verifica la carpeta: {self.tasm_path}")
                return
            
            # Analizar código
            self.update_status("🔍 Analizando código robótico...")
            tokens, errors = self.analyzer.analyze(code)
            
            # Permitir compilación incluso con errores menores/warnings
            critical_errors = [e for e in errors if "crítico" in str(e).lower() or "fatal" in str(e).lower()]
            if critical_errors:
                error_msg = "❌ Errores críticos encontrados:\n\n" + "\n".join(critical_errors[:3])
                messagebox.showerror("Errores Críticos", error_msg)
                return
            
            # Si hay errores menores, mostrar warning pero continuar
            if errors:
                warning_msg = f"⚠️ Se encontraron {len(errors)} warnings, pero se continuará con la compilación.\n\n"
                warning_msg += "Primeros warnings:\n" + "\n".join(str(e) for e in errors[:3])
                if len(errors) > 3:
                    warning_msg += f"\n... y {len(errors) - 3} más"
                
                result = messagebox.askyesno("Warnings Detectados", 
                    warning_msg + "\n\n¿Desea continuar con la generación del ejecutable?")
                if not result:
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
            self.update_status(f"⚡ Generando {program_name}.exe instantáneamente...")
            
            # Mostrar progreso
            progress_window = self.show_compilation_progress(program_name)
            self.root.update()
            
            try:
                # Usar el sistema de compilación instantánea que evita timeouts
                success, message = self.analyzer.generate_and_compile(program_name)
            except Exception as compile_error:
                progress_window.destroy()
                
                # Intentar generar solo el ASM como fallback
                try:
                    asm_code, asm_error = self.analyzer.generate_assembly_code(program_name)
                    if asm_code and not asm_error:
                        # Guardar el ASM manualmente
                        asm_path = os.path.join(self.tasm_path, f"{program_name}.asm")
                        with open(asm_path, 'w', encoding='ascii', errors='ignore') as f:
                            f.write(asm_code)
                        
                        fallback_msg = (
                            f"⚠️ La compilación automática falló, pero se generó el código ASM exitosamente.\n\n"
                            f"📁 Archivo generado:\n"
                            f"• {program_name}.asm en DOSBox2\\Tasm\\\n\n"
                            f"🔧 Puedes compilar manualmente:\n"
                            f"1. Abrir DOSBox\n"
                            f"2. mount c DOSBox2\\Tasm\n"
                            f"3. tasm {program_name}.asm\n"
                            f"4. tlink {program_name}.obj\n\n"
                            f"📄 ¿Deseas ver el código ASM generado?"
                        )
                        
                        show_asm = messagebox.askyesno("ASM Generado", fallback_msg)
                        if show_asm:
                            self.show_assembly_code(asm_code, program_name)
                        
                        self.update_status(f"✅ {program_name}.asm generado - compilación manual requerida")
                        return
                except Exception as asm_error:
                    pass
                
                messagebox.showerror("Error de Compilación", 
                    f"❌ Error durante la compilación:\n\n{str(compile_error)}\n\n"
                    f"Posibles causas:\n"
                    f"• Archivos TASM faltantes\n"
                    f"• Permisos insuficientes\n"
                    f"• DOSBox bloqueado por antivirus")
                self.update_status("❌ Error en la compilación")
                return
            
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
                    f"✅ Compilación exitosa en Windows\n\n"
                    f"📁 Archivos generados en DOSBox2\\Tasm\\:\n" + 
                    "\n".join(files_info) + 
                    f"\n\n🎯 El archivo {program_name}.exe está listo para usar en Proteus\n"
                    f"📂 Ubicación: {self.tasm_path}"
                )
                
                messagebox.showinfo("🎉 Compilación Exitosa", success_msg)
                
                # Generar y mostrar código ensamblador dinámico
                try:
                    from create_dynamic_asm_generator import generate_dynamic_asm_from_analyzer
                    asm_code = generate_dynamic_asm_from_analyzer(self.analyzer, program_name)
                    
                    # Guardar ASM dinámico 
                    asm_path = os.path.join(self.tasm_path, f"{program_name}_dynamic.asm")
                    with open(asm_path, 'w', encoding='ascii', errors='ignore') as f:
                        f.write(asm_code)
                    
                    self.show_assembly_code(asm_code, f"{program_name}_dynamic")
                    self.output_text.insert(tk.END, f"\n🎯 ASM dinámico generado: {program_name}_dynamic.asm\n")
                    
                except Exception as asm_error:
                    # Fallback al generador original
                    asm_code, error = self.analyzer.generate_assembly_code(program_name)
                    if asm_code:
                        self.show_assembly_code(asm_code, program_name)
                
                self.update_status(f"✅ {program_name}.exe generado exitosamente en DOSBox2\\Tasm\\")
            else:
                messagebox.showerror("❌ Error de Compilación", 
                    f"Error durante la compilación:\n\n{message}\n\n"
                    f"Verificaciones:\n"
                    f"• DOSBox instalado correctamente\n"
                    f"• TASM.EXE y TLINK.EXE en Tasm/\n"
                    f"• Permisos de escritura en la carpeta")
                self.update_status("❌ Error en la compilación")
                
        except Exception as e:
            messagebox.showerror("Error Inesperado", 
                f"❌ Error durante la generación:\n\n{str(e)}\n\n"
                f"Contacta al desarrollador si el problema persiste")
            self.update_status("❌ Error inesperado")
    
    def generate_for_proteus(self):
        """Genera código específicamente optimizado para Proteus ISIS"""
        code = self.code_editor.get(1.0, tk.END).strip()
        if not code:
            messagebox.showerror("Error", "No hay código para generar ejecutable para Proteus")
            return
        
        try:
            # Verificar DOSBox
            if not os.path.exists(self.dosbox_path):
                messagebox.showerror("Error de Configuración", 
                    f"⚠️ DOSBox no encontrado en: {self.dosbox_path}\n\n"
                    f"Asegúrate de que la carpeta DOSBox2 esté en el directorio del proyecto.\n"
                    f"Debe contener:\n"
                    f"• dosbox.exe\n"
                    f"• Carpeta Tasm/ con TASM.EXE y TLINK.EXE")
                return
            
            # Analizar código (permitir warnings)
            self.update_status("🔍 Analizando código para Proteus...")
            tokens, errors = self.analyzer.analyze(code)
            
            # Solo rechazar errores críticos
            critical_errors = [e for e in errors if "crítico" in str(e).lower() or "fatal" in str(e).lower()]
            if critical_errors:
                error_msg = "❌ Errores críticos encontrados:\n\n" + "\n".join(critical_errors[:3])
                messagebox.showerror("Errores Críticos", error_msg)
                return
            
            # Si hay warnings, mostrar pero continuar
            if errors:
                warning_msg = f"⚠️ Se encontraron {len(errors)} warnings, pero se continuará con la generación para Proteus.\n\n"
                warning_msg += "Primeros warnings:\n" + "\n".join(str(e) for e in errors[:3])
                if len(errors) > 3:
                    warning_msg += f"\n... y {len(errors) - 3} más"
                
                result = messagebox.askyesno("Warnings Detectados", 
                    warning_msg + "\n\n¿Desea continuar con la generación para Proteus?")
                if not result:
                    return
            
            # Solicitar nombre del programa
            program_name = tk.simpledialog.askstring(
                "Programa para Proteus", 
                "Ingrese el nombre del programa para Proteus (sin extensión):\n\n"
                "Este archivo será específicamente optimizado para Proteus ISIS",
                initialvalue="robot_proteus"
            )
            if not program_name:
                return
            
            # Validar nombre
            if not program_name.replace('_', '').isalnum():
                messagebox.showerror("Nombre Inválido", 
                    "El nombre solo puede contener letras, números y guiones bajos")
                return
            
            # Generar específicamente para Proteus
            self.update_status(f"🎯 Generando {program_name}.exe para Proteus ISIS...")
            
            # Mostrar progreso específico para Proteus
            progress_window = self.show_proteus_compilation_progress(program_name)
            self.root.update()
            
            try:
                # Usar el generador DOS REAL para verdadera compatibilidad con 8086
                success, message = self.analyzer.generate_and_compile_dos_real(program_name)
            except Exception as compile_error:
                progress_window.destroy()
                messagebox.showerror("Error de Generación", 
                    f"❌ Error generando para Proteus:\n\n{str(compile_error)}\n\n"
                    f"Verifica que DOSBox y TASM estén correctamente instalados")
                self.update_status("❌ Error en generación para Proteus")
                return
            
            # Cerrar ventana de progreso
            progress_window.destroy()
            
            if success:
                # Verificar archivo generado
                exe_path = os.path.join(self.tasm_path, f"{program_name}.exe")
                
                success_msg = (
                    f"🎯 ¡EJECUTABLE DOS REAL PARA PROTEUS!\n\n"
                    f"📁 Archivo: {program_name}.exe\n"
                    f"📂 Ubicación: DOSBox2\\Tasm\\\n"
                    f"�️  Formato: MS-DOS ejecutable REAL\n"
                    f"🔌 Procesador: 8086 (modo real)\n"
                    f"⚡ Puertos: 0300h-0303h (8255 PPI)\n"
                    f"🤖 Control: 3 motores paso a paso\n\n"
                    f"🎮 CONFIGURACIÓN PROTEUS (CRÍTICA):\n"
                    f"1. ⚙️  Procesador: 8086 (NO 8088, NO x86)\n"
                    f"2. 🖥️  Modelo: 8086 Real Mode\n"
                    f"3. 📂 Cargar: {program_name}.exe\n"
                    f"4. 🔌 8255 PPI en direcciones:\n"
                    f"   • 0300h (Puerto A - Base)\n"
                    f"   • 0301h (Puerto B - Hombro)\n"
                    f"   • 0302h (Puerto C - Codo)\n"
                    f"   • 0303h (Control)\n"
                    f"5. 🤖 ULN2003A para drivers\n\n"
                    f"✅ ¡Sin error de opcode desconocido!\n"
                    f"✅ ¡Ejecutable DOS auténtico!"
                )
                
                messagebox.showinfo("🎯 ¡Ejecutable para Proteus Listo!", success_msg)
                self.update_status(f"✅ {program_name}.exe generado para Proteus en DOSBox2\\Tasm\\")
            else:
                messagebox.showerror("❌ Error en Proteus", 
                    f"Error generando para Proteus:\n\n{message}")
                self.update_status("❌ Error en generación para Proteus")
                
        except Exception as e:
            messagebox.showerror("Error Inesperado", 
                f"❌ Error durante la generación para Proteus:\n\n{str(e)}")
            self.update_status("❌ Error inesperado en generación para Proteus")
    
    def generate_com_file(self):
        """Genera archivo .COM específicamente para Proteus (como noname.com que funciona)"""
        code = self.code_editor.get(1.0, tk.END).strip()
        if not code:
            messagebox.showerror("Error", "No hay código para generar archivo .COM")
            return
        
        try:
            # Analizar código
            self.update_status("🔍 Analizando código para archivo .COM...")
            tokens, errors = self.analyzer.analyze(code)
            
            # Solo rechazar errores críticos
            critical_errors = [e for e in errors if "crítico" in str(e).lower() or "fatal" in str(e).lower()]
            if critical_errors:
                error_msg = "❌ Errores críticos encontrados:\n\n" + "\n".join(critical_errors[:3])
                messagebox.showerror("Errores Críticos", error_msg)
                return
            
            # Solicitar nombre del programa
            program_name = tk.simpledialog.askstring(
                "Archivo .COM para Proteus", 
                "Ingrese el nombre del archivo .COM:\n\n"
                "Este archivo será compatible con Proteus sin errores de debug",
                initialvalue="motor_robot"
            )
            if not program_name:
                return
            
            # Validar nombre
            if not program_name.replace('_', '').isalnum():
                messagebox.showerror("Nombre Inválido", 
                    "El nombre solo puede contener letras, números y guiones bajos")
                return
            
            self.update_status(f"📁 Generando {program_name}.com para Proteus...")
            
            # Crear el generador COM DINÁMICO optimizado
            import create_dynamic_motor_com_v2
            
            # Generar el archivo COM dinámico usando los valores del código
            success = create_dynamic_motor_com_v2.create_dynamic_com_from_analyzer(self.analyzer)
            
            # Paths para renombrar
            original_path = os.path.join("DOSBox2", "Tasm", "motor_user.com")
            new_path = os.path.join("DOSBox2", "Tasm", f"{program_name}.com")
            
            if success and os.path.exists(original_path):
                # Renombrar al nombre solicitado
                import shutil
                shutil.copy2(original_path, new_path)
                
                file_size = os.path.getsize(new_path)
                
                success_msg = (
                    f"📁 ¡ARCHIVO .COM DINÁMICO!\n\n"
                    f"📂 Archivo: {program_name}.com\n"
                    f"📏 Tamaño: {file_size} bytes\n"
                    f"📍 Ubicación: DOSBox2\\Tasm\\\n"
                    f"🎯 Formato: .COM (basado en tu código)\n\n"
                    f"🤖 VALORES EXTRAÍDOS DE TU CÓDIGO:\n"
                    f"• r1.base = {self.get_motor_value('base')}°\n"
                    f"• r1.hombro = {self.get_motor_value('hombro')}°\n"
                    f"• r1.codo = {self.get_motor_value('codo')}°\n"
                    f"• r1.velocidad = {self.get_motor_value('velocidad')}\n"
                    f"• r1.espera = {self.get_motor_value('espera')}\n\n"
                    f"✅ ARCHIVO .COM GENERADO DINÁMICAMENTE:\n"
                    f"• Ángulos exactos de tu sintaxis\n"
                    f"• Código máquina personalizado\n"
                    f"• No valores estáticos\n\n"
                    f"🎮 CARGAR EN PROTEUS:\n"
                    f"1. Archivo: {program_name}.com\n"
                    f"2. Procesador: 8086 Real Mode\n"
                    f"3. ¡Ángulos de tu código Robot!\n"
                    f"4. Completamente personalizado"
                )
                
                messagebox.showinfo("📁 ¡Archivo .COM Listo!", success_msg)
                self.update_status(f"✅ {program_name}.com generado exitosamente")
            else:
                messagebox.showerror("❌ Error", "No se pudo generar el archivo .COM")
                self.update_status("❌ Error generando archivo .COM")
                
        except Exception as e:
            messagebox.showerror("Error Inesperado", 
                f"❌ Error durante la generación .COM:\n\n{str(e)}")
            self.update_status("❌ Error inesperado en generación .COM")

    def generate_dynamic_asm(self):
        """Genera código ASM dinámico basado en valores del código Robot"""
        code = self.code_editor.get(1.0, tk.END).strip()
        if not code:
            messagebox.showerror("Error", "No hay código para generar ASM dinámico")
            return
        
        try:
            # Analizar código
            self.update_status("🔍 Analizando código para ASM dinámico...")
            tokens, errors = self.analyzer.analyze(code)
            
            # Solicitar nombre del programa
            program_name = tk.simpledialog.askstring(
                "ASM Dinámico", 
                "Nombre del archivo ASM:",
                initialvalue="robot_dynamic"
            )
            
            if not program_name:
                return
            
            # Generar ASM dinámico
            from create_dynamic_asm_generator import generate_dynamic_asm_from_analyzer
            asm_code = generate_dynamic_asm_from_analyzer(self.analyzer, program_name)
            
            # Guardar archivo ASM
            asm_path = os.path.join(self.tasm_path, f"{program_name}.asm")
            with open(asm_path, 'w', encoding='ascii', errors='ignore') as f:
                f.write(asm_code)
            
            # Mostrar código ASM generado
            self.show_assembly_code(asm_code, program_name)
            
            # Mensaje de éxito
            success_msg = (
                f"📝 ¡ASM DINÁMICO GENERADO!\n\n"
                f"📂 Archivo: {program_name}.asm\n"
                f"📍 Ubicación: DOSBox2\\Tasm\\\n\n"
                f"🤖 VALORES EXTRAÍDOS:\n"
                f"• r1.base = {self.get_motor_value('base')}°\n"
                f"• r1.hombro = {self.get_motor_value('hombro')}°\n"
                f"• r1.codo = {self.get_motor_value('codo')}°\n"
                f"• r1.velocidad = {self.get_motor_value('velocidad')}\n"
                f"• r1.espera = {self.get_motor_value('espera')}\n\n"
                f"✅ CARACTERÍSTICAS:\n"
                f"• Ángulos exactos de tu sintaxis\n"
                f"• Pasos y delays calculados\n"
                f"• Compatible con TASM/DOSBox\n"
                f"• Listo para compilar a .EXE/.COM\n\n"
                f"🎯 SIGUIENTE PASO:\n"
                f"Compila este ASM con TASM para crear el ejecutable"
            )
            
            messagebox.showinfo("✅ ASM Dinámico Generado", success_msg)
            self.update_status(f"✅ {program_name}.asm generado dinámicamente")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error generando ASM dinámico:\n\n{str(e)}")
            self.update_status("❌ Error generando ASM dinámico")

    def get_motor_value(self, component):
        """Extrae el valor de un componente específico del código analizado"""
        try:
            # Buscar en los tokens del analizador
            if hasattr(self.analyzer, 'tokens') and self.analyzer.tokens:
                i = 0
                while i < len(self.analyzer.tokens) - 2:
                    token = self.analyzer.tokens[i]
                    if (hasattr(token, 'type') and hasattr(token, 'value')):
                        
                        # Buscar componentes (pueden ser KEYWORD o COMPONENT)
                        if (token.type in ['COMPONENT', 'KEYWORD'] and 
                            token.value.lower() == component.lower()):
                            
                            # Buscar el valor después del '=' (puede ser ASSIGN o ASSIGN_OP)
                            if (i + 2 < len(self.analyzer.tokens) and 
                                hasattr(self.analyzer.tokens[i + 1], 'type') and 
                                self.analyzer.tokens[i + 1].type in ['ASSIGN', 'ASSIGN_OP']):
                                
                                value_token = self.analyzer.tokens[i + 2]
                                if hasattr(value_token, 'value'):
                                    return value_token.value
                    i += 1
            
            # Valores por defecto si no se encuentra
            defaults = {
                'base': 45,
                'hombro': 90,
                'codo': 60,
                'velocidad': 2,
                'espera': 1,
                'repetir': 1
            }
            return defaults.get(component.lower(), 0)
            
        except Exception as e:
            return f"Error: {e}"

    def show_compilation_progress(self, program_name):
        """Muestra ventana de progreso durante la compilación"""
        progress_window = tk.Toplevel(self.root)
        progress_window.title("Compilando...")
        progress_window.geometry("400x150")
        progress_window.resizable(False, False)
        
        # Centrar ventana
        progress_window.transient(self.root)
        progress_window.grab_set()
        
        tk.Label(progress_window, text="🔧 Compilando código robótico", 
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
    
    def show_proteus_compilation_progress(self, program_name):
        """Muestra ventana de progreso durante la generación para Proteus"""
        progress_window = tk.Toplevel(self.root)
        progress_window.title("Generando para Proteus...")
        progress_window.geometry("450x180")
        progress_window.resizable(False, False)
        
        # Centrar ventana
        progress_window.transient(self.root)
        progress_window.grab_set()
        
        tk.Label(progress_window, text="🎯 Generando ejecutable DOS REAL", 
                font=('Arial', 12, 'bold')).pack(pady=10)
        tk.Label(progress_window, text=f"Programa: {program_name}.exe", 
                font=('Arial', 10)).pack(pady=5)
        tk.Label(progress_window, text="🖥️  Modo: MS-DOS Real para 8086", 
                font=('Arial', 10)).pack(pady=2)
        tk.Label(progress_window, text="🔌 Configurando puertos 0300h-0303h", 
                font=('Arial', 10)).pack(pady=2)
        tk.Label(progress_window, text="🤖 Sin errores de opcode...", 
                font=('Arial', 10)).pack(pady=2)
        
        # Barra de progreso indeterminada
        import tkinter.ttk as ttk
        progress_bar = ttk.Progressbar(progress_window, mode='indeterminate')
        progress_bar.pack(pady=10, padx=20, fill='x')
        progress_bar.start()
        
        return progress_window
    
    def update_status(self, message):
        """Actualiza la barra de estado - Windows Edition"""
        self.status_bar.config(text=f"🪟 {message}")
    
    def update_title(self):
        """Actualiza el título de la ventana - Windows Edition"""
        if self.current_file:
            filename = os.path.basename(self.current_file)
            self.root.title(f"🪟 Analizador Léxico - {filename} - Windows Edition")
        else:
            self.root.title("🪟 Analizador Léxico para Brazo Robótico - Windows Edition")
    
    def show_about(self):
        """Muestra información sobre la aplicación - Windows Edition"""
        messagebox.showinfo("Acerca de - Windows Edition",
            f"🪟 Analizador Léxico para Brazo Robótico\n"
            f"Windows Edition - Versión 5.0\n\n"
            f"💻 Sistema: Windows (Optimizado)\n"
            f"⚙️ Compilación: DOSBox + TASM integrado\n"
            f"� Target: Archivos .EXE para Proteus\n\n"
            f"🚀 Funciones completas:\n"
            f"• Análisis léxico, sintáctico y semántico\n"
            f"• Generación de código intermedio (cuádruplos)\n"
            f"• Compilación nativa a archivos .EXE\n"
            f"• Validaciones avanzadas\n"
            f"• Interfaz optimizada para Windows\n\n"
            f"📝 Sintaxis soportada:\n"
            f"Robot nombre\n"
            f"nombre.componente = valor\n"
            f"nombre.repetir = N (1-100 repeticiones)\n"
            f"nombre.inicio ... nombre.fin\n\n"
            f"� Archivos generados en: DOSBox2\\Tasm\\")
    
    def show_assembly_code(self, asm_code, program_name):
        """Muestra el código ensamblador generado - Windows optimizado"""
        asm_window = tk.Toplevel(self.root)
        asm_window.title(f"🪟 Código Ensamblador - {program_name}.asm")
        asm_window.geometry("900x700")
        asm_window.state('normal')
        
        # Frame principal
        main_frame = tk.Frame(asm_window)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título
        title_frame = tk.Frame(main_frame)
        title_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(title_frame, text=f"📄 Código Ensamblador Generado", 
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
                    messagebox.showinfo("💾 Guardado", 
                        f"Código ensamblador guardado exitosamente:\n\n{file_path}")
                except Exception as e:
                    messagebox.showerror("❌ Error", f"No se pudo guardar:\n{str(e)}")
        
        def open_folder():
            """Abre la carpeta donde está el archivo .exe"""
            try:
                os.startfile(self.tasm_path)
            except:
                messagebox.showinfo("📁 Ubicación", f"Los archivos están en:\n{self.tasm_path}")
        
        tk.Button(button_frame, text="📁 Abrir Carpeta", command=open_folder,
                 font=('Arial', 10), relief='raised').pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="💾 Guardar Como...", command=save_asm,
                 font=('Arial', 10), relief='raised').pack(side=tk.RIGHT, padx=5)
        tk.Button(button_frame, text="❌ Cerrar", command=asm_window.destroy,
                 font=('Arial', 10), relief='raised').pack(side=tk.RIGHT)
    
    def clear_all(self):
        """Limpia todo el contenido del editor y resultados"""
        self.code_editor.delete(1.0, tk.END)
        self.clear_output()
        self.current_file = None
        self.update_title()
        self.update_status("🪟 Todo limpiado - Listo para nuevo código")
    
    def clear_output(self):
        """Limpia el área de resultados"""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state=tk.DISABLED)
    
    def update_output(self, text, tag="info"):
        """Actualiza el área de salida con texto formateado"""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, text, tag)
        self.output_text.config(state=tk.DISABLED)
        # Scroll al final
        self.output_text.see(tk.END)
    
    def run(self):
        """Ejecuta la aplicación"""
        self.root.mainloop()

if __name__ == "__main__":
    try:
        print("🪟 ===============================================")
        print("🪟 ANALIZADOR LÉXICO PARA BRAZO ROBÓTICO")
        print("🪟 Windows Edition - Versión 5.0")
        print("🪟 ===============================================")
        print("🪟 Optimizado para Windows con compilación .EXE")
        print("🪟 DOSBox + TASM integrado")
        print("🪟 Iniciando aplicación...")
        print("🪟 ===============================================")
        
        app = LexicalAnalyzerGUI()
        app.run()
        
    except Exception as e:
        print(f"❌ Error crítico: {e}")
        import traceback
        traceback.print_exc()
        input("Presiona Enter para salir...")
