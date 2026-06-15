# vllm-project/vllm#23003: [Feature]: Support Diverse Beam Search (like HF transformers generation_strategies)

| 字段 | 值 |
| --- | --- |
| Issue | [#23003](https://github.com/vllm-project/vllm/issues/23003) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Diverse Beam Search (like HF transformers generation_strategies)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Motivation I’d like to request that vLLM support **Diverse Beam Search**, similar to Hugging Face’s `generate(..., generation_strategy="diverse_beam_search")`, which encourages diversity among beam outputs by adding a diversity term to the beam scoring process. Kindly refer to: https://huggingface.co/docs/transformers/generation_strategies#diverse-beam-search Integrating Diverse Beam Search could benefit diverse generation, multi-answers, improved coverage, and more robust outputs in reasoning or content generation tasks. ### Proposed Feature - Support related HF parameters: `num_beams`, `num_beam_groups`, `diversity_penalty`, etc. - Modify the scoring in beam search to penalize similarity between beams (e.g., using “group-wise” diversity term as in the original Diverse Beam Search paper). ### Alternatives Huggingface has implemented a version (https://huggingface.co/docs/transformers/generation_strategies#diverse-beam-search). ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation pag...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Support Diverse Beam Search (like HF transformers generation_strategies) feature request;stale ### 🚀 The feature, motivation and pitch ### Motivation I’d like to request that vLLM support **Diverse Beam Searc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Diverse Beam Search (like HF transformers generation_strategies) feature request;stale ### 🚀 The feature, motivation and pitch ### Motivation I’d like to request that vLLM support **Diverse Beam Search**, similar to Hug...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rse Beam Search paper). ### Alternatives Huggingface has implemented a version (https://huggingface.co/docs/transformers/generation_strategies#diverse-beam-search). ### Additional context _No response_ ### Before submit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: Support Diverse Beam Search (like HF transformers generation_strategies) feature request;stale ### 🚀 The feature, motivation and pitch ### Motivation I’d like to request that vLLM support **Diverse Beam Searc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
