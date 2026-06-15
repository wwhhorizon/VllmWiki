# vllm-project/vllm#24321: [Performance]: Garbage Collection Optimizations

| 字段 | 值 |
| --- | --- |
| Issue | [#24321](https://github.com/vllm-project/vllm/issues/24321) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Garbage Collection Optimizations

### Issue 正文摘录

### Proposal to improve performance Per a GC breakdown analysis, we observed that GC overhead is quite significant in vLLM engine. For small models (opt-125m), GC occupied ~8% of critical path time. The top GC object contributors are - Prefix KV Cache related objects - Empty list # Action Items [WIP] Simplify the BlockHash (from dataclass to sha256 byte): https://github.com/vllm-project/vllm/pull/23673 [ ] Simplify BlockHashWithGroupId (sha256 + group_id byte) [ ] As most Block only correspond to a single BlockHashWithGroupId, replace dict[int, Block] to Union[Block, dict[int, Block]] [ ] Replace empty list with Optional[list] in sampling_params stop/stop_token_ids/bad_words ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s, we observed that GC overhead is quite significant in vLLM engine. For small models (opt-125m), GC occupied ~8% of critical path time. The top GC object contributors are - Prefix KV Cache related objects - Empty list...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: sampling_params stop/stop_token_ids/bad_words ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: % of critical path time. The top GC object contributors are - Prefix KV Cache related objects - Empty list # Action Items [WIP] Simplify the BlockHash (from dataclass to sha256 byte): https://github.com/vllm-project/vll...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Cache related objects - Empty list # Action Items [WIP] Simplify the BlockHash (from dataclass to sha256 byte): https://github.com/vllm-project/vllm/pull/23673 [ ] Simplify BlockHashWithGroupId (sha256 + group_id byte)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: observed that GC overhead is quite significant in vLLM engine. For small models (opt-125m), GC occupied ~8% of critical path time. The top GC object contributors are - Prefix KV Cache related objects - Empty list # Acti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
