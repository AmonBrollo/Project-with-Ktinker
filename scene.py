#file name: scene.py
#author: Amon Brollo

import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Functions here for the scene to be drawn.
    draw_sky(canvas)

    star_x0 = 308
    star_y0 = 309
    star_x1 = 309
    star_y1 = 310
    draw_star(canvas, star_x0, star_y0, star_x1, star_y1)

    star_x0 = 24
    star_y0 = 45
    star_x1 = 26
    star_y1 = 47
    draw_star(canvas, star_x0, star_y0, star_x1, star_y1)

    star_x0 = 274
    star_y0 = 276
    star_x1 = 278
    star_y1 = 280
    draw_star(canvas, star_x0, star_y0, star_x1, star_y1)

    star_x0 = 524
    star_y0 = 166
    star_x1 = 527
    star_y1 = 169
    draw_star(canvas, star_x0, star_y0, star_x1, star_y1)

    cloud_x0 = 466
    cloud_y0 = 370
    cloud_x1 = 666
    cloud_y1 = 530
    draw_cloud(canvas, cloud_x0, cloud_y0,cloud_x1, cloud_y1)

    cloud_x0 = 390
    cloud_y0 = 390
    cloud_x1 = 576
    cloud_y1 = 500
    draw_cloud(canvas, cloud_x0, cloud_y0,cloud_x1, cloud_y1)
    
    cloud_x0 = 390
    cloud_y0 = 390
    cloud_x1 = 576
    cloud_y1 = 500
    draw_cloud(canvas, cloud_x0, cloud_y0,cloud_x1, cloud_y1)

    cloud_x0 = 476
    cloud_y0 = 390
    cloud_x1 = 850
    cloud_y1 = 600
    draw_cloud(canvas, cloud_x0, cloud_y0,cloud_x1, cloud_y1)

    cloud_x0 = 10
    cloud_y0 = 399
    cloud_x1 = 386
    cloud_y1 = 500
    draw_cloud(canvas, cloud_x0, cloud_y0,cloud_x1, cloud_y1)

    cloud_x0 = 197
    cloud_y0 = 365
    cloud_x1 = 406
    cloud_y1 = 500
    draw_cloud(canvas, cloud_x0, cloud_y0,cloud_x1, cloud_y1)

    draw_ground(canvas)

    tree_center = scene_left + 130
    tree_top = scene_top + 100
    tree_height = 600
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 200
    tree_top = scene_top + 240
    tree_height = 390
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 250
    tree_top = scene_top + 390
    tree_height = 200
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)


# Defined functions.
def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 3
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="#223127", width=1, fill="#223127")

def draw_sky(canvas):
    """Draw a sky.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a sky.
    Return: sky
    """
    sky = canvas.create_rectangle(0, 0, 800, 500, outline="#0D3B66", fill="#0D3B66")
    return sky

def draw_ground(canvas):
    """Draw the ground.
    Parameters
        canvas: The tkinter canvas where this
            function will draw the ground.
    Return: ground
    """
    ground = canvas.create_rectangle(0, 452, 800, 500, outline="#436436", fill="#436436")
    return ground

def draw_cloud(canvas, cloud_x0, cloud_y0,cloud_x1, cloud_y1):
    """Draw a cloud.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a cloud.
        cloud_x0: The x axis where the cloud will begin to be drawn.
        cloud_y0: The y axis where the cloud will begin to be drawn.
        cloud_x1: The x axis there the cloud will conclude being drawn.
        cloud_y1: The y axis there the cloud will conclude being drawn.
    Return: cloud
    """
    cloud = canvas.create_oval(cloud_x0, cloud_y0, cloud_x1, cloud_y1, outline="#72727E", fill="#72727E")
    return cloud

def draw_star(canvas, star_x0, star_y0, star_x1, star_y1):
    """Draw a star.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a star.
        star_x0: The x axis where the star will begin to be drawn.
        star_y0: The y axis where the star will begin to be drawn.
        star_x1: The x axis where the star will be done being drawn.
        star_y1: The x axis where the star will be done being drawn.
    Return: star
    """
    star = canvas.create_oval(star_x0, star_y0, star_x1, star_y1, outline="#F4D35E", fill="#F4D35E")
    return star

main()
