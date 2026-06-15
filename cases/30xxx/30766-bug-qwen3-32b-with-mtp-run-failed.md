# vllm-project/vllm#30766: [Bug]: Qwen3-32B with MTP, run failed.

| 字段 | 值 |
| --- | --- |
| Issue | [#30766](https://github.com/vllm-project/vllm/issues/30766) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-32B with MTP, run failed.

### Issue 正文摘录

### Your current environment # use vllm-0.11.2 run qwen3-32B with mtp ### 🐛 Describe the bug #server code python3 -m vllm.entrypoints.openai.api_server \ --model /upfs/models/Qwen/Qwen3-32B/ \ --served-model-name qwen3_32b \ --tensor-parallel-size 1 \ --trust-remote-code \ --max-model-len 40960 \ --max-num-batched-tokens 8192 \ --max-num-seqs 512 \ --port 8000 \ --gpu-memory-utilization 0.9 \ --no-async-scheduling \ --speculative-config '{"model": "/almp-bucket-malaysia/prod/models/antom/yz/qwen3_32b_eagle3_v1", "num_speculative_tokens": 4}' \ # test code vllm bench serve \ --host "$HOST" \ --port "$PORT" \ --model "$MODEL" \ --tokenizer "$TOKENIZER" \ --dataset-name "$DATASET" \ --num-prompts "$NUM_PROMPTS" \ --max-concurrency "$concurrency" \ --random-input-len "$RANDOM_INPUT_LEN" \ --random-output-len "$RANDOM_OUTPUT_LEN" \ --percentile-metrics "$PERCENTILE_METRICS" \ --metric-percentiles "$METRIC_PERCENTILES" \ --num-warmups 2 \ error code: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of fr...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-32B with MTP, run failed. bug;stale ### Your current environment # use vllm-0.11.2 run qwen3-32B with mtp ### 🐛 Describe the bug #server code python3 -m vllm.entrypoints.openai.api_server \ --model /upfs/mod
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Qwen3-32B with MTP, run failed. bug;stale ### Your current environment # use vllm-0.11.2 run qwen3-32B with mtp ### 🐛 Describe the bug #server code python3 -m vllm.entrypoints.openai.api_server \ --model /upfs/mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: models/antom/yz/qwen3_32b_eagle3_v1", "num_speculative_tokens": 4}' \ # test code vllm bench serve \ --host "$HOST" \ --port "$PORT" \ --model "$MODEL" \ --tokenizer "$TOKENIZER" \ --dataset-name "$DATASET" \ --num-prom...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
