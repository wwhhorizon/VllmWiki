# vllm-project/vllm#37623: [Bug]: Qwen3.5-122B-A10B-FP8 multi GPU issue(tensor-parallel-size)

| 字段 | 值 |
| --- | --- |
| Issue | [#37623](https://github.com/vllm-project/vllm/issues/37623) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-122B-A10B-FP8 multi GPU issue(tensor-parallel-size)

### Issue 正文摘录

### Your current environment Running vLLM with tensor parallelism (--tensor-parallel-size 2) fails during engine initialization with: RuntimeError: [SymmDeviceMemory] Device does not support multicasting. This happens during the AllReduceFusionPass initialization (FlashInfer allreduce fusion workspace creation). ### 🐛 Describe the bug ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ize) bug ### Your current environment Running vLLM with tensor parallelism (--tensor-parallel-size 2) fails during engine initialization with: RuntimeError: [SymmDeviceMemory] Device does not support multicasting. This...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: lticasting. This happens during the AllReduceFusionPass initialization (FlashInfer allreduce fusion workspace creation). ### 🐛 Describe the bug ### Before submitting a new issue... - [x] Make sure you already searched f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: Qwen3.5-122B-A10B-FP8 multi GPU issue(tensor-parallel-size) bug ### Your current environment Running vLLM with tensor parallelism (--tensor-parallel-size 2) fails during engine initialization with: RuntimeError:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Qwen3.5-122B-A10B-FP8 multi GPU issue(tensor-parallel-size) bug ### Your current environment Running vLLM with tensor parallelism (--tensor-parallel-size 2) fails during engine initialization with: RuntimeError:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
