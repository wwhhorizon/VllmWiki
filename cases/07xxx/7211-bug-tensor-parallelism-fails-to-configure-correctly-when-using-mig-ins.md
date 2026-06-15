# vllm-project/vllm#7211: [Bug]: Tensor parallelism fails to configure correctly when using MIG instances

| 字段 | 值 |
| --- | --- |
| Issue | [#7211](https://github.com/vllm-project/vllm/issues/7211) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tensor parallelism fails to configure correctly when using MIG instances

### Issue 正文摘录

### 🐛 Describe the bug I found a bug when trying to run a model with vllm across 2 GPU MIG partitions. I traced it back because it wasn't too hard to find but I don't know how the devs of vllm would want to move forward. I understand the intent of vllm is to take out a lot of the horrible pain of GPU management between nvidia, cuda, python, etc. but as a developer using vllm, my opinion is the ecosystem of dynamic GPU management is severely lacking as a whole and vllm is trying to plug the holes in the boat valiantly but in the end I foresee never ending issues like this. Anyway: https://github.com/vllm-project/vllm/blob/00afc7859072bdcaba30611c6563f2f7ac7104a3/vllm/executor/ray_gpu_executor.py#L200 The issue here is that I have to set CUDA_VISIBLE_DEVICES as strings before I launch ray & vllm since that is the syntax cuda uses for MIG partition allocation : https://docs.nvidia.com/datacenter/tesla/mig-user-guide/#cuda-visible-devices Thus i get: ValueError: invalid literal for int() with base 10: 'MIG-2e782cfd-36f2-55ff-a7d5-c6734444be2b' (pid=586) /miniforge3/lib/python3.10/site-packages/transformers/utils/hub.py:127: FutureWarning: Using `TRANSFORMERS_CACHE` is deprecated and w...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Tensor parallelism fails to configure correctly when using MIG instances bug;stale ### 🐛 Describe the bug I found a bug when trying to run a model with vllm across 2 GPU MIG partitions. I traced it back because i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Tensor parallelism fails to configure correctly when using MIG instances bug;stale ### 🐛 Describe the bug I found a bug when trying to run a model with vllm across 2 GPU MIG partitions. I traced it back because i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: or parallelism fails to configure correctly when using MIG instances bug;stale ### 🐛 Describe the bug I found a bug when trying to run a model with vllm across 2 GPU MIG partitions. I traced it back because it wasn't to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pment distributed_parallel;model_support;scheduler_memory cuda crash env_dependency 🐛 Describe the bug

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
