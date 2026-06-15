# vllm-project/vllm#24869: [Installation]: Assertion Error while serving vllm due to this error : assert param_data.shape == loaded_weight.shape 

| 字段 | 值 |
| --- | --- |
| Issue | [#24869](https://github.com/vllm-project/vllm/issues/24869) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Assertion Error while serving vllm due to this error : assert param_data.shape == loaded_weight.shape 

### Issue 正文摘录

### Your current environment python3 collect_env.py Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.12 (main, May 27 2025, 17:12:29) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.8.0-1031-azure-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A10-24Q Nvidia driver version : 550.144.06 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info =========...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: Assertion Error while serving vllm due to this error : assert param_data.shape == loaded_weight.shape installation;stale ### Your current environment python3 collect_env.py Collecting environment inform
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.12 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ur current environment python3 collect_env.py Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: orch version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.7.1 [pip3] torchvision==0.22.1 [pip3] transformers==4.54.1 [pip3] triton==3.3.1 [conda] Could not collect ============================== vLLM Info ============================== ROCM Version : Could not collect v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
