# vllm-project/vllm#1428: Mistral much slower than LLaMa-2-7B

| 字段 | 值 |
| --- | --- |
| Issue | [#1428](https://github.com/vllm-project/vllm/issues/1428) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Mistral much slower than LLaMa-2-7B

### Issue 正文摘录

I have finetuned both Mistral-7B and Llama2-7b on custom usecase and quantized them using AutoAWQ. Below are the benchmark results (throughput here is tokens/sec). From my understanding, shouldn't Mistral be faster or equivalent to Llama2? Can someone figure out why this is the case? ![image](https://github.com/vllm-project/vllm/assets/13467155/251b38a2-e741-4b9b-8c64-9a29c3a772e1)

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ma2-7b on custom usecase and quantized them using AutoAWQ. Below are the benchmark results (throughput here is tokens/sec). From my understanding, shouldn't Mistral be faster or equivalent to Llama2? Can someone figure...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: -7B I have finetuned both Mistral-7B and Llama2-7b on custom usecase and quantized them using AutoAWQ. Below are the benchmark results (throughput here is tokens/sec). From my understanding, shouldn't Mistral be faster...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Mistral much slower than LLaMa-2-7B I have finetuned both Mistral-7B and Llama2-7b on custom usecase and quantized them using AutoAWQ. Below are the benchmark results (throughput here is tokens/sec). From my understandi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
