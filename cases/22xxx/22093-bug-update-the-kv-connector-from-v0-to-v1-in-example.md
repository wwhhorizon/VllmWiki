# vllm-project/vllm#22093: [Bug]: update the kv_connector from v0 to v1 in example

| 字段 | 值 |
| --- | --- |
| Issue | [#22093](https://github.com/vllm-project/vllm/issues/22093) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: update the kv_connector from v0 to v1 in example

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.1 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : version 4.0.3 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Jun 18 2025, 17:59:45) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-4.18.0-2.4.3.3.kwai.x86_64-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.61 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A800-SXM4-80GB GPU 1: NVIDIA A800-SXM4-80GB GPU 2: NVIDIA A800-SXM4-80GB GPU 3: NVIDIA A800-SXM4-80GB GPU 4: NVIDIA A800-SXM4-80GB GPU 5: NVIDIA A800-SXM4-80GB GPU 6: NVIDIA A800-SXM4-80GB GPU 7: NVIDIA A800-SXM4-80GB Nvidia driver version : 535.54.03 cuDNN version : Probabl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: ========= OS : Ubuntu 24.04.1 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : version 4.0.3 Libc version : glibc-2.39 ==================
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: update the kv_connector from v0 to v1 in example bug;stale ### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.1 LTS (x86_64) GCC version : (Ub...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: untime version : 12.8.61 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A800-SXM4-80GB GPU 1: NVIDIA A800-SXM4-80GB GPU 2: NVIDIA A800-SXM4-80GB GPU 3: NVIDIA A800-SXM4-80GB GPU 4: NVIDIA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dio==2.7.0 [pip3] torchvision==0.22.0 [pip3] transformers==4.53.2 [pip3] triton==3.3.0 [pip3] tritonclient==2.59.0 [conda] Could not collect ============================== vLLM Info ============================== ROCM V...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
