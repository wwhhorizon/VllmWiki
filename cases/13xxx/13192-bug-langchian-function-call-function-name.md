# vllm-project/vllm#13192: [Bug]: 使用langchian function call 时function name 会重复导致调用失败

| 字段 | 值 |
| --- | --- |
| Issue | [#13192](https://github.com/vllm-project/vllm/issues/13192) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 使用langchian function call 时function name 会重复导致调用失败

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # 最小代码示例 from langchain_core.prompts import ChatPromptTemplate from langchain_core.prompts import MessagesPlaceholder from langchain_core.prompts import ( ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder, PromptTemplate ) from typing_extensions import Dict, Any, Union from pydantic import BaseModel from langchain_openai import ChatOpenAI from typing import List, Literal def structured_output(template: str, structure: Union[Dict[str, Any], BaseModel], structure_method: Literal["json_schema", "function_calling"] = "function_calling", **llm_params): """通用工具：创建一个结构化输出链，用于解析用户的输入。""" default_llm_params = { "model": MODEL_NAME, "streaming": False, "temperature": 0, } default_llm_params.update(llm_params) prompt = ChatPromptTemplate.from_messages([ MessagesPlaceholder(variable_name="chat_history"), HumanMessagePromptTemplate.from_template(template) ]) llm = ChatOpenAI(**default_llm_params) structured_llm = llm.with_structured_output(structure, method=structure_method) chain = prompt | structured_llm return chain # 问题 method = json_schema是正常工作，method = function_calling 就会出现 function name 不断重复情况，在其他使用langchain 进行functio...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: onment ### 🐛 Describe the bug # 最小代码示例 from langchain_core.prompts import ChatPromptTemplate from langchain_core.prompts import MessagesPlaceholder from langchain_core.prompts import ( ChatPromptTemplate, HumanMessagePr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: from typing_extensions import Dict, Any, Union from pydantic import BaseModel from langchain_openai import ChatOpenAI from typing import List, Literal def structured_output(template: str, structure: Union[Dict[str, Any]...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: 使用langchian function call 时function name 会重复导致调用失败 bug;stale ### Your current environment ### 🐛 Describe the bug # 最小代码示例 from langchain_core.prompts import ChatPromptTemplate from langchain_core.prompts import M...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ine 967, in consume_astream async for _ in event_streamer.tap_output_aiter(run_id, stream): File "/usr/local/lib/python3.11/site-packages/langchain_core/tracers/event_stream.py", line 203, in tap_output_aiter async for...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: mes ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
