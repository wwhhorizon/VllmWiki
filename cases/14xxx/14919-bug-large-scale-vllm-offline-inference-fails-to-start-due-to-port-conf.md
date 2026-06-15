# vllm-project/vllm#14919: [Bug]: Large-scale vLLM offline inference fails to start due to port conflicts.

| 字段 | 值 |
| --- | --- |
| Issue | [#14919](https://github.com/vllm-project/vllm/issues/14919) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Large-scale vLLM offline inference fails to start due to port conflicts.

### Issue 正文摘录

### Your current environment ``` PyTorch version: 2.5.1+cu124 CUDA used to build PyTorch: 12.4 Python version: 3.11.11 vLLM Version: 0.6.6.post1 NCCL_VERSION=2.17.1-1 CUDA_VERSION=12.1.1 ``` ### 🐛 Describe the bug ``` Background： We found a [similar issue](https://github.com/vllm-project/vllm/issues/11617) in the community, but the original poster closed it without providing a specific fix. Our deployment setup consists of pods with 8 GPUs each, where we run a vLLM service on each GPU for offline inference. When we scale up the number of pods (typically between 100-200 pods), we frequently encounter port conflicts. We've attempted to mitigate this by using the VLLM_PORT environment variable combined with some random information to select ports, which reduces the probability of conflicts, but the issue still persists. How should we fix this issue? Or has the community not considered this problem? If a pod has 8 GPUs, and each GPU concurrently starts a process, there's a possibility of port conflicts occurring. Error stack trace： func_return = func(*args, **kwargs) ^^^^^^^^^^^^^^^^^ File "/home/ray/anaconda3/lib/python3.11/site-packages/torch/distributed/distributed_c10d.py", line 1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e to port conflicts. bug;stale ### Your current environment ``` PyTorch version: 2.5.1+cu124 CUDA used to build PyTorch: 12.4 Python version: 3.11.11 vLLM Version: 0.6.6.post1 NCCL_VERSION=2.17.1-1 CUDA_VERSION=12.1.1 `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: bug;stale ### Your current environment ``` PyTorch version: 2.5.1+cu124 CUDA used to build PyTorch: 12.4 Python version: 3.11.11 vLLM Version: 0.6.6.post1 NCCL_VERSION=2.17.1-1 CUDA_VERSION=12.1.1 ``` ### 🐛 Describe the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: Large-scale vLLM offline inference fails to start due to port conflicts. bug;stale ### Your current environment ``` PyTorch version: 2.5.1+cu124 CUDA used to build PyTorch: 12.4 Python version: 3.11.11 vLLM Versi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: by using the VLLM_PORT environment variable combined with some random information to select ports, which reduces the probability of conflicts, but the issue still persists. How should we fix this issue? Or has the commu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e-scale vLLM offline inference fails to start due to port conflicts. bug;stale ### Your current environment ``` PyTorch version: 2.5.1+cu124 CUDA used to build PyTorch: 12.4 Python version: 3.11.11 vLLM Version: 0.6.6.p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
