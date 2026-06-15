# vllm-project/vllm#44116: routed_experts all-zero with FlashInfer (TRTLLM/CUTLASS) MoE — wire FlashInfer routing_replay_out into the capturer

| 字段 | 值 |
| --- | --- |
| Issue | [#44116](https://github.com/vllm-project/vllm/issues/44116) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;sampling;triton |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> routed_experts all-zero with FlashInfer (TRTLLM/CUTLASS) MoE — wire FlashInfer routing_replay_out into the capturer

### Issue 正文摘录

## Summary `--enable-return-routed-experts` returns **all-zero** routing when the MoE layer runs on a fused **FlashInfer** kernel (TRTLLM / CUTLASS / CuteDSL / b12x). These kernels are *internal routers* (top-k is computed inside the kernel), so the Python capture hook is never reached. On Blackwell (SM100) `moe_backend='auto'` selects FlashInfer TRTLLM, so capture is effectively broken out of the box there. The good news: the **FlashInfer side is already merged** — the TRTLLM MoE ops expose a `routing_replay_out` output. vLLM just doesn't pass/consume it yet. This issue tracks wiring it through. ## Reproduction (GB200 / Blackwell, vllm ~0.22 nightly, flashinfer 0.6.11.post2) ``` vllm serve Qwen/Qwen3-30B-A3B --enable-return-routed-experts -tp 2 curl .../v1/completions -d '{"model":"...","prompt":"The capital of France is","max_tokens":16}' # decode choices[0].routed_experts (base64 npy) ``` - **auto → FlashInfer TRTLLM:** `routed_experts` shape `(T, 48, 8)`, `min=0 max=0`, nonzero `0/7680` — every token "routes to expert 0". - **`--moe-backend triton`:** shape `(T, 48, 8)`, `min=0 max=127`, **128 distinct experts**, exactly **8 distinct per (token, layer)** — correct top-8. Gener...

## 现有链接修复摘要

#39568 [RFC] Replace shared-memory routed experts with ModelRunnerOutput transfer and HTTP support | #44115 [Bugfix] routed_experts: fall back to Triton MoE backend (FlashInfer kernels bypass capture)

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 8: routed_experts all-zero with FlashInfer (TRTLLM/CUTLASS) MoE — wire FlashInfer routing_replay_out into the capturer ## Summary `--enable-return-routed-experts` returns **all-zero** routing when the MoE layer runs on a f...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: routed_experts all-zero with FlashInfer (TRTLLM/CUTLASS) MoE — wire FlashInfer routing_replay_out into the capturer ## Summary `--enable-return-routed-experts` returns **all-zero** routing when the MoE layer runs on a f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: uffer stays zero-initialized. - The experts kernel call (`experts/trtllm_bf16_moe.py` `apply()` → `flashinfer.fused_moe.trtllm_bf16_moe(...)`) does **not** pass `routing_replay_out`. ## Proposed work FlashInfer's `trtll...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: uted inside the kernel), so the Python capture hook is never reached. On Blackwell (SM100) `moe_backend='auto'` selects FlashInfer TRTLLM, so capture is effectively broken out of the box there. The good news: the **Flas...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: / Blackwell, vllm ~0.22 nightly, flashinfer 0.6.11.post2) ``` vllm serve Qwen/Qwen3-30B-A3B --enable-return-routed-experts -tp 2 curl .../v1/completions -d '{"model":"...","prompt":"The capital of France is","max_tokens...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39568](https://github.com/vllm-project/vllm/pull/39568) | mentioned | 0.45 | [RFC] Replace shared-memory routed experts with ModelRunnerOutput transfer and HTTP support | n capture + flashinfer backend). - capture transport + entrypoint: pr #39568, pr #38939. ## note this issue was drafted with ai assistance and is intended as an actionable startin… |
| [#44115](https://github.com/vllm-project/vllm/pull/44115) | mentioned | 0.45 | [Bugfix] routed_experts: fall back to Triton MoE backend (FlashInfer kernels bypass capture) | e #39701 redesign. - interim guardrail (prevents silent all-zero): pr #44115 (falls back to triton / errors when capture + flashinfer backend). - capture transport + entrypoint: p… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
