from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def convert_to_pdf(image_folder, output_filename):
    # Lista todos los archivos en la carpeta de imágenes
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    # Ordena los archivos para mantener el orden en el PDF
    image_files.sort()
    
    # Crea un nuevo archivo PDF
    c = canvas.Canvas(output_filename, pagesize=letter)
    
    # Define el tamaño de la página del PDF basado en la primera imagen
    first_image = Image.open(os.path.join(image_folder, image_files[0]))
    width, height = first_image.size
    c.setPageSize((width, height))
    
    # Agrega cada imagen al PDF
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        img = Image.open(image_path)
        c.drawInlineImage(image_path, 0, 0, width, height)
        c.showPage()
        print (".")
    
    # Guarda el PDF
    c.save()
    print("Archibo creado")

# Ejemplo de uso
if __name__ == "__main__":
    image_folder = "book"
    output_filename = "imagenes.pdf"
    convert_to_pdf(image_folder, output_filename)
