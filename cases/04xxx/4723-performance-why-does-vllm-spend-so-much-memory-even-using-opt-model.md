# vllm-project/vllm#4723: [Performance]: Why does vllm spend so much memory even using OPT model?

| 字段 | 值 |
| --- | --- |
| Issue | [#4723](https://github.com/vllm-project/vllm/issues/4723) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Why does vllm spend so much memory even using OPT model?

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance In the vllm, the reserved memory is always around 20GB whatever the model we use. For example, the opt model is only 125M, but the reserved memory is 20GB too. I tried to run the OPT model using a **huggingface engine**, which took only **568MB** of memory. Why does the vllm framework consume that much GPU memory even for a small model? ![Screenshot 2024-05-09 at 7 25 59 PM](https://github.com/vllm-project/vllm/assets/47625290/c54a9240-22cf-47dd-9a7d-02132b5c8276) ### Your current environment (if you think it is necessary) _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: Why does vllm spend so much memory even using OPT model? performance ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ry. Why does the vllm framework consume that much GPU memory even for a small model? ![Screenshot 2024-05-09 at 7 25 59 PM](https://github.com/vllm-project/vllm/assets/47625290/c54a9240-22cf-47dd-9a7d-02132b5c8276) ###...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: only **568MB** of memory. Why does the vllm framework consume that much GPU memory even for a small model? ![Screenshot 2024-05-09 at 7 25 59 PM](https://github.com/vllm-project/vllm/assets/47625290/c54a9240-22cf-47dd-9...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance In the vllm, the reserved memory is always around 20GB whatever the model we use. For ex...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
