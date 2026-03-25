import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random

def create_organic_blob(center, radius, points=10):
    """Generates a jittery, organic-looking polygon."""
    angles = np.linspace(0, 2 * np.pi, points, endpoint=False)
    # Add random variation to the radius at each angle
    distances = [radius * random.uniform(0.6, 1.4) for _ in angles]

    vertices = []
    for angle, dist in zip(angles, distances):
        x = center[0] + dist * np.cos(angle)
        y = center[1] + dist * np.sin(angle)
        vertices.append((x, y))

    return vertices

def draw_aaron_style(num_objects=15):
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    ax.axis('off') # Remove axes for an 'art' look

    # Cohen's palette: Bright primaries, pinks, and earth tones
    colors = ['#E63946', '#457B9D', '#F1FAEE', '#A8DADC', '#FFB703', '#FB8500', '#D00000', '#FF006E']
    hatches = ['//', '\\\\', '||', '--', '++', 'xx', 'oo', '..', '***']

    for _ in range(num_objects):
        center = (random.randint(10, 90), random.randint(10, 90))
        radius = random.randint(5, 15)
        verts = create_organic_blob(center, radius)

        # Decide the 'style' of this object
        style_choice = random.random()
        color = random.choice(colors)

        if style_choice < 0.4:  # Solid Fill
            poly = patches.Polygon(verts, closed=True, facecolor=color, edgecolor='black', lw=2)
        elif style_choice < 0.7:  # Hatched / Textured
            poly = patches.Polygon(verts, closed=True, facecolor='none', edgecolor='black',
                                   hatch=random.choice(hatches), lw=1.5)
            # Add a secondary color layer behind some hatches
            if random.random() > 0.5:
                ax.add_patch(patches.Polygon(verts, closed=True, facecolor=color, alpha=0.3))
        else:  # Outline Only
            poly = patches.Polygon(verts, closed=True, fill=False, edgecolor='black', lw=3)

        ax.add_patch(poly)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    draw_aaron_style(20)