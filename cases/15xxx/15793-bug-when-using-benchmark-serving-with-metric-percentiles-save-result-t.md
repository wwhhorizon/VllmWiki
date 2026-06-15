# vllm-project/vllm#15793: [Bug]: When using benchmark_serving with --metric-percentiles & --save-result, there is KeyError in save_to_pytorch_benchmark_format

| 字段 | 值 |
| --- | --- |
| Issue | [#15793](https://github.com/vllm-project/vllm/issues/15793) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When using benchmark_serving with --metric-percentiles & --save-result, there is KeyError in save_to_pytorch_benchmark_format

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Environment ```bash # Start vLLM server vllm serve ~/DeepSeek-R1-Distill-Qwen-7B/ --served-model-name base ``` ```bash # Run benchmark python3 vllm/benchmarks/benchmark_serving.py \ --model base \ --tokenizer ~/DeepSeek-R1-Distill-Qwen-7B/ \ --dataset-name random \ --random-input-len 20 \ --random-output-len 128 \ --random-range-ratio 1.0 \ --ignore-eos \ --num-prompts 1000 \ --metric-percentiles 25,50,75 \ --save-result \ --result_dir ~/ ``` When using custom metric percentiles (e.g., `--metric-percentiles 25,50,75`), the code fails with `KeyError: 'p99_ttft_ms'` because it hardcodes p99 metrics in the save function. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: centiles & --save-result, there is KeyError in save_to_pytorch_benchmark_format bug;stale ### Your current environment ### 🐛 Describe the bug ## Environment ```bash # Start vLLM server vllm serve ~/DeepSeek-R1-Distill-Q...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: When using benchmark_serving with --metric-percentiles & --save-result, there is KeyError in save_to_pytorch_benchmark_format bug;stale ### Your current environment ### 🐛 Describe the bug ## Environment ```bash #...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: --save-result, there is KeyError in save_to_pytorch_benchmark_format bug;stale ### Your current environment ### 🐛 Describe the bug ## Environment ```bash # Start vLLM server vllm serve ~/DeepSeek-R1-Distill-Qwen-7B/ --s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
