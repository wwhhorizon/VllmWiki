# vllm-project/vllm#22048: [Bug]: Deploying the qwen3-reranker and qwen3-embedding model services using vllm, the service performance is poor. It seems that requests are still processed serially and cannot be handled concurrently?

| 字段 | 值 |
| --- | --- |
| Issue | [#22048](https://github.com/vllm-project/vllm/issues/22048) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Deploying the qwen3-reranker and qwen3-embedding model services using vllm, the service performance is poor. It seems that requests are still processed serially and cannot be handled concurrently?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug as the title said, after deploying the qwen3-reranker and qwen3-embedding model services using vllm, the service performance is poor. It seems that requests are still processed serially and cannot be handled concurrently, which is significantly different from the performance of llm services. What could be the reason for this? the qwen3-embedding cmd is vllm serve $model_path --port 9850 --served-model-name "qwen3-embedding-0.6b" --task embed --gpu-memory-utilization 0.7 --enable-prefix-caching ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Deploying the qwen3-reranker and qwen3-embedding model services using vllm, the service performance is poor. It seems that requests are still processed serially and cannot be handled concurrently? bug ### Your cu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ing ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: odel services using vllm, the service performance is poor. It seems that requests are still processed serially and cannot be handled concurrently? bug ### Your current environment ### 🐛 Describe the bug as the title sai...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
