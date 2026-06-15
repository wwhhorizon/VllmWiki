# vllm-project/vllm#44319: [Bug]: Logprobs values change based on the number of requested log probabilities

| 字段 | 值 |
| --- | --- |
| Issue | [#44319](https://github.com/vllm-project/vllm/issues/44319) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Logprobs values change based on the number of requested log probabilities

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using the latest vLLM versions when deploying LLMs on AWS Sagemaker and GCP endpoints - For AWS I am using LMI containers (e.g 763104351884.dkr.ecr.us-west-2.amazonaws.com/djl-inference:0.36.0-lmi25.0.0-cu130) - For GCP, I am building custom containers extending the latest vLLM image (`FROM vllm/vllm-openai:latest)` When requesting log probabilities using the OpenAI completions schema ("logprobs": int), I observed the following: 1. The number of requested log probabilities doesn't match the number of returned log probabilities 2. The value of the log probabilities changes based on the number of requested log probabilities Example: - logprobs = 4 `Output: logprobs: {'false': -8.47667407989502, 'true': -1.6016744375228882, 'null': -8.35167407989502}` - returned 3 values - logprobs = 10 `Output logprobs: {'false': -8.414182662963867, 'true': -10.726682662963867, 'null': -8.351682662963867, 'invalid': -10.101682662963867, 'undefined': -10.351682662963867, '#': -10.601682662963867, '//': -10.976682662963867, '---': -11.039182662963867}` - returned 8 values Notice how the value for the token "true" changes significantly, altering...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: rrent environment ### 🐛 Describe the bug I am using the latest vLLM versions when deploying LLMs on AWS Sagemaker and GCP endpoints - For AWS I am using LMI containers (e.g 763104351884.dkr.ecr.us-west-2.amazonaws.com/d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ue? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ested log probabilities Example: - logprobs = 4 `Output: logprobs: {'false': -8.47667407989502, 'true': -1.6016744375228882, 'null': -8.35167407989502}` - returned 3 values - logprobs = 10 `Output logprobs: {'false': -8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: token "true" changes significantly, altering the final prediction of the model from `false` (logprobs=4) to `true` (logprobs=10) The issue was observed for the latest vLLM versions (older version's don't present this in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Logprobs values change based on the number of requested log probabilities bug ### Your current environment ### 🐛 Describe the bug I am using the latest vLLM versions when deploying LLMs on AWS Sagemaker and GCP e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
