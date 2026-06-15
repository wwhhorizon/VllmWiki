# vllm-project/vllm#6571: [Model]: Llava-Next-Video support

| 字段 | 值 |
| --- | --- |
| Issue | [#6571](https://github.com/vllm-project/vllm/issues/6571) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Model]: Llava-Next-Video support

### Issue 正文摘录

### The model to consider. LLaVA-NeXT-Video* (LlavaNextVideoForConditionalGeneration) ### The closest model vllm already supports. Llava-Next (LlavaNextForConditionalGeneration) ### What's your difficulty of supporting the model you want? - Implement the video processor. - Implement the merging of video embedding and text embedding.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Model]: Llava-Next-Video support new-model ### The model to consider. LLaVA-NeXT-Video* (LlavaNextVideoForConditionalGeneration) ### The closest model vllm already supports. Llava-Next (LlavaNextForConditionalGenerati

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
