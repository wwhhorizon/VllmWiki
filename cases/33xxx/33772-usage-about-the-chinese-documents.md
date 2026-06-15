# vllm-project/vllm#33772: [Usage]: about the Chinese documents

| 字段 | 值 |
| --- | --- |
| Issue | [#33772](https://github.com/vllm-project/vllm/issues/33772) |
| 状态 | open |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: about the Chinese documents

### Issue 正文摘录

### Your current environment Hi team, First of all, thanks for developing vLLM, which is an efficient and easy-to-use LLM inference library that has greatly facilitated my work. I recently accessed the document site at **`https://docs.vllm.com.cn/en/latest`** and found that it contains detailed Chinese and English documentation of vLLM (the latest update time marked on the site is November 15, 2025). The content covers core features such as PagedAttention, quantization support, and hardware compatibility, which is very helpful for developers who need to use vLLM in Chinese environments. I would like to consult two questions: 1. Is the `https://docs.vllm.com.cn` site an **official maintained documentation site** for vLLM? Or is it a third-party mirrored site? 2. If I want to obtain the **static content of this site** (such as HTML files, Markdown source code, or build scripts) for offline browsing, secondary sorting, or internal deployment in the enterprise, what is the recommended way to do so? Looking forward to your reply. Thanks again for your efforts in maintaining vLLM! ### How would you like to use vllm none ### Before submitting a new issue... - [x] Make sure you already se...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ent Hi team, First of all, thanks for developing vLLM, which is an efficient and easy-to-use LLM inference library that has greatly facilitated my work. I recently accessed the document site at **`https://docs.vllm.com....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: mber 15, 2025). The content covers core features such as PagedAttention, quantization support, and hardware compatibility, which is very helpful for developers who need to use vLLM in Chinese environments. I would like...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: one ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: about the Chinese documents usage;stale ### Your current environment Hi team, First of all, thanks for developing vLLM, which is an efficient and easy-to-use LLM inference library that has greatly facilitated m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: recently accessed the document site at **`https://docs.vllm.com.cn/en/latest`** and found that it contains detailed Chinese and English documentation of vLLM (the latest update time marked on the site is November 15, 20...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
