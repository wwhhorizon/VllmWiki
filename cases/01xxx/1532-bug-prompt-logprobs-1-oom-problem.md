# vllm-project/vllm#1532: [Bug] prompt_logprobs = 1  OOM problem

| 字段 | 值 |
| --- | --- |
| Issue | [#1532](https://github.com/vllm-project/vllm/issues/1532) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] prompt_logprobs = 1  OOM problem

### Issue 正文摘录

When I set prompt_logprobs = 1, if the input is excessively long (exceeding 900 tokens), it results in an out-of-memory (OOM) error. Here are some details. ![image](https://github.com/vllm-project/vllm/assets/33774367/f967c115-bb79-43a6-a66a-309b3431990f) model: BAAI/AquiilaChat2-34B eva: 2* A100 40G

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 7c115-bb79-43a6-a66a-309b3431990f) model: BAAI/AquiilaChat2-34B eva: 2* A100 40G
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug] prompt_logprobs = 1 OOM problem bug;stale When I set prompt_logprobs = 1, if the input is excessively long (exceeding 900 tokens), it results in an out-of-memory (OOM) error. Here are some details. ![image](https:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vllm-project/vllm/assets/33774367/f967c115-bb79-43a6-a66a-309b3431990f) model: BAAI/AquiilaChat2-34B eva: 2* A100 40G
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug] prompt_logprobs = 1 OOM problem bug;stale When I set prompt_logprobs = 1, if the input is excessively long (exceeding 900 tokens), it results in an out-of-memory (OOM) error. Here are some details. ![image](https:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
