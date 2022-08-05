def is_a_texture(name):
    """ 
    Check if it's a texture by counting the number of parts for the model
    :param name: the name of the model
    :return: True if it's a texture, False otherwise
    """
    length = len(name.split('_'))

    if length > 3:
        return True
    else:
        return False