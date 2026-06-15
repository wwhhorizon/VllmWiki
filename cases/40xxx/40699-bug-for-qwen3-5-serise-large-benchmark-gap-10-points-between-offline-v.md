# vllm-project/vllm#40699: [Bug]: For Qwen3.5 serise, Large benchmark gap (~10 points) between offline vLLM inference and vLLM API server despite aligned input_ids

| 字段 | 值 |
| --- | --- |
| Issue | [#40699](https://github.com/vllm-project/vllm/issues/40699) |
| 状态 | open |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: For Qwen3.5 serise, Large benchmark gap (~10 points) between offline vLLM inference and vLLM API server despite aligned input_ids

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are seeing a significant evaluation gap (around 10 points) between: 1. offline vLLM inference (`LLM.generate` / `LLM.chat`), and 2. vLLM OpenAI-compatible API server inference Even after aligning `input_ids`, the benchmark results are still consistently different. We have tested Qwen3.5 serise using official API, sglang-served API, vllm-served API and vllm offline inference in our benchmark, when using vllm-served API, we found a significant performance drop even the whole python environment and token_ids aligned (which means we already set the chat template the same). Besides input_ids, we set the sampling params the same. Btw, we are using the same codebase when testing official API, sglang-served API and vllm-served API, so the codebase shouldn't be the reason. Is there any further method to debug? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e still consistently different. We have tested Qwen3.5 serise using official API, sglang-served API, vllm-served API and vllm offline inference in our benchmark, when using vllm-served API, we found a significant perfor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: For Qwen3.5 serise, Large benchmark gap (~10 points) between offline vLLM inference and vLLM API server despite aligned input_ids bug ### Your current environment ### 🐛 Describe the bug We are seeing a significan...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ug? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: For Qwen3.5 serise, Large benchmark gap (~10 points) between offline vLLM inference and vLLM API server despite aligned input_ids bug ### Your current environment ### 🐛 Describe the bug We are seeing a significan...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
