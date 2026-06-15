# vllm-project/vllm#16467: [Bug]: Grammar error: Pointer '/$defs/xxxxx' does not exist

| 字段 | 值 |
| --- | --- |
| Issue | [#16467](https://github.com/vllm-project/vllm/issues/16467) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Grammar error: Pointer '/$defs/xxxxx' does not exist

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm using Qwen2.5-VL-7b-instruct There seems to be a problem with model in agentic use. It cannot seem to find the reference? It throws the following error: First, when I set `--guided-decoding-backend guidance:disable-any-whitespace`: ```python {'object': 'error', 'message': "Grammar error: Pointer '/$defs/AssetTypes' does not exist", 'type': 'BadRequestError', 'param': None, 'code': 400} ``` To be clear, AssetTypes is clearly defined, and given to the system using Pydantic. ```python class AssetTypes(str, Enum): STOCK = "stock" ETF = "etf" FOREX = "forex" CRYPTO = "crypto" COMMODITY = "commodity" ``` No error in the vLLM logs. Now when I don't set the `--guided-decoding-backend`, which I believe will be `auto` by default, I get the following: Response: ```python {'object': 'error', 'message': "1 validation error for list[function-wrap[__log_extra_fields__()]]\n Invalid JSON: EOF while parsing a value at line 1 column 0 [type=json_invalid, input_value='', input_type=str]\n For further information visit https://errors.pydantic.dev/2.9/v/json_invalid", 'type': 'BadRequestError', 'param': None, 'code': 400} ``` And in the vLLM logs...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantiza...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: stale ### Your current environment ### 🐛 Describe the bug I'm using Qwen2.5-VL-7b-instruct There seems to be a problem with model in agentic use. It cannot seem to find the reference? It throws the following error: Firs...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Grammar error: Pointer '/$defs/xxxxx' does not exist bug;stale ### Your current environment ### 🐛 Describe the bug I'm using Qwen2.5-VL-7b-instruct There seems to be a problem with model in agentic use. It cannot...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ce? It throws the following error: First, when I set `--guided-decoding-backend guidance:disable-any-whitespace`: ```python {'object': 'error', 'message': "Grammar error: Pointer '/$defs/AssetTypes' does not exist", 'ty...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
