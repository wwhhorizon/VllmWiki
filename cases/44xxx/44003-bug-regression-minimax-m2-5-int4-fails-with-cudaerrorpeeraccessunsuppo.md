# vllm-project/vllm#44003: [Bug]: [Regression] MiniMax-M2.5-int4 fails with cudaErrorPeerAccessUnsupported since PR #43410

| 字段 | 值 |
| --- | --- |
| Issue | [#44003](https://github.com/vllm-project/vllm/issues/44003) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [Regression] MiniMax-M2.5-int4 fails with cudaErrorPeerAccessUnsupported since PR #43410

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Description Running `Intel/Minimax-M2.5-int4-AutoRound` on vLLM nightly fails with `cudaErrorPeerAccessUnsupported: 217` during model loading at `MiniMaxText01RMSNormTP.__init__`. Version `0.21.1rc1.dev268+gd0a100c87` works correctly. Tagging the original author, @jeejeelee for visibility. Full details are included above, but for brevity, I am running 8 RTX 3090 on a single node, all on PCIe. No NVLink. GLM suggests the following potential cause: PR #43410 ("[Kernel] Porting fuse_minimax_qk_norm to manual fusion", merged May 26 2026) moved the LamportWorkspace initialisation from lazy (first forward pass) to eager (__init__ time). The IpcBuffer class in lamport_workspace.py unconditionally calls `cudaIpcOpenMemHandle` with `cudaIpcMemLazyEnablePeerAccess`, which fails on GPU topologies that do not support peer-to-peer access (e.g., PCIe-only systems without NVLink). Working version: `0.21.1rc1.dev268+gd0a100c87` Broken version: `0.21.1rc1.dev433+g0585b5ba2` ### Expected behavior The model should load successfully, falling back to NCCL-based AllReduce when P2P access is unavailable, as it did prior to PR #43410. ### Reproducti...

## 现有链接修复摘要

#44261 [Bugfix] Skip MiniMax RMSNorm Lamport workspace when custom all-reduce is disabled

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: pported: 217` during model loading at `MiniMaxText01RMSNormTP.__init__`. Version `0.21.1rc1.dev268+gd0a100c87` works correctly. Tagging the original author, @jeejeelee for visibility. Full details are included above, bu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: [Regression] MiniMax-M2.5-int4 fails with cudaErrorPeerAccessUnsupported since PR #43410 bug ### Your current environment ### 🐛 Describe the bug ### Description Running `Intel/Minimax-M2.5-int4-AutoRound` on vLLM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: [Regression] MiniMax-M2.5-int4 fails with cudaErrorPeerAccessUnsupported since PR #43410 bug ### Your current environment ### 🐛 Describe the bug ### Description Running `Intel/Minimax-M2.5-int4-AutoRound` on vLLM...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: -parallel --max-model-len auto --gpu-memory-utilization 0.93 --attention-backend flashinfer --enable-flashinfer-autotune --reasoning-parser minimax_m2 --tool-call-parser minimax_m2 --enable-auto-tool-choice --max-num-se...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: on vLLM nightly fails with `cudaErrorPeerAccessUnsupported: 217` during model loading at `MiniMaxText01RMSNormTP.__init__`. Version `0.21.1rc1.dev268+gd0a100c87` works correctly. Tagging the original author, @jeejeelee...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#44261](https://github.com/vllm-project/vllm/pull/44261) | closes_keyword | 0.95 | [Bugfix] Skip MiniMax RMSNorm Lamport workspace when custom all-reduce is disabled | Fixes #44003. MiniMax RMSNorm's Lamport fused all-reduce path currently creates a CUDA IPC workspace whenever the fused op exists and TP world size is greater than 1. That bypasse |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
