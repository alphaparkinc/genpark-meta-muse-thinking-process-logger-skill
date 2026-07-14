from client import MetaMuseThinkingProcessLoggerClient
client = MetaMuseThinkingProcessLoggerClient()
print(client.parse_reasoning("<thought>Analyzing inputs...</thought>Answer: 42"))