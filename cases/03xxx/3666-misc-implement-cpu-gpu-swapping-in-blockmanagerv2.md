# vllm-project/vllm#3666: [Misc]: Implement CPU/GPU swapping in BlockManagerV2

| 字段 | 值 |
| --- | --- |
| Issue | [#3666](https://github.com/vllm-project/vllm/issues/3666) |
| 状态 | closed |
| 标签 | good first issue |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Implement CPU/GPU swapping in BlockManagerV2

### Issue 正文摘录

Recently, we refactored the block manager subsystem to improve testability by separating concerns of each layer. See https://github.com/vllm-project/vllm/pull/3492 for more information. The V2 implementation does not have support for CPU-GPU swapping. It can be added in the [CpuGpuBlockAllocator](https://github.com/vllm-project/vllm/blob/321dc1619ad60b6df74fa86ac6299bc83c223996/vllm/core/block/cpu_gpu_block_allocator.py). My first take on the design is that it should simply keep track of the requested swap requests and have the scheduler `get_and_clear` them after each scheduling step. ![image](https://github.com/vllm-project/vllm/assets/950914/55cf0db2-2614-463b-a053-eb3f182c01bb)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: . My first take on the design is that it should simply keep track of the requested swap requests and have the scheduler `get_and_clear` them after each scheduling step. ![image](https://github.com/vllm-project/vllm/asse...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Misc]: Implement CPU/GPU swapping in BlockManagerV2 good first issue Recently, we refactored the block manager subsystem to improve testability by separating concerns of each layer. See https://github.com/vllm-project/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ach layer. See https://github.com/vllm-project/vllm/pull/3492 for more information. The V2 implementation does not have support for CPU-GPU swapping. It can be added in the [CpuGpuBlockAllocator](https://github.com/vllm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rst issue Recently, we refactored the block manager subsystem to improve testability by separating concerns of each layer. See https://github.com/vllm-project/vllm/pull/3492 for more information. The V2 implementation d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
