import re


def slugifyer(i_string):
    """

    :param i_string:
    :return slug:
    """
    slug = re.sub(r'[\s\_]', '-', i_string)
    slug = re.sub(r'[\é\è\ë\ê]', 'e', slug)
    slug = re.sub('[\à\â\ä]', 'a', slug)
    slug = re.sub('[\ç]', 'c', slug)
    return slug
