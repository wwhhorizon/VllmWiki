# vllm-project/vllm#31919: [RFC]: Attention Restructuring Tracker

| 字段 | 值 |
| --- | --- |
| Issue | [#31919](https://github.com/vllm-project/vllm/issues/31919) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Attention Restructuring Tracker

### Issue 正文摘录

### Motivation. Attention-related code has gotten disorganized. This restructuring will clean things up and facilitate future efforts related to KV cache update fusion and MLA prefill/decode splitting. ### Proposed Change. ## PR 0 Address pre-commit issues surfaced by PR 1 * https://github.com/vllm-project/vllm/pull/31924 ## PR 1 This PR consists solely of file renaming and movement, and the necessary updates to imports * https://github.com/vllm-project/vllm/pull/31916 * Move `vllm/attention/layers` to `vllm/model_executor/layers/attention` * Move `vllm/attention/backends/abstract.py` to `vllm/v1/attention/backend.py` * Move `vllm/attention/backends/registry.py` to `vllm/v1/attention/backends/registry.py` * Eliminate `vllm/attention/backends` folder * Move `vllm/attention/utils/fa_utils.py` to `vllm/v1/attention/backends/fa_utils.py` * Move `vllm/attention/ops` to `vllm/v1/attention/ops` * Move `vllm/attention/selector.py` to `vllm/v1/attention/selector.py` ## PR 2 Address remaining pre-commit issues arising from PR 1 * https://github.com/vllm-project/vllm/pull/32052 ## PR 3 This PR moves chunks of code from `vllm/v1/attention/backends/utils.py` to `vllm/v1/attention/backend.py`,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e has gotten disorganized. This restructuring will clean things up and facilitate future efforts related to KV cache update fusion and MLA prefill/decode splitting. ### Proposed Change. ## PR 0 Address pre-commit issues...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: and facilitate future efforts related to KV cache update fusion and MLA prefill/decode splitting. ### Proposed Change. ## PR 0 Address pre-commit issues surfaced by PR 1 * https://github.com/vllm-project/vllm/pull/31924...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: layers` to `vllm/model_executor/layers/attention` * Move `vllm/attention/backends/abstract.py` to `vllm/v1/attention/backend.py` * Move `vllm/attention/backends/registry.py` to `vllm/v1/attention/backends/registry.py` *...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: tructuring will clean things up and facilitate future efforts related to KV cache update fusion and MLA prefill/decode splitting. ### Proposed Change. ## PR 0 Address pre-commit issues surfaced by PR 1 * https://github....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
