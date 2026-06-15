# vllm-project/vllm#19419: [Bug]:  JSON decode error when tool call argument is empty

| 字段 | 值 |
| --- | --- |
| Issue | [#19419](https://github.com/vllm-project/vllm/issues/19419) |
| 状态 | closed |
| 标签 | bug;tool-calling |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  JSON decode error when tool call argument is empty

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When the arguments field in a tool_calls function call contains an empty value (as shown in this example JSON), the system fails with a JSON decoding error. I think it's normal to have no parameters. ​​Example of problematic input:​ ``` {'id': 'aNGJbCUkBrv1keAe', 'function': {'arguments': '', 'name': 'HftT4P3KiLurA0bm'}, 'type': 'function'} ``` ​Resulting error traceback:​ ``` Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/serving_chat.py", line 1) = await self._preprocess_chat( File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/serving_engine.py", line conversation, mm_data_future = parse_chat_messages_futures( File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/chat_utils.py", line 1177, in p _postprocess_messages(conversation) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/chat_utils.py", line 1132, in _ item["function"]["arguments"] = json.loads( File "/usr/lib/python3.12/json/__init__.py", line 346, in loads return _default_decoder.decode(s) File "/usr/lib/python3.12/json/decoder.py", line 338, in decode obj, end = self.ra...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your curre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: :​ ``` {'id': 'aNGJbCUkBrv1keAe', 'function': {'arguments': '', 'name': 'HftT4P3KiLurA0bm'}, 'type': 'function'} ``` ​Resulting error traceback:​ ``` Traceback (most recent call last): File "/usr/local/lib/python3.12/di...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: JSON decode error when tool call argument is empty bug;tool-calling ### Your current environment ### 🐛 Describe the bug When the arguments field in a tool_calls function call contains an empty value (as shown in...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
