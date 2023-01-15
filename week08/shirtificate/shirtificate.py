from fpdf import FPDF


class Shirt:
    def __init__(self, name):
        self.name = name
        self.make()

    @classmethod
    def get(cls):
        name = input("Name: ").strip()
        return cls(name)

    def make(self):
        pdf = FPDF(orientation="portrait", format="A4")
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)

        # Set font and add as header of pdf
        pdf.set_font("helvetica", "B", size=42)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 50, border=0, txt="CS50 Shirtificate", align="C")

        # Add shirt and center image
        pdf.image("shirtificate.png", x=15, y=(297 / 4), w=180)

        # Set font of shirt and add on top
        pdf.set_font("helvetica", "B", size=32)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(-190, 300, border=0, txt=f"{self.name} took CS50", align="C")

        # Save the image as a PDF
        pdf.output("shirtificate.pdf")


def main():
    Shirt.get()


if __name__ == "__main__":
    main()
