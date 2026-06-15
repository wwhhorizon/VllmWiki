# vllm-project/vllm#42517: [Bug]: MTP produces different tokens than non-MTP at temperature=0 in eager mode

| 字段 | 值 |
| --- | --- |
| Issue | [#42517](https://github.com/vllm-project/vllm/issues/42517) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;gemm_linear;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cache;cuda;gemm;triton |
| 症状 | mismatch;nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: MTP produces different tokens than non-MTP at temperature=0 in eager mode

### Issue 正文摘录

### Describe the bug MTP n=1 produces different token sequences than non-MTP decoding at `temperature=0` when `enforce_eager=True`. The first mismatch occurs at a consistent, reproducible position (e.g., pos 99 for "Hello, my name is"). With `enforce_eager=False` (CUDA graph), outputs are 100% identical. **Root cause chain:** 1. MTP verification forward uses batch_size=2 (original + draft token), non-MTP decode uses batch_size=1 2. In eager mode, cuBLAS auto-tuner selects different GEMM algorithms for different batch sizes, with different internal accumulation orders 3. Attention output differs by 1–2 ULP (BF16) between the two paths 4. This ULP error is written into the KV cache and amplified through the attention loop (each step reads all historical K/V) 5. After ~50–100 steps, accumulated error crosses the logit decision boundary → argmax flips This is distinct from PR #38938 (batch invariance for lm_head/RMSNorm under EAGLE). The attention GEMM itself is not covered. ### Reproduction code ```python import os from vllm import LLM, SamplingParams MODEL = "/path/to/MiMo-7B-Base" PROMPT = "Hello, my name is" SEED = 42 # non-MTP baseline llm = LLM(model=MODEL, enforce_eager=True, t...

## 现有链接修复摘要

#38938 Bug/test eagle dp v0

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: non-MTP decoding at `temperature=0` when `enforce_eager=True`. The first mismatch occurs at a consistent, reproducible position (e.g., pos 99 for "Hello, my name is"). With `enforce_eager=False` (CUDA graph), outputs ar...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: mpute for verified positions KV, or extend batch invariance to attention backend dispatch - I'd be happy to submit a PR once the approach is confirmed. correctness activation_norm;attention_kv_cache;gemm_linear;model_su...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: `enforce_eager=True`. The first mismatch occurs at a consistent, reproducible position (e.g., pos 99 for "Hello, my name is"). With `enforce_eager=False` (CUDA graph), outputs are 100% identical. **Root cause chain:** 1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ause chain:** 1. MTP verification forward uses batch_size=2 (original + draft token), non-MTP decode uses batch_size=1 2. In eager mode, cuBLAS auto-tuner selects different GEMM algorithms for different batch sizes, wit...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ent internal accumulation orders 3. Attention output differs by 1–2 ULP (BF16) between the two paths 4. This ULP error is written into the KV cache and amplified through the attention loop (each step reads all historica...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38938](https://github.com/vllm-project/vllm/pull/38938) | mentioned | 0.45 | Bug/test eagle dp v0 | the logit decision boundary → argmax flips this is distinct from pr #38938 (batch invariance for lm_head/rmsnorm under eagle). the attention gemm itself is not covered. ### reprod… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
