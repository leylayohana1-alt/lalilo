from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bal Dulce Edén</title>

    <style>

        body{
            margin:0;
            font-family:Arial;
            background:#fff3f7;
        }

        header{
            background:#ff4fa3;
            color:white;
            padding:20px;

            display:flex;
            justify-content:space-between;
            align-items:center;
        }

        .logo{
            font-size:30px;
            font-weight:bold;
        }

        nav a{
            color:white;
            text-decoration:none;
            margin:0 10px;
        }

        .hero{
            height:80vh;

            background:
            linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
            url('https://images.unsplash.com/photo-1551024601-bec78aea704b');

            background-size:cover;
            background-position:center;

            display:flex;
            justify-content:center;
            align-items:center;

            color:white;
            text-align:center;
        }

        .hero h1{
            font-size:55px;
        }

        .btn{
            background:#ff4fa3;
            color:white;

            padding:12px 25px;

            text-decoration:none;

            border-radius:10px;

            display:inline-block;
            margin-top:15px;
        }

        .productos{
            padding:60px 20px;
            text-align:center;
        }

        .grid{
            display:grid;

            grid-template-columns:
            repeat(auto-fit,minmax(250px,1fr));

            gap:20px;

            margin-top:30px;
        }

        .card{
            background:white;

            border-radius:10px;

            overflow:hidden;

            box-shadow:0 0 10px rgba(0,0,0,0.2);
        }

        .card img{
            width:100%;
            height:220px;
            object-fit:cover;
        }

        .card h3{
            color:#ff4fa3;
        }

        footer{
            background:#ff4fa3;
            color:white;

            text-align:center;

            padding:20px;

            margin-top:40px;
        }

    </style>

</head>

<body>

    <header>

        <div class="logo">
            🍰 Bal Dulce Edén
        </div>

        <nav>
            <a href="#">Inicio</a>
            <a href="#">Menú</a>
            <a href="#">Contacto</a>
        </nav>

    </header>

    <section class="hero">

        <div>

            <h1>
                Los pasteles más deliciosos 🍓
            </h1>

            <p>
                Endulzamos tus momentos especiales
            </p>

            <a href="#" class="btn">
                Ver menú
            </a>

        </div>

    </section>

    <section class="productos">

        <h2>Nuestros Productos</h2>

        <div class="grid">

            <div class="card">

                <img src="https://images.unsplash.com/photo-1578985545062-69928b1d9587">

                <h3>Pastel de Chocolate</h3>

            </div>

            <div class="card">

                <img src="https://images.unsplash.com/photo-1488477181946-6428a0291777">

                <h3>Cheesecake de Fresa</h3>

            </div>

            <div class="card">

                <img src="https://images.unsplash.com/photo-1464306076886-da185f6a9d05">

                <h3>Cupcakes Gourmet</h3>

            </div>

        </div>

    </section>

    <footer>
        © 2026 Bal Dulce Edén 🍰
    </footer>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)