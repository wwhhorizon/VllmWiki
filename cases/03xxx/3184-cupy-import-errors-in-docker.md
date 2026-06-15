# vllm-project/vllm#3184: Cupy Import errors in Docker

| 字段 | 值 |
| --- | --- |
| Issue | [#3184](https://github.com/vllm-project/vllm/issues/3184) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Cupy Import errors in Docker

### Issue 正文摘录

I'm using a docker with the 12.1 nvidia/cuda container as a base. This worked perfectly for vllm unit the switch to using cupy. The cupy import breaks vllm whenever you use tensor-parallel >1. I've double checked and both the cuda version(12.1) and cupy(cupy-cuda12x) should be compatible. Any advice or guidance on this issue?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Cupy Import errors in Docker stale I'm using a docker with the 12.1 nvidia/cuda container as a base. This worked perfectly for vllm unit the switch to using cupy. The cupy import breaks vllm whenever you use tensor-para...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: py Import errors in Docker stale I'm using a docker with the 12.1 nvidia/cuda container as a base. This worked perfectly for vllm unit the switch to using cupy. The cupy import breaks vllm whenever you use tensor-parall...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Cupy Import errors in Docker stale I'm using a docker with the 12.1 nvidia/cuda container as a base. This worked perfectly for vllm unit the switch to using cupy. The cupy import breaks vllm whenever you use tensor-para...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
