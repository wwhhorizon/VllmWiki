# vllm-project/vllm#19888: [Performance]: the performance decline in fp8 inference mode

| 字段 | 值 |
| --- | --- |
| Issue | [#19888](https://github.com/vllm-project/vllm/issues/19888) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: the performance decline in fp8 inference mode

### Issue 正文摘录

### Proposal to improve performance I found currently the format of fp8 quantization in vllm is per-tensor, which may cause the performance decline in llm. So I wonder if vllm has supported or plan to support a fine-grained fp8 in the future, for example the tile-wise quantization. ### Report of performance regression I use a dataset of encyclopedic knowledge to test the Qwen2.5-7B with vllm, and found the performance of the model decreased heavily with quantization=fp8. Here is my prompt: `Prompt: " \nYou are a helpful assistant that can solve the given question step by step with the help of the wikipedia search tool. Given a question, you need to first think about the reasoning process in the mind and then provide the answer. During thinking, you can invoke the wikipedia search tool to search for fact information about specific topics if needed. The reasoning process and answer are enclosed within and tags respectively, and the search query and result are enclosed within and tags respectively. For example, This is the reasoning process. search query here search result here This is the reasoning process. The final answer is \\[ \\boxed{answer here} \\] . In the last part of the a...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Performance]: the performance decline in fp8 inference mode performance;stale ### Proposal to improve performance I found currently the format of fp8 quantization in vllm is per-tensor, which may cause the performance...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ormance;stale ### Proposal to improve performance I found currently the format of fp8 quantization in vllm is per-tensor, which may cause the performance decline in llm. So I wonder if vllm has supported or plan to supp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: invoke the wikipedia search tool to search for fact information about specific topics if needed. The reasoning process and answer are enclosed within and tags respectively, and the search query and result are enclosed w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ture, for example the tile-wise quantization. ### Report of performance regression I use a dataset of encyclopedic knowledge to test the Qwen2.5-7B with vllm, and found the performance of the model decreased heavily wit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n solve the given question step by step with the help of the wikipedia search tool. Given a question, you need to first think about the reasoning process in the mind and then provide the answer. During thinking, you can...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
