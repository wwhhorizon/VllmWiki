# vllm-project/vllm#43466: [Bug]: OpenAI chat/completion endpoints don't accept logprob_token_ids

| 字段 | 值 |
| --- | --- |
| Issue | [#43466](https://github.com/vllm-project/vllm/issues/43466) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OpenAI chat/completion endpoints don't accept logprob_token_ids

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary `SamplingParams.logprob_token_ids` is reachable from the Python `LLM` class and from the dedicated `/generative_scoring` endpoint, but **not from the standard OpenAI-compat chat-completion / completion routes** that most clients use. This blocks multilabel scoring postprocessors that need logprobs at a fixed set of label vocab ids (each label corresponds to a known vocab id; for example, digit tokens for an enumerated label set). The only available HTTP knob is `top_logprobs=N`, which returns the N tokens with highest likelihood — label ids that don't rank in the natural top-N are silently dropped from the response, even when the caller knows the exact ids and explicitly wants them. ## Steps to reproduce Start a server: ```bash vllm serve Qwen/Qwen2.5-1.5B-Instruct --max-logprobs -1 ``` Send a request that asks for a specific vocab id (`5000` here — chosen to be unlikely to rank in the natural top-5): ```python from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1", api_key="dummy") resp = client.chat.completions.create( model="Qwen/Qwen2.5-1.5B-Instruct", messages=[{"role": "user", "content": "H...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ped from the response, even when the caller knows the exact ids and explicitly wants them. ## Steps to reproduce Start a server: ```bash vllm serve Qwen/Qwen2.5-1.5B-Instruct --max-logprobs -1 ``` Send a request that as...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: wants them. ## Steps to reproduce Start a server: ```bash vllm serve Qwen/Qwen2.5-1.5B-Instruct --max-logprobs -1 ``` Send a request that asks for a specific vocab id (`5000` here — chosen to be unlikely to rank in the...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: e response with its logprob, regardless of where it ranks in the natural top-k. ## Actual behavior The `logprob_token_ids` field is silently dropped — it isn't declared on `ChatCompletionRequest`, so the pydantic model...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: bash vllm serve Qwen/Qwen2.5-1.5B-Instruct --max-logprobs -1 ``` Send a request that asks for a specific vocab id (`5000` here — chosen to be unlikely to rank in the natural top-5): ```python from openai import OpenAI c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
