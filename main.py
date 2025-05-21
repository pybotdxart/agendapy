import readline
from huggingface_hub import InferenceClient, model_info
from config import API_HF
from ocr import convertir_imagen_a_texto
import os

MODELOS_DISPONIBLES = [
    "google/gemma-2b-it",
    "google/gemma-7b-it",
    "google/gemma-3-27b-it",
    "deepseek-ai/DeepSeek-V3-0324",
    "manycore-research/SpatialLM-Llama-1B",
]

# Autocompletado con tab
def completar_modelo(texto, estado):
    opciones = [m for m in MODELOS_DISPONIBLES if m.startswith(texto)]
    if estado < len(opciones):
        return opciones[estado]
    return None

readline.parse_and_bind("tab: complete")
readline.set_completer(completar_modelo)


def usar_chat():
    print("\n💬 CHAT CON IA (escribe 'salir' para volver al menú)")
    client = InferenceClient(provider="novita", api_key=API_HF)

    while True:
        prompt = input("🧑 Tú: ")
        if prompt.lower() == "salir":
            break

        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3-0324",
            messages=[{"role": "user", "content": prompt}],
        )

        #respuesta = completion.choices[0].message.content
        respuesta = completion.choices[0].message
        print(f"🤖 IA: {respuesta}\n")


def mostrar_lista_modelos():
    print("\n📜 Modelos disponibles:")
    for idx, modelo in enumerate(MODELOS_DISPONIBLES, 1):
        print(f"{idx}. {modelo}")

    seleccion = input("\n✍️ Escribe el nombre exacto del modelo para ver detalles (o Enter para volver): ").strip()
    if not seleccion:
        return

    try:
        info = model_info(seleccion, expand="inferenceProviderMapping")
        print(f"\n🔍 Providers para '{seleccion}':")
        for nombre, datos in info.inference_provider_mapping.items():
            print(f"🔹 {nombre} - status: {datos.status} - task: {datos.task}")
    except Exception as e:
        print(f"❌ Error al obtener info del modelo: {e}")

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        print("\n===============================")
        print("🧭 MENÚ PRINCIPAL HOLA XIMELIZA")
        print("===============================")
        print("1. 💬 Usar modelo de chat")
        print("2. 📦 Listar modelos y ver detalles")
        print("3. 🖼️ OCR (imagen a texto)")
        print("0. ❌ Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            usar_chat()
        elif opcion == "2":
            mostrar_lista_modelos()
        elif opcion == "3":
            convertir_imagen_a_texto()
        elif opcion == "0":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    limpiar_pantalla()
    menu()
