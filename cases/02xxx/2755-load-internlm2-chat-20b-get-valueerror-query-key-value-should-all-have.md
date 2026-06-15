# vllm-project/vllm#2755: Load internlm2-chat-20b get ValueError: Query/Key/Value should all have BMHK or BMK shape.

| 字段 | 值 |
| --- | --- |
| Issue | [#2755](https://github.com/vllm-project/vllm/issues/2755) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Load internlm2-chat-20b get ValueError: Query/Key/Value should all have BMHK or BMK shape.

### Issue 正文摘录

vllm==0.3.0 from vllm import LLM, SamplingParams llm = LLM( model="internlm/internlm2-chat-20b", gpu_memory_utilization=.85, max_model_len=2000 , trust_remote_code=True ) get ValueError: Query/Key/Value should all have BMHK or BMK shape. query.shape: torch.Size([1, 2048, 8, 6, 128]) key.shape : torch.Size([1, 2048, 8, 6, 128]) value.shape: torch.Size([1, 2048, 8, 6, 128])

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ey/Value should all have BMHK or BMK shape. stale vllm==0.3.0 from vllm import LLM, SamplingParams llm = LLM( model="internlm/internlm2-chat-20b", gpu_memory_utilization=.85, max_model_len=2000 , trust_remote_code=True...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: stale vllm==0.3.0 from vllm import LLM, SamplingParams llm = LLM( model="internlm/internlm2-chat-20b", gpu_memory_utilization=.85, max_model_len=2000 , trust_remote_code=True ) get ValueError: Query/Key/Value should all...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t-20b get ValueError: Query/Key/Value should all have BMHK or BMK shape. stale vllm==0.3.0 from vllm import LLM, SamplingParams llm = LLM( model="internlm/internlm2-chat-20b", gpu_memory_utilization=.85, max_model_len=2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
