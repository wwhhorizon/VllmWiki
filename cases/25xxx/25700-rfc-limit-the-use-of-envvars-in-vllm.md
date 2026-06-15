# vllm-project/vllm#25700: [RFC]: Limit the use of envvars in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#25700](https://github.com/vllm-project/vllm/issues/25700) |
| 状态 | open |
| 标签 | good first issue;RFC |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Limit the use of envvars in vLLM

### Issue 正文摘录

### Motivation. vLLM's envvars are on the edge of getting out of control. There are many envvars should instead be configs. Like the attention backend, all2all kernel backend, and even there is a flag to control KV cache layout. envvars are evil because: 1. It is equivalent of using global variables everywhere in the code, which is a bad programming practice. 2. envvars have no advanced structure like, hierarchy, typechecks, etc. In summary, I think envvars are the kind of thing that is very easy to add so people tend to add envvars as the shortest path to implement their feature, but this can quickly becomes unmanageable and makes the project very hard to use. ### Proposed Change. I think we should: 1. Spend some effort on reviewing the current envvars and move many of them to configs. 2. Have very strict bar on what can be an envvar and question every new envvars in vllm. ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), w...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ol. There are many envvars should instead be configs. Like the attention backend, all2all kernel backend, and even there is a flag to control KV cache layout. envvars are evil because: 1. It is equivalent of using globa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ad programming practice. 2. envvars have no advanced structure like, hierarchy, typechecks, etc. In summary, I think envvars are the kind of thing that is very easy to add so people tend to add envvars as the shortest p...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ion backend, all2all kernel backend, and even there is a flag to control KV cache layout. envvars are evil because: 1. It is equivalent of using global variables everywhere in the code, which is a bad programming practi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nd, all2all kernel backend, and even there is a flag to control KV cache layout. envvars are evil because: 1. It is equivalent of using global variables everywhere in the code, which is a bad programming practice. 2. en...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: edge of getting out of control. There are many envvars should instead be configs. Like the attention backend, all2all kernel backend, and even there is a flag to control KV cache layout. envvars are evil because: 1. It...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
