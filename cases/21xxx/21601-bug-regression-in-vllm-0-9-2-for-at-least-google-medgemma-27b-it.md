# vllm-project/vllm#21601: [Bug]: Regression in vllm 0.9.2 for (at least) google/medgemma-27b-it

| 字段 | 值 |
| --- | --- |
| Issue | [#21601](https://github.com/vllm-project/vllm/issues/21601) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Regression in vllm 0.9.2 for (at least) google/medgemma-27b-it

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug Using the same vllm arguments, upgrade from vllm 0.9.1 to vllm 0.9.2 seems to have negatively impacted the quality of output of [google/medgemma-27b-it](https://huggingface.co/google/medgemma-27b-it), with the model now being stuck in a loop, or outputting garbage content. vllm arguments: ``` --disable-fastapi-docs --disable-log-requests --gpu-memory-utilization 0.95 --max-model-len 58294 --max-num-seqs 256 --model google/medgemma-27b-it --port 8003 --quantization fp8 --served-model-name medgemma-27b-it google/medgemma-27b-it --uvicorn-log-level warning ``` Note: the same behavior occurs with or without the inflight quantization Question asked to the model: ``` How do you differentiate bacterial from viral pneumonia? ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Regression in vllm 0.9.2 for (at least) google/medgemma-27b-it bug ### Your current environment N/A ### 🐛 Describe the bug Using the same vllm arguments, upgrade from vllm 0.9.1 to vllm 0.9.2 seems to have negati...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: en 58294 --max-num-seqs 256 --model google/medgemma-27b-it --port 8003 --quantization fp8 --served-model-name medgemma-27b-it google/medgemma-27b-it --uvicorn-log-level warning ``` Note: the same behavior occurs with or...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Regression in vllm 0.9.2 for (at least) google/medgemma-27b-it bug ### Your current environment N/A ### 🐛 Describe the bug Using the same vllm arguments, upgrade from vllm 0.9.1 to vllm 0.9.2 seems to have negati...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Regression in vllm 0.9.2 for (at least) google/medgemma-27b-it bug ### Your current environment N/A ### 🐛 Describe the bug Using the same vllm arguments, upgrade from vllm 0.9.1 to vllm 0.9.2 seems to have negati...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
