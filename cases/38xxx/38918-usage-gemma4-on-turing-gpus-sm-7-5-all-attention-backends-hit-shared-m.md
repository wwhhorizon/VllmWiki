# vllm-project/vllm#38918: [Usage]: Gemma4 on Turing GPUs (SM 7.5): all attention backends hit shared memory limits

| 字段 | 值 |
| --- | --- |
| Issue | [#38918](https://github.com/vllm-project/vllm/issues/38918) |
| 状态 | open |
| 标签 | usage |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Gemma4 on Turing GPUs (SM 7.5): all attention backends hit shared memory limits

### Issue 正文摘录

### Your current environment ```text use the builtin dockerfile to build & manually install transformers==5.5.0 ``` ### How would you like to use vllm # Summary I'd like to share a compatibility finding for awareness: **Gemma4 models cannot currently run on Turing architecture GPUs (SM 7.5, e.g. RTX 2080 Ti) via any available attention backend in vLLM** by default. I understand this is likely an edge case given the age of the hardware, but wanted to document the situation in case it's useful for the project — either for improving error messaging or for considering potential kernel tuning. ## Environment | Item | Value | |---|---| | **vLLM version** | `0.19.1rc1.dev4` | | **Commit** | [`fa9e680`](https://github.com/vllm-project/vllm/commit/fa9e68022d29c5396dfbb96d13587b6bc1bdb933) | | **GPU** | 2× NVIDIA GeForce RTX 2080 Ti (22 GB, CC 7.5, Turing) | | **CUDA Driver** | 580.126.18, CUDA 13.0 | | **Python** | 3.12 (Docker) | | **Model** | Gemma4-31B AWQ 4-bit (`google/gemma-4-31b-it`), also reproduced with `cyankiwi/gemma-4-31B-it-AWQ-4bit` | ## What happens Gemma4's `text_config` specifies `head_dim: 256` (sliding attention) and `global_head_dim: 512` (full attention). This large he...

## 现有链接修复摘要

#39018 fix(attention): fix high head dim model(Gemma4) support on limited shared memory | #43044 [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels | #43047 [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: emory limits usage ### Your current environment ```text use the builtin dockerfile to build & manually install transformers==5.5.0 ``` ### How would you like to use vllm # Summary I'd like to share a compatibility findi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Usage]: Gemma4 on Turing GPUs (SM 7.5): all attention backends hit shared memory limits usage ### Your current environment ```text use the builtin dockerfile to build & manually install transformers==5.5.0 ``` ### How...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Usage]: Gemma4 on Turing GPUs (SM 7.5): all attention backends hit shared memory limits usage ### Your current environment ```text use the builtin dockerfile to build & manually install transformers==5.5.0 ``` ### How...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: shes on first request. vllm serve /models \ --tensor-parallel-size 2 --dtype float16 \ --max-model-len 32768 # Explicitly trying each backend: vllm serve /models ... --attention-backend FLASHINFER # fails at startup vll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Gemma4 on Turing GPUs (SM 7.5): all attention backends hit shared memory limits usage ### Your current environment ```text use the builtin dockerfile to build & manually install transformers==5.5.0 ``` ### How...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39018](https://github.com/vllm-project/vllm/pull/39018) | closes_keyword | 0.95 | fix(attention): fix high head dim model(Gemma4) support on limited shared memory | Fixes issue #38918 ## Test Plan 1. **Turing GPU (RTX 2080 Ti × 2, SM 7.5):** ```bash # TRITON_ATTN backend (previously crashed on first request) vllm serve cyankiwi/gemma |
| [#43044](https://github.com/vllm-project/vllm/pull/43044) | mentioned | 0.6 | [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels | d, see Validation below). Partially addresses the same root cause in #38918, #36802, #41063, #32826. ### Motivation Triton kernels in vLLM often ship with autotune config lists tu… |
| [#43047](https://github.com/vllm-project/vllm/pull/43047) | mentioned | 0.6 | [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels | d, see Validation below). Partially addresses the same root cause in #38918, #36802, #41063, #32826. ### Motivation Triton kernels in vLLM often ship with autotune config lists tu… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
