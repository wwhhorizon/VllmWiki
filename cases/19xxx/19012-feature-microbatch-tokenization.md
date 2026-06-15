# vllm-project/vllm#19012: [Feature]: Microbatch Tokenization

| 字段 | 值 |
| --- | --- |
| Issue | [#19012](https://github.com/vllm-project/vllm/issues/19012) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Microbatch Tokenization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Tokenization is pretty slow (for concurrency=1, DGX H100's CPU can do about only about 1k tokens/ms), under high load, this becomes the performance bottleneck. In vLLM's API server today, we process each request's tokenization sequentialy: https://github.com/vllm-project/vllm/blob/b9f61e13875e1682d3982829006bec26981fde4d/vllm/entrypoints/openai/serving_engine.py#L222-L228 However, just by calling `tokenizer.__call__` with a list of string, significant speed up can be achieved. ``` In [22]: inp = "hi "*10000 In [23]: inp_batch = [inp]*16 In [24]: %timeit tokenizer(inp) 10.7 ms ± 135 μs per loop (mean ± std. dev. of 7 runs, 100 loops each) In [25]: %timeit tokenizer(inp_batch) 31.6 ms ± 407 μs per loop (mean ± std. dev. of 7 runs, 10 loops each) ``` There are several ways to speed this up. One approach is to set the thread pool to `N=number_of_cores`, however, @njhill pointed out that transformers's tokenizer actually don't release the GIL and it is not thread safe. The other alternative is to use process pool tokenizer. This has been explored in RayTokenizerGroup which is essentially an optimized version of this approach using Ray. However, t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: has been explored in RayTokenizerGroup which is essentially an optimized version of this approach using Ray. However, the serialization cost is still high. In this feature request, I propose refactoring the file's token...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: otivation and pitch Tokenization is pretty slow (for concurrency=1, DGX H100's CPU can do about only about 1k tokens/ms), under high load, this becomes the performance bottleneck. In vLLM's API server today, we process...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Microbatch Tokenization good first issue;feature request ### 🚀 The feature, motivation and pitch Tokenization is pretty slow (for concurrency=1, DGX H100's CPU can do about only about 1k tokens/ms), under hig...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: r ### Alternatives _No response_ ### Additional context This can be reproduced by running 1B models with long prompts as requests. ### Before submitting a new issue... - [x] Make sure you already searched for relevant i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: response_ ### Additional context This can be reproduced by running 1B models with long prompts as requests. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the ch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
