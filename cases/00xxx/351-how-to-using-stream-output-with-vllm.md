# vllm-project/vllm#351: How to using stream output with vllm?

| 字段 | 值 |
| --- | --- |
| Issue | [#351](https://github.com/vllm-project/vllm/issues/351) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to using stream output with vllm?

### Issue 正文摘录

Although there are some lib wrappered vllm like TGI, but I want to know how to using vllm with stream output enabled, currently hard to found out-of-box example on it. Typically, with original hf transforemrs API, one can using a TextStreamer and send into generate_kwargs to do this: ``` generate_kwargs = dict( **input_ids, max_new_tokens=50 if args.bare else 800, streamer=streamer, <--- streamer do_sample=True, num_beams=1, temperature=float(args.temp), top_k=40, top_p=float(args.top_p), ) ``` Any out-of-box I can use to enable stream in vllm? Thanks

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: **input_ids, max_new_tokens=50 if args.bare else 800, streamer=streamer, <--- streamer do_sample=True, num_beams=1, temperature=float(args.temp), top_k=40, top_p=float(
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rently hard to found out-of-box example on it. Typically, with original hf transforemrs API, one can using a TextStreamer and send into generate_kwargs to do this: ``` generate_kwargs = dict( **input_ids, max_new_tokens...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
