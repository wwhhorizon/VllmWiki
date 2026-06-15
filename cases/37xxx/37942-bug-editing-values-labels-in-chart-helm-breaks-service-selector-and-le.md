# vllm-project/vllm#37942: [Bug]: Editing `values.labels` in `chart-helm` breaks Service selector and leaves Endpoints empty

| 字段 | 值 |
| --- | --- |
| Issue | [#37942](https://github.com/vllm-project/vllm/issues/37942) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Editing `values.labels` in `chart-helm` breaks Service selector and leaves Endpoints empty

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This issue is about [chart-helm](https://github.com/vllm-project/vllm/tree/main/examples/online_serving/chart-helm). Editing `labels` in [values.yaml](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/chart-helm/values.yaml) breaks Service selector and leaves Endpoint empty. ### Steps to reproduce: 1. Edit `labels` in `values.yaml`, for example: ```yaml labels: environment: "dev" release: "my-release" ``` 2. Install the chart: ```bash helm install ./examples/online_serving/chart-helm -f ./examples/online_serving/chart-helm/values.yaml ``` 3. Check the resources: ```bash kubectl get pod -owide -n kubectl get endpointslice -n ``` ### Actual behavior The Service does not select the Pods, and the Service endpoints remain empty. In my environment, I deployed two models by executing `helm install` command respectively. The labels are as follows: ```yaml labels: environment: "cl-nagoya-ruri-v3-310m" release: "cl-nagoya-ruri-v3-310m" ``` ```yaml labels: environment: "quanttrio-qwen3-vl-30b-a3b-instruct-awq" release: "quanttrio-qwen3-vl-30b-a3b-instruct-awq" ``` The Pods are as follows: ``` $ kubectl get pod -owide -n...

## 现有链接修复摘要

#38340 [Doc] fix selector/label mismatch in helm chart

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e: ```yaml labels: environment: "dev" release: "my-release" ``` 2. Install the chart: ```bash helm install ./examples/online_serving/chart-helm -f ./examples/online_serving/chart-helm/values.yaml ``` 3. Check the resour...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: els`, while the Pod labels in the Deployment remain fixed, causing the mismatch. Issue #26932 also mentions that the Deployment selector labels are hardcoded to `environment: test` and `release: test`. ### Expected beha...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: s.yaml) breaks Service selector and leaves Endpoint empty. ### Steps to reproduce: 1. Edit `labels` in `values.yaml`, for example: ```yaml labels: environment: "dev" release: "my-release" ``` 2. Install the chart: ```ba...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: d the Service endpoints remain empty. In my environment, I deployed two models by executing `helm install` command respectively. The labels are as follows: ```yaml labels: environment: "cl-nagoya-ruri-v3-310m" release:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;mismatch;nan_inf env_dependency #38340 [Doc] fix selector/label mismatch in helm chart Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38340](https://github.com/vllm-project/vllm/pull/38340) | closes_keyword | 0.95 | [Doc] fix selector/label mismatch in helm chart | Fixes #37942 This fixes label/selector consistency in `examples/online_serving/chart-helm` by: - introducing stable selector labels (`app.kubernetes.io/name`, `app.kubernetes.i |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
