# vllm-project/vllm#14931: [Usage]: CPU使用率

| 字段 | 值 |
| --- | --- |
| Issue | [#14931](https://github.com/vllm-project/vllm/issues/14931) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: CPU使用率

### Issue 正文摘录

### Your current environment python -m vllm.entrypoints.openai.api_server \ --model /data/ModelScope/Qwen2.5-7B-Instruct \ --port 8000 \ --host 0.0.0.0 \ --dtype float16 \ --kv-cache-dtype fp8_e4m3 \ --tensor-parallel-size 1 \ --pipeline-parallel-size 1 \ --gpu-memory-utilization 0.60 \ ### How would you like to use vllm 使用上述运行大模型时，产生的进程CPU使用无法超过100%，是vllm有限制只使用一个cpu吗 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Scope/Qwen2.5-7B-Instruct \ --port 8000 \ --host 0.0.0.0 \ --dtype float16 \ --kv-cache-dtype fp8_e4m3 \ --tensor-parallel-size 1 \ --pipeline-parallel-size 1 \ --gpu-memory-utilization 0.60 \ ### How would you like to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: urrent environment python -m vllm.entrypoints.openai.api_server \ --model /data/ModelScope/Qwen2.5-7B-Instruct \ --port 8000 \ --host 0.0.0.0 \ --dtype float16 \ --kv-cache-dtype fp8_e4m3 \ --tensor-parallel-size 1 \ --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: pu吗 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: struct \ --port 8000 \ --host 0.0.0.0 \ --dtype float16 \ --kv-cache-dtype fp8_e4m3 \ --tensor-parallel-size 1 \ --pipeline-parallel-size 1 \ --gpu-memory-utilization 0.60 \ ### How would you like to use vllm 使用上述运行大模型时...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: CPU使用率 usage;stale ### Your current environment python -m vllm.entrypoints.openai.api_server \ --model /data/ModelScope/Qwen2.5-7B-Instruct \ --port 8000 \ --host 0.0.0.0 \ --dtype float16 \ --kv-cache-dtype fp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
