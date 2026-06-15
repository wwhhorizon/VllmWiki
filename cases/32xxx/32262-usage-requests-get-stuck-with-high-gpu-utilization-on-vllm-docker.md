# vllm-project/vllm#32262: [Usage]: Requests get stuck with high GPU utilization on vLLM docker

| 字段 | 值 |
| --- | --- |
| Issue | [#32262](https://github.com/vllm-project/vllm/issues/32262) |
| 状态 | open |
| 标签 | usage;unstale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Requests get stuck with high GPU utilization on vLLM docker

### Issue 正文摘录

### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Jun 4 2025, 08:56:18) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.8.0-52-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA RTX A5000 GPU 1: NVIDIA RTX A5000 Nvidia driver version : 570.86.10 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== Architecture: x86_64...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Usage]: Requests get stuck with high GPU utilization on vLLM docker usage;unstale ### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Usage]: Requests get stuck with high GPU utilization on vLLM docker usage;unstale ### Your current environment ```text ============================== System Info ============================== OS
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: untime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA RTX A5000 GPU 1: NVIDIA RTX A5000 Nvidia driver version : 570.86.10 cuDNN version : Could not collect HIP runtime v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: CL_DEBUG=TRACE vLLM engine params: `--model Qwen3-Coder-30B-A3B-Instruct-FP8 --max_model_len 160000 --enable-log-outputs --enable-log-requests --enforce-eager --tensor-parallel-size 2 --gpu-memory-utilization 0.97 --ena...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
