from typing import Any


class BaseAdapter:
    name: str = "base"

    def __init__(self, config: dict[str, Any] | None = None):
        self.config = config or {}

    def validate(self) -> bool:
        return True


class TelegramAdapter(BaseAdapter):
    name = "telegram"

    def send_message(self, chat_id: str, text: str) -> dict[str, Any]:
        return {"status": "queued", "chat_id": chat_id, "text": text, "provider": self.name}


class GeminiAdapter(BaseAdapter):
    name = "gemini"

    def generate(self, prompt: str) -> dict[str, Any]:
        return {"status": "ok", "provider": self.name, "response": f"Generated response for: {prompt}"}


class PaymentAdapter(BaseAdapter):
    name = "payment"

    def charge(self, amount: float, currency: str = "USD") -> dict[str, Any]:
        return {"status": "mock", "amount": amount, "currency": currency, "provider": self.name}


class SocialMediaAdapter(BaseAdapter):
    name = "social"

    def publish(self, message: str) -> dict[str, Any]:
        return {"status": "queued", "message": message, "provider": self.name}


class FastBotsAdapter(BaseAdapter):
    name = "fastbots"

    def trigger(self, payload: dict[str, Any]) -> dict[str, Any]:
        return {"status": "ok", "provider": self.name, "payload": payload}


class IntegrationRegistry:
    _adapters: dict[str, type[BaseAdapter]] = {
        "telegram": TelegramAdapter,
        "gemini": GeminiAdapter,
        "payment": PaymentAdapter,
        "social": SocialMediaAdapter,
        "fastbots": FastBotsAdapter,
    }

    @classmethod
    def get_adapter(cls, name: str, config: dict[str, Any] | None = None) -> BaseAdapter:
        adapter_cls = cls._adapters.get(name)
        if not adapter_cls:
            raise ValueError(f"Unsupported adapter: {name}")
        return adapter_cls(config)
