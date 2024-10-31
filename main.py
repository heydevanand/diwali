from PIL import Image, ImageDraw, ImageFont
from pyfiglet import figlet_format

def main():
    print(figlet_format("Happy Diwali!", font="big"))
    template = "template.png"
    output = f"greeting.jpg"
    name = input("Here's a little surprise for you.\nPlease enter your name: ").strip().title()
    create_greeting(template, output, name)

def create_greeting(template_path, output_path, name):
    # Load the template image
    try:
        template = Image.open(template_path)
    except FileNotFoundError:
        print("Template image not found. Please check the path.")
        return

    # Set up drawing context
    draw = ImageDraw.Draw(template)

    # Define font and size
    try:
        font = ImageFont.truetype("font.ttf", 90)
    except IOError:
        print("Font file not found. Make sure you have the font file in the directory.")
        return

    # Define text content and color
    text = name
    text_color = (0, 0, 0)

    # Calculate text size and position
    text_bbox = draw.textbbox((0, 0), text, font=font)  # Get the bounding box of the text
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    position = ((template.width - text_width) // 2, 672)

    # Add text to image
    draw.text(position, text, fill=text_color, font=font)

    # Save the edited image
    template.save(output_path)

if __name__ == "__main__":
    main()