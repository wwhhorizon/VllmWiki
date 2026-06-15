# vllm-project/vllm#1133: vllm implementation

| 字段 | 值 |
| --- | --- |
| Issue | [#1133](https://github.com/vllm-project/vllm/issues/1133) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm implementation

### Issue 正文摘录

It isn't totally clear to me how we're supposed to be running this. For example, it doesn't seem to work in tandem with transformers, calling the model with LLM I can't also call quantization_config. Also am I just calling LLM or am I supposed to be calling LlamaForCausalLM, AutoTokenizer, etc? If these things are easy fixes great, otherwise I believe there's clearly some work that needs to be done, seeing as it can't be used straight out of the box.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: xample, it doesn't seem to work in tandem with transformers, calling the model with LLM I can't also call quantization_config. Also am I just calling LLM or am I supposed to be calling LlamaForCausalLM, AutoTokenizer, e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: n tandem with transformers, calling the model with LLM I can't also call quantization_config. Also am I just calling LLM or am I supposed to be calling LlamaForCausalLM, AutoTokenizer, etc? If these things are easy fixe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
