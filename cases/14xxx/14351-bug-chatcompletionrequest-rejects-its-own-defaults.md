# vllm-project/vllm#14351: [Bug]: ChatCompletionRequest rejects its own defaults

| 字段 | 值 |
| --- | --- |
| Issue | [#14351](https://github.com/vllm-project/vllm/issues/14351) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ChatCompletionRequest rejects its own defaults

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The pydantic model `ChatCompletionRequest` found in `vllm.entrypoints.openai.protocol` rejects its own default configuration of `logprobs` and `top_logprobs`. Example to reproduce the problem: ```python from vllm.entrypoints.openai.protocol import ChatCompletionRequest request = ChatCompletionRequest(model="model", messages=[{"role": "user", "content": "content"}]) ChatCompletionRequest.model_validate(request.model_dump()) ``` Output: ``` Traceback (most recent call last): File " ", line 1, in File "/home/.../.venv/lib/python3.10/site-packages/pydantic/main.py", line 596, in model_validate return cls.__pydantic_validator__.validate_python( pydantic_core._pydantic_core.ValidationError: 1 validation error for ChatCompletionRequest Value error, when using `top_logprobs`, `logprobs` must be set to true. [type=value_error, input_value={'messages': [{'content':...ogits_processors': None}, input_type=dict] For further information visit https://errors.pydantic.dev/2.9/v/value_error ``` This becomes a problem when an instance of the class is instantiated at some point (and consequently filled with its defaults if no values for `logprobs`...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: reproduce the problem: ```python from vllm.entrypoints.openai.protocol import ChatCompletionRequest request = ChatCompletionRequest(model="model", messages=[{"role": "user", "content": "content"}]) ChatCompletionRequest...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ld change as follows: ```python @model_validator(mode="before") @classmethod def check_logprobs(cls, data): if (prompt_logprobs := data.get("prompt_logprobs")) is not None: if data.get("stream") and prompt_logprobs > 0:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ug ### Your current environment ### 🐛 Describe the bug The pydantic model `ChatCompletionRequest` found in `vllm.entrypoints.openai.protocol` rejects its own default configuration of `logprobs` and `top_logprobs`. Examp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: ChatCompletionRequest rejects its own defaults bug ### Your current environment ### 🐛 Describe the bug The pydantic model `ChatCompletionRequest` found in `vllm.entrypoints.openai.protocol` rejects its own defaul...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
