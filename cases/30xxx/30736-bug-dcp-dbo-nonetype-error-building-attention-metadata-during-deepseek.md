# vllm-project/vllm#30736: [Bug] DCP/DBO: 'NoneType' error building attention_metadata during DeepSeek-V3.1 deployment dummy run

| 字段 | 值 |
| --- | --- |
| Issue | [#30736](https://github.com/vllm-project/vllm/issues/30736) |
| 状态 | closed |
| 标签 | bug;help wanted;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;fp8;moe;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] DCP/DBO: 'NoneType' error building attention_metadata during DeepSeek-V3.1 deployment dummy run

### Issue 正文摘录

### Your current environment ```bash ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.10.0a0+git9166f61 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.19 | packaged by conda-forge | (main, Oct 22 2025, 22:29:10) [GCC 14.3.0] (64-bit runtime) Python platform : Linux-5.15.0-124-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0 : NVIDIA H200 GPU 1 : NVIDIA H200 GPU 2 : NVIDIA H200 GPU 3 : NVIDIA H200 GPU 4 : NVIDIA H200 GPU 5 : NVIDIA H200 GPU 6 : NVIDIA H200 GPU 7 : NVIDIA H200 Nvidia driver version : 570.124.06 cuDNN version : Could not collect HIP runtime version :...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug] DCP/DBO: 'NoneType' error building attention_metadata during DeepSeek-V3.1 deployment dummy run bug;help wanted;stale ### Your current environment ```bash ============================== System Info ===============...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: : 2.10.0a0+git9166f61 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.19 |...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ntion_metadata during DeepSeek-V3.1 deployment dummy run bug;help wanted;stale ### Your current environment ```bash ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --max-model-len 131072 \ --gpu-memory-utilization 0.8 \ --quantization "fp8" \ --trust-remote-code \ --enable-auto-tool-choice \ --tool-call-parser "deepseek_v31" \ --chat-template dpsk-v3.1-tool-parser-vllm.jinja \ --h...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug] DCP/DBO: 'NoneType' error building attention_metadata during DeepSeek-V3.1 deployment dummy run bug;help wanted;stale ### Your current environment ```bash ============================== System Info ===============...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
