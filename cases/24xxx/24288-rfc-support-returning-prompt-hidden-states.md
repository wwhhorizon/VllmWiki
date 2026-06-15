# vllm-project/vllm#24288: [RFC]: Support Returning Prompt Hidden States

| 字段 | 值 |
| --- | --- |
| Issue | [#24288](https://github.com/vllm-project/vllm/issues/24288) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support Returning Prompt Hidden States

### Issue 正文摘录

### Motivation. Hidden states are a valuable feature for many downstream applications, and their support has been requested and discussed in the vLLM community for a while(https://github.com/vllm-project/vllm/pull/15434 https://github.com/vllm-project/vllm/issues/4435 https://github.com/vllm-project/vllm/issues/6165 ) Currently, users who need both the prompt hidden states and the generated text must make two separate calls: LLM.encode (to obtain hidden states) and LLM.generate (to obtain generated text). This workflow is inconvenient and inefficient, especially for applications that require both outputs. The inability to return hidden states alongside generated text has also been highlighted in https://github.com/vllm-project/vllm/issues/12249 ### Proposed Change. This is a very initial draft PR: https://github.com/vllm-project/vllm/pull/24202. Will polish it after RFC. #### Configuration Add `return_prompt_hidden_states` in Sampling Config. There is prior discussion https://github.com/vllm-project/vllm/pull/15434#discussion_r2050595239 mentioning using such request-level parameter can't be handled well. In local testing, this approach appears feasible for prompt hidden states, b...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ble feature for many downstream applications, and their support has been requested and discussed in the vLLM community for a while(https://github.com/vllm-project/vllm/pull/15434 https://github.com/vllm-project/vllm/iss...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: oning using such request-level parameter can't be handled well. In local testing, this approach appears feasible for prompt hidden states, but feedback on potential disadvantages is welcome. #### How to build up prompt_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: rate (to obtain generated text). This workflow is inconvenient and inefficient, especially for applications that require both outputs. The inability to return hidden states alongside generated text has also been highlig...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: github.com/vllm-project/vllm/pull/24202. Will polish it after RFC. #### Configuration Add `return_prompt_hidden_states` in Sampling Config. There is prior discussion https://github.com/vllm-project/vllm/pull/15434#discu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
