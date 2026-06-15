# vllm-project/vllm#36155: [RFC]: dLLM support via plugin (spec-decode path reuse)

| 字段 | 值 |
| --- | --- |
| Issue | [#36155](https://github.com/vllm-project/vllm/issues/36155) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: dLLM support via plugin (spec-decode path reuse)

### Issue 正文摘录

### Motivation. Authors: Alon Kellner ([akellner@redhat.com](mailto:akellner@redhat.com)) & Tomer Garber ([tgarber@redhat.com](mailto:tgarber@redhat.com)) --- ## Summary This RFC adds block-based diffusion language model (dLLM) support in vLLM via the plugin system by **reusing the existing spec-decode data path and scheduler interface**. One engine change—calling the draft-token hook after every step when the model was executed, not only when speculative decoding is enabled—lets a plugin supply a custom scheduler, worker, and model that implement full dLLM semantics (variable **Committed** tokens, including commit-0) with **maximal encapsulation** and no new core types. The cost is overloading existing spec-decode fields when the plugin stack is used; this document states that reliance and the intended contract explicitly. --- ## Motivation Block-based dLLMs are gaining traction: they offer strong quality/speed tradeoffs, and recent benchmarks show large throughput or latency gains versus autoregressive LLMs (e.g. [WeDLM](https://arxiv.org/abs/2512.22737), [LLaDA2.1](https://arxiv.org/abs/2602.08676), [dInfer](https://arxiv.org/abs/2510.08666)). Major vLLM competitors ([SGlang](h...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [RFC]: dLLM support via plugin (spec-decode path reuse) RFC ### Motivation. Authors: Alon Kellner ([akellner@redhat.com](mailto:akellner@redhat.com)) & Tomer Garber ([tgarber@redhat.com](mailto:tgarber@redhat.com)) ---...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: hat.com)) --- ## Summary This RFC adds block-based diffusion language model (dLLM) support in vLLM via the plugin system by **reusing the existing spec-decode data path and scheduler interface**. One engine change—calli...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: gaining traction: they offer strong quality/speed tradeoffs, and recent benchmarks show large throughput or latency gains versus autoregressive LLMs (e.g. [WeDLM](https://arxiv.org/abs/2512.22737), [LLaDA2.1](https://ar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: lmdeploy/blob/main/lmdeploy/pytorch/models/sdar.py)) already support or ship dLLM-style inference. Adding dLLM support in vLLM keeps the ecosystem aligned and preserves **extensibility**: new architectures ([WeDLM](http...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: asked Draft** or **Decoded Draft**, or **Committed** to the sequence and KV cache. The unit of work is a **block** of fixed size (`DRAFT_SIZE`). ```mermaid flowchart LR subgraph AR [Autoregressive] direction LR A1[Step]...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
