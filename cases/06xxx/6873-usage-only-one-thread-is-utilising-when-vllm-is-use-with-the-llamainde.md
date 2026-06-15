# vllm-project/vllm#6873: [Usage]: Only one thread is utilising when vllm is use with the llamaindex framework on the cpu. 

| 字段 | 值 |
| --- | --- |
| Issue | [#6873](https://github.com/vllm-project/vllm/issues/6873) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Only one thread is utilising when vllm is use with the llamaindex framework on the cpu. 

### Issue 正文摘录

I am using the vllm with the llamaindex but it is utilising only single thread and taking very much time. here is my code where I am creating the instance of llm for llamaindex ```python llm = Vllm( model="/home/dev/.cache/huggingface/hub/models--google--gemma-2b-it/snapshots/4cf79afa15bef73c0b98ff5937d8e57d6071ef71", tensor_parallel_size=1, max_new_tokens=100, ) ``` ### Your current environment ```text No module named 'vllm.commit_id' from vllm.version import __version__ as VLLM_VERSION PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.39 Python version: 3.11.6 (main, Jul 24 2024, 20:29:02) [GCC 13.2.0] (64-bit runtime) Python platform: Linux-6.8.0-39-generic-x86_64-with-glibc2.39 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x8...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: urrent environment ```text No module named 'vllm.commit_id' from vllm.version import __version__ as VLLM_VERSION PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Usage]: Only one thread is utilising when vllm is use with the llamaindex framework on the cpu. usage;stale I am using the vllm with the llamaindex but it is utilising only single thread and taking very much time. here...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: rsion__ as VLLM_VERSION PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Clang...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: lising when vllm is use with the llamaindex framework on the cpu. usage;stale I am using the vllm with the llamaindex but it is utilising only single thread and taking very much time. here is my code where I am creating...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: .0+cpu [pip3] torchvision==0.19.0+cpu [pip3] transformers==4.43.3 [pip3] triton==3.0.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.3.post1 vLLM Build Flags: CUDA A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
