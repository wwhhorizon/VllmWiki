# vllm-project/vllm#41807: [Bug]: FLASH_ATTN_DIFFKV crashes on init with

| 字段 | 值 |
| --- | --- |
| Issue | [#41807](https://github.com/vllm-project/vllm/issues/41807) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FLASH_ATTN_DIFFKV crashes on init with

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug For `facebook/opt-125m`, it seems that the shape computed by `get_kv_cache_shape` is incorrect in the `FLASH_ATTN_DIFFKV` backend. The incorrect shape leads to a crash when trying to reshape KV cache tensors in `_reshape_kv_cache_tensors`. In the case of `facebook/opt-125m`, the input shape is `12582912` and the computed KV cache shape is `[512, 16, 12, 192]`. Since $512 \times 16 \times 12 \times 192 = 18874365$, reshaping fails. ## Relevant locations https://github.com/vllm-project/vllm/blob/e43a7912847ef335337476138e5e863850a4ae0a/vllm/v1/attention/backends/flash_attn_diffkv.py#L54 https://github.com/vllm-project/vllm/blob/e43a7912847ef335337476138e5e863850a4ae0a/vllm/v1/worker/gpu_model_runner.py#L6621 ## Reproducer Using vllm v0.20.0, the following python code results in `RuntimeError: shape '[512, 16, 12, 192]' is invalid for input of size 12582912`. ```python3 import vllm llm = vllm.LLM( "facebook/opt-125m", attention_config={"backend": "FLASH_ATTN_DIFFKV"}, ) llm.generate("test") ``` ## Related issues Issue #39339 seems to be related, but the root cause looks to be different. I can't reproduce #39339 locally. ## Full trac...

## 现有链接修复摘要

#42297 [Bugfix] FLASH_ATTN_DIFFKV: fix KV cache shape for non-128 head_size_v models (issue #41807)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: '[512, 16, 12, 192]' is invalid for input of size 12582912`. ```python3 import vllm llm = vllm.LLM( "facebook/opt-125m", attention_config={"backend": "FLASH_ATTN_DIFFKV"}, ) llm.generate("test") ``` ## Related issues Is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ble_memory (EngineCore pid=9168) ERROR 05-06 11:12:28 [core.py:1136] cudagraph_memory_estimate = self.model_runner.profile_cudagraph_memory() (EngineCore pid=9168) ERROR 05-06 11:12:28 [core.py:1136] ^^^^^^^^^^^^^^^^^^^...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: , attention_config={"backend": "FLASH_ATTN_DIFFKV"}, ) llm.generate("test") ``` ## Related issues Issue #39339 seems to be related, but the root cause looks to be different. I can't reproduce #39339 locally. ## Full tra...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: computed by `get_kv_cache_shape` is incorrect in the `FLASH_ATTN_DIFFKV` backend. The incorrect shape leads to a crash when trying to reshape KV cache tensors in `_reshape_kv_cache_tensors`. In the case of `facebook/opt...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: 335337476138e5e863850a4ae0a/vllm/v1/worker/gpu_model_runner.py#L6621 ## Reproducer Using vllm v0.20.0, the following python code results in `RuntimeError: shape '[512, 16, 12, 192]' is invalid for input of size 12582912...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42297](https://github.com/vllm-project/vllm/pull/42297) | closes_keyword | 0.95 | [Bugfix] FLASH_ATTN_DIFFKV: fix KV cache shape for non-128 head_size_v models (issue #41807) | Fixes #41807: `FLASH_ATTN_DIFFKV` attention backend crashes on models where `head_size_v != 128`. **Root cause**: `get_kv_cache_shape()` was a `@staticmethod` that hard-coded `Fla |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
