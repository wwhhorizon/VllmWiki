# vllm-project/vllm#19524: [Bug]: disaggregated_prefill.sh assert issubclass(connector_cls, KVConnectorBase_V1)

| 字段 | 值 |
| --- | --- |
| Issue | [#19524](https://github.com/vllm-project/vllm/issues/19524) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: disaggregated_prefill.sh assert issubclass(connector_cls, KVConnectorBase_V1)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This issue does not appear to be related to the environment, but rather stems from the class inheritance structure of the connector. According to the code, the connector name PyNcclConnector is registered to the class vllm.distributed.kv_transfer.kv_connector.simple_connector.SimpleConnector. However, this class inherits from KVConnectorBase, instead of KVConnectorBase_V1 as required. As a result, the assertion assert issubclass(connector_cls, KVConnectorBase_V1) will always fail for this connector. In summary, unless SimpleConnector is updated to inherit from KVConnectorBase_V1 and implements all the necessary v1 methods, using PyNcclConnector as the connector will consistently result in this error, regardless of the runtime environment or configuration. For reference, I am using vLLM version v0.9.1, which I compiled and installed on my own machine. The relevant code paths are: vllm/distributed/kv_transfer/kv_connector/factory.py vllm/distributed/kv_transfer/kv_connector/base.py vllm/distributed/kv_transfer/kv_connector/simple_connector.py ### Before submitting a new issue... - [x] Make sure you already searched for relevant iss...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: he runtime environment or configuration. For reference, I am using vLLM version v0.9.1, which I compiled and installed on my own machine. The relevant code paths are: vllm/distributed/kv_transfer/kv_connector/factory.py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .py ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sistently result in this error, regardless of the runtime environment or configuration. For reference, I am using vLLM version v0.9.1, which I compiled and installed on my own machine. The relevant code paths are: vllm/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: disaggregated_prefill.sh assert issubclass(connector_cls, KVConnectorBase_V1) bug ### Your current environment ### 🐛 Describe the bug This issue does not appear to be related to the environment, but rather stems...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
