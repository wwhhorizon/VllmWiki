# vllm-project/vllm#41685: [RFC]: Long-context-optimized Pipeline Parallelism, CPP + Async P2P + Dynamic Chunking

| 字段 | 值 |
| --- | --- |
| Issue | [#41685](https://github.com/vllm-project/vllm/issues/41685) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Long-context-optimized Pipeline Parallelism, CPP + Async P2P + Dynamic Chunking

### Issue 正文摘录

### Your current environment ### Motivation vLLM's current Pipeline Parallelism implementation is positioned in the [official docs](https://docs.vllm.ai/en/stable/serving/parallelism_scaling/) as a *capacity or memory* fallback: > *"Multi-node multi-GPU using tensor parallel and pipeline parallel inference: if the model is too large for a single node, combine tensor parallelism with pipeline parallelism."* This positioning is correct for the original PP use case, but it leaves a sizable performance opportunity on the table for **long-context disaggregated serving**, where PP on the prefill side is the right tool to (a) compress the prefill pool (fewer prefill GPUs feeding the same number of decode GPUs) and (b) hide long-context attention bubbles via micro-batched stages. [SGLang's chunked-pipeline blog (2026-01-15)](https://www.lmsys.org/blog/2026-01-15-chunked-pipeline/) demonstrates that long-context PP needs a specific *combination* of three techniques to actually win. Reference numbers (DeepSeek-V3.1 on H20): - **PP4 TP8 with DCK 12K → 3.31× prefill throughput** over the TP8 baseline. - At matched GPU count (32 GPUs), **PP4 TP8 outperforms PP1 TP32 by 30.5%** with DCK, and st...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [RFC]: Long-context-optimized Pipeline Parallelism, CPP + Async P2P + Dynamic Chunking bug ### Your current environment ### Motivation vLLM's current Pipeline Parallelism implementation is positioned in the [official do...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: on the table for **long-context disaggregated serving**, where PP on the prefill side is the right tool to (a) compress the prefill pool (fewer prefill GPUs feeding the same number of decode GPUs) and (b) hide long-cont...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: umbers (DeepSeek-V3.1 on H20): - **PP4 TP8 with DCK 12K → 3.31× prefill throughput** over the TP8 baseline. - At matched GPU count (32 GPUs), **PP4 TP8 outperforms PP1 TP32 by 30.5%** with DCK, and still by 18.4% even w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: llm.ai/en/stable/serving/parallelism_scaling/) as a *capacity or memory* fallback: > *"Multi-node multi-GPU using tensor parallel and pipeline parallel inference: if the model is too large for a single node, combine ten...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 's current Pipeline Parallelism implementation is positioned in the [official docs](https://docs.vllm.ai/en/stable/serving/parallelism_scaling/) as a *capacity or memory* fallback: > *"Multi-node multi-GPU using tensor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
