# vllm-project/vllm#36435: [Bug]: Responses API streaming emits tool call XML as `response.output_text.delta` instead of `response.function_call_arguments.delta` for non-harmony models

| 字段 | 值 |
| --- | --- |
| Issue | [#36435](https://github.com/vllm-project/vllm/issues/36435) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Responses API streaming emits tool call XML as `response.output_text.delta` instead of `response.function_call_arguments.delta` for non-harmony models

### Issue 正文摘录

### Your current environment ```text Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 22.04.4 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.13.12 (main, Feb 12 2026, 00:45:41) [Clang 21.1.4 ] (64-bit runtime) Python platform : Linux-6.5.0-1015-aws-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 11.5.119 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA A10G Nvidia driver version : 535.183.01 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== A...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.4 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.10.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.13.12...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: lta` instead of `response.function_call_arguments.delta` for non-harmony models bug ### Your current environment ```text Collecting environment information... uv is set ============================== System Info =======...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.4 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.9.1.4 [pip3] nvidia-cuda-cupti-cu12==12.9.79 [pip3] nvidia-cuda-nvrtc-c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Mitigation; untrained return thunk; SMT enabled with STIBP protection Vulnerability Spec rstack overflow: Vul...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
