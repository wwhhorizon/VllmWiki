# vllm-project/vllm#10181: [Feature]: support duo-attention

| 字段 | 值 |
| --- | --- |
| Issue | [#10181](https://github.com/vllm-project/vllm/issues/10181) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;quantization |
| 子分类 |  |
| Operator 关键词 | attention;quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: support duo-attention

### Issue 正文摘录

### 🚀 The feature, motivation and pitch https://github.com/mit-han-lab/duo-attention This project method significantly reduces long-context inference memory by up to 2.55x for MHA and 1.67x for GQA models while speeding up decoding by up to 2.18x and 1.50x and accelerating pre-filling by up to 1.73x and 1.63x for MHA and GQA models, respectively, with minimal accuracy loss compared to full attention. Notably, combined with quantization, DuoAttention enables Llama-3-8B decoding with 3.3 million context length on a single A100 GPU. On top of flash-attention. Looking forward to using it on vllm ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: enables Llama-3-8B decoding with 3.3 million context length on a single A100 GPU. On top of flash-attention. Looking forward to using it on vllm ### Alternatives _No response_ ### Additional context _No response_ ### Be...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s long-context inference memory by up to 2.55x for MHA and 1.67x for GQA models while speeding up decoding by up to 2.18x and 1.50x and accelerating pre-filling by up to 1.73x and 1.63x for MHA and GQA models, respectiv...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: support duo-attention feature request;stale ### 🚀 The feature, motivation and pitch https://github.com/mit-han-lab/duo-attention This project method significantly reduces long-context inference memory by up t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: up to 1.73x and 1.63x for MHA and GQA models, respectively, with minimal accuracy loss compared to full attention. Notably, combined with quantization, DuoAttention enables Llama-3-8B decoding with 3.3 million context l...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: up to 1.73x and 1.63x for MHA and GQA models, respectively, with minimal accuracy loss compared to full attention. Notably, combined with quantization, DuoAttention enables Llama-3-8B decoding with 3.3 million context l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
