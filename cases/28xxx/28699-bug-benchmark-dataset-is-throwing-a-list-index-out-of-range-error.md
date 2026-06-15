# vllm-project/vllm#28699: [Bug]: benchmark_dataset is throwing a ‘list index out of range’ error.

| 字段 | 值 |
| --- | --- |
| Issue | [#28699](https://github.com/vllm-project/vllm/issues/28699) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: benchmark_dataset is throwing a ‘list index out of range’ error.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I used the ShareGPT dataset, and `clien.sh` is written as follows: `python3 …` python3 /home/VLLM/vllm/benchmarks/benchmark_serving.py \ --host 127.0.0.1 --port 28804 \ --dataset-name sharegpt \ --dataset-path /home/VLLM/my_data/ShareGPT_V3_unfiltered_cleaned_split.json \ --model /home/huggingface/models/Qwen/Qwen3-32B \ --served_model_name Qwen3-32B \ --num-prompts ${1} \ --trust-remote-code \ --ignore-eos \ --sharegpt-output-len ${2048} \ --top-p 1 \ --top-k -1 \ --temperature 0 Then the error message is as follows: Traceback (most recent call last): File "/home/VLLM/vllm/benchmarks/benchmark_serving.py", line 1200, in main(args) File "/home/VLLM/vllm/benchmarks/benchmark_serving.py", line 740, in main input_requests = dataset_mapping[args.dataset_name]() ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/VLLM/vllm/benchmarks/benchmark_serving.py", line 721, in ).sample( ^^^^^^^ File "/home/VLLM/vllm/benchmarks/benchmark_dataset.py", line 450, in sample self.maybe_oversample_requests(samples, num_requests) File "/home/VLLM/vllm/benchmarks/benchmark_dataset.py", line 194, in maybe_oversample_requests additional = random.choices(re...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: et-path /home/VLLM/my_data/ShareGPT_V3_unfiltered_cleaned_split.json \ --model /home/huggingface/models/Qwen/Qwen3-32B \ --served_model_name Qwen3-32B \ --num-prompts ${1} \ --trust-remote-code \ --ignore-eos \ --shareg...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: g]: benchmark_dataset is throwing a ‘list index out of range’ error. bug;stale ### Your current environment ### 🐛 Describe the bug I used the ShareGPT dataset, and `clien.sh` is written as follows: `python3 …` python3 /...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: benchmark_dataset is throwing a ‘list index out of range’ error. bug;stale ### Your current environment ### 🐛 Describe the bug I used the ShareGPT dataset, and `clien.sh` is written as follows: `python3 …` python...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nge ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ks/benchmark_serving.py", line 740, in main input_requests = dataset_mapping[args.dataset_name]() ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/VLLM/vllm/benchmarks/benchmark_serving.py", line 721, in ).sample( ^^^^^...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
