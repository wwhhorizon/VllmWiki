# vllm-project/vllm#2543: Mixtral Quantization Issues

| 字段 | 值 |
| --- | --- |
| Issue | [#2543](https://github.com/vllm-project/vllm/issues/2543) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Mixtral Quantization Issues

### Issue 正文摘录

I'm currently working with quantized versions of Mixtral 8x7B provided by TheBloke, and I load them with vLLM. I'm currently with these issues: `TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ` can be well loaded, but even if the temperature has been fixed to 0, the model gives different outputs on the same prompt. The lack of deterministic is not found on traditional models. `TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ` keeps outputting nothing (is mentioned in huggingface discussions [here](https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ/discussions/3) Is there anyone having faced and resolved such a problem? I know it may not be directly related to vLLM. And is there anyone having tested a quantized Mixtral model with vLLM well? Great thx.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: loaded, but even if the temperature has been fixed to 0, the model gives different outputs on the same prompt. The lack of deterministic is not found on traditional models. `TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ` keep...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: can be well loaded, but even if the temperature has been fixed to 0, the model gives different outputs on the same prompt. The lack of deterministic is not found on traditional models. `TheBloke/Mixtral-8x7B-Instruct-v0...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: to 0, the model gives different outputs on the same prompt. The lack of deterministic is not found on traditional models. `TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ` keeps outputting nothing (is mentioned in huggingface d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Mixtral Quantization Issues bug I'm currently working with quantized versions of Mixtral 8x7B provided by TheBloke, and I load them with vLLM. I'm currently with these issues: `TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ`...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Mixtral Quantization Issues bug I'm currently working with quantized versions of Mixtral 8x7B provided by TheBloke, and I load them with vLLM. I'm currently with these issues: `TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
