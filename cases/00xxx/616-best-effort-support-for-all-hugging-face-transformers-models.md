# vllm-project/vllm#616: Best effort support for all Hugging Face transformers models

| 字段 | 值 |
| --- | --- |
| Issue | [#616](https://github.com/vllm-project/vllm/issues/616) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Best effort support for all Hugging Face transformers models

### Issue 正文摘录

With https://github.com/huggingface/text-generation-inference adopting a less friendly license, this seems like a good opportunity to add best effort support for all Hugging Face `transformers` models that generate text e.g., via `AutoModelForCausalLM` and `AutoModelForSeq2SeqLM`. This would allow them to take advantage of vLLM's other serving features while specific models can retain optimized implementations or gain them as they are implemented * https://github.com/huggingface/text-generation-inference/blob/ecf6dc3a5a31c1b0e1ed48988ddf2416b5e35660/server/text_generation_server/models/causal_lm.py#L451 * https://github.com/huggingface/text-generation-inference/blob/ecf6dc3a5a31c1b0e1ed48988ddf2416b5e35660/server/text_generation_server/models/seq2seq_lm.py#L501

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Best effort support for all Hugging Face transformers models feature request With https://github.com/huggingface/text-generation-inference adopting a less friendly license, this seems like a good opportunity to add best...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: d allow them to take advantage of vLLM's other serving features while specific models can retain optimized implementations or gain them as they are implemented * https://github.com/huggingface/text-generation-inference/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Best effort support for all Hugging Face transformers models feature request With https://github.com/huggingface/text-generation-inference adopting a less friendly license, this seems like a good opportunity to add best...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
