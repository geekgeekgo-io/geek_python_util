import json
import svgwrite
import textwrap
import base64

class ImageMediaTools ():
    def font_to_base64(self, font_path):
        with open(font_path, "rb") as font_file:
            return base64.b64encode(font_file.read()).decode('utf-8')
    def calculate_font_size(self, text, max_width, max_height):
        font_size = 100
        wrapped_text = textwrap.wrap(text, width=30)
        while font_size > 10:
            total_height = len(wrapped_text) * (font_size * 1.2)
            if total_height <= max_height and max(len(line) for line in wrapped_text) * (font_size * 0.6) <= max_width:
                return font_size
            font_size -= 1
        return 10

    def create_svg(self, key, content, filename, font_path):
        dwg = svgwrite.Drawing(filename, size=(1200, 1200))

        font_base64 = self.font_to_base64(font_path)
        font_face = f"""
            @font-face {{
                font-family: 'Gotham';
                src: url(data:font/truetype;charset=utf-8;base64,{font_base64}) format('truetype');
                font-weight: normal;
                font-style: normal;
            }}
        """

        dwg.defs.add(dwg.style(font_face))

        dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='#112233'))

        max_width = 1000
        max_height = 1000
        font_size = self.calculate_font_size(content, max_width, max_height)

        # Convert content to string if it's a dictionary
        if isinstance(content, dict):
            content = json.dumps(content, indent=4)  # Convert dict to pretty JSON string

        text_box = dwg.add(dwg.g(font_family="Gotham", font_size=font_size, fill='#223344'))

        wrapped_text = textwrap.wrap(content, width=int(max_width / (font_size * 0.6)))

        line_height = font_size * 1.2
        total_height = len(wrapped_text) * line_height

        start_y = (1200 - total_height) / 2

        for i, line in enumerate(wrapped_text):
            text_box.add(dwg.text(line, insert=(600, start_y + i * line_height), text_anchor="middle"))

        title_font_size = min(60, font_size * 1.5)
        dwg.add(dwg.text(key.capitalize(), insert=(600, 80), font_family="Gotham", font_size=title_font_size,
                         fill='#223344', text_anchor="middle"))

        dwg.save()