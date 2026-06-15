# vllm-project/vllm#19896: [Feature]: EXL3 support

| 字段 | 值 |
| --- | --- |
| Issue | [#19896](https://github.com/vllm-project/vllm/issues/19896) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: EXL3 support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch EXL3 has strong potential to become the go-to format for small BPW quantization, offering excellent perplexity-to-size performance. The authors note that changes in the format make integration with VLLM more feasible. See: https://github.com/turboderp-org/exllamav3?tab=readme-ov-file#exl3-quantization Adding EXL3 support to VLLM would be a major win, as the native EXLlama engine struggles with large-scale serving, where VLLM excels. ### Alternatives Using EXLLama for inference - bad performance, bad concurrency Using different quantization formats - more vram, or worse model performance ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ure, motivation and pitch EXL3 has strong potential to become the go-to format for small BPW quantization, offering excellent perplexity-to-size performance. The authors note that changes in the format make integration...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: itch EXL3 has strong potential to become the go-to format for small BPW quantization, offering excellent perplexity-to-size performance. The authors note that changes in the format make integration with VLLM more feasib...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tion and pitch EXL3 has strong potential to become the go-to format for small BPW quantization, offering excellent perplexity-to-size performance. The authors note that changes in the format make integration with VLLM m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: EXL3 support feature request;stale ### 🚀 The feature, motivation and pitch EXL3 has strong potential to become the go-to format for small BPW quantization, offering excellent perplexity-to-size performance. T...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
