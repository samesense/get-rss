from smolagents import CodeAgent, HfApiModel

url = "https://www.nature.com/cgt/"
url = "https://www.mdpi.com/journal/genes"
url = "https://www.science.org/journal/stm"
url = "https://www.cell.com/cell-systems/home"
url = "https://www.sciencedirect.com/journal/cell-reports"
# model_id = "meta-llama/Llama-3.3-70B-Instruct"
#
# model = HfApiModel(model_id=model_id, token="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")
# agent = CodeAgent(tools=[], model=model, add_base_tools=True)
#
# agent.run(
#     "Could you give me the 118th number in the Fibonacci sequence?",
# )

# model = LiteLLMModel(model_id="ollama_chat/llama3.2", api_key="ollama")
m = "describeai/gemini-small"
m = "meta-llama/Llama-3.3-70B-Instruct"
# m = "microsoft/phi-4"
model = HfApiModel(model_id=m)
agent = CodeAgent(
    tools=[], model=model, additional_authorized_imports=["requests", "bs4"]
)
agent.run(
    f"Could you get me the url of the rss link of the page at url '{url}'? You might need to look in data-react-helmet elements."
)
