# vllm-project/vllm#36921: [Bug]: V1 engine hangs then crashes with "No available shared memory broadcast block found / RPC call to sample_tokens timed out" under chat completions burst load on Qwen3.5-122B-A10B

| 字段 | 值 |
| --- | --- |
| Issue | [#36921](https://github.com/vllm-project/vllm/issues/36921) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 engine hangs then crashes with "No available shared memory broadcast block found / RPC call to sample_tokens timed out" under chat completions burst load on Qwen3.5-122B-A10B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are repeatedly hitting what looks like a V1 engine / multiprocess shared-memory coordination bug under bursty but otherwise normal chat-completions load. The engine will run normally for a while, then throughput suddenly drops to zero, we start seeing: `No available shared memory broadcast block found in 60 seconds.` repeated every minute, and eventually the engine dies with: - `TimeoutError: RPC call to sample_tokens timed out.` This is happening even though: - KV cache usage is still low - /dev/shm is very large (1TB) - requests are ordinary chat completions - this reproduces across multiple versions/config tweaks My launch args: ``` vllm serve Qwen/Qwen3.5-122B-A10B \ --tensor-parallel-size 8 \ --reasoning-parser qwen3 \ --served-model-name q3.5-122b \ --trust-remote-code \ --cudagraph-metrics \ --enable-prefix-caching \ --gpu-memory-utilization 0.95 \ --max-model-len 16384 \ --language-model-only \ ``` I'm seeing the error under versions: - 0.17.0 - 0.17.1 - 0.16.0rc2.dev471+g709eadbb0 Tested already with: - `--max-num-batched-tokens 8192` and lower, other args e.g. - removing the `--language-model-only`, - lowering mem ut...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: requests are ordinary chat completions - this reproduces across multiple versions/config tweaks My launch args: ``` vllm serve Qwen/Qwen3.5-122B-A10B \ --tensor-parallel-size 8 \ --reasoning-parser qwen3 \ --served-mode...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: PC call to sample_tokens timed out" under chat completions burst load on Qwen3.5-122B-A10B bug ### Your current environment ### 🐛 Describe the bug We are repeatedly hitting what looks like a V1 engine / multiprocess sha...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: removing the `--language-model-only`, - lowering mem util, - using Ray backend Using persistent caches for XDG, Torch, Triton & CUDA. This is an offline inference workload, but sent through the OpenAI-compatible chat/co...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: arser qwen3 \ --served-model-name q3.5-122b \ --trust-remote-code \ --cudagraph-metrics \ --enable-prefix-caching \ --gpu-memory-utilization 0.95 \ --max-model-len 16384 \ --language-model-only \ ``` I'm seeing the erro...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: V1 engine hangs then crashes with "No available shared memory broadcast block found / RPC call to sample_tokens timed out" under chat completions burst load on Qwen3.5-122B-A10B bug ### Your current environment ### 🐛 De...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
