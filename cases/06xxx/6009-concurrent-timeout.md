# vllm-project/vllm#6009: Concurrent timeout

| 字段 | 值 |
| --- | --- |
| Issue | [#6009](https://github.com/vllm-project/vllm/issues/6009) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Concurrent timeout

### Issue 正文摘录

### Your current environment Start Service Command： python -m vllm.entrypoints.openai.api_server --model /data/Qwen1.5-1.8B-Chat-GPTQ-Int4 --served-model-name Qwen1.5-1.8B-Chat-GPTQ-Int4 --quantization gptq --dtype float16 --gpu-memory-utilization 0.2 --tensor-parallel-size 1 --trust-remote-code --max-model-len 4096 --served-model-name qwen1.5-1.8b ### 🐛 Describe the bug ![image](https://github.com/vllm-project/vllm/assets/11584869/9658773c-e368-4688-93b3-40e5c0ab81ef) When testing with 50 concurrent requests, there are 4 failures with a prompt of connection timeout. How should this issue be resolved?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: vllm.entrypoints.openai.api_server --model /data/Qwen1.5-1.8B-Chat-GPTQ-Int4 --served-model-name Qwen1.5-1.8B-Chat-GPTQ-Int4 --quantization gptq --dtype float16 --gpu-memory-utilization 0.2 --tensor-parallel-size 1 --tr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t Start Service Command： python -m vllm.entrypoints.openai.api_server --model /data/Qwen1.5-1.8B-Chat-GPTQ-Int4 --served-model-name Qwen1.5-1.8B-Chat-GPTQ-Int4 --quantization gptq --dtype float16 --gpu-memory-utilizatio...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Concurrent timeout bug;stale ### Your current environment Start Service Command： python -m vllm.entrypoints.openai.api_server --model /data/Qwen1.5-1.8B-Chat-GPTQ-Int4 --served-model-name Qwen1.5-1.8B-Chat-GPTQ-Int4 --q...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: -project/vllm/assets/11584869/9658773c-e368-4688-93b3-40e5c0ab81ef) When testing with 50 concurrent requests, there are 4 failures with a prompt of connection timeout. How should this issue be resolved?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
