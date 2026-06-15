# vllm-project/vllm#13004: [Feature]: Disaggregated Prefill on multi-node & multi-gpu

| 字段 | 值 |
| --- | --- |
| Issue | [#13004](https://github.com/vllm-project/vllm/issues/13004) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Disaggregated Prefill on multi-node & multi-gpu

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ``` class KVTransferConfig(BaseModel): """Configuration for distributed KV cache transfer.""" # The KV connector for vLLM to transmit KV caches between vLLM instances. kv_connector: Optional[str] = None # The device used by kv connector to buffer the KV cache. # Currently only support 'cuda'. kv_buffer_device: Optional[str] = "cuda" # The buffer size for TorchDistributedConnector. Measured in number of # bytes. Recommended value: 1e9 (about 1GB). kv_buffer_size: float = 1e9 # Whether this vLLM instance produces, consumes KV cache, or both. Choices # are 'kv_producer', 'kv_consumer', and 'both'. kv_role: Optional[str] = None # The rank of this vLLM instance in the KV cache transfer. Typical value: # 0 for prefill instance, 1 for decode instance. # Currently only 1P1D is supported. kv_rank: Optional[int] = None ``` I want to deploy DeepSeek R1 with `Disaggregated Prefill`, but "Currently only 1P1D is supported." so this feature is not available for it. What's the roadmap for it? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Disaggregated Prefill on multi-node & multi-gpu feature request;stale ### 🚀 The feature, motivation and pitch ``` class KVTransferConfig(BaseModel): """Configuration for distributed KV cache transfer.""" # Th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: istributed KV cache transfer.""" # The KV connector for vLLM to transmit KV caches between vLLM instances. kv_connector: Optional[str] = None # The device used by kv connector to buffer the KV cache. # Currently only su...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: quest;stale ### 🚀 The feature, motivation and pitch ``` class KVTransferConfig(BaseModel): """Configuration for distributed KV cache transfer.""" # The KV connector for vLLM to transmit KV caches between vLLM instances....
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: class KVTransferConfig(BaseModel): """Configuration for distributed KV cache transfer.""" # The KV connector for vLLM to transmit KV caches between vLLM instances. kv_connector: Optional[str] = None # The device used by...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
