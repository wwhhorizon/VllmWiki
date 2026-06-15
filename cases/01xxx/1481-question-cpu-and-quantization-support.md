# vllm-project/vllm#1481: Question: CPU and quantization support?

| 字段 | 值 |
| --- | --- |
| Issue | [#1481](https://github.com/vllm-project/vllm/issues/1481) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Question: CPU and quantization support?

### Issue 正文摘录

Does vLLM support LLM inference on CPU? And with quantized model? What's the difference between vLLM and GGML?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Question: CPU and quantization support? Does vLLM support LLM inference on CPU? And with quantized model? What's the difference between vLLM and GGML?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tion support? Does vLLM support LLM inference on CPU? And with quantized model? What's the difference between vLLM and GGML?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
