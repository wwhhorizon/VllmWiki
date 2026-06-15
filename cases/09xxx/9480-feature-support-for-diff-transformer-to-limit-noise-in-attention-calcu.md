# vllm-project/vllm#9480: [Feature]: Support for Diff-Transformer to limit noise in attention calculation @ runtime

| 字段 | 值 |
| --- | --- |
| Issue | [#9480](https://github.com/vllm-project/vllm/issues/9480) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for Diff-Transformer to limit noise in attention calculation @ runtime

### Issue 正文摘录

### 🚀 The feature, motivation and pitch [Microsoft Research](https://www.microsoft.com/en-us/research/) and [Tsinghua University](https://www.tsinghua.edu.cn/en/) researchers have introduced [Differential Transformer](https://arxiv.org/abs/2410.05258) (Diff Transformer), a new LLM architecture that improves performance by amplifying attention to relevant context while filtering out noise. Their findings, published in a research paper, show that Diff Transformer outperforms the classic Transformer architecture in various settings. The Diff-Transformer can be applied both during the training phase and to pretrained models. When applied to pretrained models, it can enhance their robustness and accuracy in practical applications like in-context learning and text summarization. Sources below. The feature request here is to examine the application potential at vLLM runtime. paper: [ArXiv](https://arxiv.org/html/2410.05258v1) press coverage (October 16th): [VentureBeat](https://venturebeat.com/ai/microsofts-differential-transformer-cancels-attention-noise-in-llms/) ### Alternatives N/A ### Additional context github: [Diff-Transformer](https://github.com/microsoft/unilm/tree/master/Diff-T...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ff-Transformer to limit noise in attention calculation @ runtime feature request;stale ### 🚀 The feature, motivation and pitch [Microsoft Research](https://www.microsoft.com/en-us/research/) and [Tsinghua University](ht...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: . When applied to pretrained models, it can enhance their robustness and accuracy in practical applications like in-context learning and text summarization. Sources below. The feature request here is to examine the appl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ashdiff_1.py contains multi-head differential attention implemented with FlashAttention, for packages that support different qk/v dimensions (e.g., our [customized-flash-attention](https://aka.ms/flash-diff) and [xforme...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: . When applied to pretrained models, it can enhance their robustness and accuracy in practical applications like in-context learning and text summarization. Sources below. The feature request here is to examine the appl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: re request;stale ### 🚀 The feature, motivation and pitch [Microsoft Research](https://www.microsoft.com/en-us/research/) and [Tsinghua University](https://www.tsinghua.edu.cn/en/) researchers have introduced [Differenti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
