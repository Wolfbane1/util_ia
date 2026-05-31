# util_ia — Intelligent Automation Utilities

A collection of Python packages for AI-powered automation, transcription, translation, document processing, and digital monitoring. Built on Python 3.13 with local LLM inference via [Ollama](https://ollama.ai) and [MLX](https://github.com/ml-explore/mlx).

---

## Table of Contents

1. [service_manager](#1-service_manager)
2. [imagenes](#2-imagenes)
3. [traductor](#3-traductor)
4. [transcribe](#4-transcribe)
5. [incidencias](#5-incidencias)
6. [pdf2word](#6-pdf2word)
7. [cendilu](#7-cendilu)

---

## 1. service_manager

General-purpose utility packages providing core infrastructure services used across all vertical applications.

### 1.1 `file_manager.py`

PDF merging utility that walks a directory tree, collects all `.pdf` files within each subfolder, sorts them alphabetically, merges them into a single PDF, and saves it alongside the source files.

**Key function:**
- `concatenar_pdfs_en_directorios(directorio_raiz)` — Recursively processes subdirectories, merging PDFs per folder.

**Dependencies:** `PyPDF2`

---

### 1.2 `logs.py`

Logging infrastructure providing standardized log creation, configuration, and cleanup across all packages.

**Key functions:**
- `inicia_logs(log_level)` — Resets and reconfigures the root logger with a specified log level.
- `crea_log(log=logging.INFO, nombre="DEFECTO")` — Creates a named logger with a stream handler and formatter. Returns `(logger, handler)`.
- `cierra_log(logger, handler)` — Properly removes and closes a handler.
- `get_log(nombre)` — Retrieves an existing logger by name.

**Usage pattern:** All packages follow the `(logger, handler) = logs.crea_log(log, method)` → use → `logs.cierra_log(logger, handler)` pattern for clean resource management.

---

### 1.3 `mail_manager.py`

Email sending module via Gmail SMTP with SSL/TLS encryption. Supports multiple recipients, CC, and BCC with flexible input formats (comma-separated strings or lists).

**Key function:**
- `send_email(subject, body, to_email, log=None, cc=None, bcc=None)` — Sends an HTML email via Gmail's SMTP server (`smtp.gmail.com:587`).

**Features:**
- Recipient normalization (accepts strings with `,` or `;` separators, or lists/tuples).
- UTF-8 encoded subjects and HTML body.
- SSL context creation for secure connections.
- Full logging with method-level tracing.

**Note:** SMTP credentials are embedded in the source. For production use, externalize them via environment variables.

---

### 1.4 `ollama_manager.py`

The central LLM orchestration module. Provides a unified interface to multiple local and remote AI models through [Ollama](https://ollama.ai) and OpenAI-compatible APIs.

**Supported model families:**

| Family | Models |
|--------|--------|
| **Qwen** | `qwen2.5-coder:1.5b`, `qwen3:30b-a3b-thinking-2507-q4_K_M`, `qwen3:30b`, `qwen2.5vl:32b`, `qwen3-coder:latest` |
| **Microsoft** | `phi4:14b-q8_0` |
| **Mistral** | `mmistral-small3.2:latest`, `devstral:latest` |
| **Gemma** | `gemma3:27b` |
| **OpenAI** | `gpt-oss:latest` |

**Key classes:**
- `OllamaException` — Custom exception for Ollama API errors, carrying status code and response text.

**Key functions:**
- `call_ollama_api_request(model, message, tipo='generate', temperature=0.5)` — Low-level API call to Ollama's `/api/generate` or `/api/chat` endpoints. Returns the raw `requests.Response`.
- `procesa_output(response)` — Parses the JSON response, extracting content from either `message.content` or `response` keys.
- `separa_thinking_contenido(result)` — Splits `<think>...</think>\n<content>` formatted responses into thinking and content parts.
- `get_loaded_models()` — Lists all models currently loaded in the local Ollama instance.

**Thinking mode support:**
Models that support chain-of-thought reasoning return responses in the format:
```
<think><reasoning></think>
<actual content>
```

The `separa_thinking_contenido()` function parses this format, returning `(content_part, thinking_part)`.

**OpenAI-compatible API:**
Also supports the OpenAI API format via `http://localhost:11434/v1` with key `ollama`, enabling use of the `openai` Python client library with local models.

---

### 1.5 `youtube_manager.py`

YouTube video management module for downloading, listing, and querying video metadata from YouTube channels.

**Key functions:**
- `build_format_selector(resolution)` — Builds a yt-dlp format selector string prioritizing MP4/M4A containers at the requested resolution.
- `get_youtube_resolutions(youtube_url)` — Returns available video resolutions/formats for a given YouTube URL.
- `download_video_youtube(youtube_url, output_path="Downloads", resolution=None, cookies_file=None, cookies_from_browser=None)` — Downloads a YouTube video in MP4 format with configurable resolution, retry logic, and browser cookie support for authenticated/private content.
- `get_list_videos(channel_id, fromDays)` — Retrieves recent videos from a YouTube channel using the YouTube Data API.
- `get_video_visits(youtube_url)` — Retrieves view count metadata for a video.

**Features:**
- yt-dlp with Android/Web player client args for better extraction reliability.
- Browser cookie integration (`chrome`, `firefox`, `safari`) for authenticated downloads.
- Configurable resolution targeting (exact or best-available-below).
- Concurrent fragment downloads and 10-retry logic for robustness.
- Full logging with method-level tracing.

**Dependencies:** `yt-dlp`, `google-api-python-client`


## 2. imagenes

> ⚠️ **Under reconstruction** — This package is currently a placeholder and needs to be rebuilt as a proper `service_manager`-style package.

### 2.1 `genera_dibujos.ipynb`

Jupyter notebook for generating drawings/images. Currently contains a single notebook with no accompanying Python module.

**Status:** Requires refactoring into a dedicated Python module (e.g., `image_generator.py`) with proper class structure, logging, and error handling consistent with the `service_manager` pattern.

**Planned reconstruction:**
- Create a dedicated Python module with a class-based interface.
- Integrate with local image generation models (e.g., Stable Diffusion via MLX or Ollama-compatible vision models).
- Add logging infrastructure matching the `logs.py` pattern.
- Support configurable output formats and resolution parameters.

---

## 3. traductor

Document translation package using Ollama's translation models. Supports PDF, DOCX, and TXT files with intelligent chunking for large documents.

### 3.1 `document_translator.py`

Core translation engine implementing the `DocumentTranslator` class.

**Key class:**
- `DocumentTranslator(context_ratio=0.7, model='translate-gemma-27b')` — Initializes the translation engine with configurable context ratio and Ollama model.

**Key methods:**
- `set_context_ratio(ratio)` — Adjusts the context window ratio (0.0 < ratio ≤ 1.0).
- `get_supported_formats()` — Returns supported file formats: `['pdf', 'docx', 'txt']`.
- `get_supported_languages()` — Returns language name-to-code mapping (English, Spanish, French, German, Portuguese, Russian, Italian).
- `get_language_code(language_name)` — Converts a language name to its ISO code (e.g., `'Spanish'` → `'es'`).
- `translate_document(input_path, output_path, target_lang)` — Translates a document from its source language to the target language.

**Internal methods:**
- `_read_file(input_path)` — Dispatches to format-specific readers based on file extension.
- `_read_pdf(input_path)` — Extracts text from PDFs using `PyPDF2`.
- `_read_docx(input_path)` — Extracts text from DOCX files using `python-docx`.
- `_chunk_text(text)` — Splits large documents at sentence boundaries into chunks within the model's context window.
- `_translate_chunk(chunk, target_lang)` — Translates a single text chunk via Ollama.

**Supported formats:** PDF, DOCX, TXT
**Default model:** `translate-gemma-27b` (configurable)

### 3.2 `translate_pdf.py`

Standalone CLI script for translating PDF documents.

**Usage:**
```bash
python translate_pdf.py <archivo_entrada.pdf> <archivo_salida.pdf>
```

**Example:**
```bash
python translate_pdf.py documento_ingles.pdf documento_espanol.pdf
```

Translates from English to Spanish by default. Exits with error if the input file does not exist.

### 3.3 `exceptions.py`

Custom exception hierarchy for translation errors.

**Exception classes:**
- `TranslationException` — Base exception for all translation errors. Carries `message`, `errors`, and `messagio` fields.
- `TranslationUnsupportedFormatError(TranslationException)` — Raised when a file format is not supported. Carries `format` field.
- `TranslationAPIError(TranslationException)` — Raised on Ollama API communication errors (401, 429, 500). Carries `status_code` field.

---

## 4. transcribe

Audio transcription and speech-to-text package supporting multiple transcription engines (OpenAI Whisper and MLX Whisper), with audio preprocessing, chunking, and post-processing utilities.

### 4.1 `transcribe.py`

Core transcription engine with audio manipulation, chunking, and multi-engine transcription support.

**Audio constants:**
- `WHISPER_BASE = "base"`
- `WHISPER_MEDIUM = "medium"`
- `WHISPER_LARGE = "large-v2"`
- `MLX_WHISPER_LARGE = "large"`

**Audio manipulation functions:**
- `borrar_fichero(root, file_name, file_extension)` — Deletes a file from a specific directory. Warns (does not raise) if the file does not exist.
- `mover_ficheros(root, ficheros, dir_destino, borrar_transcripcion=True)` — Moves one or multiple files (and optionally their `.txt` transcription files) to a destination subdirectory within `root`.
- `unifica_ficheros_txt(root, lista_ficheros, duracion_segmento=-1)` — Merges multiple `.txt` transcription files into a single unified file, optionally adding time-range markers (e.g., `[0 - 10 minutes]`) when segments are involved.
- `convierte(root, file_name, file_extension, formato="m4a", formato_destino="mp3")` — Converts audio files between formats (e.g., M4A → MP3) using `pydub` or direct `ffmpeg` invocation for WMA files.
- `trocea_fichero(root, file_name, file_extension, duracion_segmento=15)` — Splits an audio file into fixed-duration fragments (default 15 minutes each), returning lists of fragment names and paths.

**Transcription functions:**
- `transcribe_audio_to_text(root, file, libreria="WHISPER", modelo=WHISPER_BASE, lengua="es", temperature=0, compression_ratio_threshold=2.5, wordtimestamp=True)` — Transcribes an audio file to text using either:
  - **WHISPER**: OpenAI Whisper via `whisper` library, with MPS (Metal) acceleration on macOS. Forces `float32` for MPS compatibility.
  - **MLX_WHISPER**: MLX Whisper via `mlx_whisper` library.
  Saves transcription as `.txt` alongside the audio file.
- `procesa_transcripcion(root, lista_ficheros, libreria="WHISPER", modelo=WHISPER_BASE, duracion_segmento=10)` — Orchestrates the full transcription pipeline: transcribes each fragment, unifies results, and moves processed files to a `procesado/` subdirectory.
- `amplifica_voz(root, file, file_extension)` — Amplifies/enhances voice in audio using `ffmpeg`'s `speechnorm` filter (`e=20:r=0.0003:l=1`).

**Dependencies:** `whisper`, `mlx_whisper`, `soundfile`, `torch`, `pydub`, `ffmpeg`

---

## 5. incidencias

IT incident analysis package using LLM-powered root cause analysis, classification, and solution proposal for ServiceNow-style incident tickets. Includes a Tkinter-based GUI application.

### 5.1 `incidencias.py`

Core incident analysis engine with LLM-powered root cause detection and classification.

**Prompt management:**
- `__set_prompt(tipo_prompt, prompt)` — Assigns prompts by type (`"Todas"` or `"Incidencia"`).
- `__get_prompt(tipo_prompt)` — Retrieves assigned prompts.

**Key functions:**
- `getIncidencias(url, fichero, lista_campos=["Número", "Descripción corta", "Notas de resolución"])` — Reads an Excel incident file, extracts specified fields, renames them to `id`, `desc`, `res`, adds a `status` column (default `"PEND"`), and returns `(json_list, DataFrame)`.
- `get_causa_raiz(desc, res, model="gemma3:27b", thinking=False, temperature=0.7)` — Analyzes an incident's description and resolution notes to:
  1. Classify the root cause into 14 predefined categories (Grupo 1–4, Faltan datos, Datos incorrectos, Problemas VPN/Teams/Conexión/Permisos/Software/Hardware/Configuración, Otros).
  2. Identify missing data (personal: DNI, email, phone; or non-personal: documents, case IDs).
  3. Detect workflow blockers (onboarding stalled, inactive licenses, missing access).
  4. Propose a concrete, actionable solution.
  5. Returns a JSON object with 12 fields: `classification`, `rootcause`, `solution`, `data_missing`, `personal_data`, `request_modification`, `workflow_stopped`, `previous_task_active`, `licence_inactive`, `upload_information`, `access_app_error`, `task_stopped`.

**Classification categories (14 total):**
1. Grupo 1 — Missing personal data (DNI, birthdate, email, phone)
2. Grupo 2 — Request to change process data (start/end dates, email)
3. Grupo 3 — Onboarding workflow not progressing
4. Grupo 4 — No access to portal or application
5–14. Faltan datos, Datos incorrectos, Problemas VPN/Teams/Conexión/Permisos/Software/Hardware/Configuración, Otros

**Features:**
- Thinking mode support via `thinking` parameter.
- JSON output with strict field ordering and Spanish-language values.
- Evidence-based boolean flags (`"S"`/`"N"`) with priority-based classification.

### 5.2 `incidencias_excel.py`

Extended incident analysis with additional prompt types and token estimation.

**Additional constants:**
- `PROMPT_TODOS = "Todos"`, `PROMPT_INCIDENCIAS = "Incidencia"`, `PROMPT_PROPUESTA = "Propuesta"`

**Additional function:**
- `__get_tokens(prompt: str)` — Estimates token count from prompt text (`ceil(word_count * 1.35)`).

Extends `incidencias.py` with proposal generation capabilities and token-aware prompt management.

### 5.3 `incidencias_manager.py`

Configuration-driven incident management with parameter loading from INI-style files.

**Key classes:**
- `IncidenciaException(Exception)` — Domain-specific exception with optional `causa` (original exception) field.
- `ParametrosIncidencias(fichero_apps="parametros/app.ini", fichero_prompts="parametros/prompts.ini")` — Loads and manages application configurations and prompts.

**Internal dictionaries:**
- `_apps: Dict[str, str]` — Application name-to-description mapping.
- `_prompts: Dict[str, Dict[str, str]]` — Nested prompt dictionary: `{app_name: {prompt_type: prompt_text}}`.

**Key methods:**
- `_loadApp(ruta_fichero)` — Loads apps from a JSON Lines file (each line: `{"nombre_app", "descripcion_app", "servicenow_id"}`).
- `_loadPrompts(ruta_fichero)` — Loads prompts from a JSON file with nested structure per application.
- `_setApp(nombre_app, descripcion_app)` — Adds/updates an app entry.
- `_getApp(nombre_app)` — Retrieves an app description (raises `KeyError` if not found).
- `_setPrompt(nombre_app, tipo_prompt, texto_prompt)` — Adds/updates a prompt for a specific app (type constrained to `PromptTipo`).

**Prompt types (`PromptTipo`):**
- `PROMPT_ANALIZA_TODAS` — Analyze all incidents summary.
- `PROMPT_ANALIZA_CAUSA_RAIZ` — Root cause analysis per incident.
- `PROMPT_GENERA_PROPUESTAS` — Generate solution proposals.
- `PROMPT_GENERA_PROMPT` — Dynamic prompt generation.
- `PROMPT_GENERA_DESC_SOL` — Calculate description/solution.
- `PROMPT_CONSOLIDA_ANALISIS_GENERAL` — Consolidate general analysis.

**Class:** `Incidencias` — Main incident processing class with configurable app, incident file, apps file, prompts file, and optional record limit.

### 5.4 `incidenciasAPP.py`

Tkinter-based GUI application for interactive incident analysis (version 0.3.0).

**Features:**
- Model selection (general and incident-specific models).
- Application selection dropdown.
- Excel file loading via file dialog.
- Single-pipeline execution: `main_incidencias(url, fichero, lista_campos, ...)`.
- Real-time thread-safe logging displayed in the GUI window.
- Settings editor (`settings.ini`) with configurable parameters:
  - `url_ia` — Ollama API URL (default: `http://localhost:11434`).
  - `path_salida` — Output directory.
  - `prompt1_defecto` / `prompt2_defecto` — Default prompts (supports file path or literal text).
  - `lista_campos` — Excel column names (default: `"Número, Descripción, Notas de resolución"`).
  - `thinking_incidencia` / `thinking_general` — Thinking mode toggles.
  - `temperature` — Model temperature (default: 0.7).

**Worker architecture:**
- Pipeline runs in a separate thread with a `QueueHandler` for thread-safe log forwarding to the GUI.
- Optional log file output (`incidencias_gui.log`).
- Graceful subprocess termination on window close.

**Global variables:**
- `modelos_general: list[str]` — Available general models.
- `modelos_incidencia: list[str]` — Available incident-specific models.
- `fichero_origen_path: str | None` — Selected Excel file path.

---

## 6. pdf2word

PDF-to-Word conversion package using MLX-powered vision language models (VLM) for OCR-based transcription of PDF pages into structured text and DOCX documents.

### 6.1 `extrae_pdf.py`

PDF transcription engine using MLX Vision Language Models for OCR-style page-by-page transcription.

**Key class:**
- `PDFTranscriber(pdf_path, output_dir, dpi=200, max_tokens=8192, temperature=0.0, prompt=None, overwrite=False, model_name=None, log_level=logging.INFO)` — Initializes the PDF transcription pipeline.

**Configuration:**
- `DEFAULT_PROMPT` — Instructions for literal, complete page transcription (no summarization, no correction, no added text).
- `DEFAULT_MODEL = "mlx-community/Qwen3.5-35B-A3B-4bit"` — Default MLX VLM model.
- `OLD_MODEL = "mlx-community/Qwen3.5-9B-MLX-4bit"` — Legacy model fallback.

**Private methods:**
- `_create_logger(log_level)` — Creates a named logger with stream handler and formatter.
- `_already_done(out_file, overwrite)` — Skips already-processed pages unless `overwrite=True`.
- `_render_page_to_pil(page, dpi)` — Renders a PDF page to a PIL `Image.Image` at the specified DPI (zoom factor = `dpi / 72.0`).
- `_save_page_image(image, output_dir)` — Saves the rendered page as PNG.
- `_save_text(text, path)` — Writes text content to a file.
- `_split_thinking_and_answer(text)` — Parses `<think>...</think>\n<answer>` format, returning `(thinking, answer)` tuple.
- `_build_prompt(processor, model, base_prompt)` — Applies the chat template expected by MLX-VLM for 1-image input.
- `_transcribe_page(image)` — Full page transcription: builds prompt, calls `mlx_vlm.generate()`, splits thinking/answer, handles retries (up to 3) for invalid responses.

**Public methods:**
- `process_pdf(start_page=None, end_page=None)` — Processes a PDF page-by-page:
  1. Renders each page to PNG at specified DPI.
  2. Transcribes each page using the configured MLX VLM.
  3. Saves transcription as `pagina_XXXX.txt` (with padding based on total page count).
  4. Saves thinking output as `pagina_XXXX.dbg`.
  5. Saves errors as `pagina_XXXX_error.txt` for failed pages.
  6. Retries up to 3 times for invalid responses (empty thinking or responses starting with "The user" or "<thinking>").
- `genera_docx()` — Combines all `pagina_*.txt` files (sorted by name) into a single `.docx` document with headings per page.

**Dependencies:** `fitz` (PyMuPDF), `mlx_vlm`, `PIL`, `python-docx`

---

## 7. cendilu

Digital sentinel package for monitoring YouTube channels for content related to a specific person (Lucía). Downloads videos, generates summaries using MLX vision models, and sends periodic email reports.

### 7.1 `cendilu.py`

YouTube monitoring and analysis engine for the "Digital Sentinel for Lucía" project.

**Configuration management:**
- `read_params(ruta_fichero)` — Reads a JSON Lines config file (each line: `{"id", "valor", "descripcion"}`). Creates the file with a default `ultima_ejecucion` value (current date + 7 days) if it does not exist. Returns `{id: [valor, descripcion]}`.
- `update_param(parametros, pid, nuevo_valor, nueva_descripcion=None)` — Updates a parameter's value (and optionally description) in the dictionary.
- `save_params(ruta_fichero, parametros)` — Writes the parameter dictionary back to a JSON Lines file.

**Video analysis functions:**
- `get_resumen_url(youtube_url, log=logging.INFO, resolution="480")` — Downloads a YouTube video at the specified resolution, generates a summary using the MLX vision model (`mlx-community/Qwen3.5-9B-MLX-4bit`), and deletes the temporary video file. Returns the summary text.
- `get_lista_urls(canales, fromDays, log=logging.INFO)` — Retrieves recent videos from a list of monitored YouTube channels (within `fromDays` days), enriching each video with `channel_id` and `channel_desc` metadata.

**Email report generation:**
- `generate_email_body(urls)` — Generates an HTML email body with per-channel tables containing: date, title, YouTube URL, view count, video summary, and whether Lucía appears in the video (`"Sí"`/`"No"` based on title keyword matching).

**Main entry point:**
- `main_comprueba_youtube_clase(log=logging.INFO, fromDays=None, ficheroIni='cendilu.ini')` — Orchestrates the full monitoring pipeline:
  1. Reads `cendilu.ini` to get the last execution timestamp.
  2. Retrieves all monitored channels from configuration.
  3. Fetches recent videos from all channels (since last execution).
  4. For each video: downloads, summarizes via MLX VLM, checks for Lucía's presence.
  5. Generates an HTML email report grouped by channel.
  6. Sends emails to two recipients (`zzddfge@gmail.com` and `mjgaray76@gmail.com`).
  7. Updates and saves the last execution timestamp in `cendilu.ini`.

### 7.2 `cendilu.ini`

Configuration file in JSON Lines format storing monitoring parameters.

**Example entry:**
```json
{"id": "ultima_ejecucion", "valor": "2026-01-10T16:19:43Z", "descripcion": "Fecha de última ejecución"}
```

**Current parameters:**
- `ultima_ejecucion` — Timestamp of the last monitoring run (used to determine which videos to check).

### 7.3 `cendilu.ipynb`

Jupyter notebook containing the interactive development version of the cendilu monitoring logic.

**Dependencies:** `youtube_manager`, `ollama_manager`, `mail_manager`, `logs`

