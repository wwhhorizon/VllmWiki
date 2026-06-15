# vllm-project/vllm#37765: [Feature]: Consolidate GPTQ Quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#37765](https://github.com/vllm-project/vllm/issues/37765) |
| 状态 | closed |
| 标签 | help wanted;feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Consolidate GPTQ Quantization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We currently have two files: - `gptq.py` - `gptq_marlin.py` These are not needed. We now have decoupled the quantization format integration and kernels. We should delete gptq.py and consolidate everything into `gptq_marlin.py` Then, we should rename `gptq_marlin.py` to `auto_gptq.py` ### Alternatives none ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Consolidate GPTQ Quantization help wanted;feature request ### 🚀 The feature, motivation and pitch We currently have two files: - `gptq.py` - `gptq_marlin.py` These are not needed. We now have decoupled the qu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: marlin.py` These are not needed. We now have decoupled the quantization format integration and kernels. We should delete gptq.py and consolidate everything into `gptq_marlin.py` Then, we should rename `gptq_marlin.py` t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Consolidate GPTQ Quantization help wanted;feature request ### 🚀 The feature, motivation and pitch We currently have two files: - `gptq.py` - `gptq_marlin.py` These are not needed. We now have decoupled the qu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
