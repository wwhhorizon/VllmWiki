# vllm-project/vllm#17661: [Bug]: Can't serve can we serve Q4_K_M-GGUF  Model

| 字段 | 值 |
| --- | --- |
| Issue | [#17661](https://github.com/vllm-project/vllm/issues/17661) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Can't serve can we serve Q4_K_M-GGUF  Model

### Issue 正文摘录

### Your current environment vllm 0.8.4 ### 🐛 Describe the bug can we serve this model using vllm? `NoelJacob/Meta-Llama-3-8B-Instruct-Q4_K_M-GGUF ` This didn't work: ``` VLLM_USE_V1=0 vllm serve NoelJacob/Meta-Llama-3-8B-Instruct-Q4_K_M-GGUF --max-model-len 4096 --gpu-memory-utilization 0.90 --distributed-executor-backend mp --hf-config-path meta-llama/Meta-Llama-3-8B-Instruct --tokenizer meta-llama/Meta-Llama-3-8B-Instruct --load-format gguf ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Can't serve can we serve Q4_K_M-GGUF Model bug;stale ### Your current environment vllm 0.8.4 ### 🐛 Describe the bug can we serve this model using vllm? `NoelJacob/Meta-Llama-3-8B-Instruct-Q4_K_M-GGUF ` This didn'...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ax-model-len 4096 --gpu-memory-utilization 0.90 --distributed-executor-backend mp --hf-config-path meta-llama/Meta-Llama-3-8B-Instruct --tokenizer meta-llama/Meta-Llama-3-8B-Instruct --load-format gguf ``` ### Before su...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Can't serve can we serve Q4_K_M-GGUF Model bug;stale ### Your current environment vllm 0.8.4 ### 🐛 Describe the bug can we serve this model using vllm? `NoelJacob/Meta-Llama-3-8B-Instruct-Q4_K_M-GGUF ` This didn'...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
