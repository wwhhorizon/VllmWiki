# vllm-project/vllm#10981: [Bug]: Why is structured output in 0.6.4.post1 leading to RAM OOM but 0.6.3.post1 has a workaround? 

| 字段 | 值 |
| --- | --- |
| Issue | [#10981](https://github.com/vllm-project/vllm/issues/10981) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Why is structured output in 0.6.4.post1 leading to RAM OOM but 0.6.3.post1 has a workaround? 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using structured output or function calling completely fills up my RAM and lets the process crash after 100 calls or something (I have 128gb ram, so for less ram it might be after a couple of calls already). In #7332 a workaround was mentioned by setting ```extra_body={"guided_decoding_backend": "lm-format-enforcer"}``` which worked on 0.6.3.post1. **Unfortunately each structured output fails** for some reason at this version. 0.6.4 does not work at all with guided_decoding_backend it seems. 0.6.4.post1 produces really good structured outputs, but the **workaround does not seem to work**, my memory still overflows. Does someone know why the workaround works in 0.6.3.post1 and not in 0.6.4.post1 and how one could make it work? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .post1 has a workaround? bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using structured output or function calling completely fills up my RAM and lets the process cras...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 32 a workaround was mentioned by setting ```extra_body={"guided_decoding_backend": "lm-format-enforcer"}``` which worked on 0.6.3.post1. **Unfortunately each structured output fails** for some reason at this version. 0....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: . **Unfortunately each structured output fails** for some reason at this version. 0.6.4 does not work at all with guided_decoding_backend it seems. 0.6.4.post1 produces really good structured outputs, but the **workarou...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: Why is structured output in 0.6.4.post1 leading to RAM OOM but 0.6.3.post1 has a workaround? bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using structured outp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
