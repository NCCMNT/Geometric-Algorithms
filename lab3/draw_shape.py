import matplotlib.pyplot as plt

def draw_shape():
    points = []

    def onclick(event):
        if event.button == 1:
            x, y = event.xdata, event.ydata
            points.append((x,y))
            plt.plot(x,y,'bo')
            plt.draw()

    def on_key(event):

        if event.key == 'enter' and len(points) > 2:
            polygon_points = points + [points[0]]
            xs, ys = zip(*polygon_points)
            plt.plot(xs,ys, 'b-')
            plt.draw()

        elif event.key == 'r':
            points.clear()
            plt.cla()
            ax.set_title('Left click mouse to add point. "Enter" to draw polygon. "r" to reset drawing')
            ax.set_xlim(0,10)
            ax.set_ylim(0,10)
            plt.draw()

    fig, ax = plt.subplots()
    ax.set_title('Left click mouse to add point. "Enter" to draw polygon. "r" to reset drawing')
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)

    fig.canvas.mpl_connect('button_press_event', onclick)
    fig.canvas.mpl_connect('key_press_event', on_key)

    plt.show()
    return points