# vllm-project/vllm#43820: Spec decode with multimodal pruning gives Eagle drafter shifted embeddings but unshifted M-RoPE positions

| 字段 | 值 |
| --- | --- |
| Issue | [#43820](https://github.com/vllm-project/vllm/issues/43820) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | model_support;multimodal_vlm;speculative_decoding |
| 子分类 | wrong_output |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Spec decode with multimodal pruning gives Eagle drafter shifted embeddings but unshifted M-RoPE positions

### Issue 正文摘录

### Summary I can reproduce a V1 speculative decoding issue where multimodal pruning + M-RoPE cause the Eagle drafter to see M-RoPE positions that do not match the shifted multimodal embeddings gathered for the draft pass. The suspicious path is: - `propose_draft_token_ids()` computes `target_positions` - it calls `_gather_mm_embeddings(scheduler_output, shift_computed_tokens=1)` - `_gather_mm_embeddings()` uses `req_state.num_computed_tokens + shift_computed_tokens` for the multimodal embedding overlap window - but with multimodal pruning + M-RoPE enabled it recomputes/copies M-RoPE positions using unshifted `req_state.num_computed_tokens` - `drafter.propose(..., target_positions=target_positions)` then consumes the same `target_positions` buffer Runtime instrumentation shows that the multimodal embeddings correspond to the shifted token window, while the positions consumed by the drafter at those same multimodal rows are unshifted. On a later decode step, `_gather_mm_embeddings()` also mutates the `target_positions` view before `drafter.propose()` consumes it. ### Environment - vLLM main: `5963c194787d30ed4a49c1e2e01010d8dffe1e79` - vLLM version: `0.21.1rc1.dev343+g5963c1947.d20...

## 现有链接修复摘要

#43832 [Bugfix][V1][Spec Decode] Don't mutate M-RoPE state from draft-path _gather_mm_embeddings (#43820)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: Spec decode with multimodal pruning gives Eagle drafter shifted embeddings but unshifted M-RoPE positions ### Summary I can reproduce a V1 speculative decoding issue where multimodal pruning + M-RoPE cause the Eagle dra
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: dffe1e79` - vLLM version: `0.21.1rc1.dev343+g5963c1947.d20260527` - GPU: A100-SXM4-40GB - Driver: `580.159.03` - PyTorch: `2.11.0+cu130` - Target model: `Qwen/Qwen3-VL-4B-Instruct` - Draft model: `AngelSlim/Qwen3-VL-4B-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Spec decode with multimodal pruning gives Eagle drafter shifted embeddings but unshifted M-RoPE positions ### Summary I can reproduce a V1 speculative decoding issue where multimodal pruning + M-RoPE cause the Eagle dra...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: the shifted multimodal embeddings gathered for the draft pass. The suspicious path is: - `propose_draft_token_ids()` computes `target_positions` - it calls `_gather_mm_embeddings(scheduler_output, shift_computed_tokens=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ct_eagle3` - Spec decode: `method=eagle3`, `num_speculative_tokens=2` - `dtype=bfloat16`, `enforce_eager=True`, `max_model_len=1024`, `max_num_batched_tokens=1024`, `max_num_seqs=1` - Synthetic image input, `video_pruni...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43832](https://github.com/vllm-project/vllm/pull/43832) | closes_keyword | 0.95 | [Bugfix][V1][Spec Decode] Don't mutate M-RoPE state from draft-path _gather_mm_embeddings (#43820) | Fixes #43820 — speculative decoding with multimodal pruning + M-RoPE produced output that diverged from the non-speculative reference. Root cause: the draft path's `_gather_mm_embe |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
