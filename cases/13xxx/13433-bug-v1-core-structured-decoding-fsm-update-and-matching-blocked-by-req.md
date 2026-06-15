# vllm-project/vllm#13433: [Bug]: [V1][Core] Structured decoding - FSM update and matching blocked by request status

| 字段 | 值 |
| --- | --- |
| Issue | [#13433](https://github.com/vllm-project/vllm/issues/13433) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [V1][Core] Structured decoding - FSM update and matching blocked by request status

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Guided decoding for version V1 (related to #12388 ) does not advance the FSM when we use xgrammar as the backed. This then leads to guided decoding being disabled for subsequent steps. The reason for Guided decoding being skipped is because _is_gramma_ready return True only when the request is waiting and not when its running. There is a change needed in in the request.py [snippet ](https://github.com/vllm-project/vllm/pull/12388/files#diff-35f85e99eae8897d78a45f6a8d21bb69f9d8fe4a51e072bf299118dadac612f3R209) . So that the _is_grammar_ready is True even when we have the request in the Running stage. This would help update the states and accept tokens [here](https://github.com/vllm-project/vllm/pull/12388/files#diff-80ee7e2a62f9dcfbb8a312dc4e3948557e97ef187290daebbcae1e28596bda29R354) To run the Code (run this code after after you resolve the issue #13429 is fixed (I had an hacky solution for that issue. will soon post a clean version if) ): ```from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = Samplin...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ug]: [V1][Core] Structured decoding - FSM update and matching blocked by request status bug;stale ### Your current environment ### 🐛 Describe the bug Guided decoding for version V1 (related to #12388 ) does not advance...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Your current environment ### 🐛 Describe the bug Guided decoding for version V1 (related to #12388 ) does not advance the FSM when we use xgrammar as the backed. This then leads to guided decoding being disabled for subs...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: [V1][Core] Structured decoding - FSM update and matching blocked by request status bug;stale ### Your current environment ### 🐛 Describe the bug Guided decoding for version V1 (related to #12388 ) does not advanc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Grammar.builtin_json_grammar(), backend="xgrammar")) llm = LLM(model="MODEL OF YOUR CHOICE") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: [V1][Core] Structured decoding - FSM update and matching blocked by request status bug;stale ### Your current environment ### 🐛 Describe the bug Guided decoding for version V1 (related to #12388 ) does not advanc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
