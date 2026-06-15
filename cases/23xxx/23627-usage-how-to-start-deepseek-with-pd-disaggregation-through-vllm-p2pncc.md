# vllm-project/vllm#23627: [Usage]: How to start deepseek with pd disaggregation through vllm p2pncclcommunicator?

| 字段 | 值 |
| --- | --- |
| Issue | [#23627](https://github.com/vllm-project/vllm/issues/23627) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to start deepseek with pd disaggregation through vllm p2pncclcommunicator?

### Issue 正文摘录

### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : TencentOS Server 4.4 (x86_64) GCC version : (Tencent Compiler 12.3.1.4) 12.3.1 20230912 (TencentOS 12.3.1.4-2) Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.38 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 | packaged by Anaconda, Inc. | (main, Jun 5 2025, 13:09:17) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.4.241-1-tlinux4-0017.7-x86_64-with-glibc2.38 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H20 GPU 1: NVIDIA H20 GPU 2: NVIDIA H20 GPU 3: NVIDIA H20 GPU 4: NVIDIA H20 GPU 5: NVIDIA H20 GPU 6: NVIDIA H20 GPU 7: NVIDIA H20 Nvidia driver version : 535.247.01...

## 现有链接修复摘要

#20988 [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ======= OS : TencentOS Server 4.4 (x86_64) GCC version : (Tencent Compiler 12.3.1.4) 12.3.1 20230912 (TencentOS 12.3.1.4-2) Clang version : Could not collect CMake version : Could not collect Libc version
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.7.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: age;stale ### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : TencentOS Server 4.4 (x86_64) GCC version : (Tencent Co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: deepseek with pd disaggregation through vllm p2pncclcommunicator? usage;stale ### Your current environment ```text Collecting environment information... ============================== System Info =======================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: u128 [pip3] torchvision==0.22.1+cu128 [pip3] transformers==4.55.2 [pip3] triton==3.3.1 [conda] numpy 2.2.6 pypi_0 pypi [conda] nvidia-cublas-cu12 12.8.3.14 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.8.57

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20988](https://github.com/vllm-project/vllm/pull/20988) | mentioned | 0.6 | [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | . #23631: [Bug]: Qwen3-30B-A3B-GPTQ-Int4 infer failure！... [bug] 7. #23627: [Usage]: How to start deepseek with pd disaggregation throug... [usage] 8. #23626: [Feature]: Support f… |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23631: Should have ROCm label: NO (0 matches) #23627: Should have ROCm label: NO (0 matches) #23626: Should have ROCm label: NO (0 matches) #23621: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
