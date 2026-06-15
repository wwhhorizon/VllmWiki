# vllm-project/vllm#26105: [Bug]: LLama4 produces all zero tokens after first token

| 字段 | 值 |
| --- | --- |
| Issue | [#26105](https://github.com/vllm-project/vllm/issues/26105) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: LLama4 produces all zero tokens after first token

### Issue 正文摘录

### Your current environment Note that while my environment uses the latest transformers release, this has been shown to be an issue in recent and previous releases as well ### 🐛 Describe the bug The llama4 model seems to produce all `0` tokens after the first token. The first token seems to be correct, as demonstrated from examples such as `("234 + 353 = ", "587")`. I haven't had the resource to be able to confirm this with the unquantized base model. However, since the first generated token is correct, I find it unlikely that this issue is purely explained by quantization. ```python from vllm import LLM; llm = LLM("RedHatAI/Llama-4-Maverick-17B-128E-Instruct-quantized.w4a16", tensor_parallel_size=4) llm.generate("Hello there") ``` ``` [RequestOutput( request_id=0, prompt='Hello there', prompt_token_ids=[200000, 19873, 1609], encoder_prompt=None, encoder_prompt_token_ids=None, prompt_logprobs=None, outputs=[CompletionOutput(index=0, text='!', token_ids=[13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], cumulative_logprob=None, logprobs=None, finish_reason=length, stop_reason=None)], finished=True, metrics=None, lora_request=None, num_cached_tokens=0, multi_modal_placeholders={})]...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: hat this issue is purely explained by quantization. ```python from vllm import LLM; llm = LLM("RedHatAI/Llama-4-Maverick-17B-128E-Instruct-quantized.w4a16", tensor_parallel_size=4) llm.generate("Hello there") ``` ``` [R...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: LLama4 produces all zero tokens after first token bug;stale ### Your current environment Note that while my environment uses the latest transformers release, this has been shown to be an issue in recent and previ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: LLama4 produces all zero tokens after first token bug;stale ### Your current environment Note that while my environment uses the latest transformers release, this has been shown to be an issue in recent and previ...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
