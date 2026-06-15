# vllm-project/vllm#5797: [Bug]: OpenAI API emulation incompatible with shell_gpt OpenAI API calls

| 字段 | 值 |
| --- | --- |
| Issue | [#5797](https://github.com/vllm-project/vllm/issues/5797) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OpenAI API emulation incompatible with shell_gpt OpenAI API calls

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.39 Python version: 3.12.3 | packaged by Anaconda, Inc. | (main, May 6 2024, 19:46:43) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.8.0-35-generic-x86_64-with-glibc2.39 Is CUDA available: N/A CUDA runtime version: 12.0.140 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA RTX 6000 Ada Generation GPU 1: NVIDIA RTX 6000 Ada Generation Nvidia driver version: 535.171.04 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.2 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.2 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.2 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.2 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.2 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.2 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.2 HIP runtime version: N/A MIOpen runti...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rrent environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Clang...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ]: OpenAI API emulation incompatible with shell_gpt OpenAI API calls bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: France?' The capital of France is Paris. sedna:~$ OPENAI_BASE_URL=http://triton:8000/v1 sgpt --model=Qwen/Qwen2-beta-7B-Chat 'Capital of France?' ╭─────────────────────────────── Traceback (most recent call last) ──────...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
