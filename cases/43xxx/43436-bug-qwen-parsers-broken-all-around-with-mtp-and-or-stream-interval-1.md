# vllm-project/vllm#43436: [Bug]: Qwen parsers broken all around with MTP and/or stream-interval > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#43436](https://github.com/vllm-project/vllm/issues/43436) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen parsers broken all around with MTP and/or stream-interval > 1

### Issue 正文摘录

### Your current environment vllm-0.21.1rc1.dev180+gc68c55d43-cp38-abi3-manylinux_2_28_x86_64.whl ### 🐛 Describe the bug There is a lot of fixes to parsers these days, including active ongoing work in Gemma. This all is also related to Qwen parsers, where with MTP (which implies multiple tokens at a time), or with stream-interval more than 1, or even without both, is broken as of now in multiple ways in streaming mode. 1) last tokens of reasoning blocks got lost. It is in effect even without MTP or interval more than 1, it was here for months already. 2) case 1 It can be so severe that &lt;/think&gt; itself is lost, and reasoning+content parts, combined, do not form complete &lt;/think&gt; at all - this is new to MTP, but a subset of 1 actually as it seems. 3) reasoning -> content transition can be absolutely random: a) start of &lt;/think&gt; in reasoning chunk, end in first content chunk b) all &lt;/think&gt; in content chunk c) end of reasoning (!) with &lt;/think&gt; - in first content chunk d) all the above including missing/broken &lt;/think&gt;, see 1 & 2 4) tool call missing argument value (parsed as empty argument) - like in Gemma parser issue nearby, absolutely the same...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen parsers broken all around with MTP and/or stream-interval > 1 bug ### Your current environment vllm-0.21.1rc1.dev180+gc68c55d43-cp38-abi3-manylinux_2_28_x86_64.whl ### 🐛 Describe the bug There is a lot of fi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: of now in multiple ways in streaming mode. 1) last tokens of reasoning blocks got lost. It is in effect even without MTP or interval more than 1, it was here for months already. 2) case 1 It can be so severe that &lt;/t...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: s a lot of fixes to parsers these days, including active ongoing work in Gemma. This all is also related to Qwen parsers, where with MTP (which implies multiple tokens at a time), or with stream-interval more than 1, or...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
