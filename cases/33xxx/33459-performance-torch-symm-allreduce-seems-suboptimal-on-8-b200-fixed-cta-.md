# vllm-project/vllm#33459: [Performance]: Torch symm AllReduce seems suboptimal on 8×B200 (fixed CTA count?)

| 字段 | 值 |
| --- | --- |
| Issue | [#33459](https://github.com/vllm-project/vllm/issues/33459) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Torch symm AllReduce seems suboptimal on 8×B200 (fixed CTA count?)

### Issue 正文摘录

### Proposal to improve performance On 8×B200 systems, the Torch symmetric AllReduce appears to be suboptimal likely due to fixed number of CTAs. ### AllReduce on 8×B200 (time in µs) Hidden dims = 8192, bfloat16 ### Report of performance regression _No response_ ### Misc discussion on performance I would also like to share TokenWeave fused kernel (https://github.com/microsoft/tokenweave) performance on 8xB200 (bfloat16, hidden dims=8192). ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: mber of CTAs. ### AllReduce on 8×B200 (time in µs) Hidden dims = 8192, bfloat16 ### Report of performance regression _No response_ ### Misc discussion on performance I would also like to share TokenWeave fused kernel (h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Performance]: Torch symm AllReduce seems suboptimal on 8×B200 (fixed CTA count?) performance ### Proposal to improve performance On 8×B200 systems, the Torch symmetric AllReduce appears to be suboptimal likely due to f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: (time in µs) Hidden dims = 8192, bfloat16 ### Report of performance regression _No response_ ### Misc discussion on performance I would also like to share TokenWeave fused kernel (https://github.com/microsoft/tokenweave...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
