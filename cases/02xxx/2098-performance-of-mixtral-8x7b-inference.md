# vllm-project/vllm#2098: performance of Mixtral-8x7B inference

| 字段 | 值 |
| --- | --- |
| Issue | [#2098](https://github.com/vllm-project/vllm/issues/2098) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | attention |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> performance of Mixtral-8x7B inference

### Issue 正文摘录

I am a loyal user of vllm ! I tested Mixtral-8x7B-inference last day with vllm 0.2.4 and transformers 4.36.0 on 2 x A100 80G, and I got about 15 tokens per second. But I got about 100 tokens / s with this (https://www.together.ai/blog/together-inference-engine-v1), they don't open source, just web. So will vllm team follow up on this work, that seems a bit faster. They mentioned “Over the past several months, our team and collaborators have released a number of techniques that optimize inference performance including [FlashAttention-2](https://together.ai/blog/tri-dao-flash-attention), [Flash-Decoding](https://together.ai/blog/flash-decoding-for-long-context-inference), and [Medusa](https://together.ai/blog/medusa), available in the open source and incorporated into many [libraries](https://github.com/Dao-AILab/flash-attention/blob/main/usage.md). Our team has combined these techniques with our own optimizations and today we are excited to announce the Together Inference Engine.” ![image](https://github.com/vllm-project/vllm/assets/10004234/27fac133-e833-46c7-b5a2-4996f363c28e) As a loyal user, I hope vllm can follow up on relevant work. I wish vllm better and better.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ed a number of techniques that optimize inference performance including [FlashAttention-2](https://together.ai/blog/tri-dao-flash-attention), [Flash-Decoding](https://together.ai/blog/flash-decoding-for-long-context-inf...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: combined these techniques with our own optimizations and today we are excited to announce the Together Inference Engine.” ![image](https://github.com/vllm-project/vllm/assets/10004234/27fac133-e833-46c7-b5a2-4996f363c28...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: l-8x7B-inference last day with vllm 0.2.4 and transformers 4.36.0 on 2 x A100 80G, and I got about 15 tokens per second. But I got about 100 tokens / s with this (https://www.together.ai/blog/together-inference-engine-v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: vant work. I wish vllm better and better. performance attention_kv_cache;speculative_decoding attention I am a loyal user of vllm !
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: performance of Mixtral-8x7B inference I am a loyal user of vllm ! I tested Mixtral-8x7B-inference last day with vllm 0.2.4 and transformers 4.36.0 on 2 x A100 80G, and I got about 15 tokens per second. But I got about 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
