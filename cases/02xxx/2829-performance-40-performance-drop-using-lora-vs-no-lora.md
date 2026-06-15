# vllm-project/vllm#2829: [Performance] 40% performance drop using lora vs no lora

| 字段 | 值 |
| --- | --- |
| Issue | [#2829](https://github.com/vllm-project/vllm/issues/2829) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance] 40% performance drop using lora vs no lora

### Issue 正文摘录

``` ... Processed prompts: 100% 1321/1321 [09:09<00:00, 2.40it/s] training | ic| "Testing '" + lora + "'": "Testing 'models/v3/checkpoint-1000'" Processed prompts: 100% 1321/1321 [16:01<00:00, 1.37it/s] training | ic| "Lora '" + lora + "' testing complete.": "Lora 'models/v3/checkpoint-1000' testing complete." training | ic| "Testing '" + lora + "'": "Testing 'models/v3/final_lora'" Processed prompts: 100% 1321/1321 [15:59<00:00, 1.38it/s] training | ic| "Lora '" + lora + "' testing complete.": "Lora 'models/v3/final_lora' testing complete." training | ic| "Testing '" + lora + "'": "Testing 'models/v3/checkpoint-2000'" ... ``` Testing offline batched inference with a big bunch of long context, short reply prompts, feeding the vllm engine all 1321 prompts as a list in a single batch. Tested on an 80GB A100. This isn't a bug per se, or a major problem, more like a... note. I guess a big performance drop for loras is expected?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: m engine all 1321 prompts as a list in a single batch. Tested on an 80GB A100. This isn't a bug per se, or a major problem, more like a... note. I guess a big performance drop for loras is expected?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 09<00:00, 2.40it/s] training | ic| "Testing '" + lora + "'": "Testing 'models/v3/checkpoint-1000'" Processed prompts: 100% 1321/1321 [16:01<00:00, 1.37it/s] training | ic| "Lora '" + lora + "' testing complete.": "Lora...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: cessed prompts: 100% 1321/1321 [09:09<00:00, 2.40it/s] training | ic| "Testing '" + lora + "'": "Testing 'models/v3/checkpoint-1000'" Processed prompts: 100% 1321/1321 [16:01<00:00, 1.37it/s] training | ic| "Lora '" + l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
