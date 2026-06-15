# vllm-project/vllm#33921: [Bug]: Qwen3 Instruct context is limited to 8K

| 字段 | 值 |
| --- | --- |
| Issue | [#33921](https://github.com/vllm-project/vllm/issues/33921) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | fp8 |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3 Instruct context is limited to 8K

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am facing some longer context issues with `Qwen/Qwen3-4B-Instruct-2507-FP8`. The official supported context-size is 256K. However, whatever I set as max `max-model-len`, I get: ``` This model's maximum context length is 8192 tokens. ``` For example, setting `--max-model-len: 262144`, `/v1/models` returns `"max_model_len":262144` which is correct, but running a request with a single 10k tokens prompt I get ``` {'error': {'message': "This model's maximum context length is 8192 tokens. However, your request has 10031 input tokens. Please reduce the length of the input messages. (parameter=input_tokens, value=10031) None", 'type': 'BadRequestError', 'param': None, 'code': 400}} ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: I am facing some longer context issues with `Qwen/Qwen3-4B-Instruct-2507-FP8`. The official supported context-size is 256K. However, whatever I set as max `max-model-len`, I get: ``` This model's maximum context length...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ug;stale ### Your current environment ### 🐛 Describe the bug I am facing some longer context issues with `Qwen/Qwen3-4B-Instruct-2507-FP8`. The official supported context-size is 256K. However, whatever I set as max `ma...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3 Instruct context is limited to 8K bug;stale ### Your current environment ### 🐛 Describe the bug I am facing some longer context issues with `Qwen/Qwen3-4B-Instruct-2507-FP8`. The official supported context-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Qwen3 Instruct context is limited to 8K bug;stale ### Your current environment ### 🐛 Describe the bug I am facing some longer context issues with `Qwen/Qwen3-4B-Instruct-2507-FP8`. The official supported context-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
