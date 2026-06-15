# vllm-project/vllm#36215: [Performance]: vLLM is slower than SGLang when deploying the Qwen3.5 model.

| 字段 | 值 |
| --- | --- |
| Issue | [#36215](https://github.com/vllm-project/vllm/issues/36215) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: vLLM is slower than SGLang when deploying the Qwen3.5 model.

### Issue 正文摘录

### Proposal to improve performance Based on the results on the evaluation datasets, SGLang demonstrates significantly better inference performance than vLLM under the same hardware environment. Across the three benchmark datasets, SGLang achieves an overall inference speed improvement of approximately 3.1× to 5.3× compared to vLLM 。 test model is: Qwen3.5-35B-A3B, one GPU ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ormance ### Proposal to improve performance Based on the results on the evaluation datasets, SGLang demonstrates significantly better inference performance than vLLM under the same hardware environment. Across the three...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: vLLM is slower than SGLang when deploying the Qwen3.5 model. performance ### Proposal to improve performance Based on the results on the evaluation datasets, SGLang demonstrates significantly better infer...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
