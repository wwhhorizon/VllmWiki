# vllm-project/vllm#7912: [Usage]: Confirm tool calling is not supported and this is the closest thing can be done

| 字段 | 值 |
| --- | --- |
| Issue | [#7912](https://github.com/vllm-project/vllm/issues/7912) |
| 状态 | closed |
| 标签 | usage;stale;tool-calling |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Confirm tool calling is not supported and this is the closest thing can be done

### Issue 正文摘录

Hi. LLM -> Llama-3.1-8B-Instruct In the vllm docs, it is said that: > Tool calling in the chat completion API > > vLLM supports only named function calling in the chat completion API. The tool_choice options auto and required are not yet supported but on the roadmap. > > To use a named function you need to define the function in the tools parameter and call it in the tool_choice parameter. > > It is the callers responsibility to prompt the model with the tool information, vLLM will not automatically manipulate the prompt. This may change in the future. > > vLLM will use guided decoding to ensure the response matches the tool parameter object defined by the JSON schema in the tools parameter. > > Please refer to the OpenAI API reference documentation for more information. 1. Can we confirm that this still holds? I see bunch of related PRs and good progress, so I'd like to be sure. 2. Since tool calling without named functions does not work, we can't use libraries/frameworks for Agentic AI such as AutoGen. Correct? For example, when this code is run (from AutoGen docs): ``` import os from autogen import UserProxyAgent, ConversableAgent from typing import Annotated, Literal Operator...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: is is the closest thing can be done usage;stale;tool-calling Hi. LLM -> Llama-3.1-8B-Instruct In the vllm docs, it is said that: > Tool calling in the chat completion API > > vLLM supports only named function calling in...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: . Correct? For example, when this code is run (from AutoGen docs): ``` import os from autogen import UserProxyAgent, ConversableAgent from typing import Annotated, Literal Operator = Literal["+", "-", "*", "/"] def calc...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: return a * b elif operator == "/": return int(a / b) else: raise ValueError("Invalid operator") # Let's first define the assistant agent that suggests tool calls. assistant = ConversableAgent( name="Assistant", system_m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: calling is not supported and this is the closest thing can be done usage;stale;tool-calling Hi. LLM -> Llama-3.1-8B-Instruct In the vllm docs, it is said that: > Tool calling in the chat completion API > > vLLM supports...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ********************* ``` But when I run it with my local LLM with vllm backend, it does not execute the function, it replies normally instead: (again, just a part of it) ``` >>>>>>>> USING AUTO REPLY... Assistant (to U...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
