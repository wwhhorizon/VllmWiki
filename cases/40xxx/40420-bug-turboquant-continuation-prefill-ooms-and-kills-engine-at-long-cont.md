# vllm-project/vllm#40420: [Bug]: TurboQuant `_continuation_prefill` OOMs and kills engine at long-context prefill (~185K actual tokens)

| 字段 | 值 |
| --- | --- |
| Issue | [#40420](https://github.com/vllm-project/vllm/issues/40420) |
| 状态 | open |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;quantization;triton |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: TurboQuant `_continuation_prefill` OOMs and kills engine at long-context prefill (~185K actual tokens)

### Issue 正文摘录

### Summary On the open hybrid-TurboQuant stack (umbrella PR #39931), a single chat-completion request whose tokenized prompt exceeds ~185K tokens reliably kills the entire vLLM engine (CUDA OOM in the prefill path), not just the individual request. The server has to be restarted. This is well below the `--max-model-len=262144` the model advertises and KV cache reports as provisioned. ### Environment - GPU: RTX 5090 (sm_120, 32 GiB) - Model: `cyankiwi/Qwen3.6-35B-A3B-AWQ-4bit` - `--kv-cache-dtype=turboquant_4bit_nc --max-model-len=262144 --max-num-seqs=16 --gpu-memory-utilization=0.87` - GPU KV cache size reported at startup: 548,864 tokens · 2.00x concurrency at 256K - Base image: `vllm/vllm-openai:cu130-nightly` + PR #39931 + the 6 open follow-up PRs I've been tracking (LCM page-size #40128, GDN dual-stream #39748, FA3/4 passthrough #40092, FLA TMA gate #37700, hybrid kv-token capacity #40384, triton decode OOB clamp #40074). ### Reproducer 1. Start the stack with `--kv-cache-dtype=turboquant_4bit_nc --max-model-len=262144 --gpu-memory-utilization=0.87`. 2. Send one chat completion whose tokenized prompt is between ~185K and 262K tokens (e.g. a long NIAH-style haystack). OOM-pro...

## 现有链接修复摘要

#37700 [Bugfix] Fix FLA Hopper/TMA misclassification on SM12x desktop Blackwell | #39748 [Perf] Re-enable dual-stream input projection for Qwen3/Qwen3.5 GDN | #39931 [Feature] TurboQuant: support hybrid models and uniform quantization | #40074 [Bugfix] Fix TurboQuant KV cache index-out-of-bounds in Triton decode kernel | #40092 [TurboQuant] enable FA3/FA4 for prefill paths | #40128 fix: handle non-divisible page sizes in hybrid model KV cache unification | #40384 [Bugfix] Exclude O(1) Mamba groups from hybrid KV cache token capacity | #41422 [Attention][TurboQuant] Sparse V tile-skip (opt-in)

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: nized prompt exceeds ~185K tokens reliably kills the entire vLLM engine (CUDA OOM in the prefill path), not just the individual request. The server has to be restarted. This is well below the `--max-model-len=262144` th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: up PRs I've been tracking (LCM page-size #40128, GDN dual-stream #39748, FA3/4 passthrough #40092, FLA TMA gate #37700, hybrid kv-token capacity #40384, triton decode OOB clamp #40074). ### Reproducer 1. Start the stack...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 9748, FA3/4 passthrough #40092, FLA TMA gate #37700, hybrid kv-token capacity #40384, triton decode OOB clamp #40074). ### Reproducer 1. Start the stack with `--kv-cache-dtype=turboquant_4bit_nc --max-model-len=262144 -...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: TurboQuant `_continuation_prefill` OOMs and kills engine at long-context prefill (~185K actual tokens) ### Summary On the open hybrid-TurboQuant stack (umbrella PR #39931), a single chat-completion request whose...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: TurboQuant `_continuation_prefill` OOMs and kills engine at long-context prefill (~185K actual tokens) ### Summary On the open hybrid-TurboQuant stack (umbrella PR #39931), a single chat-completion request whose...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37700](https://github.com/vllm-project/vllm/pull/37700) | mentioned | 0.45 | [Bugfix] Fix FLA Hopper/TMA misclassification on SM12x desktop Blackwell | 40128, gdn dual-stream #39748, fa3/4 passthrough #40092, fla tma gate #37700, hybrid kv-token capacity #40384, triton decode oob clamp #40074). ### reproducer 1. start the stack w… |
| [#39748](https://github.com/vllm-project/vllm/pull/39748) | mentioned | 0.45 | [Perf] Re-enable dual-stream input projection for Qwen3/Qwen3.5 GDN | llow-up prs i've been tracking (lcm page-size #40128, gdn dual-stream #39748, fa3/4 passthrough #40092, fla tma gate #37700, hybrid kv-token capacity #40384, triton decode oob cla… |
| [#39931](https://github.com/vllm-project/vllm/pull/39931) | mentioned | 0.45 | [Feature] TurboQuant: support hybrid models and uniform quantization | ncurrency at 256k - base image: `vllm/vllm-openai:cu130-nightly` + pr #39931 + the 6 open follow-up prs i've been tracking (lcm page-size #40128, gdn dual-stream #39748, fa3/4 pas… |
| [#40074](https://github.com/vllm-project/vllm/pull/40074) | mentioned | 0.45 | [Bugfix] Fix TurboQuant KV cache index-out-of-bounds in Triton decode kernel | gate #37700, hybrid kv-token capacity #40384, triton decode oob clamp #40074). ### reproducer 1. start the stack with `--kv-cache-dtype=turboquant_4bit_nc --max-model-len=262144 -… |
| [#40092](https://github.com/vllm-project/vllm/pull/40092) | mentioned | 0.45 | [TurboQuant] enable FA3/FA4 for prefill paths | king (lcm page-size #40128, gdn dual-stream #39748, fa3/4 passthrough #40092, fla tma gate #37700, hybrid kv-token capacity #40384, triton decode oob clamp #40074). ### reproducer… |
| [#40128](https://github.com/vllm-project/vllm/pull/40128) | mentioned | 0.45 | fix: handle non-divisible page sizes in hybrid model KV cache unification | r #39931 + the 6 open follow-up prs i've been tracking (lcm page-size #40128, gdn dual-stream #39748, fa3/4 passthrough #40092, fla tma gate #37700, hybrid kv-token capacity #4038… |
| [#40384](https://github.com/vllm-project/vllm/pull/40384) | mentioned | 0.45 | [Bugfix] Exclude O(1) Mamba groups from hybrid KV cache token capacity | 3/4 passthrough #40092, fla tma gate #37700, hybrid kv-token capacity #40384, triton decode oob clamp #40074). ### reproducer 1. start the stack with `--kv-cache-dtype=turboquant_… |
| [#41422](https://github.com/vllm-project/vllm/pull/41422) | mentioned | 0.6 | [Attention][TurboQuant] Sparse V tile-skip (opt-in) | requires 264 MB, current size is 262 MB`) — separate bug, tracked at [#40420](https://github.com/vllm-project/vllm/issues/40420). For the long-context bench below, both control an… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
