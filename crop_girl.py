from PIL import Image

try:
    img = Image.open('/Users/yashkothari/.gemini/antigravity/brain/c6f3db4d-b333-4778-baf8-48190ece7903/creative_designer_about_section_1774200266576.png')
    width, height = img.size
    print(f"Screenshot size: {width}x{height}")
    
    # The image is the full viewport width (~1280 or so) and height (~800)
    # The girl is right in the center. Let's crop the center third horizontally, and the middle portion vertically.
    x_center = width // 2
    y_center = height // 2
    
    # Let's crop a box around the center
    w_crop = 500
    h_crop = 650
    left = x_center - (w_crop // 2)
    top = y_center - (h_crop // 2) + 50 # adjust slightly down
    girl = img.crop((left, top, left+w_crop, top+h_crop))
    girl.save('/Users/yashkothari/Downloads/stitch_creative_designer_portfolio/assets/girl-portrait.jpg')
    print("Girl portrait saved properly.")
except Exception as e:
    print(f"Error: {e}")
