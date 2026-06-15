# vllm-project/vllm#24206: [Installation]: fail to install in cuda 118 with v100.

| 字段 | 值 |
| --- | --- |
| Issue | [#24206](https://github.com/vllm-project/vllm/issues/24206) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: fail to install in cuda 118 with v100.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 20.04.6 LTS (x86_64) GCC version : (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version : Could not collect CMake version : version 3.25.0 Libc version : glibc-2.31 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu118 Is debug build : False CUDA used to build PyTorch : 11.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.18 (main, Jun 5 2025, 13:14:17) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.4.0-172-generic-x86_64-with-glibc2.31 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 11.8.89 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: Tesla V100-SXM2-32GB GPU 1: Tesla V100-SXM2-32GB GPU 2: Tesla V100-SXM2-32GB GPU 3: Tesla V100-SXM2-32GB GPU 4: Tesla V100-SXM2-32GB GPU 5: Tesla V100-SXM2-32GB GPU 6: Tesla V100-SXM2-32GB GPU 7: Tesla V100...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: fail to install in cuda 118 with v100. installation;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... ==============================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Installation]: fail to install in cuda 118 with v100. installation;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... ============================== S...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ```text The output of `python collect_env.py` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 20.04.6 LTS (x86_64) GCC version : (Ubuntu 9.4.0-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: u118 [pip3] torchvision==0.22.1+cu118 [pip3] transformers==4.56.0 [pip3] triton==3.3.1 [conda] numpy 2.2.6 pypi_0 pypi [conda] nvidia-cublas-cu11 11.11.3.6 pypi_0 pypi [conda] nvidia-cuda-cupti-cu11 11.8.87
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ch version : 2.7.1+cu118 Is debug build : False CUDA used to build PyTorch : 11.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
