# vllm-project/vllm#1010: Misalignment of model embeddings & Addition of RoPe Scaling.

| 字段 | 值 |
| --- | --- |
| Issue | [#1010](https://github.com/vllm-project/vllm/issues/1010) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Misalignment of model embeddings & Addition of RoPe Scaling.

### Issue 正文摘录

I intend on submitting a PR to include embeddings as well as rope scaling. Most of this is completed already, however during testing of the embeddings I wasn't able to get any consistency with that of hugging faces pipeline. Most of this I believe is the 1D tensors and the is a focus on batch generation, maybe a missing float32 somewhere 🤷 ... I'm also probably missing something too. Anyways, after playing around for quite a while I figured I'd drop a note and see if one of the project team might shed some light. The following is the best run at what we have available currently (to my knowledge) within vllm. While forward does in fact create embeddings, they are severely mis aligned with that of hugging face. While this isn't a necessity it would be the ideal state, so that vectors stored could be leverage from multiple code bases, if they were all so generate by a standard. Using forward via worker.py snippet: ``` output = self.model.model.forward( input_ids=input_tokens, positions=input_positions, kv_caches=self.gpu_cache, input_metadata=input_metadata, cache_events=cache_events )[0, :] ``` I'd like to match that of something like the following that would get used via hugging fa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Misalignment of model embeddings & Addition of RoPe Scaling. I intend on submitting a PR to include embeddings as well as rope scaling. Most of this is completed already, however during testing of the embeddings I wasn'...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: s the 1D tensors and the is a focus on batch generation, maybe a missing float32 somewhere 🤷 ... I'm also probably missing something too. Anyways, after playing around for quite a while I figured I'd drop a note and see...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: input_positions, kv_caches=self.gpu_cache, input_metadata=input_metadata, cache_events=cache_events )[0, :] ``` I'd like to match that of something like the following that would get used via hugging face transformers: `...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ell as rope scaling. Most of this is completed already, however during testing of the embeddings I wasn't able to get any consistency with that of hugging faces pipeline. Most of this I believe is the 1D tensors and the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
