# vllm-project/vllm#38697: [Performance]: llmcompressor W8A8 Inference: decoding stage speed is lower than FP16

| 字段 | 值 |
| --- | --- |
| Issue | [#38697](https://github.com/vllm-project/vllm/issues/38697) |
| 状态 | open |
| 标签 | performance |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: llmcompressor W8A8 Inference: decoding stage speed is lower than FP16

### Issue 正文摘录

### Proposal to improve performance May be a new kernel. ### Report of performance regression I found a performance problem in llmcompressor https://github.com/vllm-project/llm-compressor/issues/2549 I examine the trace in perfetto and find that the root cause is W8A8 kernel is slower than FP16 in decoding stage (25us vs 16us). In the smoothquant paper, decoding stage should have 1.35x on OPT-30B with bsz=1, seqlen=512. ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nel is slower than FP16 in decoding stage (25us vs 16us). In the smoothquant paper, decoding stage should have 1.35x on OPT-30B with bsz=1, seqlen=512. ### Misc discussion on performance _No response_ ### Your current e...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: to improve performance May be a new kernel. ### Report of performance regression I found a performance problem in llmcompressor https://github.com/vllm-project/llm-compressor/issues/2549 I examine the trace in perfetto...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: slower than FP16 in decoding stage (25us vs 16us). In the smoothquant paper, decoding stage should have 1.35x on OPT-30B with bsz=1, seqlen=512. ### Misc discussion on performance _No response_ ### Your current environm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
