import accept_headers as ah
import pytest

def empty_language():
    return []

def english_language():
    return ['en', 'en-US']

def all_language():
    return ['en', 'en-US', 'fr']

class TestAcceptHeaders:
    def test_empty(self):
        assert ah.accept_header(empty_language()) == False
    
    def test_response(self):
        #print(*english_language)
        assert ah.accept_header(english_language()) == 200
    
    def test_language_filter(self):
        assert ah.get_filtered_languages(all_language(), '^en.*') == ['en', 'en-US']
