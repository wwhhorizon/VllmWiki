# vllm-project/vllm#14497: [Bug]: remove_oldest LRU lora may remove lora which is still in usage

| 字段 | 值 |
| --- | --- |
| Issue | [#14497](https://github.com/vllm-project/vllm/issues/14497) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: remove_oldest LRU lora may remove lora which is still in usage

### Issue 正文摘录

### Your current environment Remove_oldest LRU lora may remove lora which is still in usage. In LRUCacheWorkerLoRAManger's code: # Loading succeeded, now check if we will exceed cache capacity and # evict if the oldest adapter if so if len(self._adapter_manager) + 1 > self._adapter_manager.capacity: assert isinstance(self._adapter_manager, LRUCacheLoRAModelManager) self._adapter_manager.remove_oldest_adapter() This will call remove_oldest_adapter() and remove a LoRA on GPU, but this could remove LoRA which is still being used. For example, a batch requires LoRA{1, 2, 3, 4} has finished a step, the first request is ended and LoRA-1 will not be used. Then a new request which requires LoRA-5 is added and do prefill: it need to remove a LoRA first, but below code may remove LoRA-2: def remove_oldest(self, *, remove_pinned: bool = False) -> None: if not self.cache: return if not remove_pinned: # pop the oldest item in the cache that is not pinned lru_key = next( (key for key in self.cache if key not in self.pinned_items), ALL_PINNED_SENTINEL) if lru_key is ALL_PINNED_SENTINEL: raise RuntimeError("All items are pinned, " "cannot remove oldest from the cache.") else: lru_key = next(iter(...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: xample, a batch requires LoRA{1, 2, 3, 4} has finished a step, the first request is ended and LoRA-1 will not be used. Then a new request which requires LoRA-5 is added and do prefill: it need to remove a LoRA first, bu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 's code: # Loading succeeded, now check if we will exceed cache capacity and # evict if the oldest adapter if so if len(self._adapter_manager) + 1 > self._adapter_manager.capacity: assert isinstance(self._adapter_manage...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: N/A ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: LoRAManger's code: # Loading succeeded, now check if we will exceed cache capacity and # evict if the oldest adapter if so if len(self._adapter_manager) + 1 > self._adapter_manager.capacity: assert isinstance(self._adap...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: remove LoRA-2: def remove_oldest(self, *, remove_pinned: bool = False) -> None: if not self.cache: return if not remove_pinned: # pop the oldest item in the cache that is not pinned lru_key = next( (key for key in

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
