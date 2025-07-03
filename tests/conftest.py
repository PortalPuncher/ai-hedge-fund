import sys
from types import ModuleType

# Stub pandas
pd_stub = ModuleType("pandas")
pd_stub.DataFrame = object
pd_stub.Series = object
pd_stub.to_datetime = lambda x, *a, **k: x
pd_stub.to_numeric = lambda x, *a, **k: x
sys.modules.setdefault("pandas", pd_stub)

# Stub rich modules used by progress
class Console:
    def __init__(self, *a, **k):
        pass
class Live:
    def __init__(self, *a, **k):
        pass
    def start(self):
        pass
    def stop(self):
        pass
class Table:
    def __init__(self, *a, **k):
        self.columns = []
    def add_column(self, *a, **k):
        pass
    def add_row(self, *a, **k):
        pass
class Style:
    def __init__(self, *a, **k):
        pass
class Text:
    def __init__(self, *a, **k):
        pass
    def append(self, *a, **k):
        pass
rich_console = ModuleType("rich.console"); rich_console.Console = Console
rich_live = ModuleType("rich.live"); rich_live.Live = Live
rich_table = ModuleType("rich.table"); rich_table.Table = Table
rich_style = ModuleType("rich.style"); rich_style.Style = Style
rich_text = ModuleType("rich.text"); rich_text.Text = Text
sys.modules.setdefault("rich.console", rich_console)
sys.modules.setdefault("rich.live", rich_live)
sys.modules.setdefault("rich.table", rich_table)
sys.modules.setdefault("rich.style", rich_style)
sys.modules.setdefault("rich.text", rich_text)

# Stub pydantic
pydantic_stub = ModuleType("pydantic")
class BaseModel:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
    def model_dump(self):
        return self.__dict__
    def json(self):
        import json
        return json.dumps(self.model_dump())

pydantic_stub.BaseModel = BaseModel
pydantic_stub.Field = lambda *a, **k: None
sys.modules.setdefault("pydantic", pydantic_stub)

# Stub langchain_core modules
lang_msgs = ModuleType("langchain_core.messages")
class HumanMessage:
    def __init__(self, content=None, name=None):
        self.content = content
        self.name = name
lang_msgs.HumanMessage = HumanMessage
sys.modules.setdefault("langchain_core.messages", lang_msgs)

lang_prompts = ModuleType("langchain_core.prompts")
class ChatPromptTemplate:
    @classmethod
    def from_messages(cls, messages):
        return cls()
    def invoke(self, data):
        return data
lang_prompts.ChatPromptTemplate = ChatPromptTemplate
sys.modules.setdefault("langchain_core.prompts", lang_prompts)

# Stub langchain provider packages used by src.llm.models
for name in [
    "langchain_anthropic",
    "langchain_deepseek",
    "langchain_google_genai",
    "langchain_groq",
    "langchain_openai",
    "langchain_ollama",
]:
    sys.modules.setdefault(name, ModuleType(name))

# Add BaseMessage for graph.state imports
class BaseMessage:
    pass
lang_msgs.BaseMessage = BaseMessage

# Stub requests module
requests_stub = ModuleType("requests")
def _dummy(*a, **k):
    raise RuntimeError("request called without patching")
requests_stub.get = _dummy
requests_stub.post = _dummy
sys.modules.setdefault("requests", requests_stub)
requests_stub.Response = type('Response', (), {})

# Provide dummy classes for langchain provider stubs
for name in [
    "langchain_anthropic",
    "langchain_deepseek",
    "langchain_google_genai",
    "langchain_groq",
    "langchain_openai",
    "langchain_ollama",
]:
    mod = sys.modules[name]
    mod.ChatAnthropic = type('ChatAnthropic', (), {})
    mod.ChatDeepSeek = type('ChatDeepSeek', (), {})
    mod.ChatGoogleGenerativeAI = type('ChatGoogleGenerativeAI', (), {})
    mod.ChatGroq = type('ChatGroq', (), {})
    mod.ChatOpenAI = type('ChatOpenAI', (), {})
    mod.ChatOllama = type('ChatOllama', (), {})
import sys, types; import types; sys.modules.setdefault("numpy", types.ModuleType("numpy"))

# Simplified Price and PriceResponse models
from src.data import models as data_models

class Price(BaseModel):
    def __init__(self, **k):
        for key, val in k.items():
            setattr(self, key, val)
    def model_dump(self):
        return self.__dict__

class PriceResponse(BaseModel):
    def __init__(self, **k):
        self.ticker = k.get('ticker')
        self.prices = [Price(**p) for p in k.get('prices', [])]

data_models.Price = Price
data_models.PriceResponse = PriceResponse
