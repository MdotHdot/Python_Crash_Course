# tests the get_formatted_name function in name_function.py
def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    from name_function import get_formatted_name
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
    
def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    from name_function import get_formatted_name
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'