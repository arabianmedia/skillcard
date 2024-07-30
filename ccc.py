from PIL import Image, ImageDraw, ImageFont

def generate_certificate(name, course, date):
    certificate = Image.open("certificate_background.png")
    draw = ImageDraw.Draw(certificate)
    
    font = ImageFont.truetype("Roboto-Medium.ttf", 40)

    name_position = (400, 300)
    course_position = (400, 400)
    date_position = (400, 500)
    

    draw.text(name_position, f"Certificate of Completion\n\nThis is to certify that\n\n{name}", font=font, fill="black")
    draw.text(course_position, f"has completed the course\n\n{course}", font=font, fill="black")
    draw.text(date_position, f"Date: {date}", font=font, fill="black")
    
    certificate.save(f"{name}_certificate.png")

generate_certificate("John Doe", "Python Programming", "July 29, 2024")
