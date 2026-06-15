# vllm-project/vllm#37076: [Bug]: Potential use-after-free in KV block allocator under eviction pressure

| 字段 | 值 |
| --- | --- |
| Issue | [#37076](https://github.com/vllm-project/vllm/issues/37076) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | wrong_output |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;mismatch;nondeterministic |
| 根因提示 | env_dependency;memory_layout;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Potential use-after-free in KV block allocator under eviction pressure

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are fuzzing VLLM for a class project and found a few issues, after a while of triaging we think this issue is particularly of interest to report: ## Summary With `--enable-prefix-caching`, concurrent requests that share a KV prefix block produce non-deterministic output even at `temperature=0`. The affected request receives a spurious extra token at the start of its output, a token that belongs to a different request's cached block, which indicates the prefix cache returned the wrong block boundary. This was discovered by a black-box fuzzer targeting vLLM's OpenAI-compatible API. The bug reproduces in **10/10 runs** on a fresh server with no special configuration. ## Environment - **vLLM version:** tested on `>= 0.6` - **Model:** `Qwen/Qwen2.5-0.5B-Instruct` - **Flags:** `--enable-prefix-caching --gpu-memory-utilization 0.95` - **Hardware:** NVIDIA RTX A6000 (48 GB) ## What Happens **Expected:** A request with `temperature=0` over an identical prompt always produces identical output. **Actual:** The same request (`r7_s_s_s`) produces different output across runs — sometimes the correct continuation, sometimes with a spurious t...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 7: refix-caching`, concurrent requests that share a KV prefix block produce non-deterministic output even at `temperature=0`. The affected request receives a spurious extra token at the start of its output, a token that be...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e API. The bug reproduces in **10/10 runs** on a fresh server with no special configuration. ## Environment - **vLLM version:** tested on `>= 0.6` - **Model:** `Qwen/Qwen2.5-0.5B-Instruct` - **Flags:** `--enable-prefix-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ble-prefix-caching --gpu-memory-utilization 0.95` - **Hardware:** NVIDIA RTX A6000 (48 GB) ## What Happens **Expected:** A request with `temperature=0` over an identical prompt always produces identical output. **Actual...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: . The bug reproduces in **10/10 runs** on a fresh server with no special configuration. ## Environment - **vLLM version:** tested on `>= 0.6` - **Model:** `Qwen/Qwen2.5-0.5B-Instruct` - **Flags:** `--enable-prefix-cachi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: that belongs to a different request's cached block, which indicates the prefix cache returned the wrong block boundary. This was discovered by a black-box fuzzer targeting vLLM's OpenAI-compatible API. The bug reproduce...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
