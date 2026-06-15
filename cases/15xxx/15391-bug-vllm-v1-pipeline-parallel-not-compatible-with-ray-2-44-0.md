# vllm-project/vllm#15391: [Bug]: vllm V1 pipeline parallel not compatible with ray==2.44.0

| 字段 | 值 |
| --- | --- |
| Issue | [#15391](https://github.com/vllm-project/vllm/issues/15391) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm V1 pipeline parallel not compatible with ray==2.44.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm attempting to deploy the llama3-70B model using 8 H20 GPUs (TP2, PP4) with vllm V1 and ray backend. The codes run successfully under `ray==2.43.0`, but encounter `cudaErrorIllegalAddress` when upgraded to `ray==2.44.0` (released 3 days ago). To reproduce the error: ``` VLLM_USE_V1=1 vllm serve Llama-3.1-70B -tp 2 -pp 4 --distributed-executor-backend="ray" --no-enable-prefix-caching ``` ``` python vllm/benchmarks/benchmark_serving.py --backend vllm --model Llama-3.1-70B --dataset-name sharegpt --dataset-path ShareGPT_V3_unfiltered_cleaned_split.json --num-prompts 200 ``` Error detail: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: backend. The codes run successfully under `ray==2.43.0`, but encounter `cudaErrorIllegalAddress` when upgraded to `ray==2.44.0` (released 3 days ago). To reproduce the error: ``` VLLM_USE_V1=1 vllm serve Llama-3.1-70B -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ent environment ### 🐛 Describe the bug I'm attempting to deploy the llama3-70B model using 8 H20 GPUs (TP2, PP4) with vllm V1 and ray backend. The codes run successfully under `ray==2.43.0`, but encounter `cudaErrorIlle...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ed-executor-backend="ray" --no-enable-prefix-caching ``` ``` python vllm/benchmarks/benchmark_serving.py --backend vllm --model Llama-3.1-70B --dataset-name sharegpt --dataset-path ShareGPT_V3_unfiltered_cleaned_split.j...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: oy the llama3-70B model using 8 H20 GPUs (TP2, PP4) with vllm V1 and ray backend. The codes run successfully under `ray==2.43.0`, but encounter `cudaErrorIllegalAddress` when upgraded to `ray==2.44.0` (released 3 days a...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: llegalAddress` when upgraded to `ray==2.44.0` (released 3 days ago). To reproduce the error: ``` VLLM_USE_V1=1 vllm serve Llama-3.1-70B -tp 2 -pp 4 --distributed-executor-backend="ray" --no-enable-prefix-caching ``` ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
