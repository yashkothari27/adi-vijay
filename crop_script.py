from PIL import Image

try:
    img = Image.open('emkG58dmDBzIOR2IP3Q1a9u4m4 (3).jpg')
    print(f"Original size: {img.size}")
    # The image width is 1828.
    # We want to find the girl portrait section.
    # Let's crop a few test images and output them to a tmp dir to verify.
    # Actually, we can just crop the central region of the "Creative Designer" section.
    img1 = img.crop((700, 250, 1500, 1050))
    img1.save('assets/girl-portrait-test1.jpg')
    
    # Also extract the tools section
    tools = img.crop((100, 700, 450, 1000))
    tools.save('assets/tools-test1.jpg')

    # Playlist section
    playlist = img.crop((1300, 200, 1750, 700))
    playlist.save('assets/playlist-test1.jpg')
    
    print("Cropped tests saved to assets/")
except Exception as e:
    print(f"Error: {e}")
