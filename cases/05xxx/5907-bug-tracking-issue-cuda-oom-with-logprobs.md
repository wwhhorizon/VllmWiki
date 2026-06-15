# vllm-project/vllm#5907: [Bug]: TRACKING ISSUE: CUDA OOM with Logprobs

| 字段 | 值 |
| --- | --- |
| Issue | [#5907](https://github.com/vllm-project/vllm/issues/5907) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 25; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;cuda |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TRACKING ISSUE: CUDA OOM with Logprobs

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug vLLM has an issue where we can go OOM if too many `logprobs` are requested. The reason that this happens is that there are three sources of memory usage: * Model weights * KV caches * Activations When determining the KV cache size, we calculate peak memory running a long prefill * without logprobs * If a prompt requests many logprobs, however, this is an additional source of memory usage which is not considered during warmup and can cause OOM because we have nothing in scheduler to prevent this We have received several examples of this: * https://github.com/vllm-project/vllm/issues/5890 * https://github.com/vllm-project/vllm/issues/5060 << some of the OOM issues in `AsyncEngineDeadError` * Anyone running MMLU or ARC in lm-eval-harness Attempt to fix this: * https://github.com/vllm-project/vllm/pull/5355 I am working on a design to address this issue

## 现有链接修复摘要

#11544 Bounded peak memory in Top-P-Top-K with chunked sorting

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: TRACKING ISSUE: CUDA OOM with Logprobs bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug vLLM has an issue where we can go OOM if too many `logprobs`...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: TRACKING ISSUE: CUDA OOM with Logprobs bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug vLLM has an issue where we can go OOM if too many `logprobs`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nce attention_kv_cache;model_support;scheduler_memory cache;cuda oom env_dependency #11544 Bounded peak memory in Top-P-Top-K with chunked sorting Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: TRACKING ISSUE: CUDA OOM with Logprobs bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug vLLM has an issue where we can go OOM if too many `logprobs`...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: son that this happens is that there are three sources of memory usage: * Model weights * KV caches * Activations When determining the KV cache size, we calculate peak memory running a long prefill * without logprobs * I...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#11544](https://github.com/vllm-project/vllm/pull/11544) | closes_keyword | 0.95 | Bounded peak memory in Top-P-Top-K with chunked sorting | FIX #5907 (*link existing issues this PR will resolve*) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
