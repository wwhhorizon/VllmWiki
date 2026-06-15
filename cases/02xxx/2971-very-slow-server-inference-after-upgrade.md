# vllm-project/vllm#2971: Very Slow Server Inference After Upgrade

| 字段 | 值 |
| --- | --- |
| Issue | [#2971](https://github.com/vllm-project/vllm/issues/2971) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Very Slow Server Inference After Upgrade

### Issue 正文摘录

Recently upgraded to the latest version 0.3.2 and I've noticed a total slowdown in outputs. Here's my speed on the 0.2.7 release `Avg prompt throughput: 1006.0 tokens/s, Avg generation throughput: 273.8 tokens/s,` Here's my speed on 0.3.2 `Avg prompt throughput: 175.5 tokens/s, Avg generation throughput: 15.5 tokens/s,` start command: ``` python -m vllm.entrypoints.openai.api_server \ --model code/hf-models/OpenHermes-2.5-Mistral-7B --max-model-len 8192 ``` On a single 4090.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: start command: ``` python -m vllm.entrypoints.openai.api_server \ --model code/hf-models/OpenHermes-2.5-Mistral-7B --max-model-len 8192 ``` On a single 4090.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Very Slow Server Inference After Upgrade Recently upgraded to the latest version 0.3.2 and I've noticed a total slowdown in outputs. Here's my speed on the 0.2.7 release `Avg prompt throughput: 1006.0 tokens/s, Avg gene...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Very Slow Server Inference After Upgrade Recently upgraded to the latest version 0.3.2 and I've noticed a total slowdown in outputs. Here's my speed on the 0.2.7 release `Avg prompt throughput: 1006.0 tokens/s, Avg gene...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
