# vllm-project/vllm#7315: [Feature]: Support attention backend with FlexAttention

| 字段 | 值 |
| --- | --- |
| Issue | [#7315](https://github.com/vllm-project/vllm/issues/7315) |
| 状态 | closed |
| 标签 | feature request;torch.compile;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support attention backend with FlexAttention

### Issue 正文摘录

### 🚀 The feature, motivation and pitch FlexAttention was proposed as a performant attention implementation leveraging `torch.compile` with easy APIs for adding support for complex attention variants such as Causal, [Relative Positional Embeddings](https://paperswithcode.com/method/relative-position-encodings), [Alibi](https://paperswithcode.com/method/alibi), [Sliding Window Attention](https://mistral.ai/news/announcing-mistral-7b/), [PrefixLM](https://twitter.com/andersonbcdefg/status/1800907703688339569), [Document Masking/Sample Packing/Jagged Tensors](https://github.com/pytorch/torchtune/pull/875), [Tanh Soft-Capping](https://twitter.com/LysandreJik/status/1807779471891538199), [PagedAttention](https://arxiv.org/abs/2309.06180), etc. https://pytorch.org/blog/flexattention/ While it is not the fastest attention backend (yet!) it is clearly performant enough while enabling much more flexibility than current compiled backends to easily implement attention features we need for crucial models, like Soft-capping in Gemma 2 which we currently rely on FlashInfer for. Not to mention it is a first-class citizen for `torch.compile`. **The current blocker is it will not be available unti...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: Support attention backend with FlexAttention feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch FlexAttention was proposed as a performant attention implementation leveraging `torch.c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ure]: Support attention backend with FlexAttention feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch FlexAttention was proposed as a performant attention implementation leveraging `torch.compil...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: iled backends to easily implement attention features we need for crucial models, like Soft-capping in Gemma 2 which we currently rely on FlashInfer for. Not to mention it is a first-class citizen for `torch.compile`. **...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support attention backend with FlexAttention feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch FlexAttention was proposed as a performant attention implementation leveraging `torch.c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: mention it is a first-class citizen for `torch.compile`. **The current blocker is it will not be available until PyTorch 2.5.0.** ![image](https://github.com/user-attachments/assets/4e508c4c-1b80-4b97-b8b6-89f3db6b1639)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
