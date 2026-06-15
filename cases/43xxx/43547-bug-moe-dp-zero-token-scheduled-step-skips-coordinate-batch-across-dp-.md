# vllm-project/vllm#43547: [Bug]: MoE+DP — zero-token-scheduled step skips coordinate_batch_across_dp for ray/mp DP backends → ~T+1h NCCL reduce_scatter deadlock

| 字段 | 值 |
| --- | --- |
| Issue | [#43547](https://github.com/vllm-project/vllm/issues/43547) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;quantization |
| 症状 | oom;slowdown |
| 根因提示 | dtype;memory_layout;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MoE+DP — zero-token-scheduled step skips coordinate_batch_across_dp for ray/mp DP backends → ~T+1h NCCL reduce_scatter deadlock

### Issue 正文摘录

> **TL;DR (added 2026-05-26):** Pinned to a missing dummy-run for the > `ray` / `mp` DP backends at > [`vllm/v1/worker/gpu_model_runner.py:3915-3931`](https://github.com/vllm-project/vllm/blob/main/vllm/v1/worker/gpu_model_runner.py#L3915-L3931). > When `num_scheduled_tokens == 0` the `_dummy_run(1)` that fires > `coordinate_batch_across_dp` is gated on > `distributed_executor_backend == "external_launcher"`. Under `ray` > (and `mp`) DP a zero-token-scheduled rank silently returns > `EMPTY_MODEL_RUNNER_OUTPUT` without participating in the per-step DP > collective; the partner DP rank advances by one; drift accumulates > ~one collective per asymmetric step; after ~1h a real MoE > `reduce_scatter` hangs. > Suggested fix (single-line semantic change) and full mechanism trace > in [this comment](https://github.com/vllm-project/vllm/issues/43547#issuecomment-4544158898). > The metadata/skip-path mechanism story in the original report below > turned out to be wrong (verified by code-trace) — symptom evidence > stands, the actual cause is the DP coordination skip. --- ### Your current environment ### 🐛 Describe the bug **TL;DR:** Under steady-state MoE inference (no warmup/CUDA-graph inv...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: l-len 32768 \ --max-num-seqs 32 \ --gpu-memory-utilization 0.9 \ --dtype bfloat16 \ --kv-cache-dtype fp8 \ --enforce-eager \ --tool-call-parser minimax_m2 \ --reasoning-parser minimax_m2 \ --trust-remote-code ``` Each D...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: inate_batch_across_dp for ray/mp DP backends → ~T+1h NCCL reduce_scatter deadlock > **TL;DR (added 2026-05-26):** Pinned to a missing dummy-run for the > `ray` / `mp` DP backends at > [`vllm/v1/worker/gpu_model_runner.p...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: ng in the per-step DP > collective; the partner DP rank advances by one; drift accumulates > ~one collective per asymmetric step; after ~1h a real MoE > `reduce_scatter` hangs. > Suggested fix (single-line semantic chan...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: zero-token-scheduled step skips coordinate_batch_across_dp for ray/mp DP backends → ~T+1h NCCL reduce_scatter deadlock > **TL;DR (added 2026-05-26):** Pinned to a missing dummy-run for the > `ray` / `mp` DP backends at...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ithub.com/vllm-project/vllm/issues/43547#issuecomment-4544158898). > The metadata/skip-path mechanism story in the original report below > turned out to be wrong (verified by code-trace) — symptom evidence > stands, the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
