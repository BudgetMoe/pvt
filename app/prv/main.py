"""FastAPI app creation, logger configuration and main API routes."""

import llama_index
from launcher import create_app
from di import global_injector

# Add LlamaIndex simple observability
llama_index.set_global_handler("simple")

app = create_app(global_injector)
