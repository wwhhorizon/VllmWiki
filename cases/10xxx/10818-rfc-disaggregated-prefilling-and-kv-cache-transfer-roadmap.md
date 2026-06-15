# vllm-project/vllm#10818: [RFC]: Disaggregated prefilling and KV cache transfer roadmap

| 字段 | 值 |
| --- | --- |
| Issue | [#10818](https://github.com/vllm-project/vllm/issues/10818) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Disaggregated prefilling and KV cache transfer roadmap

### Issue 正文摘录

### Motivation. Here is the roadmap for disaggregated prefill (and general-purpose kv cache transfer). Feel free to contribute :grin:. ### Proposed Change. - XpYd support (X vLLM prefill instances, and Y vLLM decode instances, very likely that the tp and pp are not the same between prefill and decode instances) - [ ] ~~[Feature] Allow specifying region-of-interest / roi on `num_head` dimension and `layer` dimension (currently the `roi` tensor only contains tokens dimension)~~ (mooncake team proposed new design) - [ ] ~~[Feature] XpYd support by building multiple connections between Xp and Yd~~ (We now go for KVCache-store-based design. If you prefer direct P2P please raise concerns in vLLM #feat-prefill-disaggregation channel) - [ ] [Feature] XpYd support by letting Xp connect to one KV cache server, and connect this server to Yd (#12957) - Building connection - [ ] [Usage] Keep distributed connection alive by periodically sending dummy requests. - [ ] [Usage] Build connection by running `vllm connect` (#11791 ) - [ ] [Feature] allow connecting prefiller and decoder between different nodes - [ ] [Perf] Build connection by directly talking to the `Engine` instead of talking to the...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [RFC]: Disaggregated prefilling and KV cache transfer roadmap RFC;stale ### Motivation. Here is the roadmap for disaggregated prefill (and general-purpose kv cache transfer). Feel free to contribute :grin:. ### Proposed...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: same between prefill and decode instances) - [ ] ~~[Feature] Allow specifying region-of-interest / roi on `num_head` dimension and `layer` dimension (currently the `roi` tensor only contains tokens dimension)~~ (mooncak...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: he observability APIs already exposed by vLLM - [ ] [Feature] Initial routing support (send the decoding request to the most available decode instance first) - Testing - [x] [Feature] Offline disaggregated prefill testi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [RFC]: Disaggregated prefilling and KV cache transfer roadmap RFC;stale ### Motivation. Here is the roadmap for disaggregated prefill (and general-purpose kv cache transfer). Feel free to contribute :grin:. ### Proposed...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
