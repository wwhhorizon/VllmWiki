# vllm-project/vllm#5534: [Performance]: How use vllm.attention.ops.triton_flash_attention replace flash_attn package

| 字段 | 值 |
| --- | --- |
| Issue | [#5534](https://github.com/vllm-project/vllm/issues/5534) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: How use vllm.attention.ops.triton_flash_attention replace flash_attn package

### Issue 正文摘录

### Proposal to improve performance My gpu is tool old so that can't install flash_attn package. So, I want use vllm.attention.ops.triton_flash_attention replace flash_attn package ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ```

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Performance]: How use vllm.attention.ops.triton_flash_attention replace flash_attn package performance;stale ### Proposal to improve performance My gpu is tool old so that can't install flash_attn package. So, I want u...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: le ### Proposal to improve performance My gpu is tool old so that can't install flash_attn package. So, I want use vllm.attention.ops.triton_flash_attention replace flash_attn package ### Report of performance regressio...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ention.ops.triton_flash_attention replace flash_attn package performance;stale ### Proposal to improve performance My gpu is tool old so that can't install flash_attn package. So, I want use vllm.attention.ops.triton_fl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: on_flash_attention replace flash_attn package ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
