# vllm-project/vllm#319: Question regarding PagedAttention Layer and Attention Processing for Batches

| 字段 | 值 |
| --- | --- |
| Issue | [#319](https://github.com/vllm-project/vllm/issues/319) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Question regarding PagedAttention Layer and Attention Processing for Batches

### Issue 正文摘录

Hello, I would like to inquire about the behavior of the PagedAttention Layer. Upon reviewing its implementation, it appears that the layer processes all requests in a batch collectively, utilizing a single kernel. This raises a concern for me as it doesn’t seem to adopt a splitting mechanism prior to processing the attention operation. To provide context, the ORCA paper, presented at OSDI 2022 ([link](https://www.usenix.org/conference/osdi22/presentation/yu)), introduces a split mechanism which enables selective batching or iteration-level scheduling. This mechanism ensures that each request within a batch pays attention solely to its own set of sentences. In contrast, without employing such a splitting approach, there is a potential issue where requests within the batch (other than the first one) would inadvertently pay attention not only to their own sentences but also to unrelated sentences belonging to other requests. I have empirically observed the repercussions of this behavior: I conducted a benchmark test using the benchmark_throughput script, and it was evident that the output text yielded divergent results depending on whether I executed it with a single prompt versus w...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: operation. To provide context, the ORCA paper, presented at OSDI 2022 ([link](https://www.usenix.org/conference/osdi22/presentation/yu)), introduces a split mechanism which enables selective batching or iteration-level...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: e empirically observed the repercussions of this behavior: I conducted a benchmark test using the benchmark_throughput script, and it was evident that the output text yielded divergent results depending on whether I exe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s raises a concern for me as it doesn’t seem to adopt a splitting mechanism prior to processing the attention operation. To provide context, the ORCA paper, presented at OSDI 2022 ([link](https://www.usenix.org/conferen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: y --dataset ShareGPT_V3_unfiltered_cleaned_split.json --num-prompts 1 --model='facebook/opt-1.3b' # Ouput prompt "for my characters world.\n> no plot Can you elaborate? Cognizant Q4 profit up 10 pct, parts revenue growt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: on reviewing its implementation, it appears that the layer processes all requests in a batch collectively, utilizing a single kernel. This raises a concern for me as it doesn’t seem to adopt a splitting mechanism prior...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
