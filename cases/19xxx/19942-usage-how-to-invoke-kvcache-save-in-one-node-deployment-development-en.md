# vllm-project/vllm#19942: [Usage]: how to invoke KVCache save in one node deployment development enviroment

| 字段 | 值 |
| --- | --- |
| Issue | [#19942](https://github.com/vllm-project/vllm/issues/19942) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to invoke KVCache save in one node deployment development enviroment

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I would like to let below method run more in single node deployment development environment ··· VLLM_LOGGING_LEVEL=INFO VLLM_ATTENTION_BACKEND=FLASH_ATTN VLLM_USE_V1=1 bin/vua-vllm serve mistralai/Mistral-7B-Instruct-v0.2 --gpu-memory-utilization 0.90 --tensor-parallel-size 2 --kv-transfer-config '{"kv_connector":"VUAStorageConnector_V1","kv_role":"kv_both","kv_connector_extra_config": {"shared_storage_path": "/mnt/nvme1n1/nfsrdma/test1"}}' --no-enable-prefix-caching --max-num-batched-tokens 30720 --port 8000 ··· ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ment development environment ··· VLLM_LOGGING_LEVEL=INFO VLLM_ATTENTION_BACKEND=FLASH_ATTN VLLM_USE_V1=1 bin/vua-vllm serve mistralai/Mistral-7B-Instruct-v0.2 --gpu-memory-utilization 0.90 --tensor-parallel-size 2 --kv-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ··· ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 2 --gpu-memory-utilization 0.90 --tensor-parallel-size 2 --kv-transfer-config '{"kv_connector":"VUAStorageConnector_V1","kv_role":"kv_both","kv_connector_extra_config": {"shared_storage_path": "/mnt/nvme1n1/nfsrdma/test...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: invoke KVCache save in one node deployment development enviroment usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I would like to let below m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: v_connector_extra_config": {"shared_storage_path": "/mnt/nvme1n1/nfsrdma/test1"}}' --no-enable-prefix-caching --max-num-batched-tokens 30720 --port 8000 ··· ### Before submitting a new issue... - [x] Make sure you alrea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
