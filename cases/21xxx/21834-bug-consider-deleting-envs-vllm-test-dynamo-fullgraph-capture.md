# vllm-project/vllm#21834: [Bug]: Consider deleting envs.VLLM_TEST_DYNAMO_FULLGRAPH_CAPTURE

| 字段 | 值 |
| --- | --- |
| Issue | [#21834](https://github.com/vllm-project/vllm/issues/21834) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Consider deleting envs.VLLM_TEST_DYNAMO_FULLGRAPH_CAPTURE

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM doesn't work without fullgraph=True Dynamo, so we should just delete it. The deletion might be a little tricky because there are some other libraries that use this function: https://github.com/search?q=repo%3Avllm-project%2Fvllm-ascend%20VLLM_TEST_DYNAMO_FULLGRAPH_CAPTURE&type=code, so we'd need to figure out what matters and delete those first. "Bug" because "VLLM_TEST_DYNAMO_FULLGRAPH_CAPTURE=0" may not do anything ### Alternatives Keep it around forever ### Additional context n/a ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ug]: Consider deleting envs.VLLM_TEST_DYNAMO_FULLGRAPH_CAPTURE bug;torch.compile ### 🚀 The feature, motivation and pitch vLLM doesn't work without fullgraph=True Dynamo, so we should just delete it. The deletion might b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: re are some other libraries that use this function: https://github.com/search?q=repo%3Avllm-project%2Fvllm-ascend%20VLLM_TEST_DYNAMO_FULLGRAPH_CAPTURE&type=code, so we'd need to figure out what matters and delete those...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: Consider deleting envs.VLLM_TEST_DYNAMO_FULLGRAPH_CAPTURE bug;torch.compile ### 🚀 The feature, motivation and pitch vLLM doesn't work without fullgraph=True Dynamo, so we should just delete it. The deletion might...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
