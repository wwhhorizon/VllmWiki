# vllm-project/vllm#1593: Distributed Inference error

| 字段 | 值 |
| --- | --- |
| Issue | [#1593](https://github.com/vllm-project/vllm/issues/1593) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Distributed Inference error

### Issue 正文摘录

when I exctute code `llm = LLM("/chinese-alpaca-2-13b", tensor_parallel_size=1)` just worked fine but when I change args like `llm = LLM("/chinese-alpaca-2-13b", tensor_parallel_size=2)` an error occurred in the code > torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1275, internal error, NCCL version 2.15.5 > ncclInternalError: Internal check failed. > Last error: > Duplicate GPU detected : rank 0 and rank 1 both on CUDA device 27000 and I tried two ways but did not work ``` 1 import os os.environ["CUDA_VISIBLE_DEVICES"] = str(device_id) ``` ``` 2 device_id = rank % torch.cuda.device_count() torch.cuda.set_device(device_id) ``` how can I solve this problem?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1275, internal error, NCCL version 2.15.5 > ncclInternalError: Internal check failed. > Last error: > Duplicate GPU detected : rank 0 and rank 1 both on CUDA device 27000 an...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: parallel_size=2)` an error occurred in the code > torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1275, internal error, NCCL version 2.15.5 > ncclInternalError: Int...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: iled. > Last error: > Duplicate GPU detected : rank 0 and rank 1 both on CUDA device 27000 and I tried two ways but did not work ``` 1 import os os.environ["CUDA_VISIBLE_DEVICES"] = str(device_id) ``` ``` 2 device_id =...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
