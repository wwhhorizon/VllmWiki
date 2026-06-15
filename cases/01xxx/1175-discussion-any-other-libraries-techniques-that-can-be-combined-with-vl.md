# vllm-project/vllm#1175: [Discussion] Any other libraries/techniques that can be combined with vllm to further speed up inference?

| 字段 | 值 |
| --- | --- |
| Issue | [#1175](https://github.com/vllm-project/vllm/issues/1175) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Discussion] Any other libraries/techniques that can be combined with vllm to further speed up inference?

### Issue 正文摘录

My current setup is this, and it takes around 2 seconds to generate a response from a prompt, was wondering if there are additional libraries/packages that can be used on top of vllm to achieve subsecond performance? ` llm = LLM(model="mosaicml/mpt-7b-instruct", trust_remote_code=True,dtype="float16",tensor_parallel_size=2) `

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ce? ` llm = LLM(model="mosaicml/mpt-7b-instruct", trust_remote_code=True,dtype="float16",tensor_parallel_size=2) `
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: can be used on top of vllm to achieve subsecond performance? ` llm = LLM(model="mosaicml/mpt-7b-instruct", trust_remote_code=True,dtype="float16",tensor_parallel_size=2) `

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
