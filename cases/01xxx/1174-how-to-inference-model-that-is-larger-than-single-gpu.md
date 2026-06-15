# vllm-project/vllm#1174: How to inference model that is larger than single GPU?

| 字段 | 值 |
| --- | --- |
| Issue | [#1174](https://github.com/vllm-project/vllm/issues/1174) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to inference model that is larger than single GPU?

### Issue 正文摘录

I am using: ```python # load model and inference llm = vllm.LLM( MODEL_NAME, seed=SEED, ) params = vllm.SamplingParams( temperature=TEMPERATURE, top_p=TOP_P, max_tokens=MAX_TOKENS, presence_penalty=PRESENCE_PENALTY, frequency_penalty=FREQUENCY_PENALTY, ) results: List[InferenceResult] = [] for batch in batches: generated = llm.generate(batch, params) for output in generated: results.append( InferenceResult( prompt=output.prompt, response=output.outputs[0].text ) ) ``` but when I chose a 13b on my 4090, it does not seem to split the model across both gpus?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: How to inference model that is larger than single GPU? I am using: ```python # load model and inference llm = vllm.LLM( MODEL_NAME, seed=SEED, ) params = vllm.SamplingParams( temperature=TEMPERATUR

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
