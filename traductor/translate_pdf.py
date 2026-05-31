#!/usr/bin/env python3
"""
Script para traducir un documento PDF de inglés a español.

Uso:
    python translate_pdf.py <archivo_entrada.pdf> <archivo_salida.pdf>

Ejemplo:
    python translate_pdf.py documento_ingles.pdf documento_espanol.pdf
"""

import sys
import os
import logging

# Añadir directorio raíz al path para importar traductor
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from traductor.document_translator import DocumentTranslator


def main():
    """Traduce un documento PDF de inglés a español."""
    # Configurar logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Verificar argumentos
    if len(sys.argv) != 3:
        print("Uso: python translate_pdf.py <archivo_entrada.pdf> <archivo_salida.pdf>")
        print("\nEjemplo:")
        print("  python translate_pdf.py documento_ingles.pdf documento_espanol.pdf")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Verificar que el archivo de entrada existe
    if not os.path.exists(input_path):
        print(f"Error: El archivo '{input_path}' no existe.")
        sys.exit(1)

    print(f"Traduciendo: {input_path}")
    print(f"Salida: {output_path}")
    print("-" * 50)

    try:
        # Crear traductor con configuración por defecto
        translator = DocumentTranslator()

        # Traducir documento de inglés a español
        translator.translate_document(
            input_path=input_path,
            output_path=output_path,
            target_lang="Spanish"  # También se puede usar "es"
        )

        print("-" * 50)
        print(f"Documento traducido guardado en: {output_path}")

    except Exception as e:
        print(f"Error durante la traducción: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
