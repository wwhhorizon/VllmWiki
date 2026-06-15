# vllm-project/vllm#21796: [RFC]: Optimize embedding task

| 字段 | 值 |
| --- | --- |
| Issue | [#21796](https://github.com/vllm-project/vllm/issues/21796) |
| 状态 | open |
| 标签 | RFC;keep-open |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Optimize embedding task

### Issue 正文摘录

### Motivation. Since PR https://github.com/vllm-project/vllm/pull/21270 we now have full support for encoder embedding models. These models include not only the BERT-type models but also models such as Alibaba-NLP/gte-Qwen2-1.5B-instruct that are decoder models converted to encoder. Encoder models continue to be essential for information retrieval use cases such as RAG because their bidirectional attention gives them superior performance over decoder models with causal attention. vLLM stated mission is "Easy, fast, and cheap LLM serving for everyone". Embedding model serving has been easy since V0, but is it also fast? [Snowflake's excellent blog post](https://www.snowflake.com/en/engineering-blog/embedding-inference-arctic-16x-faster/) suggests otherwise. In it they show a series of optimizations that they did in their backend to 4x the throughput of seq len 512. While one of the optimizations is specific to their infrastructure where vLLM runs behind a gRPC frontend, the other optimizations suggest that there is room for improvement. There aren't many details about the specific vLLM version that was used as a baseline, but the model was Snowflake/snowflake-arctic-embed-m-v1.5,...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: to encoder. Encoder models continue to be essential for information retrieval use cases such as RAG because their bidirectional attention gives them superior performance over decoder models with causal attention. vLLM s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: m-project/vllm/pull/21270 we now have full support for encoder embedding models. These models include not only the BERT-type models but also models such as Alibaba-NLP/gte-Qwen2-1.5B-instruct that are decoder models con...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: els but also models such as Alibaba-NLP/gte-Qwen2-1.5B-instruct that are decoder models converted to encoder. Encoder models continue to be essential for information retrieval use cases such as RAG because their bidirec...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: o 4x the throughput of seq len 512. While one of the optimizations is specific to their infrastructure where vLLM runs behind a gRPC frontend, the other optimizations suggest that there is room for improvement. There ar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: U tasks As noted in the Snowflake blog, most embedding models are quite small and since they don't support optimizations such as chunked prefill, the GPU utilization could be sub-optimal. In their case they solved it ru...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
