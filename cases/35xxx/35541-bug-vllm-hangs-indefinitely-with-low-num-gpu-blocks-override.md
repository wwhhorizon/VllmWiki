# vllm-project/vllm#35541: [Bug]: vLLM hangs indefinitely with low `num_gpu_blocks_override`

| 字段 | 值 |
| --- | --- |
| Issue | [#35541](https://github.com/vllm-project/vllm/issues/35541) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM hangs indefinitely with low `num_gpu_blocks_override`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When `num_gpu_blocks_override` is set to a low value (e.g., 50) and multiple rounds of generation are performed on the same LLM instance, vLLM hangs indefinitely. ## Minimal reproduction ```python from vllm import LLM, SamplingParams llm = LLM( model="facebook/opt-125m", gpu_memory_utilization=0.3, num_gpu_blocks_override=50, enforce_eager=True, ) sp = SamplingParams(max_tokens=50, temperature=0) # Round 1: short prompts — completes fine out1 = llm.generate(["Hello, my name is"] * 10, sp, use_tqdm=False) # Round 2: stress prompts — hangs indefinitely # Each prompt is ~1002 tokens, requiring 63 blocks, but only 49 are available out2 = llm.generate(["The quick brown fox. " * 100] * 5, sp, use_tqdm=False) # ^^^ hangs here (scheduler retries forever, never aborts) ``` ## Expected behavior vLLM should abort requests that can never fit in the KV cache block pool with a clear error, rather than hanging indefinitely. ## Observed behavior The process hangs with no output, no error, and no timeout. Must be killed externally. Tested with `gpu_memory_utilization` values 0.3, 0.5, and 0.7, all with `num_gpu_blocks_override=50`. ## Root cause...

## 现有链接修复摘要

#35570 Fix (v1): prevent scheduler hang when request exceeds total KV capacity

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: The quick brown fox. " * 100] * 5, sp, use_tqdm=False) # ^^^ hangs here (scheduler retries forever, never aborts) ``` ## Expected behavior vLLM should abort requests that can never fit in the KV cache block pool with a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: vLLM hangs indefinitely. ## Minimal reproduction ```python from vllm import LLM, SamplingParams llm = LLM( model="facebook/opt-125m", gpu_memory_utilization=0.3, num_gpu_blocks_override=50, enforce_eager=True, ) sp = Sa...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: [Bug]: vLLM hangs indefinitely with low `num_gpu_blocks_override` bug ### Your current environment ### 🐛 Describe the bug When `num_gpu_blocks_override` is set to a low value (e.g., 50) and multiple rounds of generation...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: s, but request stays in waiting queue ``` ## Environment - GPU: NVIDIA RTX 4070 (12 GB) - vLLM: 0.15.1 - CUDA: 12.9 - Python: 3.12 ### Before submitting a new issue... - [x] Make sure you already searched for relevant i...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: Expected behavior vLLM should abort requests that can never fit in the KV cache block pool with a clear error, rather than hanging indefinitely. ## Observed behavior The process hangs with no output, no error, and no ti...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35570](https://github.com/vllm-project/vllm/pull/35570) | closes_keyword | 0.95 | Fix (v1): prevent scheduler hang when request exceeds total KV capacity | Fixes #35541 Description This PR addresses a potential infinite hang in the V1 scheduler, specifically when num_gpu_blocks_override is set to a low value or when a single request |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
