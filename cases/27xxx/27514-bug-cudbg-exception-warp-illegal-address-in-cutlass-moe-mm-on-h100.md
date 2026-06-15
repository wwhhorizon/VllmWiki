# vllm-project/vllm#27514: [Bug]: CUDBG_EXCEPTION_WARP_ILLEGAL_ADDRESS in `cutlass_moe_mm` on h100

| 字段 | 值 |
| --- | --- |
| Issue | [#27514](https://github.com/vllm-project/vllm/issues/27514) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDBG_EXCEPTION_WARP_ILLEGAL_ADDRESS in `cutlass_moe_mm` on h100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I encountered a bug while running Maverick-FP8 on 8xH100 and GLM-4.6-FP8 on 8xH100 on vLLM 0.10.2 and vLLM 0.11.0. I've root-caused it down to the cutlass kernel and provide a model-independent reproduction. Note that I tested Maverick on 0.8.4 and did _not_ see this bug. Note also that the repro script below uses the GLM-4.6-FP8 config. ``` $ python reproduce_cutlass_failure.py cutlass_repro.json INFO 10-25 21:31:11 [__init__.py:216] Automatically detected platform cuda. Using device: cuda:0 PyTorch: 2.8.0+cu128, vLLM: 0.11.0 M,N,K = 256,384,5120 | experts = 160 per_act_token=True per_out_ch=True Invoking cutlass_moe_mm ... Traceback (most recent call last): File "/ephemeral/block/reproduce_cutlass_failure.py", line 93, in main() File "/ephemeral/block/reproduce_cutlass_failure.py", line 89, in main torch.cuda.synchronize(device) File "/ephemeral/block/.venv/lib/python3.11/site-packages/torch/cuda/__init__.py", line 1085, in synchronize return torch._C._cuda_synchronize() ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ torch.AcceleratorError: CUDA error: an illegal memory access was encountered CUDA kernel errors might be asynchronously reported a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ight be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` When I enable light coredumps, I see: ``` [21:28:42.017208] coredump: Dete...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: t ### 🐛 Describe the bug I encountered a bug while running Maverick-FP8 on 8xH100 and GLM-4.6-FP8 on 8xH100 on vLLM 0.10.2 and vLLM 0.11.0. I've root-caused it down to the cutlass kernel and provide a model-independent...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: CUDBG_EXCEPTION_WARP_ILLEGAL_ADDRESS in `cutlass_moe_mm` on h100 bug;stale ### Your current environment ### 🐛 Describe the bug I encountered a bug while running Maverick-FP8 on 8xH100 and GLM-4.6-FP8 on 8xH100 on...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: CUDBG_EXCEPTION_WARP_ILLEGAL_ADDRESS in `cutlass_moe_mm` on h100 bug;stale ### Your current environment ### 🐛 Describe the bug I encountered a bug while running Maverick-FP8 on 8xH100 and GLM-4.6-FP8 on 8xH100 on...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: CUDBG_EXCEPTION_WARP_ILLEGAL_ADDRESS in `cutlass_moe_mm` on h100 bug;stale ### Your current environment ### 🐛 Describe the bug I encountered a bug while running Maverick-FP8 on 8xH100 and GLM-4.6-FP8 on 8xH100 on...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
