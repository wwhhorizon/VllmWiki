# vllm-project/vllm#30750: [Bug]: assert part_size_n % scales.nelement() == 0 (Marlin FP8 Kernel)

| 字段 | 值 |
| --- | --- |
| Issue | [#30750](https://github.com/vllm-project/vllm/issues/30750) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: assert part_size_n % scales.nelement() == 0 (Marlin FP8 Kernel)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Issue occured when testing newly released `mistralai/Devstral-2-123B-Instruct-2512`. Repro (with CUDA_VISIBLE_DEVICES limiting vLLM to the 2 A100s): ``` vllm serve mistralai/Devstral-2-123B-Instruct-2512 --served-model-name Devstral-2 --enable-auto-tool-choice --tool-call-parser mistral --swap-space 16 --max-num-seqs 32 --max-model-len 262144 --gpu-memory-utilization 0.97 --tensor-parallel-size 2 --trust-remote-code ``` This model is released as FP8. Since Ampere does not natively support FP8, it is utilizing Marlin kernel. In this case, vllm fails to start up, with the following error message: ``` (Worker_TP1 pid=407) WARNING 12-16 06:22:54 [marlin_utils_fp8.py:99] Your GPU does not have native support for FP8 computation but FP8 quantization is being used. Weight-only FP8 compression will be used leveraging the Marlin kernel. This may degrade performance for compute-heavy workloads. (Worker_TP0 pid=406) ERROR 12-16 06:22:55 [multiproc_executor.py:754] WorkerProc failed to start. (Worker_TP0 pid=406) ERROR 12-16 06:22:55 [multiproc_executor.py:754] Traceback (most recent call last): (Worker_TP0 pid=406) ERROR 12-16 06:22:55 [mul...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: g newly released `mistralai/Devstral-2-123B-Instruct-2512`. Repro (with CUDA_VISIBLE_DEVICES limiting vLLM to the 2 A100s): ``` vllm serve mistralai/Devstral-2-123B-Instruct-2512 --served-model-name Devstral-2 --enable-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: assert part_size_n % scales.nelement() == 0 (Marlin FP8 Kernel) bug ### Your current environment ### 🐛 Describe the bug Issue occured when testing newly released `mistralai/Devstral-2-123B-Instruct-2512`. Repro (...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;k...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: A100s): ``` vllm serve mistralai/Devstral-2-123B-Instruct-2512 --served-model-name Devstral-2 --enable-auto-tool-choice --tool-call-parser mistral --swap-space 16 --max-num-seqs 32 --max-model-len 262144 --gpu-memory-ut...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: gits;speculative_decoding cuda;fp8;kernel;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
