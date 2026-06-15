# vllm-project/vllm#37304: [Bug]: Language Models Test (Extended Generation) test_models[False-False-5-32-bigcode/starcoder2-3b] test issue

| 字段 | 值 |
| --- | --- |
| Issue | [#37304](https://github.com/vllm-project/vllm/issues/37304) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Language Models Test (Extended Generation) test_models[False-False-5-32-bigcode/starcoder2-3b] test issue

### Issue 正文摘录

### Your current environment main ### 🐛 Describe the bug I got the test to fail under the following two situations: 1. We're trying to upgrade PyTorch from 2.10 to 2.11. The test succeeds in PyTorch 2.10, but fails in PyTorch 2.11 ([logs](https://buildkite.com/vllm/ci/builds/56028#019ce7ae-eb9b-41be-90ae-310763ec6438)) 2. In PyTorch 2.10, if I add [--enforce-eager](https://github.com/vllm-project/vllm/blob/3717a4dd475e6a936df0c84b043743310368e766/tests/models/language/generation/test_common.py#L178), the test fails. The error message looks the same in both cases. ([logs](https://buildkite.com/vllm/ci/builds/56028#019ce7ae-eb9b-41be-90ae-310763ec6438)) ``` [2026-03-13T16:18:07Z] E AssertionError: Test1: -- [2026-03-13T16:18:07Z] E Matched tokens: [222, 40, 494, 447, 9009, 98, 828, 366] [2026-03-13T16:18:07Z] E hf: '\n# + [markdown] id="5f7o229v00-L"\n# **1950** - ' {59: -4.088154315948486, 58: -4.088154315948486, 56: -4.213154315948486, 55: -4.213154315948486, 54: -4.213154315948486} [2026-03-13T16:18:07Z] E vllm: '\n# + [markdown] id="68284477"\n# **1950**\n#\n# - ' {59: Logprob(logprob=-4.071040153503418, rank=1, decoded_token='6'), 56: Logprob(logprob=-4.196040153503418, rank=2,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test succeeds in PyTorch 2.10, but fails in PyTorch 2.11 ([logs](https://buildkite.com/vllm/ci/builds/56028#019ce7ae-eb9b-41be-90ae-310763ec6438)) 2. In PyTorch 2.10, if I add [--enforce-eager](https://github.com/vllm-p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Language Models Test (Extended Generation) test_models[False-False-5-32-bigcode/starcoder2-3b] test issue bug ### Your current environment main ### 🐛 Describe the bug I got the test to fail under the following tw...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: Language Models Test (Extended Generation) test_models[False-False-5-32-bigcode/starcoder2-3b] test issue bug ### Your current environment main ### 🐛 Describe the bug I got the test to fail under the following tw...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: re? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: test though. @hmellor I see you poked around at this file recently for Gemma and Gemma2. Do you have any thoughts here? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
