import pytest
from interface import HeadlineLLM, HeadlineResponseHandler

def test_clean():                                                   # Test that whitespace/empty lines and lines beginning with '#' are removed
    handler = HeadlineResponseHandler("test_file.txt")
    lines = ["Headline 1  \n", "# asddfsa" ,'\n', "#  Comment", "Headline 2 "]
    clean_lines = handler.clean(lines)
    assert clean_lines == ["Headline 1", "Headline 2"]              # Assert the lines are cleaned properly
    
def test_clean_response():                                          # Test that list is made lowercase, and trailing whitespace is removed correctly
    llm = HeadlineLLM()
    unclean_response_list = [" Positive ", "NEGATIVE ", " neutral "]
    clean_response_list = llm.clean_response(unclean_response_list)
    assert clean_response_list == ["positive", "negative", "neutral"]