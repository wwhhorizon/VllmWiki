# vllm-project/vllm#3152: Serve model Mixtral-8x7B on 4xA100 cuda=12.1, pytorch=2.1.2 failed

| 字段 | 值 |
| --- | --- |
| Issue | [#3152](https://github.com/vllm-project/vllm/issues/3152) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Serve model Mixtral-8x7B on 4xA100 cuda=12.1, pytorch=2.1.2 failed

### Issue 正文摘录

It display error message: "cupy_backends.cuda.libs.nccl.NcclError: NCCL_ERROR_INVALID_USAGE: invalid usage" This error happens for vllm==0.3.2 while vllm==0.2.7 works oky. To reproduce it: python -m vllm.entrypoits.api_server --model mistralai/Mixtral-8x7B-v0.1 --tensor-parallel-size 2

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Serve model Mixtral-8x7B on 4xA100 cuda=12.1, pytorch=2.1.2 failed stale It display error message: "cupy_backends.cuda.libs.nccl.NcclError: NCCL_ERROR_INVALID_USAGE: invalid usage" This error happens for vllm==0.3.2 whi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 0 cuda=12.1, pytorch=2.1.2 failed stale It display error message: "cupy_backends.cuda.libs.nccl.NcclError: NCCL_ERROR_INVALID_USAGE: invalid usage" This error happens for vllm==0.3.2 while vllm==0.2.7 works oky. To repr...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ge" This error happens for vllm==0.3.2 while vllm==0.2.7 works oky. To reproduce it: python -m vllm.entrypoits.api_server --model mistralai/Mixtral-8x7B-v0.1 --tensor-parallel-size 2 development distributed_parallel;mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: -parallel-size 2 development distributed_parallel;model_support cuda env_dependency It display error message:
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Serve model Mixtral-8x7B on 4xA100 cuda=12.1, pytorch=2.1.2 failed stale It display error message: "cupy_backends.cuda.libs.nccl.NcclError: NCCL_ERROR_INVALID_USAGE: invalid usage" This error happens for vllm==0.3.2 whi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
