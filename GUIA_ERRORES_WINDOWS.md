# GUÍA DE SOLUCIÓN DE ERRORES EN WINDOWS

## 🚨 SI TIENES ERRORES DE COMPILACIÓN EN WINDOWS

El programa ha sido optimizado específicamente para Windows. Si experimentas errores de compilación, sigue esta guía paso a paso:

---

## ✅ SOLUCIÓN RÁPIDA (RECOMENDADA)

### 1. EJECUTAR REPARACIÓN AUTOMÁTICA
```
1. Clic derecho en "repair_dosbox.bat"
2. Seleccionar "Ejecutar como administrador"
3. Esperar a que termine el proceso
4. Ejecutar "start_analyzer.bat" normalmente
```

### 2. SI LA REPARACIÓN AUTOMÁTICA FALLA
```
1. Clic derecho en "start_analyzer.bat"
2. Seleccionar "Ejecutar como administrador"
3. Probar compilación
```

---

## 🔧 SOLUCIONES ESPECÍFICAS POR ERROR

### ERROR: "DOSBox no encontrado"
**Causa:** Archivos de DOSBox faltantes o corruptos
**Solución:**
1. Verificar que existe la carpeta `DOSBox2`
2. Verificar que existe `DOSBox2\dosbox.exe`
3. Si faltan archivos, descargar proyecto completo nuevamente

### ERROR: "Error de permisos" o "Access Denied"
**Causa:** Permisos insuficientes de Windows
**Solución:**
1. Clic derecho en la carpeta del proyecto
2. Propiedades → Seguridad → Editar
3. Seleccionar tu usuario
4. Marcar "Control total"
5. Aplicar y Aceptar

### ERROR: "DOSBox bloqueado" o se cierra inmediatamente
**Causa:** Windows Defender o antivirus bloqueando DOSBox
**Solución:**
1. Abrir Windows Defender Security Center
2. Protección antivirus y contra amenazas
3. Configuración de protección antivirus y contra amenazas
4. Exclusiones → Agregar exclusión → Carpeta
5. Seleccionar la carpeta completa del proyecto
6. Reiniciar y probar

### ERROR: "TASM no encontrado" o "TLINK no encontrado"
**Causa:** Archivos del compilador faltantes
**Solución:**
1. Verificar carpeta `DOSBox2\Tasm`
2. Debe contener: TASM.EXE, TLINK.EXE, COMPLINK.EXE
3. Si faltan, ejecutar `repair_dosbox.bat`

### ERROR: "Timeout en compilación"
**Causa:** DOSBox tarda mucho en responder
**Solución:**
1. Cerrar otros programas
2. Agregar exclusión de antivirus (ver arriba)
3. Ejecutar como administrador
4. Reiniciar Windows si persiste

---

## 📋 VERIFICACIÓN DE SISTEMA

### Archivos Requeridos
Verifica que existan estos archivos:
```
DOSBox2/
├── dosbox.exe                  ✓ Ejecutable principal
├── configuracion.conf          ✓ Configuración personalizada
└── Tasm/
    ├── TASM.EXE               ✓ Compilador
    ├── TLINK.EXE              ✓ Enlazador
    └── COMPLINK.EXE           ✓ Utilidad
```

### Scripts de Control
```
repair_dosbox.bat              ✓ Reparación automática
start_analyzer.bat             ✓ Inicio del programa
```

---

## 🖥️ REQUISITOS DEL SISTEMA

### Windows
- **Versión:** Windows 10 o superior
- **Arquitectura:** x64 (recomendado)
- **RAM:** Mínimo 4GB
- **Espacio:** 100MB libres

### Python
- **Versión:** Python 3.9 o superior
- **Instalación:** Desde python.org
- **PATH:** Debe estar en variables de entorno
- **Verificación:** `python --version` en cmd

### Permisos
- **Administrador:** Recomendado para primera ejecución
- **Antivirus:** Exclusión configurada para DOSBox2
- **Escritura:** Permisos completos en carpeta del proyecto

---

## 🚀 PROCESO DE COMPILACIÓN NORMAL

### Cuando Todo Funciona Correctamente:
1. **Cargar código:** Abrir archivo .robot
2. **Analizar:** Clic en "Analizar Código"
3. **Generar EXE:** Clic en "Generar .EXE"
4. **Ver resultado:** Archivo .exe en DOSBox2\Tasm\

### Mensajes de Éxito:
```
✓ Análisis léxico completado
✓ Análisis sintáctico exitoso  
✓ Validaciones semánticas OK
✓ Cuádruplos generados
✓ Código ensamblador creado
✓ Compilación exitosa: programa.exe
```

---

## 🆘 SI NADA FUNCIONA

### Reinstalación Completa:
1. Eliminar carpeta del proyecto actual
2. Descargar proyecto completo nuevamente
3. Extraer en ubicación sin espacios ni caracteres especiales
4. Ejecutar `repair_dosbox.bat` como administrador
5. Configurar exclusión de antivirus
6. Probar con `start_analyzer.bat`

### Contacto de Soporte:
Si persisten los problemas después de seguir esta guía:
1. Ejecutar `diagnose_compilation.py`
2. Copiar el resultado completo
3. Contactar con el desarrollador incluyendo:
   - Versión de Windows
   - Mensaje de error exacto
   - Resultado del diagnóstico
   - Pasos ya intentados

---

## ⚡ CONSEJOS DE RENDIMIENTO

### Para Compilaciones Más Rápidas:
1. Agregar exclusión de antivirus (más importante)
2. Ejecutar como administrador
3. Cerrar programas innecesarios
4. Usar nombres de archivo simples (sin espacios ni acentos)

### Mantenimiento:
- Ejecutar `repair_dosbox.bat` semanalmente
- Mantener Windows actualizado
- Verificar permisos después de actualizaciones de Windows
- Respaldar configuración cuando funcione correctamente

---

**Última actualización:** Diciembre 2024  
**Versión:** Windows Optimizada  
**Compatibilidad:** Windows 10/11 x64
