from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'ip-ingenieria-demo-secret-key'

SERVICES = [
    {
        'title': 'Planos de fabricación',
        'description': 'Desarrollo de planos técnicos para fabricación, montaje y producción con enfoque en claridad, detalle y trazabilidad.'
    },
    {
        'title': 'Cubicación y listas de materiales',
        'description': 'Cubicaciones completas, metrados, despieces y apoyo en presupuestos para proyectos metalmecánicos e industriales.'
    },
    {
        'title': 'Modelos para fundición',
        'description': 'Diseño de modelos para fundición, alimentación, mecanizados posteriores y documentación técnica asociada.'
    },
    {
        'title': 'Piezas mecanizadas',
        'description': 'Planos y modelado de piezas mecanizadas, ejes, soportes, acoples, conjuntos y componentes especiales.'
    },
    {
        'title': 'Estructuras metálicas',
        'description': 'Planos de estructuras, plataformas, soportes, pasarelas, barandas y elementos industriales.'
    },
    {
        'title': 'Fabricación a pedido',
        'description': 'Gestión de solicitudes para fabricar piezas y conjuntos según requerimiento del cliente y alcance del proyecto.'
    },
]

PROJECTS = [
    'Planos de piezas y conjuntos mecánicos',
    'Planos de modelos para fundición',
    'Cubicaciones para fabricación y montaje',
    'Planos de estructuras metálicas e industriales',
]

@app.route('/')
def index():
    return render_template('index.html', services=SERVICES, projects=PROJECTS)

@app.route('/cotizar', methods=['POST'])
def cotizar():
    nombre = request.form.get('nombre', '').strip()
    correo = request.form.get('correo', '').strip()
    telefono = request.form.get('telefono', '').strip()
    servicio = request.form.get('servicio', '').strip()
    mensaje = request.form.get('mensaje', '').strip()

    if not nombre or not correo or not mensaje:
        flash('Por favor completa nombre, correo y descripción del trabajo.', 'error')
        return redirect(url_for('index') + '#cotizacion')

    flash(
        f'Gracias, {nombre}. Tu solicitud fue registrada como demostración local. Luego podrás conectar este formulario a correo, WhatsApp o base de datos.',
        'success'
    )
    return redirect(url_for('index') + '#cotizacion')
    import os

    if __name__ == '__main__':
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)


