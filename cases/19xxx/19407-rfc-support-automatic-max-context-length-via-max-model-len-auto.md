# vllm-project/vllm#19407: [RFC]: Support automatic max context length via `--max-model-len auto`

| 字段 | 值 |
| --- | --- |
| Issue | [#19407](https://github.com/vllm-project/vllm/issues/19407) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support automatic max context length via `--max-model-len auto`

### Issue 正文摘录

### Motivation. vLLM engine expect the memory is enough to serve at least 1 request of `max-model-len` [[pointer](https://github.com/vllm-project/vllm/blob/5f1ac1e1d14ce239ea6ea99e276ad90cdc342132/vllm/v1/core/kv_cache_utils.py#L562)]. When `max-model-len` is unset, vllm will read that from model configuration, this is problematic as 10M or infinite context model will get increasingly more common. For example, when running llama4 scout (10M) model using the following command: ``` vllm serve meta-llama/Llama-4-Scout-17B-16E-Instruct -tp 8 ``` It throws following error after ~10 minutes of initialization: ``` ValueError: To serve at least one request with the models's max seq len (10485760), (240.00 GiB KV cache is needed, which is larger than the available KV cache memory (88.38 GiB). Based on the available memory, the estimated maximum model length is 3861424. Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine. ``` While prior work like https://github.com/vllm-project/vllm/pull/16168 by @lengrongfu and @heheda12345 make it straightforward for users to adjust max-model-len, this still requires 1 failed attempt when people are trying n...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [RFC]: Support automatic max context length via `--max-model-len auto` RFC;stale ### Motivation. vLLM engine expect the memory is enough to serve at least 1 request of `max-model-len` [[pointer](https://github.com/vllm-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: FC]: Support automatic max context length via `--max-model-len auto` RFC;stale ### Motivation. vLLM engine expect the memory is enough to serve at least 1 request of `max-model-len` [[pointer](https://github.com/vllm-pr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: be annoying to maintain this setting for multiple hardware and parallelism settings. It's also not uncommon to see user confusions about OOMs due to this reason. ### Proposed Change. Support `--max-model-len auto` that...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: least one request with the models's max seq len (10485760), (240.00 GiB KV cache is needed, which is larger than the available KV cache memory (88.38 GiB). Based on the available memory, the estimated maximum model leng...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: truncates max-model-len to the max context length supportable by HBM capacity and warn users about overrides. Actual change requires some refactoring for initialization code to ensure updates got populated properly to `...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
