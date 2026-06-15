# vllm-project/vllm#38718: [Bug]: NVFP4 MoE produces garbage output on SM120 (RTX 5080) with CPU Weight Offloading — Nemotron-Cascade-2-30B-A3B

| 字段 | 值 |
| --- | --- |
| Issue | [#38718](https://github.com/vllm-project/vllm/issues/38718) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel;moe;quantization |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: NVFP4 MoE produces garbage output on SM120 (RTX 5080) with CPU Weight Offloading — Nemotron-Cascade-2-30B-A3B

### Issue 正文摘录

### Your current environment - vLLM: 0.18.2rc1.dev25+gef53395e2 (built from main, 2026-04-01, includes PRs #33417 and #29242) - FlashInfer: 0.6.6 - PyTorch: 2.12.0a0+git6fcbf6d - CUDA: 13.2 - GPU: NVIDIA GeForce RTX 5080 (SM 12.0, 16 GB VRAM) - Driver: 595.45.04 - OS: Ubuntu 24.04, Linux 6.17.0-19-generic ### Model `nvidia/Nemotron-Cascade-2-30B-A3B-NVFP4` — NemotronH hybrid architecture (Mamba2 + MoE + Attention), NVFP4 quantized via modelopt. - 52 layers: 6 attention + 23 Mamba2 SSM + 23 MoE (128 routed experts, 6 active, 1 shared) - ~18.4 GB on disk → requires `--cpu-offload-gb 5` to fit on 16 GB VRAM ### Describe the bug All NVFP4 MoE backends produce numerically incorrect (garbage) output on SM120 when CPU offloading is enabled. The model loads successfully, the engine starts, and inference runs without errors — but the output is completely wrong (immediate EOS or random tokens). **Every MoE backend tested produces garbage:** | MoE Backend | CUDA Arch | Crash? | Output | |---|---|---|---| | FLASHINFER_CUTLASS | compute_120a (default) | Yes — illegal instruction | N/A | | FLASHINFER_CUTLASS | compute_120f (via `FLASHINFER_CUDA_ARCH_LIST=12.0f`) | No | Empty + EOS (1 token) | |...

## 现有链接修复摘要

#29242 [Kernel] Add NVFP4 MoE CUTLASS support for SM120 | #33417 fix: Add SM120 (RTX Blackwell) support for FlashInfer CUTLASS NVFP4 MoE kernels

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: NVFP4 MoE produces garbage output on SM120 (RTX 5080) with CPU Weight Offloading — Nemotron-Cascade-2-30B-A3B ### Your current environment - vLLM: 0.18.2rc1.dev25+gef53395e2 (built from main, 2026-04-01, includes...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: NVFP4 MoE produces garbage output on SM120 (RTX 5080) with CPU Weight Offloading — Nemotron-Cascade-2-30B-A3B ### Your current environment - vLLM: 0.18.2rc1.dev25+gef53395e2 (built from main, 2026-04-01, includes...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: UDA_ARCH_LIST=12.0f`) | No | Empty + EOS (1 token) | | VLLM_CUTLASS | precompiled | No | ":" + EOS (2 tokens) | | MARLIN | N/A | No | Garbage | **Example outputs:** | Prompt | Output | Expected | |---|---|---| | "What i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: AM) - Driver: 595.45.04 - OS: Ubuntu 24.04, Linux 6.17.0-19-generic ### Model `nvidia/Nemotron-Cascade-2-30B-A3B-NVFP4` — NemotronH hybrid architecture (Mamba2 + MoE + Attention), NVFP4 quantized via modelopt. - 52 laye...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: fit on 16 GB VRAM ### Describe the bug All NVFP4 MoE backends produce numerically incorrect (garbage) output on SM120 when CPU offloading is enabled. The model loads successfully, the engine starts, and inference runs w...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29242](https://github.com/vllm-project/vllm/pull/29242) | mentioned | 0.45 | [Kernel] Add NVFP4 MoE CUTLASS support for SM120 | ev25+gef53395e2 (built from main, 2026-04-01, includes prs #33417 and #29242) - flashinfer: 0.6.6 - pytorch: 2.12.0a0+git6fcbf6d - cuda: 13.2 - gpu: nvidia geforce rtx 5080 (sm 12… |
| [#33417](https://github.com/vllm-project/vllm/pull/33417) | mentioned | 0.45 | fix: Add SM120 (RTX Blackwell) support for FlashInfer CUTLASS NVFP4 MoE kernels | 0.18.2rc1.dev25+gef53395e2 (built from main, 2026-04-01, includes prs #33417 and #29242) - flashinfer: 0.6.6 - pytorch: 2.12.0a0+git6fcbf6d - cuda: 13.2 - gpu: nvidia geforce rtx… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
