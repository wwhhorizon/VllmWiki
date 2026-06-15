# vllm-project/vllm#40536: [Feature]: Support iterative in-place weight editing on TP workers (online RLHF / steering / abliteration)

| 字段 | 值 |
| --- | --- |
| Issue | [#40536](https://github.com/vllm-project/vllm/issues/40536) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature]: Support iterative in-place weight editing on TP workers (online RLHF / steering / abliteration)

### Issue 正文摘录

### Motivation We built a TP=4 abliteration pipeline for `openai/gpt-oss-120b` (117B params, 128 experts × 36 layers, MoE) that runs 150 Optuna trials each doing: 1. Edit `attn.o_proj.weight` in-place on all TP workers 2. Expert-granular edits to fused `mlp.experts.w2_weight` (128 experts × 36 layers) 3. MoE router logit suppression 4. Run 800-prompt benchmark (100 benign + 100 harmful × 4 datasets) 5. Restore weights 6. Next trial with new edit plan Per-trial end-to-end time dropped from **~2 min (HF pipeline-parallel)** to **~60s (vLLM TP=4 + `collective_rpc` in-place edit)** — a ~2× throughput improvement. Same pattern applies to: - Online RLHF reward-model updates (single-process, no trainer/server split) - Test-time quantization experiments - LoRA merging at runtime - Abliteration / refusal suppression research - Quantization-aware steering ### What works today ```python from vllm import LLM llm = LLM( model="/path/to/model", tensor_parallel_size=4, enforce_eager=True, # (1) REQUIRED # ... ) def _worker_edit(worker, plan): model = worker.model_runner.model for layer_idx, w_new in plan.items(): model.layers[layer_idx].self_attn.o_proj.weight.data.copy_(w_new) return len(plan)...

## 现有链接修复摘要

#40096 [Frontend][Core] Add sparse NCCL weight transfer support for in-place updates

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ture]: Support iterative in-place weight editing on TP workers (online RLHF / steering / abliteration) ### Motivation We built a TP=4 abliteration pipeline for `openai/gpt-oss-120b` (117B params, 128 experts × 36 layers...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: - Quantization-aware steering ### What works today ```python from vllm import LLM llm = LLM( model="/path/to/model", tensor_parallel_size=4, enforce_eager=True, # (1) REQUIRED # ... ) def _worker_edit(worker, plan): mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ments - LoRA merging at runtime - Abliteration / refusal suppression research - Quantization-aware steering ### What works today ```python from vllm import LLM llm = LLM( model="/path/to/model", tensor_parallel_size=4,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: 8 experts × 36 layers) 3. MoE router logit suppression 4. Run 800-prompt benchmark (100 benign + 100 harmful × 4 datasets) 5. Restore weights 6. Next trial with new edit plan Per-trial end-to-end time dropped from **~2...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: use case. | Security posture regression | | `VLLM_FUSED_MOE_UNQUANTIZED_BACKEND=triton` (MoE only) | `FLASHINFER_TRTLLM` backend's `process_weights_after_loading` repacks `w2_weight` into an opaque block layout. In-plac...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40096](https://github.com/vllm-project/vllm/pull/40096) | mentioned | 0.45 | [Frontend][Core] Add sparse NCCL weight transfer support for in-place updates | ight-editing use case. ### complementarity with #39451 - **#39451 / #40096** (bedeks et al.): trainer-process → vllm-process over nccl with sparse masks. great for async rlhf wher… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
