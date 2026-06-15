# vllm-project/vllm#13058: [V1][Help Wanted] Porting missing sampling parameters to V1

| 字段 | 值 |
| --- | --- |
| Issue | [#13058](https://github.com/vllm-project/vllm/issues/13058) |
| 状态 | closed |
| 标签 | good first issue;v1 |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [V1][Help Wanted] Porting missing sampling parameters to V1

### Issue 正文摘录

### Anything you want to discuss about vllm. To switch the engine from V0 to V1, we need to comprehensively support the sampling parameters in https://github.com/vllm-project/vllm/blob/main/vllm/sampling_params.py While most of the key parameters are already supported, some of them are missing: TODO (help wanted): - [x] `n` (parallel sampling) #10980 @afeldman-nm - [x] `guided_decoding` (structured decoding) #12388 @aarnphm - [x] `logit_bias` #13079 @houseroad - [x] `min_p` #13191 @AoyuQC - [ ] `bad_words` (originally implemented via logits processor) #13376 @22quinn - [x] `allowed_token_ids` (originally implemented via logits processor) #13210 @houseroad Parameters that will not be supported in V1: * best_of * logits_processors ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ors ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
