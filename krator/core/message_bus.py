import asyncio
from collections import defaultdict
from typing import Any, Dict, List

class MessageBus:
    """Simple asyncio-based publish/subscribe message bus."""

    def __init__(self) -> None:
        self._subs: Dict[str, List[asyncio.Queue]] = defaultdict(list)

    def subscribe(self, topic: str) -> asyncio.Queue:
        """Subscribe to a topic and return an asyncio.Queue for messages."""
        q: asyncio.Queue = asyncio.Queue()
        self._subs[topic].append(q)
        return q

    def unsubscribe(self, topic: str, queue: asyncio.Queue) -> None:
        """Remove a subscriber queue from a topic."""
        if topic in self._subs:
            self._subs[topic] = [q for q in self._subs[topic] if q is not queue]
            if not self._subs[topic]:
                del self._subs[topic]

    async def publish(self, topic: str, message: Any) -> None:
        """Publish a message to all subscribers of a topic."""
        for q in list(self._subs.get(topic, [])):
            await q.put(message)
