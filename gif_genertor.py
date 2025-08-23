from PIL import Image

frames = []

for i in range(1, 5):
    new_frame = Image.open(f"img{i}.png")
    frames.append(new_frame)

frames[0].save("output.gif", save_all=True, append_images=frames[1:], duration=300, loop=0)

print("✅ GIF created as output.gif")