# This is an additional feature for LCD in Ardupy on Wio Terminal

class LCD_print:
    def __init__(self, lcd, font_size, bg_color=None, fg_color=None):
        self.prints = []
        self.pl = 10 * font_size    # Per line has 10 pixels height per font size
        self.lcd = lcd
        if bg_color == None:
            self.bg_color = lcd.color.BLACK
            lcd.fillScreen(lcd.color.BLACK)
        else:
            self.bg_color = bg_color
            lcd.fillScreen(bg_color)
        lcd.setTextSize(font_size)
        if fg_color == None:
            lcd.setTextColor(lcd.color.GREEN)
        else:
            lcd.setTextColor(fg_color)
        self.line = 1
        self.line_limit = round(24/font_size)
    
    def println(self, text, l=None):
        if l == None:
            if self.line <= 0:
                self.lcd.drawString(str(text), 0, 0)
                self.line = 2
                self.prints.append(text)
            elif self.line > self.line_limit:
                self.prints.pop(0)
                self.prints.append(text)
                self.lcd.fillScreen(self.bg_color)
                for index, _ in enumerate(self.prints):
                    self.println(_, index)
                self.line += 1
                pass
            else:
                self.lcd.drawString(str(text), 0, self.pl*(self.line-1))
                self.line += 1
                self.prints.append(text)
        else:
            self.lcd.drawString(str(text), 0, self.pl*l)
            self.line += 1
