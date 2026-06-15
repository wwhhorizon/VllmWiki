# vllm-project/vllm#33497: [Bug]: Low acceptance rate for DeepSeek-V3.2 with `deepseek_mtp` speculative method in v0.15.0

| 字段 | 值 |
| --- | --- |
| Issue | [#33497](https://github.com/vllm-project/vllm/issues/33497) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Low acceptance rate for DeepSeek-V3.2 with `deepseek_mtp` speculative method in v0.15.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Steps to Reproduce 1. Start the vLLM server with the following command: ``` vllm serve deepseek-ai/DeepSeek-V3.2 \ --tensor-parallel-size 8 \ --tokenizer-mode deepseek_v32 \ --tool-call-parser deepseek_v32 \ --enable-auto-tool-choice \ --reasoning-parser deepseek_v3 \ --speculative_config '{"num_speculative_tokens":1, "method":"deepseek_mtp"}' ``` 2. Run the benchmark with: ``` vllm bench serve \ --dataset-name random \ --random-input-len 1000 \ --random-prefix-len 0 \ --random-output-len 1000 \ --random-range-ratio 0 \ --base-url http://127.0.0.1:8000 \ --model deepseek-ai/DeepSeek-V3.2 \ --num-prompts 128 \ --max-concurrency 8 \ --ignore-eos ``` ## Expected Behavior Acceptance rate should be much higher. ## Actual Behavior Benchmark results show: ``` ============ Serving Benchmark Result ============ Successful requests: 128 Failed requests: 0 Maximum request concurrency: 8 Benchmark duration (s): 493.11 Total input tokens: 128000 Total generated tokens: 128000 Request throughput (req/s): 0.26 Output token throughput (tok/s): 259.58 Peak output token throughput (tok/s): 261.00 Peak concurrent requests: 11.00 Total token thro...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: "num_speculative_tokens":1, "method":"deepseek_mtp"}' ``` 2. Run the benchmark with: ``` vllm bench serve \ --dataset-name random \ --random-input-len 1000 \ --random-prefix-len 0 \ --random-output-len 1000 \ --random-r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Low acceptance rate for DeepSeek-V3.2 with `deepseek_mtp` speculative method in v0.15.0 bug ### Your current environment ### 🐛 Describe the bug ## Steps to Reproduce 1. Start the vLLM server with the following co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ol-choice \ --reasoning-parser deepseek_v3 \ --speculative_config '{"num_speculative_tokens":1, "method":"deepseek_mtp"}' ``` 2. Run the benchmark with: ``` vllm bench serve \ --dataset-name random \ --random-input-len...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: bug ### Your current environment ### 🐛 Describe the bug ## Steps to Reproduce 1. Start the vLLM server with the following command: ``` vllm serve deepseek-ai/DeepSeek-V3.2 \ --tensor-parallel-size 8 \ --tokenizer-mode d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
