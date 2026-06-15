# vllm-project/vllm#27751: [Bug]: Issue with  Flashinfer Autotune + DP or TP + Eager-Mode

| 字段 | 值 |
| --- | --- |
| Issue | [#27751](https://github.com/vllm-project/vllm/issues/27751) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Issue with  Flashinfer Autotune + DP or TP + Eager-Mode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running ``` VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 VLLM_ALL2ALL_BACKEND="deepep_high_throughput" vllm serve openai/gpt-oss-20b --data-parallel-size 2 --tensor-parallel-size 1 --enable-expert-parallel --no-enable-prefix-caching --enforce-eager ``` or ``` VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 VLLM_ALL2ALL_BACKEND="allgather_reducescatter" canhazgpu run -g2 -- vllm serve openai/gpt-oss-20b --data-parallel-size 2 --tensor-parallel-size 1 --enable-expert-parallel --no-enable-prefix-caching --port 9010 --enforce-eager ``` Fails during engine startup with, ``` (EngineCore_DP1 pid=3074289) File "/home/varun-sundar-rabindranath/code/vllm/vllm-test/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl (EngineCore_DP1 pid=3074289) return forward_call(*args, **kwargs) (EngineCore_DP1 pid=3074289) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP1 pid=3074289) File "/home/varun-sundar-rabindranath/code/vllm/vllm/model_executor/layers/fused_moe/modular_kernel.py", line 1168, in forward (EngineCore_DP1 pid=3074289) fused_out = self._fused_experts( (EngineCore_DP1 pid=3074289) ^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP1 pid=30742...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ent error. ("deepep_high_throughput", turns cuda graph off but has torch-compile on - so it generally is a eager-mode issue) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ronment ### 🐛 Describe the bug Running ``` VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 VLLM_ALL2ALL_BACKEND="deepep_high_throughput" vllm serve openai/gpt-oss-20b --data-parallel-size 2 --tensor-parallel-size 1 --enable-exper...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Issue with Flashinfer Autotune + DP or TP + Eager-Mode bug ### Your current environment ### 🐛 Describe the bug Running ``` VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 VLLM_ALL2ALL_BACKEND="deepep_high_throughput" vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: _scale_routed_moe (EngineCore_DP1 pid=3074289) return get_trtllm_moe_sm100_module().trtllm_fp4_block_scale_moe( (EngineCore_DP1 pid=3074289) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP1 pid=...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: FP8=1 VLLM_ALL2ALL_BACKEND="deepep_high_throughput" vllm serve openai/gpt-oss-20b --data-parallel-size 2 --tensor-parallel-size 1 --enable-expert-parallel --no-enable-prefix-caching --enforce-eager ``` or ``` VLLM_USE_F...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
