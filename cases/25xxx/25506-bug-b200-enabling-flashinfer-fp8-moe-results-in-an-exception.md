# vllm-project/vllm#25506: [Bug]: [B200] Enabling FlashInfer FP8 MoE results in an exception

| 字段 | 值 |
| --- | --- |
| Issue | [#25506](https://github.com/vllm-project/vllm/issues/25506) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [B200] Enabling FlashInfer FP8 MoE results in an exception

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running DeepSeekR1 on 8xB200 with VLLM_USE_FLASHINFER_MOE_FP8=1 results in the following exception: ``` File "/home/alexm/code/vllm/vllm/model_executor/layers/fused_moe/modular_kernel.py", line 923, in forward (EngineCore_DP0 pid=4145559) (Worker_TP0 pid=4145565) ERROR 09-23 12:17:54 [multiproc_executor.py:671] fused_out = self._maybe_chunk_fused_experts( (EngineCore_DP0 pid=4145559) (Worker_TP0 pid=4145565) ERROR 09-23 12:17:54 [multiproc_executor.py:671] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=4145559) (Worker_TP0 pid=4145565) ERROR 09-23 12:17:54 [multiproc_executor.py:671] File "/home/alexm/code/vllm/vllm/model_executor/layers/fused_moe/modular_kernel.py", line 711, in _maybe_chunk_fused_experts (EngineCore_DP0 pid=4145559) (Worker_TP0 pid=4145565) ERROR 09-23 12:17:54 [multiproc_executor.py:671] return self._do_fused_experts( (EngineCore_DP0 pid=4145559) (Worker_TP0 pid=4145565) ERROR 09-23 12:17:54 [multiproc_executor.py:671] ^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=4145559) (Worker_TP0 pid=4145565) ERROR 09-23 12:17:54 [multiproc_executor.py:671] File "/home/alexm/code/vllm/vllm/model_executor/layers/fused_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;fp8;moe;opera...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: [B200] Enabling FlashInfer FP8 MoE results in an exception bug ### Your current environment ### 🐛 Describe the bug Running DeepSeekR1 on 8xB200 with VLLM_USE_FLASHINFER_MOE_FP8=1 results in the following exceptio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: [B200] Enabling FlashInfer FP8 MoE results in an exception bug ### Your current environment ### 🐛 Describe the bug Running DeepSeekR1 on 8xB200 with VLLM_USE_FLASHINFER_MOE_FP8=1 results in the following exceptio...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: [B200] Enabling FlashInfer FP8 MoE results in an exception bug ### Your current environment ### 🐛 Describe the bug Running DeepSeekR1 on 8xB200 with VLLM_USE_FLASHINFER_MOE_FP8=1 results in the following exceptio...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: [B200] Enabling FlashInfer FP8 MoE results in an exception bug ### Your current environment ### 🐛 Describe the bug Running DeepSeekR1 on 8xB200 with VLLM_USE_FLASHINFER_MOE_FP8=1 results in the following exceptio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
