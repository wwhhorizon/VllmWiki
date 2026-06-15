# vllm-project/vllm#33341: [Feature][Performance][Speculative Decoding]: Support Full CUDA Graph for the drafter

| 字段 | 值 |
| --- | --- |
| Issue | [#33341](https://github.com/vllm-project/vllm/issues/33341) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature][Performance][Speculative Decoding]: Support Full CUDA Graph for the drafter

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, the drafter code in eagle.py only supports piecewise CUDA graphs. Integrating full CUDA graphs would speed up the drafter execution and reduce the full runtime e.g. of speculative decoding with `method=draft_model`. This should be possible in practice because we already run the model in full CUDA graph mode when they run standalone (without speculative decoding). I made some measurements to forecast how much faster SD would run with full CUDA graphs, and arrived at ~5% increased TPOT: https://tomasruizt.github.io/posts/09_full-cuda-graphs-spec-decode/#method ### Alternatives _No response_ ### Additional context Some thoughts about what might be necessary to implement full CUDA graphs: * The buffers used by the drafter should be static. Just like `self.input_ids`, and `self.positions` have buffers, so also should the KV-cache related ones. E.g. `self._slot_mapping` was recently introduced by https://github.com/vllm-project/vllm/pull/25954. We should check if `seq_lens` and `query_start_loc` also need buffers. * PyTorch operations (e.g. during input preparation) should be checked to make sure they use the input buffers of the drafte...

## 现有链接修复摘要

#33318 Drafter Supports Multiple KVCache Groups

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Feature][Performance][Speculative Decoding]: Support Full CUDA Graph for the drafter feature request;stale ### 🚀 The feature, motivation and pitch Currently, the drafter code in eagle.py only supports piecewise CUDA gr...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ons` have buffers, so also should the KV-cache related ones. E.g. `self._slot_mapping` was recently introduced by https://github.com/vllm-project/vllm/pull/25954. We should check if `seq_lens` and `query_start_loc` also...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature][Performance][Speculative Decoding]: Support Full CUDA Graph for the drafter feature request;stale ### 🚀 The feature, motivation and pitch Currently, the drafter code in eagle.py only supports piecewise CUDA gr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: faster SD would run with full CUDA graphs, and arrived at ~5% increased TPOT: https://tomasruizt.github.io/posts/09_full-cuda-graphs-spec-decode/#method ### Alternatives _No response_ ### Additional context Some thought...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: * During inference, in the decode section of the drafter, the `cudagraph_dispatcher.dispatch()` should be passed `uniform_decode=True`, so that both `cudagraph_runtime_mode` and `batch_desc` are passed to `set_forward_c...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33318](https://github.com/vllm-project/vllm/pull/33318) | mentioned | 0.6 | Drafter Supports Multiple KVCache Groups | ache workloads are slower than expected due to piecewise CUDA graphs (#33341): \| Configuration \| Standalone \| SD \| Slowdown \| Logs \| \|---------------\|----------\|-----\|----------\|-… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
