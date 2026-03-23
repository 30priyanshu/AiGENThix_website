from fastapi import APIRouter, HTTPException

from app.core.config import settings
from app.schemas.chat import ChatRequest, ChatResponse

from google import genai
from google.genai import types as genai_types


router = APIRouter(prefix="/api/chat", tags=["chat"])


def _get_gemini_client() -> genai.Client:
    api_key = settings.GEMINI_API_KEY
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured on the server")
    return genai.Client(api_key=api_key)


@router.post("", response_model=ChatResponse)
async def chat_with_gemini(payload: ChatRequest) -> ChatResponse:
    """
    Chat endpoint used by the website chatbot.

    Guardrails:
    - Only answer using the provided `context` (RAG from website content)
    - If context is not enough, respond with a constrained fallback message
    """
    # Basic server-side guardrail: very short or empty input
    q = payload.question.strip()
    if not q or len(q) < 2:
        raise HTTPException(status_code=400, detail="Question is too short")

    try:
        client = _get_gemini_client()
    except RuntimeError as exc:
        # Make missing config obvious to frontend/dev
        raise HTTPException(status_code=503, detail=str(exc)) from exc

    system_prompt = (
        "You are the official AiGENThix website assistant.\n"
        "You MUST answer ONLY using the provided website context.\n"
        "If the context does not contain enough information to answer,\n"
        "say that you can only answer questions about AiGENThix and its website\n"
        "and suggest contacting info@aigenthix.com for more details.\n"
        "Do not invent details or discuss topics that are not in the context.\n"
        "\n"
        "Style:\n"
        "- Tone: professional, friendly, and confident.\n"
        "- Use short paragraphs. Use bullet points when listing features/capabilities.\n"
        "- If the user asks about a product, focus on that product’s capabilities from context.\n"
        "- If the user asks about services, answer from service context.\n"
        "- If the user asks about industries, answer from industry context.\n"
        "- If the user asks about core principles, answer from principles context.\n"
        "- If the user asks for contact details, provide phone/email/address from context.\n"
        "- If helpful, ask ONE brief follow-up question to clarify (only when context supports multiple options).\n"
    )

    user_content = (
        "Use ONLY the following website context to answer.\n\n"
        f"Website context:\n{payload.context}\n\n"
        f"User question:\n{payload.question}\n\n"
        "Write a natural, helpful answer. "
        "If the context does not contain the answer, say you can only answer "
        "questions about AiGENThix and suggest contacting info@aigenthix.com."
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_content,
            config=genai_types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.5,
                top_p=0.9,
                max_output_tokens=360,
            ),
        )
    except Exception as exc:  # pragma: no cover - runtime safety
        raise HTTPException(status_code=500, detail="Chat service error") from exc

    text = (response.text or "").strip()
    if not text:
        text = (
            "I can only answer questions about AiGENThix, our services, products, and "
            "information that appears on our website. "
            "Please contact info@aigenthix.com for more details."
        )

    return ChatResponse(answer=text)

