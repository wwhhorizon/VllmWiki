# vllm-project/vllm#2481: Waht is the shape of the attention score for Paged Attention?

| 字段 | 值 |
| --- | --- |
| Issue | [#2481](https://github.com/vllm-project/vllm/issues/2481) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Waht is the shape of the attention score for Paged Attention?

### Issue 正文摘录

Thanks for your excellent work! Recently, I have been learning the source code of the vLLM. But, I have some difficulties in understanding codes: (csrc/attention/attention_kernels.cu) ``` In the kernel--paged_attention_kernel, // Compute softmax. const float inv_sum = __fdividef(1.f, exp_sum + 1e-6f); for (int i = thread_idx; i < num_tokens; i += NUM_THREADS) { logits[i] *= inv_sum; } ``` Questions: 1) Is the logits[i] storing the attetion score of the the ith token? 2) Besides, I also want to learn what is the shape of the attention score ? Thanks for your help!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
