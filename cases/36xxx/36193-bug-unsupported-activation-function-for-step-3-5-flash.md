# vllm-project/vllm#36193: [Bug]: Unsupported Activation Function for Step-3.5-Flash

| 字段 | 值 |
| --- | --- |
| Issue | [#36193](https://github.com/vllm-project/vllm/issues/36193) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unsupported Activation Function for Step-3.5-Flash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ROCM Aiter Quantized MoE path does not support the SwiGLU_STEP activation function used by Step-3.5-Flash, causing runtime ValueError when using a quantized Step-3.5-Flash model for inference. In `vllm/model_executor/layers/quantization/quark/quark_moe.py`, `QuarkOCP_MX_MoEMethod` class's `rocm_aiter_fused_experts()` function calls `rocm_aiter_fused_experts` from `vllm.model_executor.layers.fused_moe.rocm_aiter_fused_moe`, which only supports SiLU and GeLU as activation functions. Error Traceback Expected: Process EngineCore_DP0: (EngineCore_DP0 pid=1000324) Traceback (most recent call last): (EngineCore_DP0 pid=1000324) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP0 pid=1000324) self.run() (EngineCore_DP0 pid=1000324) File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_DP0 pid=1000324) self._target(*self._args, **self._kwargs) (EngineCore_DP0 pid=1000324) File "/app/vllm_src/vllm/v1/engine/core.py", line 1104, in run_engine_core (EngineCore_DP0 pid=1000324) raise e (EngineCore_DP0 pid=1000324) File "/app/vllm_src/vllm/v1/engine/core.py", line 1090, i...

## 现有链接修复摘要

#39109 [ROCm] Fall back from AITER for SWIGLUSTEP MoE

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ^^^^^^^^^^^^^ (EngineCore_DP0 pid=1000324) File "/app/vllm_src/vllm/tracing/otel.py", line 178, in sync_wrapper (EngineCore_DP0 pid=1000324) return func(*args, **kwargs) (EngineCore_DP0 pid=1000324) ^^^^^^^^^^^^^^^^^^^^...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: h bug;rocm ### Your current environment ### 🐛 Describe the bug ROCM Aiter Quantized MoE path does not support the SwiGLU_STEP activation function used by Step-3.5-Flash, causing runtime ValueError when using a quantized...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Unsupported Activation Function for Step-3.5-Flash bug;rocm ### Your current environment ### 🐛 Describe the bug ROCM Aiter Quantized MoE path does not support the SwiGLU_STEP activation function used by Step-3.5-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: mine_available_memory (EngineCore_DP0 pid=1000324) self.model_runner.profile_run() (EngineCore_DP0 pid=1000324) File "/app/vllm_src/vllm/v1/worker/gpu_model_runner.py", line 5235, in profile_run (EngineCore_DP0 pid=1000...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: -Flash, causing runtime ValueError when using a quantized Step-3.5-Flash model for inference. In `vllm/model_executor/layers/quantization/quark/quark_moe.py`, `QuarkOCP_MX_MoEMethod` class's `rocm_aiter_fused_experts()`...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39109](https://github.com/vllm-project/vllm/pull/39109) | closes_keyword | 0.95 | [ROCm] Fall back from AITER for SWIGLUSTEP MoE | Fixes #36193 Signed-off-by: Bortlesboat <bortlesboat@users.noreply.github.com> |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
