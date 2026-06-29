from flask import Flask

app = Flask(__name__)

@app.route('/')
def obtener_saludo():
    # Aquí metemos el HTML y el CSS que verá el navegador web
    html_con_css = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Nota para el Ingeniero</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background: linear-gradient(135deg, #1e1e2f, #252542);
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: #ffffff;
            }
            .tarjeta {
                background-color: rgba(255, 255, 255, 0.05);
                backdrop-filter: blur(10px);
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
                border: 1px solid rgba(255, 255, 255, 0.1);
                text-align: center;
                max-width: 500px;
                animation: aparecer 1s ease-out;
            }
            h1 {
                font-size: 2.5rem;
                color: #00ffcc;
                margin-bottom: 20px;
                text-shadow: 0 0 10px rgba(0, 255, 204, 0.3);
            }
            p {
                font-size: 1.3rem;
                line-height: 1.6;
                color: #e0e0e0;
            }
            .badge {
                display: inline-block;
                margin-top: 20px;
                padding: 8px 15px;
                background-color: #ff3366;
                color: white;
                font-weight: bold;
                border-radius: 20px;
                font-size: 0.9rem;
            }
            @keyframes aparecer {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <div class="tarjeta">
            <h1>¡Mensaje del Sistema!</h1>
            <p>Hola ing pongame 10 no vale instalar el docker</p>
            <div class="badge">Despliegue Exitoso </div>
        </div>
    </body>
    </html>
    """
    return html_con_css

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)