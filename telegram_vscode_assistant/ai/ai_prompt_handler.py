"""AI prompt handler using OpenAI API (Copilot-like code generation)."""
import logging
from ..config import OPENAI_API_KEY, OPENAI_MODEL

logger = logging.getLogger(__name__)


def generate_code(prompt: str) -> str:
    """Generate code using OpenAI API (GPT-4 or similar).
    
    Falls back to stub if API key is not configured.
    """
    if not OPENAI_API_KEY or OPENAI_API_KEY.startswith("sk-proj-YOUR"):
        logger.warning("OpenAI API key not configured. Using stub response.")
        return generate_code_stub(prompt)
    
    try:
        from openai import OpenAI
        
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful code generation assistant. Generate clean, production-ready code."
                },
                {
                    "role": "user",
                    "content": f"Generate code for: {prompt}\n\nProvide only the code, no explanations."
                }
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        code = response.choices[0].message.content.strip()
        logger.info("Generated code via OpenAI")
        return code
    except ImportError:
        logger.error("openai library not installed. Run: pip install openai")
        return generate_code_stub(prompt)
    except Exception as e:
        logger.error("OpenAI API error: %s. Using stub.", e)
        return generate_code_stub(prompt)


def generate_code_stub(prompt: str) -> str:
    """Fallback stub for when API is unavailable."""
    return f"\n// Generated code for: {prompt}\n// TODO: Implement this functionality\n"

