# 📘 Changelog

All notable changes to this project will be documented in this file.

## [1.1.3] - 2025-04-03

### Added
- ✅ Unit test suite using `pytest` with fixtures and mocks.
- 🧪 Tests for `update_memory`, `get_memory`, `memory_counter`, and `compressed_memory`.
- 🔧 Editable install via `pip install -e .` for better developer experience.

### Changed
- 🔀 Refactored code to allow dependency injection and mocking.
- 🧩 Improved import paths using `package_dir={'': 'src'}` in `setup.py`.
- 📦 Mocked `tokenizer(...).to().input_ids` structure to match Hugging Face’s API.

### Fixed
- 🐛 Resolved `AttributeError` in tests caused by incorrect tokenizer mock return types.

---

## [1.1.2] - 2024-10-01

### Added
- 🚀 GPU support with automatic PyTorch device detection.
- 🧠 Batch-based summarization (BATCH_SIZE=5) for better performance.
- 📊 Token-based memory counter for more precise history handling.

### Changed
- 🧼 Refactored `update_memory` with dynamic compression and auto-trim.
- 🤖 Improved summarization using BART with optimized beam search.

### Fixed
- 📈 Enhanced logging for memory events (compression, trimming).
- 🧱 Better error handling during summarization operations.

---

## 🔧 How to use this file

1. 📌 **Met à jour ce fichier à chaque version.**
2. 🏷️ Quand tu crées une GitHub Release, **copie-colle la section correspondante**.
3. 🧪 Tu peux automatiser les entrées avec `commitizen`, `standard-version`, ou `semantic-release` si tu veux un workflow CI/CD plus complet.

---