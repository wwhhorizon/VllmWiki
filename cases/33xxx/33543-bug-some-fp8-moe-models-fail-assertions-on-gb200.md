# vllm-project/vllm#33543: [Bug]: Some FP8 MoE models fail assertions on GB200

| 字段 | 值 |
| --- | --- |
| Issue | [#33543](https://github.com/vllm-project/vllm/issues/33543) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Some FP8 MoE models fail assertions on GB200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug #### Description Currently on SM100 GPUs, for FP8 MoE models, the flashinfer MoE backend is enabled by default, which causes the following errors. Some models' routing requires FP32 precision, and the routing input is dynamically converted to FP32, making this MoE model unsuitable for using this backend. ```python (EngineCore_DP0 pid=1661750) (Worker_TP0 pid=1661756) ERROR 02-02 04:06:37 [multiproc_executor.py:852] File "/mnt/data/jeejee/vllm_dev/vllm/.venv/lib/python3.12/site-packages/flashinfer/fused_moe/core.py", line 1635, in trtllm_fp8_block_scale_moe_op (EngineCore_DP0 pid=1661750) (Worker_TP0 pid=1661756) ERROR 02-02 04:06:37 [multiproc_executor.py:852] result = moe_op.trtllm_fp8_block_scale_moe( (EngineCore_DP0 pid=1661750) (Worker_TP0 pid=1661756) ERROR 02-02 04:06:37 [multiproc_executor.py:852] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=1661750) (Worker_TP0 pid=1661756) ERROR 02-02 04:06:37 [multiproc_executor.py:852] File "python/tvm_ffi/cython/function.pxi", line 923, in tvm_ffi.core.Function.__call__ (EngineCore_DP0 pid=1661750) (Worker_TP0 pid=1661756) ERROR 02-02 04:06:37 [multiproc_executor.py:852] Fil...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: Some FP8 MoE models fail assertions on GB200 bug ### Your current environment ### 🐛 Describe the bug #### Description Currently on SM100 GPUs, for FP8 MoE models, the flashinfer MoE backend is enabled by default,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: bug #### Description Currently on SM100 GPUs, for FP8 MoE models, the flashinfer MoE backend is enabled by default, which causes the following errors. Some models' routing requires FP32 precision, and the routing input...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: which causes the following errors. Some models' routing requires FP32 precision, and the routing input is dynamically converted to FP32, making this MoE model unsuitable for using this backend. ```python (EngineCore_DP0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Some FP8 MoE models fail assertions on GB200 bug ### Your current environment ### 🐛 Describe the bug #### Description Currently on SM100 GPUs, for FP8 MoE models, the flashinfer MoE backend is enabled by default,...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Some FP8 MoE models fail assertions on GB200 bug ### Your current environment ### 🐛 Describe the bug #### Description Currently on SM100 GPUs, for FP8 MoE models, the flashinfer MoE backend is enabled by default,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
