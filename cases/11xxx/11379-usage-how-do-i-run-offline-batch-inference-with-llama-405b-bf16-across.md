# vllm-project/vllm#11379: [Usage]: How do I run offline batch inference with Llama 405B BF16 across multinode (via SLURM)

| 字段 | 值 |
| --- | --- |
| Issue | [#11379](https://github.com/vllm-project/vllm/issues/11379) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How do I run offline batch inference with Llama 405B BF16 across multinode (via SLURM)

### Issue 正文摘录

### Your current environment N/A ### How would you like to use vllm I want to run offline inference with Llama 405B BF16. I have access to several 8xH100/A100 nodes and I want to use a set of them (more than 2) to run the model at a high context length. However I can only access these nodes via SLURM and can't directly run commands on them. I looked through tons of issues and tutorials but none of them seem to account for using multiple nodes via slurm for offline inference. It would be super helpful if someone can provide a reference script/point to some resources for the same. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: o run offline inference with Llama 405B BF16. I have access to several 8xH100/A100 nodes and I want to use a set of them (more than 2) to run the model at a high context length. However I can only access these nodes via...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How do I run offline batch inference with Llama 405B BF16 across multinode (via SLURM) usage;stale ### Your current environment N/A ### How would you like to use vllm I want to run offline inference with Llama...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Usage]: How do I run offline batch inference with Llama 405B BF16 across multinode (via SLURM) usage;stale ### Your current environment N/A ### How would you like to use vllm I want to run offline inference with Llama...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: batch inference with Llama 405B BF16 across multinode (via SLURM) usage;stale ### Your current environment N/A ### How would you like to use vllm I want to run offline inference with Llama 405B BF16. I have access to se...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
