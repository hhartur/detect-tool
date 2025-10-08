from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame
from PySide6.QtCore import QTimer, QPropertyAnimation, QRect, QEasingCurve, Qt
from PySide6.QtGui import QPainter, QLinearGradient, QColor, QPaintEvent

class SkeletonLoader(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(150)
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.setLoopCount(-1)
        
        self.gradient_position = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_gradient)
        self.timer.stop() # Start stopped, only animate when visible
        
        self.base_color = QColor(45, 45, 45) # Darker base for skeleton
        self.highlight_color = QColor(60, 60, 60) # Slightly lighter for animation
        
    def update_gradient(self):
        self.gradient_position = (self.gradient_position + 4) % (self.width() + 200) # Faster and wider sweep
        self.update()
        
    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), self.base_color)
        
        gradient = QLinearGradient(self.gradient_position - 100, 0, self.gradient_position + 100, 0)
        gradient.setColorAt(0, self.base_color)
        gradient.setColorAt(0.5, self.highlight_color)
        gradient.setColorAt(1, self.base_color)
        
        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)
        
        # Draw skeleton shapes
        painter.drawRect(20, 20, self.width() - 40, 20) # Title line
        painter.drawRect(20, 60, self.width() - 60, 15) # Detail line 1
        painter.drawRect(20, 90, self.width() - 80, 15) # Detail line 2
        painter.drawRect(20, 120, self.width() - 100, 15) # Detail line 3
        
    def start_animation(self):
        self.timer.start(30) # Faster update for smoother animation
        
    def stop_animation(self):
        self.timer.stop()
        self.gradient_position = 0 # Reset position
        self.update() # Redraw to static base color


