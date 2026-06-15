# vllm-project/vllm#17029: [Feature]: add hostname in metrics for clustering deployment

| 字段 | 值 |
| --- | --- |
| Issue | [#17029](https://github.com/vllm-project/vllm/issues/17029) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: add hostname in metrics for clustering deployment

### Issue 正文摘录

### 🚀 The feature, motivation and pitch # Feature Request: Add hostname in metrics for clustering deployment ## Problem Statement When deploying vLLM as a Model-as-a-Service behind an API gateway with multiple backend instances, accessing the `/metrics` endpoint returns metrics from a random backend instance without any instance identification. This makes it impossible to: 1. Associate metrics with specific instances 2. Track performance across the cluster 3. Identify problematic instances 4. Perform proper load balancing based on instance-specific metrics ## Proposed Solution Enhance the vLLM metrics system to include instance identification by: 1. Adding a mandatory `instance_id` label to all metrics exported through the `/metrics` endpoint 2. Using the container hostname by default (automatically populated as `HOSTNAME` in most container environments) 3. Allowing custom instance ID configuration through environment variables or configuration files ## Implementation Details The implementation could be achieved by modifying the `Metrics` class in metrics.py: ## Benefits 1. **Improved Observability**: Operators can track performance metrics per instance 2. **Better Debugging**: Qu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ithout any instance identification. This makes it impossible to: 1. Associate metrics with specific instances 2. Track performance across the cluster 3. Identify problematic instances 4. Perform proper load balancing ba...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: or clustering deployment ## Problem Statement When deploying vLLM as a Model-as-a-Service behind an API gateway with multiple backend instances, accessing the `/metrics` endpoint returns metrics from a random backend in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: add hostname in metrics for clustering deployment feature request;stale ### 🚀 The feature, motivation and pitch # Feature Request: Add hostname in metrics for clustering deployment ## Problem Statement When d...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ploying vLLM as a Model-as-a-Service behind an API gateway with multiple backend instances, accessing the `/metrics` endpoint returns metrics from a random backend instance without any instance identification. This make...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: tered environments, which is becoming increasingly common as LLM serving scales. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
