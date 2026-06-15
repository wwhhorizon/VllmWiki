# vllm-project/vllm#39790: [Performance]: Significant TTFT Regression with Speculative Decoding (EAGLE3)

| 字段 | 值 |
| --- | --- |
| Issue | [#39790](https://github.com/vllm-project/vllm/issues/39790) |
| 状态 | open |
| 标签 | performance |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Significant TTFT Regression with Speculative Decoding (EAGLE3)

### Issue 正文摘录

### Proposal to improve performance When enabling speculative decoding (tested with both EAGLE3 and DFlash methods), I observe a substantial increase in Time-To-First-Token (TTFT), particularly at the P99 percentile. While the expected improvement in Time-Per-Output-Token (TPOT) is confirmed, the TTFT degradation appears to be an inherent overhead of the speculative decoding process that might be more pronounced than previously understood. ### Report of performance regression I started a vLLM server with a target model and enable a draft model via --speculative-config. **Example for EAGLE3 on GPU:** ```bash vllm serve /path/to/Qwen3-8B \ --served-model-name qwen3-8b \ --port 8188 \ --enforce-eager \ --speculative-config '{"method": "eagle3", "model": "/path/to/Qwen3-8B-speculator.eagle3", "num_speculative_tokens": 15}' ``` Then I ran a benchmark using the vllm bench serve command with a custom dataset (MATH-500): ```bash vllm bench serve \ --model /path/to/Qwen3-8B \ --base-url http://127.0.0.1:8188 \ --served-model-name qwen3-8b \ --dataset-name custom \ --dataset-path /path/to/dataset.jsonl \ --num-prompts 50 \ --max-concurrency 1 \ --temperature 0 ``` **Baseline (No Speculative...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Performance]: Significant TTFT Regression with Speculative Decoding (EAGLE3) performance ### Proposal to improve performance When enabling speculative decoding (tested with both EAGLE3 and DFlash methods), I observe a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Report of performance regression I started a vLLM server with a target model and enable a draft model via --speculative-config. **Example for EAGLE3 on GPU:** ```bash vllm serve /path/to/Qwen3-8B \ --served-model-name q...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: Significant TTFT Regression with Speculative Decoding (EAGLE3) performance ### Proposal to improve performance When enabling speculative decoding (tested with both EAGLE3 and DFlash methods), I observe a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: del ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
