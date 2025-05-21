from PIL import Image
import pytesseract
import pyperclip
import os

# 🔧 CONFIGURA LA RUTA DE TESSERACT EN WINDOWS
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"

def convertir_imagen_a_texto():
    archivo_imagen = "agenda.jpg"
    archivo_salida = "agenda.ocr.txt"

    print("\n🖼️ OCR - Procesar imagen:", archivo_imagen)

    if not os.path.exists(archivo_imagen):
        print(f"❌ No se encontró el archivo '{archivo_imagen}' en el directorio actual.")
        return

    try:
        imagen = Image.open(archivo_imagen)
        texto = pytesseract.image_to_string(imagen, lang='spa')  # Cambia a 'eng' si quieres inglés

        with open(archivo_salida, "w", encoding="utf-8") as f:
            f.write(texto)

        pyperclip.copy(texto)

        print(f"✅ Texto extraído guardado en '{archivo_salida}' y copiado al portapapeles.")
        print("\n📄 Fragmento del texto extraído:\n")
        print(texto[:500] + ("..." if len(texto) > 500 else ""))

    except Exception as e:
        print("❌ Error procesando la imagen:", e)
