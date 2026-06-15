# vllm-project/vllm#26932: [Feature]: A more generalized vLLM Helm chart

| 字段 | 值 |
| --- | --- |
| Issue | [#26932](https://github.com/vllm-project/vllm/issues/26932) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: A more generalized vLLM Helm chart

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The vLLM Helm template for `deployment.yaml` hardcodes several things. For my use case benchmarking [llm-d ](https://github.com/llm-d/llm-d)which uses vLLM, I would like to deploy the model server engine using the upstream vLLM chart. This requires a flexible design. Listing the current behavior today and the ideal behavior to enable my use-case. | Helm values/Deployment field | Current behavior | Desired behavior | |------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | The deployment name | Hardcoded to `{{ .Release.Name }}-deployment-vllm` | `{{ .Release.Name }}` | | Deployment selector labels | Hardcoded to `environment: test` and `release: t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: roach is mount emptyDir volumes in locations that vllm uses a cache or compile space for some models. This speaks to need of a flexible volume and volumeMount. | | Annotations | Does not exist
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tps://github.com/llm-d/llm-d)which uses vLLM, I would like to deploy the model server engine using the upstream vLLM chart. This requires a flexible design. Listing the current behavior today and the ideal behavior to e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: A more generalized vLLM Helm chart feature request;stale ### 🚀 The feature, motivation and pitch The vLLM Helm template for `deployment.yaml` hardcodes several things. For my use case benchmarking [llm-d ](ht...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: template for `deployment.yaml` hardcodes several things. For my use case benchmarking [llm-d ](https://github.com/llm-d/llm-d)which uses vLLM, I would like to deploy the model server engine using the upstream vLLM chart...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
