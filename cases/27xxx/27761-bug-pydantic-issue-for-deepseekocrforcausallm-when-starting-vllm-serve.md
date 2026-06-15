# vllm-project/vllm#27761: [Bug]: pydantic issue for DeepseekOCRForCausalLM when starting vllm server for deepseek-ocr

| 字段 | 值 |
| --- | --- |
| Issue | [#27761](https://github.com/vllm-project/vllm/issues/27761) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: pydantic issue for DeepseekOCRForCausalLM when starting vllm server for deepseek-ocr

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Jun 4 2025, 08:56:18) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.10.192-183.736.amzn2.x86_64-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU 4: NVIDIA A100-SXM4-80GB GPU 5: NVIDIA A100-SXM4-80GB GPU 6: NVIDIA A100-SXM4-80GB GPU 7: NVIDIA A100-SXM4-80GB Nvidia driver version...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.35 ==================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: deepseek-ocr bug ### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.4.1 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: n Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Retbleed: Vulnerable Vulnerability Spec rstack overflo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
