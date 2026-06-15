# vllm-project/vllm#21042: [Bug]: I use the Qwen2.5-14B with tool. It can't call more than one tool.

| 字段 | 值 |
| --- | --- |
| Issue | [#21042](https://github.com/vllm-project/vllm/issues/21042) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: I use the Qwen2.5-14B with tool. It can't call more than one tool.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python import asyncio from typing import Literal from langchain_core.messages import HumanMessage from langchain_core.tools import tool from langchain_openai import ChatOpenAI from langgraph.checkpoint.memory import MemorySaver from langgraph.graph import END, StateGraph, MessagesState from langgraph.prebuilt import ToolNode @tool def search(query:str): """ 查询问题中提到的城市天气 :param query: :return: """ if "上海" in query.lower() or "shanghai" in query.lower(): return "现在30°,有雾" return "现在是35°,阳光明媚。" @tool def suggest(pos:str, weather:str): """ 根据地点和当地天气给我出行建议 :param :return: """ return f"{pos} 地点的天气{weather}, 高温黄色预警，出门记得带伞，避免晒伤" tools = [search,suggest] tool_node = ToolNode(tools) model = ChatOpenAI(model="qwen2.5-14b-instruct", temperature=0, streaming=False).bind_tools(tools) def should_continue(state: MessagesState) -> Literal["tools", END]: message = state['messages'] last_message = message[-1] if last_message.tool_calls: return "tools" return END def call_model(state:MessagesState): message = state['messages'] print("====") print(message) print("====") response = model.invoke(message) return {"messages": [response]} async def mai...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: stale ### Your current environment ### 🐛 Describe the bug ```python import asyncio from typing import Literal from langchain_core.messages import HumanMessage from langchain_core.tools import tool from langchain_openai...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: I use the Qwen2.5-14B with tool. It can't call more than one tool. bug;stale ### Your current environment ### 🐛 Describe the bug ```python import asyncio from typing import Literal from langchain_core.messages im...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: : I use the Qwen2.5-14B with tool. It can't call more than one tool. bug;stale ### Your current environment ### 🐛 Describe the bug ```python import asyncio from typing import Literal from langchain_core.messages import...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: raph, MessagesState from langgraph.prebuilt import ToolNode @tool def search(query:str): """ 查询问题中提到的城市天气 :param query: :return: """ if "上海" in query.lower() or "shanghai" in query.lower(): return "现在30°,有雾" return "现在是...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
