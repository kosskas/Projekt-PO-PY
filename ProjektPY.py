from Silnik.Swiat import *
from Rosliny import *
from Zwierzeta import *


def main():
    app = QApplication([])
    S = Swiat(20, 20)
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()
