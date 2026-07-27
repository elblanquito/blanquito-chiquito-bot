# Blanquito Chiquito 💢
Blanquito Chiquito es un bot de Discord creado en Python con `discord.py`.

<img width="348" height="267" alt="image" src="https://github.com/user-attachments/assets/2a436d01-e9b6-4c40-9ec7-1bf81789eb04" />

## 🚀 Instalación

### 1. Requisitos previos
- [Python 3.11](https://www.python.org/downloads/) o superior instalado.
- Git (opcional, para clonar el repositorio).
- Una cuenta de Discord y una aplicación creada en el [Discord Developer Portal](https://discord.com/developers/applications).

### 2. Crear tu aplicación en Discord
1. Entra al [Discord Developer Portal](https://discord.com/developers/applications) y crea una **New Application**.
2. Ve a la pestaña **Bot** y presiona **Reset Token** para obtener tu token (guárdalo, lo usarás en el paso 4).
3. En la misma pestaña, activa el la opcion **Message Content Intent** (es obligatorio para que el bot lea comandos con prefijo).
4. Ve a **instalaciones**, abajo del todo en **Ámbitos** agrega la categoria de `bot` y en en **Permisos** agrega los permisos que quieres que tenga el bot, en la misma pestaña podras encontrar el **Enlace de instalación**

### 3. Clonar o descargar el proyecto
puedes descargarlo manualmente o descargarlo por la consola:
```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

### 4. Configurar el token
Crea un archivo llamado **`.env`** en la raíz del proyecto con el siguiente contenido:
```env
DISCORD_TOKEN=tu_token_aqui
```
> ⚠️ No dejes espacios alrededor del `=` y nunca subas este archivo a un repositorio público.

### 5. Instalar las dependencias
creamos un entorno virtual y luego instalamos las dependencias:
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```
```bash
pip install -r requirements.txt
```

### 6. Iniciar el bot
```bash
python main.py
```

La proxima vez que quieras encenderlo no necesitaras repetir todo el proceso para volver a encenderlo. Solo abre una consola en la carpeta del proyecto y ejecuta:
```bash
venv\Scripts\activate
```
```bash
python main.py
```

## 📜 Comandos disponibles
| Comando | Descripción |
|---|---|
| `.saluda` / `.ayuda` / `.help` | Muestra el mensaje de bienvenida y comandos. |
| `.blanco <mensaje>` | Repite el mensaje que le pases. |
| `.tomate` | Datos importantes sobre tomates 🍅. |
| `.suma <n1> <n2> ...` | Suma los números que le pases. |
| `.gato <texto opcional>` | Envía una imagen de un gato con un mensaje (via [cataas.com](https://cataas.com)). |

## 🛠️ Tecnologías usadas
- [discord.py](https://discordpy.readthedocs.io/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://pypi.org/project/requests/)
