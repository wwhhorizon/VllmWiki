# vllm-project/vllm#5898: [Bug]: Inconsistent Responses with VLLM When Batch Size > 1 even temperature = 0

| 字段 | 值 |
| --- | --- |
| Issue | [#5898](https://github.com/vllm-project/vllm/issues/5898) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 46; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Inconsistent Responses with VLLM When Batch Size > 1 even temperature = 0

### Issue 正文摘录

### 🐛 Describe the bug Test Environment: - Hardware: A100 80GB GPU - Model: Llama3-8b **- Parameters: temperature = 0, max_tokens = 1024, max_num_seqs = 256, seed=1** - I make OpenAI-Compatilbe Server using python -m vllm.entrypoints.openai.api_server ... Test Method: - First, requests were sent one at a time to verify if the same prompt consistently produces the same response. - Second, more than one requests with same prompt at a time were sent to verify if the same prompt consistently produces the same response. Discovered Issue: **- Consistency with Single Request: When the batch size is 1, the same prompt consistently produces the same response.** **- Inconsistency with Multiple Requests: When the batch size increases to more than 1, the responses for the same prompt become inconsistent.** - When I set vllm server with parameter max_num_seqs = 1, the result is all same I think this suggests that the issue arises from the way the Batch Scheduler processes multiple requests together. My problem is similar with others https://github.com/vllm-project/vllm/issues/3544 https://github.com/vllm-project/vllm/issues/4606 https://github.com/vllm-project/vllm/issues/608

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: stent Responses with VLLM When Batch Size > 1 even temperature = 0 bug;unstale ### 🐛 Describe the bug Test Environment: - Hardware: A100 80GB GPU - Model: Llama3-8b **- Parameters: temperature = 0, max_tokens = 1024, ma...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: le ### 🐛 Describe the bug Test Environment: - Hardware: A100 80GB GPU - Model: Llama3-8b **- Parameters: temperature = 0, max_tokens = 1024, max_num_seqs = 256, seed=1** - I make OpenAI-Compatilbe Server using python -m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: re = 0 bug;unstale ### 🐛 Describe the bug Test Environment: - Hardware: A100 80GB GPU - Model: Llama3-8b **- Parameters: temperature = 0, max_tokens = 1024, max_num_seqs = 256, seed=1** - I make OpenAI-Compatilbe Server...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Batch Size > 1 even temperature = 0 bug;unstale ### 🐛 Describe the bug Test Environment: - Hardware: A100 80GB GPU - Model: Llama3-8b **- Parameters: temperature = 0, max_tokens = 1024, max_num_seqs = 256, seed=1** - I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
