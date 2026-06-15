# vllm-project/vllm#26639: [Bug]: ValueError: No valid structured output parameter found

| 字段 | 值 |
| --- | --- |
| Issue | [#26639](https://github.com/vllm-project/vllm/issues/26639) |
| 状态 | closed |
| 标签 | bug;structured-output |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: No valid structured output parameter found

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm will crash when `"response_format": {"type":"text"}` is in chat completions request. The value 'text' is a valid option for the `type` in `ResponseFormat`. However, in the new `to_sampling_params()` code(https://github.com/vllm-project/vllm/blob/v0.11.0/vllm/entrypoints/openai/protocol.py#L727), whenever `response_format` is not empty, a value is assigned to `self.structured_outputs`, which leads to a validation error. sample request: ```json { "model":"DeepSeek-V3.2-Exp", "messages": [{"role":"user","content":"hello"}], "max_tokens":2048, "stream":false, "response_format":{"type":"text"} } ``` crash logs here: ```text (EngineCore_DP0 pid=80621) Process EngineCore_DP0: (EngineCore_DP0 pid=80621) Traceback (most recent call last): (EngineCore_DP0 pid=80621) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP0 pid=80621) self.run() (EngineCore_DP0 pid=80621) File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_DP0 pid=80621) self._target(*self._args, **self._kwargs) (EngineCore_DP0 pid=80621) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/co...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory;speculative_decoding cuda;operator;triton build_error;c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: l crash when `"response_format": {"type":"text"}` is in chat completions request. The value 'text' is a valid option for the `type` in `ResponseFormat`. However, in the new `to_sampling_params()` code(https://github.com...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: environment ### 🐛 Describe the bug vllm will crash when `"response_format": {"type":"text"}` is in chat completions request. The value 'text' is a valid option for the `type` in `ResponseFormat`. However, in the new `to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: orting;model_support;scheduler_memory;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
