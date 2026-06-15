# vllm-project/vllm#32109: [Bug]: Blackwell (SM120) FP8 MoE path fails for GLM-4.7 : No compiled cutlass_scaled_mm for CUDA device capability: 120 on RTX PRO 6000 Blackwell

| 字段 | 值 |
| --- | --- |
| Issue | [#32109](https://github.com/vllm-project/vllm/issues/32109) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Blackwell (SM120) FP8 MoE path fails for GLM-4.7 : No compiled cutlass_scaled_mm for CUDA device capability: 120 on RTX PRO 6000 Blackwell

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I’m trying to serve zai-org/GLM-4.7-FP8 on RTX PRO 6000 Blackwell (SM120 / compute capability 12.0) and vLLM fails during startup with a CUTLASS kernel selection error: No compiled cutlass_scaled_mm for CUDA device capability: 120. Required capability: 90 or 100 What I tried - vLLM 0.13 wheel - vLLM nightly wheel - Local build from source, including: - TORCH_CUDA_ARCH_LIST="12.0 12.1" - VLLM_CUTLASS_SRC_DIR pointing at CUTLASS 4.3.5 - Also attempted disabling the CUTLASS scaled-mm path via LLM_DISABLED_KERNELS=CutlassScaledMMLinearKernel All variants still hit the same error. Repro command ```bash vllm serve zai-org/GLM-4.7-FP8 \ --tensor-parallel-size 4 \ --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 1 \ --tool-call-parser glm47 \ --reasoning-parser glm45 \ --enable-auto-tool-choice \ --served-model-name glm-4.7-fp8 ``` Error / stack trace excerpt ``` (Worker_TP1 pid=187666) ERROR 01-10 22:23:50 [multiproc_executor.py:822] File "/kmmdata/vllm/vllm/vllm/compilation/cuda_graph.py", line 222, in __call__ (Worker_TP1 pid=187666) ERROR 01-10 22:23:50 [multiproc_executor.py:822] return self.runnable(*ar...

## 现有链接修复摘要

#32237 [Fix][MoE] Add SM120 support for FP8 MoE path

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: Blackwell (SM120) FP8 MoE path fails for GLM-4.7 : No compiled cutlass_scaled_mm for CUDA device capability: 120 on RTX PRO 6000 Blackwell bug ### Your current environment ### 🐛 Describe the bug I’m trying to ser...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Blackwell (SM120) FP8 MoE path fails for GLM-4.7 : No compiled cutlass_scaled_mm for CUDA device capability: 120 on RTX PRO 6000 Blackwell bug ### Your current environment ### 🐛 Describe the bug I’m trying to ser...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: Blackwell (SM120) FP8 MoE path fails for GLM-4.7 : No compiled cutlass_scaled_mm for CUDA device capability: 120 on RTX PRO 6000 Blackwell bug ### Your current environment ### 🐛 Describe the bug I’m trying to ser...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Blackwell (SM120) FP8 MoE path fails for GLM-4.7 : No compiled cutlass_scaled_mm for CUDA device capability: 120 on RTX PRO 6000 Blackwell bug ### Your current environment ### 🐛 Describe the bug I’m trying to ser...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: Blackwell (SM120) FP8 MoE path fails for GLM-4.7 : No compiled cutlass_scaled_mm for CUDA device capability: 120 on RTX PRO 6000 Blackwell bug ### Your current environment ### 🐛 Describe the bug I’m trying to ser...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32237](https://github.com/vllm-project/vllm/pull/32237) | closes_keyword | 0.95 | [Fix][MoE] Add SM120 support for FP8 MoE path | Resolves #32109 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
