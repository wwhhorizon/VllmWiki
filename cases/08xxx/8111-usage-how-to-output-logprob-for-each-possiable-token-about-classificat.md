# vllm-project/vllm#8111: [Usage]: How to output logprob for each possiable token about classification or determin task?

| 字段 | 值 |
| --- | --- |
| Issue | [#8111](https://github.com/vllm-project/vllm/issues/8111) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to output logprob for each possiable token about classification or determin task?

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 9.3.1 20200408 (Red Hat 9.3.1-2) Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.17 Python version: 3.10.9 (main, Jan 11 2023, 15:21:40) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.el7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 11.7.99 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800 80GB PCIe GPU 1: NVIDIA A800 80GB PCIe GPU 2: NVIDIA A800 80GB PCIe GPU 3: NVIDIA A800 80GB PCIe GPU 4: NVIDIA A800 80GB PCIe GPU 5: NVIDIA A800 80GB PCIe GPU 6: NVIDIA A800 80GB PCIe GPU 7: NVIDIA A800 80GB PCIe Nvidia driver version: 535.54.03 cuDNN version: Probably one of the following: /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn.so.8.9.2 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.9.2 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.9.2 /usr/local/cuda-11.7/targets/x86_64-lin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rrent environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 9.3.1 20200408 (Red Hat 9.3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: age;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: llm i am using LLM to run a classification task, and i deploy qwen2-72B-int4 by vllm. I need vllm return prob about each class. when i do as follow, it return prob 0, what's wrong? ``` from openai import OpenAI openai_a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ansformers==3.0.1 [pip3] torch==2.3.1 [pip3] transformers==4.42.4 [pip3] triton==2.3.1 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.1.3.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.1.105

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
