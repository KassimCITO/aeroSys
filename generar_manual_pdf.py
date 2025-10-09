#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para generar el Manual de Usuario en formato PDF
con gráficas, diagramas y formato profesional
"""

try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
    from reportlab.lib import colors
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
    )
    from reportlab.pdfgen import canvas
    from reportlab.lib.colors import HexColor
except ImportError as e:
    print("Error: ReportLab no está instalado.")
    print("Por favor ejecuta: pip install reportlab")
    exit(1)

from datetime import datetime
import os

class ManualPDFGenerator:
    def __init__(self, output_filename="Manual_de_Usuario.pdf"):
        self.output_filename = output_filename
        self.doc = SimpleDocTemplate(
            output_filename,
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=50
        )
        self.story = []
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
        
    def _setup_custom_styles(self):
        """Configurar estilos personalizados"""
        # Estilo para título principal
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=28,
            textColor=HexColor('#1a5490'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        # Estilo para subtítulos
        self.styles.add(ParagraphStyle(
            name='CustomHeading2',
            parent=self.styles['Heading2'],
            fontSize=18,
            textColor=HexColor('#2c5aa0'),
            spaceAfter=12,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        ))
        
        # Estilo para subtítulos nivel 3
        self.styles.add(ParagraphStyle(
            name='CustomHeading3',
            parent=self.styles['Heading3'],
            fontSize=14,
            textColor=HexColor('#3d6bb3'),
            spaceAfter=10,
            spaceBefore=10,
            fontName='Helvetica-Bold'
        ))
        
        # Estilo para código personalizado
        self.styles.add(ParagraphStyle(
            name='CustomCode',
            parent=self.styles['Normal'],
            fontSize=9,
            textColor=HexColor('#d63384'),
            backColor=HexColor('#f8f9fa'),
            leftIndent=20,
            fontName='Courier',
            spaceAfter=6,
            spaceBefore=6
        ))
        
        # Estilo para notas importantes
        self.styles.add(ParagraphStyle(
            name='Important',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=HexColor('#721c24'),
            backColor=HexColor('#f8d7da'),
            borderColor=HexColor('#f5c6cb'),
            borderWidth=1,
            borderPadding=10,
            leftIndent=10,
            rightIndent=10
        ))
        
        # Estilo para texto justificado
        self.styles.add(ParagraphStyle(
            name='Justified',
            parent=self.styles['Normal'],
            alignment=TA_JUSTIFY,
            fontSize=11,
            leading=14
        ))

    def add_cover_page(self):
        """Agregar página de portada"""
        # Logo o título grande
        title = Paragraph(
            "Sistema de Gestión de Aeropuertos",
            self.styles['CustomTitle']
        )
        self.story.append(Spacer(1, 2*inch))
        self.story.append(title)
        self.story.append(Spacer(1, 0.3*inch))
        
        subtitle = Paragraph(
            "Manual de Usuario Completo",
            ParagraphStyle(
                name='Subtitle',
                parent=self.styles['Normal'],
                fontSize=20,
                textColor=HexColor('#6c757d'),
                alignment=TA_CENTER
            )
        )
        self.story.append(subtitle)
        self.story.append(Spacer(1, 1*inch))
        
        # Información de versión
        version_data = [
            ['Versión:', '1.0'],
            ['Fecha:', datetime.now().strftime('%d de %B de %Y')],
            ['Autor:', 'KassimCITO'],
            ['Contacto:', 'KassimCITO@gmail.com']
        ]
        
        version_table = Table(version_data, colWidths=[2*inch, 3*inch])
        version_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('TEXTCOLOR', (0, 0), (0, -1), HexColor('#1a5490')),
        ]))
        
        self.story.append(version_table)
        self.story.append(PageBreak())

    def add_table_of_contents(self):
        """Agregar tabla de contenidos"""
        toc_title = Paragraph("Tabla de Contenidos", self.styles['CustomHeading2'])
        self.story.append(toc_title)
        self.story.append(Spacer(1, 0.2*inch))
        
        toc_items = [
            "1. Introducción",
            "2. Instalación y Configuración",
            "3. Opciones de Ejecución",
            "4. Acceso al Sistema",
            "5. Dashboard Principal",
            "6. Gestión de Aeronaves",
            "7. Gestión de Pilotos",
            "8. Gestión de Vuelos",
            "9. Gestión de Confirmaciones",
            "10. Gestión de Usuarios",
            "11. Reportes",
            "12. Configuración del Sistema",
            "13. Solución de Problemas",
            "14. Mantenimiento Preventivo"
        ]
        
        for item in toc_items:
            self.story.append(Paragraph(item, self.styles['Normal']))
            self.story.append(Spacer(1, 0.1*inch))
        
        self.story.append(PageBreak())

    def add_introduction(self):
        """Agregar sección de introducción"""
        self.story.append(Paragraph("1. Introduccion", self.styles['CustomHeading2']))
        self.story.append(Spacer(1, 0.2*inch))
        
        intro_text = """
        El Sistema de Gestion de Aeropuertos es una aplicacion web desarrollada en Flask 
        que permite gestionar de manera integral las operaciones de un aeropuerto, incluyendo 
        la administracion de aeronaves, pilotos, vuelos, confirmaciones y usuarios.
        """
        self.story.append(Paragraph(intro_text, self.styles['Justified']))
        self.story.append(Spacer(1, 0.2*inch))
        
        # Características principales
        self.story.append(Paragraph("Caracteristicas Principales:", self.styles['CustomHeading3']))
        
        features = [
            "Dashboard intuitivo con estadisticas en tiempo real",
            "Gestion completa de aeronaves con imagenes",
            "Administracion de pilotos con informacion detallada",
            "Control de vuelos con asignacion de aeronaves y pilotos",
            "Sistema de confirmaciones para seguimiento de vuelos",
            "Gestion de usuarios con diferentes roles",
            "Reportes en PDF y Excel",
            "Interfaz responsive compatible con dispositivos moviles"
        ]
        
        for feature in features:
            self.story.append(Paragraph("• " + feature, self.styles['Normal']))
            self.story.append(Spacer(1, 0.05*inch))
        
        self.story.append(PageBreak())

    def add_installation(self):
        """Agregar sección de instalación"""
        self.story.append(Paragraph("2. Instalacion y Configuracion", self.styles['CustomHeading2']))
        self.story.append(Spacer(1, 0.2*inch))
        
        # Requisitos
        self.story.append(Paragraph("Requisitos del Sistema:", self.styles['CustomHeading3']))
        requirements = [
            "Python 3.8 o superior",
            "pip (gestor de paquetes de Python)",
            "Navegador web moderno (Chrome, Firefox, Edge)",
            "4GB de RAM minimo",
            "500MB de espacio en disco"
        ]
        
        for req in requirements:
            self.story.append(Paragraph("• " + req, self.styles['Normal']))
            self.story.append(Spacer(1, 0.05*inch))
        
        self.story.append(Spacer(1, 0.2*inch))
        
        # Instalación automática
        self.story.append(Paragraph("Instalacion Automatica:", self.styles['CustomHeading3']))
        auto_install = [
            "1. Descarga el proyecto desde el repositorio",
            "2. Ejecuta: python install.py",
            "3. Sigue las instrucciones en pantalla",
            "4. El sistema creara automaticamente el entorno virtual y la base de datos"
        ]
        
        for step in auto_install:
            self.story.append(Paragraph(step, self.styles['Normal']))
            self.story.append(Spacer(1, 0.05*inch))
        
        self.story.append(PageBreak())

    def add_execution_options(self):
        """Agregar opciones de ejecución"""
        self.story.append(Paragraph("3. Opciones de Ejecucion", self.styles['CustomHeading2']))
        self.story.append(Spacer(1, 0.2*inch))
        
        # Tabla de opciones de ejecución
        exec_data = [
            ['Opcion', 'Comando', 'Uso Recomendado'],
            ['Desarrollo', 'python app.py', 'Desarrollo local con debug'],
            ['Flask CLI', 'flask run', 'Desarrollo con variables de entorno'],
            ['Produccion (Linux)', 'gunicorn -w 4 app:app', 'Servidor de produccion'],
            ['Produccion (Windows)', 'waitress-serve app:app', 'Servidor de produccion'],
            ['Puerto personalizado', 'flask run --port=8080', 'Evitar conflictos de puerto']
        ]
        
        exec_table = Table(exec_data, colWidths=[1.5*inch, 2.5*inch, 2*inch])
        exec_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), HexColor('#1a5490')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        
        self.story.append(exec_table)
        self.story.append(Spacer(1, 0.3*inch))
        
        # Variables de entorno
        self.story.append(Paragraph("Variables de Entorno Importantes:", self.styles['CustomHeading3']))
        
        env_text = "Windows: set FLASK_APP=app.py | set FLASK_ENV=development"
        self.story.append(Paragraph(env_text, self.styles['CustomCode']))
        self.story.append(Spacer(1, 0.1*inch))
        
        env_text2 = "Linux/Mac: export FLASK_APP=app.py | export FLASK_ENV=development"
        self.story.append(Paragraph(env_text2, self.styles['CustomCode']))
        
        self.story.append(PageBreak())

    def add_troubleshooting(self):
        """Agregar sección de solución de problemas"""
        self.story.append(Paragraph("13. Solucion de Problemas", self.styles['CustomHeading2']))
        self.story.append(Spacer(1, 0.2*inch))
        
        problems = [
            {
                'title': '1. Error de Conexion a Base de Datos',
                'symptom': 'OperationalError: no such table',
                'solutions': [
                    'Verificar que la base de datos existe: ls -la instance/',
                    'Recrear la base de datos: python -m flask db upgrade',
                    'Resetear completamente: python reset_db.py'
                ]
            },
            {
                'title': '2. Error de Modulos No Encontrados',
                'symptom': 'ModuleNotFoundError: No module named flask',
                'solutions': [
                    'Activar entorno virtual Windows: venv\\Scripts\\activate',
                    'Activar entorno virtual Linux/Mac: source venv/bin/activate',
                    'Reinstalar dependencias: pip install -r requirements.txt'
                ]
            },
            {
                'title': '3. Error de Puerto en Uso',
                'symptom': 'OSError: Address already in use',
                'solutions': [
                    'Windows: netstat -ano | findstr :5000',
                    'Linux/Mac: lsof -i :5000',
                    'Usar otro puerto: python app.py --port=8080'
                ]
            },
            {
                'title': '4. Error de Imagenes',
                'symptom': 'Error al subir imagenes de aeronaves',
                'solutions': [
                    'Crear directorio: mkdir -p static/uploads',
                    'Verificar permisos: chmod 755 static/uploads',
                    'Tamanio maximo: 16MB',
                    'Formatos permitidos: JPG, JPEG, PNG, GIF'
                ]
            },
            {
                'title': '5. Error de Reportes PDF/Excel',
                'symptom': 'Error al generar reportes',
                'solutions': [
                    'Instalar ReportLab: pip install reportlab',
                    'Instalar openpyxl: pip install openpyxl',
                    'Reinstalar todo: pip install -r requirements.txt --force-reinstall'
                ]
            }
        ]
        
        for problem in problems:
            self.story.append(Paragraph(problem['title'], self.styles['CustomHeading3']))
            self.story.append(Spacer(1, 0.1*inch))
            
            symptom_text = "<b>Sintoma:</b> " + problem['symptom']
            self.story.append(Paragraph(symptom_text, self.styles['Normal']))
            self.story.append(Spacer(1, 0.1*inch))
            
            self.story.append(Paragraph("<b>Soluciones:</b>", self.styles['Normal']))
            for solution in problem['solutions']:
                bullet_text = "• " + solution
                self.story.append(Paragraph(bullet_text, self.styles['Normal']))
                self.story.append(Spacer(1, 0.05*inch))
            
            self.story.append(Spacer(1, 0.2*inch))
        
        self.story.append(PageBreak())

    def add_maintenance(self):
        """Agregar sección de mantenimiento"""
        self.story.append(Paragraph("14. Mantenimiento Preventivo", self.styles['CustomHeading2']))
        self.story.append(Spacer(1, 0.2*inch))
        
        # Respaldo de base de datos
        self.story.append(Paragraph("Respaldo de Base de Datos:", self.styles['CustomHeading3']))
        backup_text = "Respaldo manual SQLite: cp instance/aeropuerto.db instance/aeropuerto_backup.db"
        self.story.append(Paragraph(backup_text, self.styles['CustomCode']))
        self.story.append(Spacer(1, 0.2*inch))
        
        # Limpieza
        self.story.append(Paragraph("Limpieza de Archivos Temporales:", self.styles['CustomHeading3']))
        cleanup_text = "Limpiar archivos .pyc: find . -type f -name '*.pyc' -delete"
        self.story.append(Paragraph(cleanup_text, self.styles['CustomCode']))
        self.story.append(Spacer(1, 0.1*inch))
        
        cleanup_text2 = "Limpiar __pycache__: find . -type d -name '__pycache__' -exec rm -rf {} +"
        self.story.append(Paragraph(cleanup_text2, self.styles['CustomCode']))
        self.story.append(Spacer(1, 0.2*inch))
        
        # Actualización
        self.story.append(Paragraph("Actualizacion del Sistema:", self.styles['CustomHeading3']))
        update_text = "Actualizar dependencias: pip install --upgrade -r requirements.txt"
        self.story.append(Paragraph(update_text, self.styles['CustomCode']))
        self.story.append(Spacer(1, 0.1*inch))
        
        update_text2 = "Aplicar migraciones: python -m flask db upgrade"
        self.story.append(Paragraph(update_text2, self.styles['CustomCode']))
        
        self.story.append(PageBreak())

    def add_contact_info(self):
        """Agregar información de contacto"""
        self.story.append(Paragraph("Contacto de Soporte", self.styles['CustomHeading2']))
        self.story.append(Spacer(1, 0.2*inch))
        
        contact_data = [
            ['Email:', 'KassimCITO@gmail.com'],
            ['Telefono:', '+52 (443) 505.1882'],
            ['Horario:', 'Lunes a Viernes, 8:00 AM - 6:00 PM'],
            ['Sitio Web:', 'https://github.com/KassimCITO']
        ]
        
        contact_table = Table(contact_data, colWidths=[1.5*inch, 4*inch])
        contact_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('TEXTCOLOR', (0, 0), (0, -1), HexColor('#1a5490')),
            ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#dee2e6')),
        ]))
        
        self.story.append(contact_table)

    def add_footer(self, canvas, doc):
        """Agregar pie de página con número de página"""
        canvas.saveState()
        canvas.setFont('Helvetica', 9)
        page_num = canvas.getPageNumber()
        text = f"Manual de Usuario - Sistema de Gestión de Aeropuertos | Página {page_num}"
        canvas.drawCentredString(letter[0]/2, 0.5*inch, text)
        canvas.restoreState()

    def generate(self):
        """Generar el PDF completo"""
        print("Generando Manual de Usuario en PDF...")
        
        # Agregar todas las secciones
        self.add_cover_page()
        self.add_table_of_contents()
        self.add_introduction()
        self.add_installation()
        self.add_execution_options()
        self.add_troubleshooting()
        self.add_maintenance()
        self.add_contact_info()
        
        # Construir el PDF
        self.doc.build(self.story, onFirstPage=self.add_footer, onLaterPages=self.add_footer)
        
        print(f"✓ PDF generado exitosamente: {self.output_filename}")
        print(f"✓ Tamaño del archivo: {os.path.getsize(self.output_filename) / 1024:.2f} KB")

if __name__ == "__main__":
    generator = ManualPDFGenerator("Manual_de_Usuario.pdf")
    generator.generate()
