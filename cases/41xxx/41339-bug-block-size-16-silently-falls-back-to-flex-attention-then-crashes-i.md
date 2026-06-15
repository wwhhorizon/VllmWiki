# vllm-project/vllm#41339: [Bug]: block_size < 16 silently falls back to FLEX_ATTENTION, then crashes in Triton compilation

| 字段 | 值 |
| --- | --- |
| Issue | [#41339](https://github.com/vllm-project/vllm/issues/41339) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: block_size < 16 silently falls back to FLEX_ATTENTION, then crashes in Triton compilation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In vLLM 0.19.1, setting `block_size` = 16` requirement (see root cause below). ## Reproducer ```python import vllm print(f"vllm version: {vllm.__version__}") from vllm import LLM, SamplingParams llm = LLM( model="meta-llama/Llama-3.2-1B-Instruct", block_size=8, #can be set to any value = 1, N >= 1 and K >= 16 ``` The Inductor-generated kernel `triton_tem_fused_flex_attention_0` is compiled with `BLOCK_M=16, BLOCK_N=8, SPARSE_KV_BLOCK_SIZE=8` (on `cc=89` with `bfloat16`), and `BLOCK_N` is the K dimension of the inner `tl.dot(P, V)`. Triton hard-asserts `K >= 16`. **So the underlying bug is:** vLLM's fallback path is unreachable for `block_size = 16 → EngineDeadError ``` The selector logic in `vllm/platforms/cuda.py` knows that the upper-priority backends reject small block sizes, but does not encode the `BLOCK_N >= 16` constraint of the FLEX_ATTENTION Triton template. Full log with `VLLM_LOGGING_LEVEL=DEBUG`: [debug.log](https://github.com/user-attachments/files/27232249/debug.log) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner...

## 现有链接修复摘要

#41363 (bugfix): block_size check for flex attn

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ize` = 16` requirement (see root cause below). ## Reproducer ```python import vllm print(f"vllm version: {vllm.__version__}") from vllm import LLM, SamplingParams llm = LLM( model="meta-llama/Llama-3.2-1B-Instruct", blo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: : block_size < 16 silently falls back to FLEX_ATTENTION, then crashes in Triton compilation bug ### Your current environment ### 🐛 Describe the bug In vLLM 0.19.1, setting `block_size` = 16` requirement (see root cause...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: d with `BLOCK_M=16, BLOCK_N=8, SPARSE_KV_BLOCK_SIZE=8` (on `cc=89` with `bfloat16`), and `BLOCK_N` is the K dimension of the inner `tl.dot(P, V)`. Triton hard-asserts `K >= 16`. **So the underlying bug is:** vLLM's fall...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ize = 16 → EngineDeadError ``` The selector logic in `vllm/platforms/cuda.py` knows that the upper-priority backends reject small block sizes, but does not encode the `BLOCK_N >= 16` constraint of the FLEX_ATTENTION Tri...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: block_size < 16 silently falls back to FLEX_ATTENTION, then crashes in Triton compilation bug ### Your current environment ### 🐛 Describe the bug In vLLM 0.19.1, setting `block_size` = 16` requirement (see root c...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41363](https://github.com/vllm-project/vllm/pull/41363) | closes_keyword | 0.95 | (bugfix): block_size check for flex attn | Closes #41339 ## Description Previously, when a user set block_size < 16 (e.g., block_size=8), vLLM would trigger a cryptic Triton compilation error during the runtime, which w |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
