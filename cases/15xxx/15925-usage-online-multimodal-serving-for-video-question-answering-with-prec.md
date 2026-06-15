# vllm-project/vllm#15925: [Usage]: online multimodal serving for video question answering with precomputed vision tokens (stored on the disk).

| 字段 | 值 |
| --- | --- |
| Issue | [#15925](https://github.com/vllm-project/vllm/issues/15925) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: online multimodal serving for video question answering with precomputed vision tokens (stored on the disk).

### Issue 正文摘录

### Your current environment Python 3.10 ### How would you like to use vllm Hello guys, I am using vLLM to serve the LLaVa-Next-7B model in an online mode for video understanding tasks. Since the video loading and embedding process takes a long time, I use the model's vision encoder to precompute the vision token of the video and store it on the disk. How can I modify the code so that I can directly load the embedding during online serving, e.g., send a request with the user question and the disk path of the video embedding to the LLM server, or is there a better way to do that? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: online multimodal serving for video question answering with precomputed vision tokens (stored on the disk). usage;stale ### Your current environment Python 3.10 ### How would you like to use vllm Hello guys, I...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ion answering with precomputed vision tokens (stored on the disk). usage;stale ### Your current environment Python 3.10 ### How would you like to use vllm Hello guys, I am using vLLM to serve the LLaVa-Next-7B model in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: at? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
