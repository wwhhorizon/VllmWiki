# vllm-project/vllm#30847: [Bug]: Qwen 3VL via Efficient Video Sampling (EVS) to trim video embeddings and found that the number of tokens after timestamp in the Prompt was not aligned with the actual number of tokens after pruning?

| 字段 | 值 |
| --- | --- |
| Issue | [#30847](https://github.com/vllm-project/vllm/issues/30847) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen 3VL via Efficient Video Sampling (EVS) to trim video embeddings and found that the number of tokens after timestamp in the Prompt was not aligned with the actual number of tokens after pruning?

### Issue 正文摘录

### Your current environment 、 ### 🐛 Describe the bug 1、get_video_replacement_qwen3vl frames_idx_token=[165, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33] 2、compute_retention_mask 3、embed_input_ids input_ids: From the above 1 and 3, it can be seen that the data in frames_idx_token is the same as that in embed_input_ids, The first frame contains 165 tokens, while the rest contain 33 tokens 151656 is the ID of the video token. The number of 151656 is the number of video tokens. The sum of the number of video tokens in all frames is the same as the sum of frames_idx_token. Regarding the second item: compute_contention_mask EVS cropped mask, it was found that the number of tokens in the first frame was 165, while the number of tokens in other frames was different, Based on the above 1, 2, and 3, it can be concluded that the current implementation of EVS pruning algorithm has problems That is, the number of tokens after timestamp in the Prompt does not match the actual number of tokens that should be retained after EVS pruning. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right co...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Qwen 3VL via Efficient Video Sampling (EVS) to trim video embeddings and found that the number of tokens after timestamp in the Prompt was not aligned with the actual number of tokens after pruning? bug ### Your...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Qwen 3VL via Efficient Video Sampling (EVS) to trim video embeddings and found that the number of tokens after timestamp in the Prompt was not aligned with the actual number of tokens after pruning? bug ### Your...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
