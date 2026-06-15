# vllm-project/vllm#25853: [Usage]: ​​How to Add torch.cuda.nvtx Code in vLLM to Monitor Model GPU Usage​​

| 字段 | 值 |
| --- | --- |
| Issue | [#25853](https://github.com/vllm-project/vllm/issues/25853) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: ​​How to Add torch.cuda.nvtx Code in vLLM to Monitor Model GPU Usage​​

### Issue 正文摘录

```text I intend to evaluate the performance of the [Qwen3-4B-AWQ] model in a specific environment. I tried to check the GPU performance using nsys, but nothing showed up. Why is this the case? Secondly, I want to use nvtx to check the GPU occupancy rate of the model calls, but an error occurred. How can these problems be solved? ``` ### This is my error ### My current environment ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 | packaged by Anaconda, Inc. | (main, May 6 2024, 19:46:43) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.15.0-136-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA ru...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: I intend to evaluate the performance of the [Qwen3-4B-AWQ] model in a specific environment. I tried to check the GPU performance using nsys, but nothing showed up. Why is this the case? Secondly, I want to use nvtx to c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Usage]: ​​How to Add torch.cuda.nvtx Code in vLLM to Monitor Model GPU Usage​​ usage;stale ```text I intend to evaluate the performance of the [Qwen3-4B-AWQ] model in a specific environment. I tried to check the GPU pe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: ​​How to Add torch.cuda.nvtx Code in vLLM to Monitor Model GPU Usage​​ usage;stale ```text I intend to evaluate the performance of the [Qwen3-4B-AWQ] model in a specific environment. I tried to check the GPU pe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: w to Add torch.cuda.nvtx Code in vLLM to Monitor Model GPU Usage​​ usage;stale ```text I intend to evaluate the performance of the [Qwen3-4B-AWQ] model in a specific environment. I tried to check the GPU performance usi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.8.0 [pip3] torchvision==0.23.0 [pip3] transformers==4.56.2 [pip3] triton==3.4.0 [conda] numpy 2.3.2 pypi_0 pypi [conda] nvidia-cublas-cu12 12.8.4.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.8.90

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
