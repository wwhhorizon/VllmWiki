# vllm-project/vllm#28724: [New Model]: add unsloth/MiniMax-M2-GGUF support

| 字段 | 值 |
| --- | --- |
| Issue | [#28724](https://github.com/vllm-project/vllm/issues/28724) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: add unsloth/MiniMax-M2-GGUF support

### Issue 正文摘录

### The model to consider. Can you add support for unsloth/MiniMax-M2-GGUF? Both UD-Q4-K-XL and Q4_K_M is preferred. ### The closest model vllm already supports. MiniMax/MiniMax-M2 has already supported many GGUF models also supported. ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [New Model]: add unsloth/MiniMax-M2-GGUF support stale ### The model to consider. Can you add support for unsloth/MiniMax-M2-GGUF? Both UD-Q4-K-XL and Q4_K_M is preferred. ### The closest model vllm already supports. Mi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [New Model]: add unsloth/MiniMax-M2-GGUF support stale ### The model to consider. Can you add support for unsloth/MiniMax-M2-GGUF? Both UD-Q4-K-XL and Q4_K_M is preferred. ### The closest model vllm already supports. Mi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: add unsloth/MiniMax-M2-GGUF support stale ### The model to consider. Can you add support for unsloth/MiniMax-M2-GGUF? Both UD-Q4-K-XL and Q4_K_M is preferred. ### The closest model vllm already supports. Mi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
