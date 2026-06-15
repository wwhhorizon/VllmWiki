# vllm-project/vllm#33889: [Usage]: RuntimeError: CUDA error: invalid device ordinal

| 字段 | 值 |
| --- | --- |
| Issue | [#33889](https://github.com/vllm-project/vllm/issues/33889) |
| 状态 | open |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: RuntimeError: CUDA error: invalid device ordinal

### Issue 正文摘录

### Your current environment I am running this [tutorial](https://docs.vllm.ai/en/latest/examples/offline_inference/rlhf/). Here my script is the same except my ray init ```python ray.init( runtime_env={ "excludes": [".venv/", ".git/", "*.pyc", "__pycache__/"], "env_vars": { "VIRTUAL_ENV": "", # Unset VIRTUAL_ENV for Ray workers "PYTHON_EXECUTABLE": ".venv/bin/python3", }, } ) ``` I have 4 A100s. But when I try to run the example, I get a RuntimeError: CUDA error: invalid device ordinal. Any bugs with the example ``` ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.8 (main, Jan 14 2025, 22:49:14) [Clang 19.1.6 ] (64-bit runtime) Python platform : Linux-5.15.0-151-generic-x86_64-with-glibc2...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ===============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Usage]: RuntimeError: CUDA error: invalid device ordinal usage;stale ### Your current environment I am running this [tutorial](https://docs.vllm.ai/en/latest/examples/offline_inference/rlhf/). Here my script is the sam...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s [tutorial](https://docs.vllm.ai/en/latest/examples/offline_inference/rlhf/). Here my script is the same except my ray init ```python ray.init( runtime_env={ "excludes": [".venv/", ".git/", "*.pyc", "__pycache__/"], "e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: RuntimeError: CUDA error: invalid device ordinal usage;stale ### Your current environment I am running this [tutorial](https://docs.vllm.ai/en/latest/examples/offline_inference/rlhf/). Here my script is the sam...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.2.7.post1 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.6.4.1 [pip3] nvidia-cuda-cccl-cu12==12.9.27 [pip3] nvidia-cuda-cu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
