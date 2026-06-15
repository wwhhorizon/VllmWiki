# vllm-project/vllm#41031: [Bug]: AssertionError in sampler.py:383

| 字段 | 值 |
| --- | --- |
| Issue | [#41031](https://github.com/vllm-project/vllm/issues/41031) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AssertionError in sampler.py:383

### Issue 正文摘录

### Your current environment **Summary:** During boundary fuzzing of the vLLM inference server (SDK AIC.1.22.0.62) using the SentinelFuzz tool, we identified a critical stability bug in the sampler component. Sending a single API request with prompt_logprobs=20 causes an AssertionError at sampler.py:383, which terminates the server process. All in-flight requests are killed. The server requires a manual restart to recover. This bug is present in open-source vLLM code and is reproducible 100% of the time. **File & Location** Repository: vllm-project/vllm (open source) File: vllm/model_executor/layers/sampler.py Line: 383 Error: AssertionError (assertion in logits accounting loop) Stack trace class: PROCESS_CRASH (no HTTP response — connection refused after crash) **How We Found It** This bug was discovered by SentinelFuzz, an boundary fuzzing tool that generates semantically-aware adversarial API requests targeting known parameter boundaries in the LLM inference pipeline. The tool's knowledge base identified prompt_logprobs as a parameter that interacts with the sampler's internal logits accounting loop and generated boundary-value test cases above the normally tested range. 1 |Sta...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: a critical stability bug in the sampler component. Sending a single API request with prompt_logprobs=20 causes an AssertionError at sampler.py:383, which terminates the server process. All in-flight requests are killed....
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: restart to recover. This bug is present in open-source vLLM code and is reproducible 100% of the time. **File & Location** Repository: vllm-project/vllm (open source) File: vllm/model_executor/layers/sampler.py Line: 38...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: File & Location** Repository: vllm-project/vllm (open source) File: vllm/model_executor/layers/sampler.py Line: 383 Error: AssertionError (assertion in logits accounting loop) Stack trace class: PROCESS_CRASH (no HTTP r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t to recover. This bug is present in open-source vLLM code and is reproducible 100% of the time. **File & Location** Repository: vllm-project/vllm (open source) File: vllm/model_executor/layers/sampler.py Line: 383 Erro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: , ) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
