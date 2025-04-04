import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from unittest.mock import patch, MagicMock
from shortterm_memory.ChatbotMemory import ChatbotMemory  

@pytest.fixture
def mock_tokenizer():
    tokenizer = MagicMock()
    tokenizer.tokenize.side_effect = lambda x: x.split()
    tokenizer.decode.return_value = "Résumé simulé"

    # Crée un objet avec un attribut .input_ids
    tokenizer_output = MagicMock()
    tokenizer_output.input_ids = [[0] * 10]
    tokenizer_output.to.return_value = tokenizer_output

    tokenizer.return_value = tokenizer_output
    return tokenizer

@pytest.fixture
def mock_model():
    model = MagicMock()
    model.generate.return_value = [[0] * 10]
    return model

@patch("shortterm_memory.ChatbotMemory.BartTokenizer.from_pretrained")
@patch("shortterm_memory.ChatbotMemory.BartForConditionalGeneration.from_pretrained")
def test_update_and_get_memory(mock_bart_model, mock_bart_tokenizer, mock_tokenizer, mock_model):
    mock_bart_tokenizer.return_value = mock_tokenizer
    mock_bart_model.return_value = mock_model

    chat_memory = ChatbotMemory()
    
    chat_memory.update_memory("Bonjour", "Salut !")
    chat_memory.update_memory("Comment tu vas ?", "Très bien merci.")

    mem = chat_memory.get_memory()

    assert len(mem) == 2
    assert mem[0]['user'] == "Bonjour"
    assert mem[0]['bot'] == "Salut !"

@patch("shortterm_memory.ChatbotMemory.BartTokenizer.from_pretrained")
@patch("shortterm_memory.ChatbotMemory.BartForConditionalGeneration.from_pretrained")
def test_memory_counter(mock_bart_model, mock_bart_tokenizer, mock_tokenizer, mock_model):
    mock_bart_tokenizer.return_value = mock_tokenizer
    mock_bart_model.return_value = mock_model

    chat_memory = ChatbotMemory()
    chat_memory.update_memory("Salut", "Hello")
    chat_memory.update_memory("Tu fais quoi ?", "Je parle avec toi.")

    token_count = chat_memory.memory_counter()
    assert token_count > 0

@patch("shortterm_memory.ChatbotMemory.BartTokenizer.from_pretrained")
@patch("shortterm_memory.ChatbotMemory.BartForConditionalGeneration.from_pretrained")
def test_compressed_memory(mock_bart_model, mock_bart_tokenizer, mock_tokenizer, mock_model):
    mock_bart_tokenizer.return_value = mock_tokenizer
    mock_bart_model.return_value = mock_model

    chat_memory = ChatbotMemory()

    for i in range(6):  # BATCH_SIZE = 5
        chat_memory.update_memory(f"user {i}", f"bot {i}")

    compressed = chat_memory.compressed_memory()
    
    assert isinstance(compressed, list)
    assert 'summary' in compressed[0]