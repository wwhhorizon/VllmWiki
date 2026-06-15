# vllm-project/vllm#31856: [Bug]: Text degeneration / repetition loops with MiniMax-M2.1-NVFP4 on v0.14.0rc1.dev308

| 字段 | 值 |
| --- | --- |
| Issue | [#31856](https://github.com/vllm-project/vllm/issues/31856) |
| 状态 | open |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Text degeneration / repetition loops with MiniMax-M2.1-NVFP4 on v0.14.0rc1.dev308

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary Text degeneration / infinite repetition loops when using **MiniMax-M2.1-NVFP4** (NVFP4 quantized MoE model) with expert parallelism enabled. The model enters repetition loops during reasoning (inside ` ` blocks), never produces a proper answer, and hits `max_tokens` with `finish_reason=length`. ## Regression Info | Version | Commit | Status | |---------|--------|--------| | `0.14.0rc1.dev201` | `adcf682fc` | ✅ Works correctly | | `0.14.0rc1.dev308` | `d49899732` | ❌ Text degeneration | **Same configuration used for both versions** - the only difference is the vLLM version. ## Symptoms - Model starts reasoning in ` ` block - Gets stuck repeating phrases like: - `"We need to compute a total distance traveled based on a given input parameters"` - `"system. We had $50. She buys 3 books..."` - Sometimes hallucinates fake `System:` / `User:` turn markers - Never exits the loop, hits `max_tokens` - `finish_reason: length` (not `stop`) **Trigger:** Any prompt requiring multi-step reasoning (not limited to math - users report issues across various reasoning tasks). ## Reproduction **Model:** `lukealonso/MiniMax-M2.1-NVFP4` **St...

## 现有链接修复摘要

#42171 Avoid mixed CUDA graphs for NVFP4 CUTLASS MoE | #42670 [Bugfix][NVFP4] Expose batch-invariance for FlashInfer + CUTLASS FP4 MoE

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: Text degeneration / repetition loops with MiniMax-M2.1-NVFP4 on v0.14.0rc1.dev308 ### Your current environment ### 🐛 Describe the bug ## Summary Text degeneration / infinite repetition loops when using **MiniMax-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: nd hits `max_tokens` with `finish_reason=length`. ## Regression Info | Version | Commit | Status | |---------|--------|--------| | `0.14.0rc1.dev201` | `adcf682fc` | ✅ Works correctly | | `0.14.0rc1.dev308` | `d49899732...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: **MiniMax-M2.1-NVFP4** (NVFP4 quantized MoE model) with expert parallelism enabled. The model enters repetition loops during reasoning (inside ` ` blocks), never produces a proper answer, and hits `max_tokens` with `fin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: Model:** `lukealonso/MiniMax-M2.1-NVFP4` **Startup command:** ```bash # FlashInfer MoE configuration export VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8_CUTLASS=1 export VLLM_FLASHINFER_MOE_BACKEND=throughput export VLLM_USE_FLA...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: nite repetition loops when using **MiniMax-M2.1-NVFP4** (NVFP4 quantized MoE model) with expert parallelism enabled. The model enters repetition loops during reasoning (inside ` ` blocks), never produces a proper answer...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42171](https://github.com/vllm-project/vllm/pull/42171) | closes_keyword | 0.95 | Avoid mixed CUDA graphs for NVFP4 CUTLASS MoE | Fixes #31856. This adds a targeted guardrail for NVFP4 MoE models using CUTLASS-family MoE backends. When the selected config combines: - NVFP4 MoE - `moe_backend` in `auto`, `cu |
| [#42670](https://github.com/vllm-project/vllm/pull/42670) | mentioned | 0.6 | [Bugfix][NVFP4] Expose batch-invariance for FlashInfer + CUTLASS FP4 MoE | fer`, `MiniMax-M2 repetition`) returned only unrelated changes. Issue #31856 itself has root-cause analysis from the reporter but no fix linked. ## Test plan Repro environment: B2… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
