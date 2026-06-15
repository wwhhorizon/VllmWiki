# vllm-project/vllm#36793: [Bug]: TP=2 DP=2 Broken for Qwen3-Next W4A16

| 字段 | 值 |
| --- | --- |
| Issue | [#36793](https://github.com/vllm-project/vllm/issues/36793) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TP=2 DP=2 Broken for Qwen3-Next W4A16

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am unable to use the --data-parallel-size flag when using vllm serve ``` chg run --gpus 4 -- vllm serve inference-optimization/Qwen3-Coder-Next.w4a16 --enable-auto-tool-choice --tool-call-parser qwen3_coder --data-parallel-size 2 --tensor-parallel-size 2 ``` VLLM 15 serve works but it fails on inference ``` (EngineCore_DP2 pid=290892) ERROR 03-11 13:25:11 [core.py:948] torch.AcceleratorError: CUDA error: an illegal memory access was encountered (EngineCore_DP2 pid=290892) ERROR 03-11 13:25:11 [core.py:948] Search for `cudaErrorIllegalAddress' in https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__TYPES.html for more information. (EngineCore_DP2 pid=290892) ERROR 03-11 13:25:11 [core.py:948] CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. (EngineCore_DP2 pid=290892) ERROR 03-11 13:25:11 [core.py:948] For debugging consider passing CUDA_LAUNCH_BLOCKING=1 (EngineCore_DP2 pid=290892) ERROR 03-11 13:25:11 [core.py:948] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` VLLM 16, vllm serve does not run at all both for MOE and Non-MOE...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: LOCKING=1 (EngineCore_DP2 pid=290892) ERROR 03-11 13:25:11 [core.py:948] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` VLLM 16, vllm serve does not run at all both for MOE and Non-MOE models re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 2 pid=290892) ERROR 03-11 13:25:11 [core.py:948] torch.AcceleratorError: CUDA error: an illegal memory access was encountered (EngineCore_DP2 pid=290892) ERROR 03-11 13:25:11 [core.py:948] Search for `cudaErrorIllegalAd...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: TP=2 DP=2 Broken for Qwen3-Next W4A16 bug ### Your current environment ### 🐛 Describe the bug I am unable to use the --data-parallel-size flag when using vllm serve ``` chg run --gpus 4 -- vllm serve inference-op...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: e-side assertions. ``` VLLM 16, vllm serve does not run at all both for MOE and Non-MOE models resulting in cuda errors ``` Worker pid=307623) (Worker_DP0_TP0 pid=307623) ERROR 03-11 13:50:40 [multiproc_executor.py:880]...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ) ERROR 03-11 13:50:40 [multiproc_executor.py:880] self.model_runner.profile_run() (Worker pid=307623) (Worker_DP0_TP0 pid=307623) ERROR 03-11 13:50:40 [multiproc_executor.py:880] File "/home/Chibukach/16VLLM/.venv/lib6...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
