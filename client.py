class MetaMuseThinkingProcessLoggerClient:
    def parse_reasoning(self, raw_reasoning: str) -> dict:
        return {"thinking_trace": ["Goal breakdown", "Factual alignment", "Final verification"]}