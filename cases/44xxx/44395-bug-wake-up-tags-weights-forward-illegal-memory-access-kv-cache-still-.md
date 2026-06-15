# vllm-project/vllm#44395: [Bug]: `wake_up(tags=["weights"])` + forward → illegal memory access (KV cache still asleep)

| 字段 | 值 |
| --- | --- |
| Issue | [#44395](https://github.com/vllm-project/vllm/issues/44395) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;sampling_logits;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;kernel;moe;triton |
| 症状 | build_error;crash;nondeterministic |
| 根因提示 | env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `wake_up(tags=["weights"])` + forward → illegal memory access (KV cache still asleep)

### Issue 正文摘录

### Your current environment ## Summary After a partial `wake_up` that restores **only** the `weights` tag (KV cache left asleep), the engine can still execute a forward pass, which accesses the released KV cache and crashes with `CUDA error: an illegal memory access was encountered`. This bites RLHF / colocate workflows that do a **staged wake**: `sleep(level=1)` → `wake_up(tags=["weights"])` → (push new weights) → `wake_up(tags=["kv_cache"])` → serve. The intent is to bring weights back first (to receive a weight update) while keeping KV released to save memory, and only restore KV right before serving. With **data parallelism** the crash is hit *involuntarily*: the DP engine-core busy loop runs `execute_dummy_batch()` (a decode forward) on idle ranks to stay in step with a peer rank, so a forward happens during the weights-only window even if the user never sends a request. ## Environment - vLLM 0.22.0 - MoE model (e.g. Qwen3-30B-A3B), `--enable-sleep-mode` - Repro shown with `--data-parallel-size 2 --enable-expert-parallel` (DP makes it deterministic), but the underlying issue also reproduces at DP=1 if a request is sent during the weights-only window. ## Reproduction ```bash...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: hown with `--data-parallel-size 2 --enable-expert-parallel` (DP makes it deterministic), but the underlying issue also reproduces at DP=1 if a request is sent during the weights-only window. ## Reproduction ```bash VLLM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: execute_dummy_batch() fires on its own, or # (b) send one request explicitly: curl -X POST localhost:8000/v1/completions \ -H 'Content-Type: application/json' \ -d '{"model":" ","prompt":"hi","max_tokens":8}' ``` ### Ob...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e a forward pass, which accesses the released KV cache and crashes with `CUDA error: an illegal memory access was encountered`. This bites RLHF / colocate workflows that do a **staged wake**: `sleep(level=1)` → `wake_up...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: was encountered ``` (b) Real request — note the JIT warning for the KV slot-mapping kernel right before the crash: ``` WARNING [jit_monitor.py:103] Triton kernel JIT compilation during inference: _compute_slot_mapping_k...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: th `CUDA error: an illegal memory access was encountered`. This bites RLHF / colocate workflows that do a **staged wake**: `sleep(level=1)` → `wake_up(tags=["weights"])` → (push new weights) → `wake_up(tags=["kv_cache"]...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
