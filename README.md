# 🧪 LLM API Tester

Este proyecto es una suite de pruebas automatizadas para validar respuestas de modelos LLM utilizando las APIs de OpenAI, Claude (Anthropic) y Hugging Face.

---

## 🚀 Tecnologías utilizadas

- Python 3.10
- Pytest
- Docker
- OpenAI SDK
- Anthropic SDK
- Hugging Face Hub
- python-dotenv

---

## 🖥️ ¿Cómo correrlo localmente?

1. Clona el repositorio:
   ```bash
   git clone https://github.com/juliagomezg/llm_api_tester.git
   cd llm_api_tester
Crea un archivo .env con tus llaves de API:

ini
Copiar
Editar
OPENAI_API_KEY=tu_clave
ANTHROPIC_API_KEY=tu_clave
HUGGINGFACE_API_KEY=tu_clave
Activa un entorno virtual y ejecuta:

bash
Copiar
Editar
pip install -r requirements.txt
PYTHONPATH=. pytest
🐳 ¿Cómo usarlo con Docker?
Construye la imagen:

bash
Copiar
Editar
docker build -t llm-api-tester .
Corre los tests:

bash
Copiar
Editar
docker run --rm llm-api-tester
📁 Estructura del proyecto
bash
Copiar
Editar
llm_api_tester/
├── src/
│   └── llm_clients/
│       ├── openai_client.py
│       ├── claude_client.py
│       └── hf_client.py
├── tests/
│   ├── test_openai.py
│   ├── test_claude.py
│   └── test_huggingface.py
├── Dockerfile
├── requirements.txt
├── .env
└── README.md
✨ Autora
Proyecto creado como parte de mi aprendizaje en pruebas QA y modelos de lenguaje:

Julia Gómez
GitHub: @juliagomezg
