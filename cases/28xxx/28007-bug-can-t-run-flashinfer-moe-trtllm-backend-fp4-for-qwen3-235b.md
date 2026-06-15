# vllm-project/vllm#28007: [Bug]: Can't run Flashinfer MoE TRTLLM backend FP4 for Qwen3 235B

| 字段 | 值 |
| --- | --- |
| Issue | [#28007](https://github.com/vllm-project/vllm/issues/28007) |
| 状态 | closed |
| 标签 | bug;nvidia |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't run Flashinfer MoE TRTLLM backend FP4 for Qwen3 235B

### Issue 正文摘录

### Your current environment ``` ================================= [9ec78181b8c7:56683:0:56683] Caught signal 8 (Floating point exception: integer divide by zero) ==== backtrace (tid: 56683) ==== 0 /opt/hpcx/ucx/lib/libucs.so.0(ucs_handle_error+0x2e4) [0x7d74482f5654] 1 /opt/hpcx/ucx/lib/libucs.so.0(+0x3684c) [0x7d74482f584c] 2 /opt/hpcx/ucx/lib/libucs.so.0(+0x36bda) [0x7d74482f5bda] 3 /usr/lib/x86_64-linux-gnu/libc.so.6(+0x45330) [0x7d78508a0330] 4 /root/.cache/flashinfer/0.4.1/100a/cached_ops/fused_moe_trtllm_sm100/fused_moe_trtllm_sm100.so(_ZN3moe3dev7routing15routingDeepSeek12KernelParamsIf13__nv_bfloat16Lb0ELb1EE15setKernelParamsERKNS2_4DataE+0x7f) [0x7d7281d7d39f] 5 /root/.cache/flashinfer/0.4.1/100a/cached_ops/fused_moe_trtllm_sm100/fused_moe_trtllm_sm100.so(_ZN3moe3dev7routing15routingDeepSeek7runImplERNS2_4DataEPv+0x358d) [0x7d7281d6cdad] 6 /root/.cache/flashinfer/0.4.1/100a/cached_ops/fused_moe_trtllm_sm100/fused_moe_trtllm_sm100.so(_ZN12tensorrt_llm7kernels13trtllmgen_moe7Routing6Runner3runEPvS4_iiiiiiifPiS5_S5_S5_S5_S5_S4_S5_S5_S5_S5_N11batchedGemm6trtllm3gen5DtypeEbbNS2_17RoutingMethodTypeEP11CUstream_st+0x1e81) [0x7d7281d66791] 7 /root/.cache/flashinfer/0.4.1/100a/ca...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Can't run Flashinfer MoE TRTLLM backend FP4 for Qwen3 235B bug;nvidia ### Your current environment ``` ================================= [9ec78181b8c7:56683:0:56683] Caught signal 8 (Floating point exception: int...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: Can't run Flashinfer MoE TRTLLM backend FP4 for Qwen3 235B bug;nvidia ### Your current environment ``` ================================= [9ec78181b8c7:56683:0:56683] Caught signal 8 (Floating point exception: int...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: Can't run Flashinfer MoE TRTLLM backend FP4 for Qwen3 235B bug;nvidia ### Your current environment ``` ================================= [9ec78181b8c7:56683:0:56683] Caught signal 8 (Floating point exception: int...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculativ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 0330] 4 /root/.cache/flashinfer/0.4.1/100a/cached_ops/fused_moe_trtllm_sm100/fused_moe_trtllm_sm100.so(_ZN3moe3dev7routing15routingDeepSeek12KernelParamsIf13__nv_bfloat16Lb0ELb1EE15setKernelParamsERKNS2_4DataE+0x7f) [0x...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
