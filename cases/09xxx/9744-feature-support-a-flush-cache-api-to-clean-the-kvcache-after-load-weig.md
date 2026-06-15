# vllm-project/vllm#9744: [Feature]: Support a `flush_cache` API to clean the kvcache after `load_weights`

| 字段 | 值 |
| --- | --- |
| Issue | [#9744](https://github.com/vllm-project/vllm/issues/9744) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support a `flush_cache` API to clean the kvcache after `load_weights`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When using vllm to generate rollout in typical rlhf training (e.g. as in [OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)), we need to reload the weight of each vllm served model after each rollout training round. And on the other hand, many RLHF algorihms need to sample multiple responses from a given prompt (e.g. GRPO, RLOO and variant of PPO), which makes prefix caching an important feature for the performance of RLHF. However, in the current vllm impl, the cached prefix won't be updated after `load_weights`, making the new model running with the old cached prefix. It will be great if we can support an API to invalid the old kv cache or automatically do that within `load_weights`. A reference implementation would be [sglang/srt/managers/scheduler.py#L1143](https://github.com/sgl-project/sglang/blob/6fcd6d7d6dec7aea858d7441effd8a04b6d05474/python/sglang/srt/managers/scheduler.py#L1143): ```python def update_weights(self, recv_req: UpdateWeightReqInput): """In-place update of the weights.""" success, message = self.tp_worker.update_weights(recv_req) if success: flash_cache_success = self.flush_cache() assert flash_cache_success, "C...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: rt a `flush_cache` API to clean the kvcache after `load_weights` feature request;stale ### 🚀 The feature, motivation and pitch When using vllm to generate rollout in typical rlhf training (e.g. as in [OpenRLHF/OpenRLHF]...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: , motivation and pitch When using vllm to generate rollout in typical rlhf training (e.g. as in [OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)), we need to reload the weight of each vllm served model after ea...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ompt (e.g. GRPO, RLOO and variant of PPO), which makes prefix caching an important feature for the performance of RLHF. However, in the current vllm impl, the cached prefix won't be updated after `load_weights`, making...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: hed prefix. It will be great if we can support an API to invalid the old kv cache or automatically do that within `load_weights`. A reference implementation would be [sglang/srt/managers/scheduler.py#L1143](https://gith...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
