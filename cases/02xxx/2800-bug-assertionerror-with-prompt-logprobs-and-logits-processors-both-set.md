# vllm-project/vllm#2800: [bug] AssertionError with prompt_logprobs and logits_processors both set

| 字段 | 值 |
| --- | --- |
| Issue | [#2800](https://github.com/vllm-project/vllm/issues/2800) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [bug] AssertionError with prompt_logprobs and logits_processors both set

### Issue 正文摘录

version 0.3.0 with prompt_logprobs and logits_processors both set ``` def proc(token_ids, logits_row): return logits_row sampling_params = SamplingParams(temperature=0.8, top_p=0.95, prompt_logprobs=100, logits_processors=[proc]) ``` got error ``` File "/opt/conda/lib/python3.10/site-packages/vllm/model_executor/layers/sampler.py", line 74, in forward logits = _apply_logits_processors(logits, sampling_metadata) File "/opt/conda/lib/python3.10/site-packages/vllm/model_executor/layers/sampler.py", line 162, in _apply_logits_processors assert logits_row_idx == logits.shape[0] AssertionError ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [bug] AssertionError with prompt_logprobs and logits_processors both set version 0.3.0 with prompt_logprobs and logits_processors both set ``` def proc(token_ids, logits_row): return logits_row sampling_params = Samplin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ne 74, in forward logits = _apply_logits_processors(logits, sampling_metadata) File "/opt/conda/lib/python3.10/site-packages/vllm/model_executor/layers/sampler.py", line 162, in _apply_logits_processors assert logits_ro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ) ``` got error ``` File "/opt/conda/lib/python3.10/site-packages/vllm/model_executor/layers/sampler.py", line 74, in forward logits = _apply_logits_processors(logits, sampling_metadata) File "/opt/conda/lib/python3.10/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
