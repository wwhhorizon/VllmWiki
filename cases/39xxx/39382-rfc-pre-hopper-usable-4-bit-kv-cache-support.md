# vllm-project/vllm#39382: [RFC]: Pre-Hopper-usable 4-bit KV cache support

| 字段 | 值 |
| --- | --- |
| Issue | [#39382](https://github.com/vllm-project/vllm/issues/39382) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Pre-Hopper-usable 4-bit KV cache support

### Issue 正文摘录

### Motivation. for local gemma4 use this is kinda the big one if KV cache stays fp8/int8-only, long context gets way less practical. at that point it's supported, sure, but it still feels like the part that actually matters for local users is missing i really want this to exist ngl ### Proposed Change. not trying to start another huge transforms / nvfp4 / mxfp4 rabbit hole here i mean something way simpler: plain 4-bit KV cache support that people can actually use on pre-Hopper GPUs too main thing i want to know is whether vLLM is actually interested in supporting that and not just for gemma4 either. feels like this would be useful for other models too if the goal is making long-context local use less painful ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. this is mostly coming from the local-user side tbh for local gemma4, pre-Hopper-usable q4 KV cache feels like one of the biggest missing pieces right now. so i figured i'd just ask directly instead of dancing around it ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation pag...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: tion. for local gemma4 use this is kinda the big one if KV cache stays fp8/int8-only, long context gets way less practical. at that point it's supported, sure, but it still feels like the part that actually matters for...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Pre-Hopper-usable 4-bit KV cache support RFC ### Motivation. for local gemma4 use this is kinda the big one if KV cache stays fp8/int8-only, long context gets way less practical. at that point it's supported, sur...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Pre-Hopper-usable 4-bit KV cache support RFC ### Motivation. for local gemma4 use this is kinda the big one if KV cache stays fp8/int8-only, long context gets way less practical. at that point it's supported, sure, but...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ssing pieces right now. so i figured i'd just ask directly instead of dancing around it ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [RFC]: Pre-Hopper-usable 4-bit KV cache support RFC ### Motivation. for local gemma4 use this is kinda the big one if KV cache stays fp8/int8-only, long context gets way less practical. at that point it's supported, sur...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
