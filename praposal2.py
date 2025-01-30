import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, FancyBboxPatch

def heart_shape(t):
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y

t = np.linspace(0, 2 * np.pi, 200)
x, y = heart_shape(t)

fig, ax = plt.subplots()
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_aspect('equal')
ax.axis('off')

# Heart drawing
line, = ax.plot([], [], 'r', lw=3)

# Text elements
text = ax.text(0, 0, '', fontsize=18, ha='center', va='center', color='red', fontweight='bold')
response_text = ax.text(0, -5, '', fontsize=22, ha='center', va='center', color='purple', fontweight='bold')

# Sparkle effect
sparkles = [ax.plot([], [], '*', color='yellow', markersize=5)[0] for _ in range(10)]

# Floating balloon
ball = Circle((0, -10), 0.5, color='pink')
ax.add_patch(ball)

def init():
    line.set_data([], [])
    text.set_text('')
    response_text.set_text('')
    ball.center = (0, -10)
    for sparkle in sparkles:
        sparkle.set_data([], [])
    return [line, text, response_text, ball] + sparkles

def update(frame):
    line.set_data(x[:frame], y[:frame])
    if frame > len(t) // 3:
        text.set_text("Will you be mine?")
        text.set_fontsize(20 + 2 * np.sin(frame / 10))  # Pulsating effect
    if frame > 2 * len(t) // 3:
        response_text.set_text("Yes! ❤️")
        response_text.set_fontsize(20 + 4 * np.sin(frame / 8))  # Animated effect
    
    # Balloon floating up
    ball.center = (x[frame % len(t)], y[frame % len(t)] - 5)
    
    # Sparkle effect
    for sparkle in sparkles:
        sparkle.set_data(np.random.uniform(-15, 15, 1), np.random.uniform(-15, 15, 1))
    
    return [line, text, response_text, ball] + sparkles

ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=False, interval=30)
plt.show()
