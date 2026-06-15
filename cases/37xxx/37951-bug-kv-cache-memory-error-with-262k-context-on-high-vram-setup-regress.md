# vllm-project/vllm#37951: [Bug]: KV Cache Memory Error with 262K Context on High VRAM Setup (Regression from Previous Version)

| 字段 | 值 |
| --- | --- |
| Issue | [#37951](https://github.com/vllm-project/vllm/issues/37951) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: KV Cache Memory Error with 262K Context on High VRAM Setup (Regression from Previous Version)

### Issue 正文摘录

### Your current environment **Description:** When running vLLM with a 262144 max sequence length, the engine fails to initialize due to insufficient KV cache memory, despite having a high VRAM configuration (~96GB). This behavior did not occur in previous versions under similar or identical setups. **Reproduction Command:** (see attached log) **Observed Behavior:** The engine fails during initialization with the following error: > ValueError: To serve at least one request with the model's max seq len (262144), 27.45 GiB KV cache is needed, but only 23.43 GiB is available. The system reports: * Available KV cache memory: 23.43 GiB * Required KV cache memory: 27.45 GiB This leads to engine startup failure. **Expected Behavior:** Given a ~96GB VRAM environment, this configuration should not hit KV cache limits. Previous versions were able to run similar configurations without triggering this error. **Additional Notes:** * Model loads successfully (~50.76 GiB used) before KV cache allocation failure * Prefix caching and speculative decoding are enabled * No explicit GPU memory cap was set beyond defaults **Regression:** This appears to be a regression, as the same setup did not fail...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ory Error with 262K Context on High VRAM Setup (Regression from Previous Version) bug ### Your current environment **Description:** When running vLLM with a 262144 max sequence length, the engine fails to initialize due...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: itialize due to insufficient KV cache memory, despite having a high VRAM configuration (~96GB). This behavior did not occur in previous versions under similar or identical setups. **Reproduction Command:** (see attached...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: KV Cache Memory Error with 262K Context on High VRAM Setup (Regression from Previous Version) bug ### Your current environment **Description:** When running vLLM with a 262144 max sequence length, the engine fail...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: alization with the following error: > ValueError: To serve at least one request with the model's max seq len (262144), 27.45 GiB KV cache is needed, but only 23.43 GiB is available. The system reports: * Available KV ca...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: KV Cache Memory Error with 262K Context on High VRAM Setup (Regression from Previous Version) bug ### Your current environment **Description:** When running vLLM with a 262144 max sequence length, the engine fail...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
