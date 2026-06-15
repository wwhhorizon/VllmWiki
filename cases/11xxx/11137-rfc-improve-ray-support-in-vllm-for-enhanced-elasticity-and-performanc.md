# vllm-project/vllm#11137: [RFC]: Improve Ray Support in vLLM for Enhanced Elasticity and Performance

| 字段 | 值 |
| --- | --- |
| Issue | [#11137](https://github.com/vllm-project/vllm/issues/11137) |
| 状态 | closed |
| 标签 | RFC;ray;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Improve Ray Support in vLLM for Enhanced Elasticity and Performance

### Issue 正文摘录

### Motivation. This RFC proposes integrating native Ray support with the vLLM inference engine to enhance resource management, elasticity, and performance. We aim to address key issues related to resource allocation delays, version compatibility, and deployment efficiency. Integrating Ray with vLLM poses several challenges that impact scalability and performance: - **Elastic Resource Allocation**: Instances where Ray clusters are still pending resource allocation can cause premature task exits. - **Version Compatibility**: Discrepancies between Ray, Python, and vLLM versions complicate deployments, especially in distributed environments. - **Advanced Resource Placement**: Current placement strategies do not fully leverage Ray's capabilities, affecting performance optimization. ### Proposed Change. 1. Elastic Scenarios Support: Introduce an elastic resource waiting mechanism that allows vLLM tasks to delay execution until all requested resources are available, reducing premature exits. related issue: https://github.com/vllm-project/vllm/issues/11134 2. Configurable PG_WAIT_TIMEOUT: Allow users to specify the maximum time Ray waits for resources to be ready, with a default of 1800...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: rove Ray Support in vLLM for Enhanced Elasticity and Performance RFC;ray;stale ### Motivation. This RFC proposes integrating native Ray support with the vLLM inference engine to enhance resource management, elasticity,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [RFC]: Improve Ray Support in vLLM for Enhanced Elasticity and Performance RFC;ray;stale ### Motivation. This RFC proposes integrating native Ray support with the vLLM inference engine to enhance resource management, el...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Elastic Scenarios Support: Introduce an elastic resource waiting mechanism that allows vLLM tasks to delay execution until all requested resources are available, reducing premature exits. related issue: https://github.c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: /vllm-project/vllm/issues/11136 5. Support multi-node vLLM inference in scale. https://github.com/ray-project/kuberay/issues/2323 This is a little bit out of vLLM's scope and I create an issue in KubeRay repo earlier. W...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s. related issue: https://github.com/vllm-project/vllm/issues/11134 2. Configurable PG_WAIT_TIMEOUT: Allow users to specify the maximum time Ray waits for resources to be ready, with a default of 1800 seconds. This flex...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
