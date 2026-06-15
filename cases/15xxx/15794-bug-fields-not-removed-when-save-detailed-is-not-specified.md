# vllm-project/vllm#15794: [Bug]: Fields not removed when save_detailed is not specified

| 字段 | 值 |
| --- | --- |
| Issue | [#15794](https://github.com/vllm-project/vllm/issues/15794) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Fields not removed when save_detailed is not specified

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Run the benchmark without --save-detailed ```Bash python benchmark_serving.py --model base --tokenizer ~/DeepSeek-R1-Distill-Qwen-7B/ --dataset-name random --random-input-len 20 --random-output-len 128 --random-range-ratio 1.0 --ignore-eos --num-prompts 1 --save-result --result_dir ~/ ``` Based on the code: ```Python if not args.save_detailed: # Remove fields with too many data points for field in [ "input_lens", "output_lens", "ttfts", "itls", "generated_texts", "errors" ]: if field in result_json: del result_json[field] ``` These fields should be removed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: benchmark without --save-detailed ```Bash python benchmark_serving.py --model base --tokenizer ~/DeepSeek-R1-Distill-Qwen-7B/ --dataset-name random --random-input-len 20 --random-output-len 128 --random-range-ratio 1.0...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: g;stale ### Your current environment ### 🐛 Describe the bug Run the benchmark without --save-detailed ```Bash python benchmark_serving.py --model base --tokenizer ~/DeepSeek-R1-Distill-Qwen-7B/ --dataset-name random --r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Fields not removed when save_detailed is not specified bug;stale ### Your current environment ### 🐛 Describe the bug Run the benchmark without --save-detailed ```Bash python benchmark_serving.py --model base --to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Fields not removed when save_detailed is not specified bug;stale ### Your current environment ### 🐛 Describe the bug Run the benchmark without --save-detailed ```Bash python benchmark_serving.py --model base --to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
