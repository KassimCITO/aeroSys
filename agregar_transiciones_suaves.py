#!/usr/bin/env python3
"""
Agregar transiciones CSS suaves a todos los formularios
"""

import os

# Estilos CSS para transiciones suaves
transition_styles = '''
        /* Transiciones suaves para formularios */
        .form-container {
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            transform-origin: top;
        }
        
        .form-container.hiding {
            opacity: 0;
            transform: translateY(-20px) scale(0.98);
            pointer-events: none;
        }
        
        .form-container.showing {
            animation: slideDown 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        @keyframes slideDown {
            from {
                opacity: 0;
                transform: translateY(-30px) scale(0.95);
            }
            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }
        
        /* Transición suave para botones */
        .btn {
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .btn:active {
            transform: scale(0.96);
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }
        
        /* Transición para cards */
        .card {
            transition: all 0.3s ease;
        }
        
        /* Modal transitions mejoradas */
        .modal.fade .modal-dialog {
            transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s ease;
        }
        
        .modal.show .modal-dialog {
            transform: scale(1);
        }
'''

# Funciones JavaScript mejoradas para transiciones
js_functions = '''
// Funciones mejoradas con transiciones suaves
function showFormWithTransition(formId, title) {
    var form = document.getElementById(formId);
    if (!form) return;
    
    // Agregar clase para animación
    form.classList.remove('hiding');
    form.style.display = 'block';
    
    // Forzar reflow para activar animación
    void form.offsetWidth;
    
    form.classList.add('showing');
    
    // Actualizar título si existe
    var formTitle = document.getElementById('formTitle');
    if (formTitle && title) {
        formTitle.textContent = title;
    }
    
    // Scroll suave al formulario
    setTimeout(function() {
        form.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 100);
}

function hideFormWithTransition(formId) {
    var form = document.getElementById(formId);
    if (!form) return;
    
    // Agregar clase de salida
    form.classList.add('hiding');
    form.classList.remove('showing');
    
    // Ocultar después de la animación
    setTimeout(function() {
        form.style.display = 'none';
        form.classList.remove('hiding');
    }, 400); // Duración de la transición
    
    // Scroll suave al inicio
    window.scrollTo({ top: 0, behavior: 'smooth' });
}
'''

templates_to_update = {
    'templates/aeronaves.html': {
        'formId': 'formArea',
        'hasCard': True
    },
    'templates/pilotos.html': {
        'formId': 'formArea',
        'hasCard': True
    },
    'templates/vuelos.html': {
        'formId': 'formCard',
        'hasCard': True
    },
    'templates/usuarios.html': {
        'formId': 'formArea',
        'hasCard': True
    },
    'templates/confirmaciones.html': {
        'formId': 'formArea',
        'hasCard': True
    }
}

for template_path, config in templates_to_update.items():
    if not os.path.exists(template_path):
        print(f"⚠️  {template_path} no encontrado")
        continue
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    form_id = config['formId']
    
    # 1. Agregar estilos CSS si no existen
    if 'form-container.hiding' not in content and '<style>' in content:
        content = content.replace('</style>', transition_styles + '\n    </style>', 1)
        print(f"✅ {template_path} - Estilos agregados")
    
    # 2. Agregar clase form-container al formulario
    if f'id="{form_id}"' in content and 'class="card' in content:
        # Buscar el div del card y agregar form-container
        import re
        pattern = f'(<div class="card[^"]*"[^>]*id="{form_id}")'
        if re.search(pattern, content):
            content = re.sub(
                pattern,
                f'\\1 form-container',
                content
            )
        else:
            # Intentar al revés (id antes de class)
            pattern = f'(<div[^>]*id="{form_id}"[^>]*class="card[^"]*")'
            content = re.sub(
                pattern,
                lambda m: m.group(0).replace('class="card', 'class="card form-container'),
                content
            )
        print(f"✅ {template_path} - Clase form-container agregada")
    
    # 3. Mejorar función showCreate
    old_show = f'''function showCreate() {{
    resetForm();
    document.getElementById('formTitle').textContent = '''
    
    if old_show in content:
        # Obtener el título completo
        import re
        match = re.search(r"document\.getElementById\('formTitle'\)\.textContent = '([^']+)';", content)
        if match:
            title = match.group(1)
            
            new_show = f'''function showCreate() {{
    resetForm();
    showFormWithTransition('{form_id}', '{title}');
    var saveBtn = document.querySelector('#{form_id} button.btn-success');
    if (saveBtn) saveBtn.onclick = save{template_path.split('/')[-1].replace('.html', '').capitalize()};
}}'''
            
            # Reemplazar toda la función showCreate
            pattern = r'function showCreate\(\) \{[^}]+\}'
            content = re.sub(pattern, new_show, content)
            print(f"✅ {template_path} - showCreate actualizada")
    
    # 4. Mejorar función hideForm
    old_hide = f'''function hideForm() {{
    resetForm();
    document.getElementById('{form_id}').style.display = 'none';
}}'''
    
    new_hide = f'''function hideForm() {{
    hideFormWithTransition('{form_id}');
    setTimeout(resetForm, 400);
}}'''
    
    if old_hide in content:
        content = content.replace(old_hide, new_hide)
        print(f"✅ {template_path} - hideForm actualizada")
    
    # 5. Agregar funciones JavaScript globales si no existen
    if 'function showFormWithTransition' not in content:
        # Buscar donde insertar (antes de la última función o antes de </script>)
        insert_pos = content.rfind('</script>')
        if insert_pos != -1:
            content = content[:insert_pos] + '\n' + js_functions + '\n' + content[insert_pos:]
            print(f"✅ {template_path} - Funciones de transición agregadas")
    
    # Guardar archivo actualizado
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("\n🎉 Transiciones suaves agregadas a todos los formularios!")
print("   ✨ Animaciones de entrada suaves")
print("   ✨ Animaciones de salida elegantes")
print("   ✨ Scroll automático al formulario")
print("   ✨ Efectos hover mejorados en botones")
