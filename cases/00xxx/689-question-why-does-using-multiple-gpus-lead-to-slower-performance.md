# vllm-project/vllm#689: [Question] Why does using multiple gpus lead to slower performance?

| 字段 | 值 |
| --- | --- |
| Issue | [#689](https://github.com/vllm-project/vllm/issues/689) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Question] Why does using multiple gpus lead to slower performance?

### Issue 正文摘录

When I set tensor_parallel_size to > 1, the wall time increases though everything else is down. Am I doing something wrong in my setup where using multiple gpus is actually slower than using one? ``` vllm = LLM( model="mosaicml/mpt-7b-instruct", trust_remote_code=True, dtype="float16", tensor_parallel_size=1, gpu_memory_utilization=.95, ) CPU times: user 3.66 s, sys: 262 ms, total: 3.93 s Wall time: 1.11 s ``` ``` vllm = LLM( model="mosaicml/mpt-7b-instruct", trust_remote_code=True, dtype="float16", tensor_parallel_size=2, gpu_memory_utilization=.95, ) CPU times: user 65.5 ms, sys: 32.2 ms, total: 97.7 ms Wall time: 1.27 s ```

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ( model="mosaicml/mpt-7b-instruct", trust_remote_code=True, dtype="float16", tensor_parallel_size=1, gpu_memory_utilization=.95, ) CPU times: user 3.66 s, sys: 262 ms, total: 3.93 s Wall time: 1.11 s ``` ``` vllm = LLM(...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tensor_parallel_size to > 1, the wall time increases though everything else is down. Am I doing something wrong in my setup where using multiple gpus is actually slower than using one? ``` vllm = LLM( model="mosaicml/mp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ing multiple gpus is actually slower than using one? ``` vllm = LLM( model="mosaicml/mpt-7b-instruct", trust_remote_code=True, dtype="float16", tensor_parallel_size=1, gpu_memory_utilization=.95, ) CPU times: user 3.66...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
