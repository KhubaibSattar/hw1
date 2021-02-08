def remove_channel(src: MyImage, red: bool = False, green: bool = False,blue: bool = False) -> MyImage:
    """Returns a copy of src in which the indicated channels are suppressed.
    Suppresses the red channel if no channel is indicated. src is not modified.
    Args:
    - src: the image whose copy the indicated channels have to be suppressed.
    - red: suppress the red channel if this is True.
    - green: suppress the green channel if this is True.
    - blue: suppress the blue channel if this is True.
    Returns:
    a copy of src with the indicated channels suppressed.
    """
    im = Image.open('MyImage.png')
    # rgb_image = im.convert('RGB')
    # width, height = im.size
    if im.mode == 'RGB':
        pass
    else:
        im = im.convert('RGB')
    # for i in range(width):
    #     for j in range(height):
    #         pix_rgb = rgb_image.getpixel((w,h))
    #         if red == True:

    #         if green == True:

    #         if blue == True:

    #         else:
    im_rgb_channels = im.copy()
    r,g,b = im_rgb_channels.split()
    if red == True:
        r = 0
    if green == True:
        g = 0
    if blue == True:
        b = 0
    else:
        r = 0
    
    im = im.merge('RGB', (r,g,b))
    print(im)

    # pass


def rotations(src: MyImage) -> MyImage:
    """Returns an image containing the 4 rotations of src.
    The new image has twice the dimensions of src. src is not modified.
    Args:
    - src: the image whose rotations have to be stored and returned.
    Returns:
    an image twice the size of src and containing the 4 rotations of src.
    """
    im = Image.open('MyImage.png')
    angle = 0
    while angle != 360:
        angle += 90
        rot_im = im.rotate(angle)
        print(rot_im)
        
    # pass


def apply_mask(src: MyImage, maskfile: str, average: bool = True) -> MyImage:
    """Returns an copy of src with the mask from maskfile applied to it.
    maskfile specifies a text file which contains an n by n mask. It has the
    following format:
    - the first line contains n
    - the next n^2 lines contain 1 element each of the flattened mask
    Args:
    - src: the image on which the mask is to be applied
    - maskfile: path to a file specifying the mask to be applied
    - average: if True, averaging should to be done when applying the mask
    Returns:
    an image which the result of applying the specified mask to src.
    """
    im = Image.open('MyImage.png')
    im_rgb = im.convert('RGB')
    if average == True:
        width, height = im.size()
        
        for i in range(width):
            for j in range(height):
                pix = im_rgb.getpixel((i,j))
                r,g,b = pix.split()
                
                sum = r + g + b
                avg = sum/ 3
                r = avg
                g = avg
                b = avg
            im = im.merge('RGB', (r,g,b))
        return im 
