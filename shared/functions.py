def is_a_texture(name):
    """ 
    Check if it's a texture by counting the number of parts for the model
    :param name: the name of the model
    :return: True if it's a texture, False otherwise
    """
    if "_diff_" in name:
        return True
    return False


def is_a_prop(ped):
    if ped.endswith('_p') or "_p_" in ped:
        return True
    return False


def clean_ped_name(ped, is_a_prop):
    if ped.startswith('mp_'):
        p = ped.split('_')

        if is_a_prop:
            return '_'.join(p[:5])

        return '_'.join(p[:4])

    return ped
