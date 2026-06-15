# vllm-project/vllm#15602: How to install and use vLLM to serve multiple large language models

| 字段 | 值 |
| --- | --- |
| Issue | [#15602](https://github.com/vllm-project/vllm/issues/15602) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to install and use vLLM to serve multiple large language models

### Issue 正文摘录

### Proposal to improve performance How to install and use vLLM to serve multiple large language models: google/gemma-3-27b-it mistralai/Mistral-Small-3.1-24B-Instruct-2503 Skywork/Skywork-R1V-38B Qwen/Qwen2.5-VL The core issue is that gemma-3-27b requires a very specific (often newer) version of the transformers library. Installing this specific version might break compatibility with vLLM itself or with other models (like certain Mistral or Qwen versions) which might rely on a different, possibly more stable or slightly older, transformers version that vLLM commonly supports. ### Report of performance regression How to install and use vLLM to serve multiple large language models: google/gemma-3-27b-it mistralai/Mistral-Small-3.1-24B-Instruct-2503 Skywork/Skywork-R1V-38B Qwen/Qwen2.5-VL The core issue is that gemma-3-27b requires a very specific (often newer) version of the transformers library. Installing this specific version might break compatibility with vLLM itself or with other models (like certain Mistral or Qwen versions) which might rely on a different, possibly more stable or slightly older, transformers version that vLLM commonly supports. ### Misc discussion on perform...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: How to install and use vLLM to serve multiple large language models stale ### Proposal to improve performance How to install and use vLLM to serve multiple large language models: google/gemma-3-27b-it mistralai/Mistral-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: How to install and use vLLM to serve multiple large language models stale ### Proposal to improve performance How to install and use vLLM to serve multiple large language models: google/gemma-3-27b-it mistralai/Mistral-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ultiple large language models: google/gemma-3-27b-it mistralai/Mistral-Small-3.1-24B-Instruct-2503 Skywork/Skywork-R1V-38B Qwen/Qwen2.5-VL The core issue is that gemma-3-27b requires a very specific (often newer) versio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: sformers version that vLLM commonly supports. ### Report of performance regression How to install and use vLLM to serve multiple large language models: google/gemma-3-27b-it mistralai/Mistral-Small-3.1-24B-Instruct-2503...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: to install and use vLLM to serve multiple large language models: google/gemma-3-27b-it mistralai/Mistral-Small-3.1-24B-Instruct-2503 Skywork/Skywork-R1V-38B Qwen/Qwen2.5-VL The core issue is that gemma-3-27b requires a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
