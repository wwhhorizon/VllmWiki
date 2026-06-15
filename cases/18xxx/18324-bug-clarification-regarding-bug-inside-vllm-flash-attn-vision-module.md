# vllm-project/vllm#18324: [Bug]: Clarification regarding bug inside vllm-flash-attn vision module

| 字段 | 值 |
| --- | --- |
| Issue | [#18324](https://github.com/vllm-project/vllm/issues/18324) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Clarification regarding bug inside vllm-flash-attn vision module

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug Hi, I am looking for a clarification regarding the [warning message that pops up](https://github.com/vllm-project/vllm/blob/b6a6e7a529d72e50cbe0c0b5360cf890124260e6/vllm/model_executor/models/vision.py#L91) when trying to load a Molmo Vision model in vLLM. It seems that the warning message was first introduced [in this PR](https://github.com/vllm-project/vllm/pull/9016/files#r2088014308) and carried along with many refactors but I couldn't find any discussion or reference to what the actual bug was or any issue tracking it in the vllm-flash-attn repo. It seems anyway that the `vllm-flash-attn` repo is (mostly) up-to-date with the latest flash-attn, so I'm confused why this bug still exists in the fork but not in the main repo. ``` "Current `vllm-flash-attn` has a bug inside vision module, so we use xformers backend instead. You can run `pip install flash-attn` to use flash-attention backend." ``` Can we add an issue tracking this and add it to the warning message or perhaps remove the check if it is perhaps no longer relevant? cc @ywang96 @mrsalehi @DarkLight1337 @mgoin ### Before submitting a new issue... - [x] Make sure you...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ent `vllm-flash-attn` has a bug inside vision module, so we use xformers backend instead. You can run `pip install flash-attn` to use flash-attention backend." ``` Can we add an issue tracking this and add it to the war...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: side vision module, so we use xformers backend instead. You can run `pip install flash-attn` to use flash-attention backend." ``` Can we add an issue tracking this and add it to the warning message or perhaps remove the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: in ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/b6a6e7a529d72e50cbe0c0b5360cf890124260e6/vllm/model_executor/models/vision.py#L91) when trying to load a Molmo Vision model in vLLM. It seems that the warning message was first introduced [in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g]: Clarification regarding bug inside vllm-flash-attn vision module bug;stale ### Your current environment N/A ### 🐛 Describe the bug Hi, I am looking for a clarification regarding the [warning message that pops up](ht...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
