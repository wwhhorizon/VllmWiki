# vllm-project/vllm#26927: [Feature]: Enable custom init containers in vLLM helm chart

| 字段 | 值 |
| --- | --- |
| Issue | [#26927](https://github.com/vllm-project/vllm/issues/26927) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Enable custom init containers in vLLM helm chart

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm currently exploring the integration of the upstream vLLM Helm chart with [llm-d](https://github.com/llm-d/llm-d/tree/main), a Kubernetes-native distributed inferencing stack. llm-d utilizes a [sidecar container as a routing proxy](https://github.com/llm-d/llm-d-routing-sidecar) for prefill/decode scenarios, which forwards requests to prefill pods. This proxy is deployed as an init container on decode instances to ensure it is available before the main server starts. However, the current upstream vLLM Helm chart has a limitation: when `.extraInit` is specified, the [init container ](https://github.com/vllm-project/vllm/blob/14f845634481d5223f4573461c6e2a4fe57eda98/examples/online_serving/chart-helm/values.yaml#L76C1-L83C1)is hardcoded to perform model downloads. This restricts our ability to customize the init container behavior for use cases like llm-d. To enable benchmarking llm-d, so we need more flexible init container configuration. I have two potential approaches to address this. Depending on community feedback, I'm happy to open a PR for the preferred solution. ### Alternatives Solution 1: breaking change for existing users but cle...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Enable custom init containers in vLLM helm chart feature request ### 🚀 The feature, motivation and pitch I'm currently exploring the integration of the upstream vLLM Helm chart with [llm-d](https://github.com...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: lpath: "relative_s3_model_path/opt-125m" pvcStorage: "1Gi" awsEc2MetadataDisabled: true # Add custom init containers custom: - name: llm-d-routing-proxy image: ghcr.io/llm-d/llm-d-routing-sidecar:v0.2.0 args: [] command...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nline_serving/chart-helm/values.yaml#L76C1-L83C1)is hardcoded to perform model downloads. This restricts our ability to customize the init container behavior for use cases like llm-d. To enable benchmarking llm-d, so we...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ustomize the init container behavior for use cases like llm-d. To enable benchmarking llm-d, so we need more flexible init container configuration. I have two potential approaches to address this. Depending on community...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: distributed inferencing stack. llm-d utilizes a [sidecar container as a routing proxy](https://github.com/llm-d/llm-d-routing-sidecar) for prefill/decode scenarios, which forwards requests to prefill pods. This proxy is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
