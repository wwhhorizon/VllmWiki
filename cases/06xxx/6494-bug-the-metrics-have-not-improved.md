# vllm-project/vllm#6494: [Bug]: The metrics have not improved.

| 字段 | 值 |
| --- | --- |
| Issue | [#6494](https://github.com/vllm-project/vllm/issues/6494) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;scheduler_memory;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The metrics have not improved.

### Issue 正文摘录

### Your current environment VLLM is 0.5.0，A100 ， CUDA 12.1 ### 🐛 Describe the bug 1、 CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server \ --model /home/Qwen1.5-1.8B-Chat \ --gpu-memory-utilization 0.5 \ --enable-prefix-caching Metrics： num request: 2000 NUM ttft: 62.9838 ms tpot: 14.4647 ms avg_latency: 1567.14ms avg_throughput: 485.52tokens/s 2、 CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server \ --model /home/Qwen1.5-1.8B-Chat \ --gpu-memory-utilization 0.5 \ --enable-prefix-caching \ --speculative-model "[ngram]" \ --num-speculative-tokens 8 \ --use-v2-block-manager \ --ngram-prompt-lookup-max 8 \ --ngram-prompt-lookup-min 2 \ Metrics： num request: 2000 NUM ttft: 66.4831 ms tpot: 21.7066 ms avg_latency: 1360.00ms avg_throughput: 301.09tokens/s The version of VLLM is 0.5.0, on an A100 machine with CUDA 12.1. The metrics for versions 1 and 2 are being compared. I believe that version 2 should have improvements in all metrics, but currently, they have decreased instead. Why is that, and how should the parameters be adjusted?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: The metrics have not improved. bug;stale ### Your current environment VLLM is 0.5.0，A100 ， CUDA 12.1 ### 🐛 Describe the bug 1、 CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server \ --model /home/Q...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: --enable-prefix-caching Metrics： num request: 2000 NUM ttft: 62.9838 ms tpot: 14.4647 ms avg_latency: 1567.14ms avg_throughput: 485.52tokens/s 2、 CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server \ --m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t: 21.7066 ms avg_latency: 1360.00ms avg_throughput: 301.09tokens/s The version of VLLM is 0.5.0, on an A100 machine with CUDA 12.1. The metrics for versions 1 and 2 are being compared. I believe that version 2 should h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: have not improved. bug;stale ### Your current environment VLLM is 0.5.0，A100 ， CUDA 12.1 ### 🐛 Describe the bug 1、 CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server \ --model /home/Qwen1.5-1.8B-Chat \...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: \ --speculative-model "[ngram]" \ --num-speculative-tokens 8 \ --use-v2-block-manager \ --ngram-prompt-lookup-max 8 \ --ngram-prompt-lookup-min 2 \ Metrics： num request: 2000 NUM ttft: 66.4831 ms tpot: 21.7066 ms avg_la...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
