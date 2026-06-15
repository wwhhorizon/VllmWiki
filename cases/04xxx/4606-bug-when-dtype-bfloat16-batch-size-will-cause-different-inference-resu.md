# vllm-project/vllm#4606: [Bug]: when dtype='bfloat16', batch_size will cause different inference results

| 字段 | 值 |
| --- | --- |
| Issue | [#4606](https://github.com/vllm-project/vllm/issues/4606) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: when dtype='bfloat16', batch_size will cause different inference results

### Issue 正文摘录

### Your current environment ``` # reproduce codes: from vllm import LLM, SamplingParams import datasets raw_datasets = datasets.load_dataset( "truthful_qa", 'generation') questions = [i['question'] for i in raw_datasets['validation']] llm = LLM(model="mistralai/Mistral-7B-Instruct-v0.2" , dtype='bfloat16', trust_remote_code=True) sampling_params = SamplingParams( temperature=0, max_tokens=256 ) for batch_size in [32, 64, 256]: outputs = llm.generate( questions[:batch_size], sampling_params ) for o in outputs[:5]: print(o.outputs[0].text) print() print('------------------------------') ``` ### 🐛 Describe the bug when dtype='bfloat16', changing the `batch_size `to different numbers, will cause the obvious differences in `outputs` above. This issue does not exist in float16 and 32.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: when dtype='bfloat16', batch_size will cause different inference results bug;stale ### Your current environment ``` # reproduce codes: from vllm import LLM, SamplingParams import datasets raw_datasets = datasets....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: amplingParams import datasets raw_datasets = datasets.load_dataset( "truthful_qa", 'generation') questions = [i['question'] for i in raw_datasets['validation']] llm = LLM(model="mistralai/Mistral-7B-Instruct-v0.2" , dty...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ifferent inference results bug;stale ### Your current environment ``` # reproduce codes: from vllm import LLM, SamplingParams import datasets raw_datasets = datasets.load_dataset( "truthful_qa", 'generation') questions...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ug;stale ### Your current environment ``` # reproduce codes: from vllm import LLM, SamplingParams import datasets raw_datasets = datasets.load_dataset( "truthful_qa", 'generation') questions = [i['question'] for i in ra...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: dtype='bfloat16', batch_size will cause different inference results bug;stale ### Your current environment ``` # reproduce codes: from vllm import LLM, SamplingParams import datasets raw_datasets = datasets.load_dataset...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
