# vllm-project/vllm#19188: [Bug]: V0.9.0.1 Docker images,  NCCL fails with Cuda failure 'operation not supported' on torchrun with vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#19188](https://github.com/vllm-project/vllm/issues/19188) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V0.9.0.1 Docker images,  NCCL fails with Cuda failure 'operation not supported' on torchrun with vLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Description When running a simple PyTorch distributed `all_reduce` test using `torchrun` and NCCL as backend, we encountered **different critical errors** in two versions of `vLLM`: * `v0.8.5.post1`: all workers start, but **`all_reduce` returns incorrect result** → all ranks get value `1.0` instead of `4.0`. * `v0.9.0.1`: `all_reduce` fails with a **`DistBackendError` due to cuda error 'operation not supported'\`**. The test passes successfully when using the **GLOO backend**, or when skipping vLLM entirely. This suggests a regression or conflict introduced when vLLM loads/configures NCCL. --- 1. Use 4-GPU machine (RTX A5000), Ubuntu 20.04, CUDA 12.2–12.4 installed, driver version 570+ 2. Run this `test.py` using `torchrun --nproc-per-node=4`: ```python # Test PyTorch NCCL import torch import torch.distributed as dist dist.init_process_group(backend="nccl") local_rank = dist.get_rank() % torch.cuda.device_count() torch.cuda.set_device(local_rank) data = torch.FloatTensor([1,] * 128).to("cuda") dist.all_reduce(data, op=dist.ReduceOp.SUM) torch.cuda.synchronize() value = data.mean().item() world_size = dist.get_world_size() as...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: V0.9.0.1 Docker images, NCCL fails with Cuda failure 'operation not supported' on torchrun with vLLM bug;stale ### Your current environment ### 🐛 Describe the bug ### Description When running a simple PyTorch dis...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: V0.9.0.1 Docker images, NCCL fails with Cuda failure 'operation not supported' on torchrun with vLLM bug;stale ### Your current environment ### 🐛 Describe the bug ### Description When running a simple PyTorch dis...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: imple PyTorch distributed `all_reduce` test using `torchrun` and NCCL as backend, we encountered **different critical errors** in two versions of `vLLM`: * `v0.8.5.post1`: all workers start, but **`all_reduce` returns i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: irely. This suggests a regression or conflict introduced when vLLM loads/configures NCCL. --- 1. Use 4-GPU machine (RTX A5000), Ubuntu 20.04, CUDA 12.2–12.4 installed, driver version 570+ 2. Run this `test.py` using `to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ls with Cuda failure 'operation not supported' on torchrun with vLLM bug;stale ### Your current environment ### 🐛 Describe the bug ### Description When running a simple PyTorch distributed `all_reduce` test using `torch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
