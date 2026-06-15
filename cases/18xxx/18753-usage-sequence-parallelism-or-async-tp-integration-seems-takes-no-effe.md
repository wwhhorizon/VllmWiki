# vllm-project/vllm#18753: [Usage]: sequence parallelism or async tp integration seems takes no effect on Qwen3-MoE

| 字段 | 值 |
| --- | --- |
| Issue | [#18753](https://github.com/vllm-project/vllm/issues/18753) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: sequence parallelism or async tp integration seems takes no effect on Qwen3-MoE

### Issue 正文摘录

### Your current environment x ### How would you like to use vllm vllm serve /data/team/Qwen3-30B-A3B -tp 2 -O '{"level":3, "pass_config": {"enable_async_tp": true}}' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: sequence parallelism or async tp integration seems takes no effect on Qwen3-MoE usage ### Your current environment x ### How would you like to use vllm vllm serve /data/team/Qwen3-30B-A3B -tp 2 -O '{"level":3,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ]: sequence parallelism or async tp integration seems takes no effect on Qwen3-MoE usage ### Your current environment x ### How would you like to use vllm vllm serve /data/team/Qwen3-30B-A3B -tp 2 -O '{"level":3, "pass_...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: uence parallelism or async tp integration seems takes no effect on Qwen3-MoE usage ### Your current environment x ### How would you like to use vllm vllm serve /data/team/Qwen3-30B-A3B -tp 2 -O '{"level":3, "pass_config...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
