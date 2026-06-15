# vllm-project/vllm#5248: [Misc]: vllm ONLY allocate KVCache on the first device in CUDA_VISIBLE_DEVICES

| 字段 | 值 |
| --- | --- |
| Issue | [#5248](https://github.com/vllm-project/vllm/issues/5248) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: vllm ONLY allocate KVCache on the first device in CUDA_VISIBLE_DEVICES

### Issue 正文摘录

### KVCache usage it seems like the KVCache is only allocated on the first device in CUDA_VISIBLE_DEVICES, even if using `tensor-parallel-size` > 1. Is there any plan to support full KVCache allocated in all devices? [cache_engine.py](https://github.com/vllm-project/vllm/tree/main/vllm/worker) ```python # Initialize the cache. # line 56 self.gpu_cache = self._allocate_kv_cache(self.num_gpu_blocks, "cuda") ```

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Misc]: vllm ONLY allocate KVCache on the first device in CUDA_VISIBLE_DEVICES stale ### KVCache usage it seems like the KVCache is only allocated on the first device in CUDA_VISIBLE_DEVICES, even if using `tensor-paral...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: # line 56 self.gpu_cache = self._allocate_kv_cache(self.num_gpu_blocks, "cuda") ```
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: : vllm ONLY allocate KVCache on the first device in CUDA_VISIBLE_DEVICES stale ### KVCache usage it seems like the KVCache is only allocated on the first device in CUDA_VISIBLE_DEVICES, even if using `tensor-parallel-si...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
