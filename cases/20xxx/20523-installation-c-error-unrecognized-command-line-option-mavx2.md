# vllm-project/vllm#20523: [Installation]: c++: error: unrecognized command-line option ‘-mavx2’

| 字段 | 值 |
| --- | --- |
| Issue | [#20523](https://github.com/vllm-project/vllm/issues/20523) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;operator;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: c++: error: unrecognized command-line option ‘-mavx2’

### Issue 正文摘录

### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (aarch64) GCC version : (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version : Could not collect CMake version : version 4.0.3 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.7 (main, Dec 15 2023, 18:04:41) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-6.6.87.2-microsoft-standard-WSL2-aarch64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : False CUDA runtime version : No CUDA CUDA_MODULE_LOADING set to : N/A GPU models and configuration : No CUDA Nvidia driver version : No CUDA cuDNN version : No CUDA HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== Architecture: aarch64 CPU op-mode(s): 32-bit, 64-bit Addr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: c++: error: unrecognized command-line option ‘-mavx2’ installation ### Your current environment ```text ============================== System Info ============================== OS
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ==================== OS : Ubuntu 22.04.5 LTS (aarch64) GCC version : (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version : Could not collect CMake version : version 4.0.3 Libc version : glibc-2.35 ======
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Mitigation; Enhanced IBRS Vulnerability Spec rstack overflow...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: runtime version : No CUDA CUDA_MODULE_LOADING set to : N/A GPU models and configuration : No CUDA Nvidia driver version : No CUDA cuDNN version : No CUDA HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: dio==2.7.0 [pip3] torchvision==0.22.0 [pip3] transformers==4.53.1 [pip3] tritonclient==2.56.0 [conda] galore-torch 1.0 pypi_0 pypi [conda] mindietorch 1.0.0+torch2.1.0.abi0 pypi_0 pypi [conda] numpy 1.26.4

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
