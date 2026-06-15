# vllm-project/vllm#1877: Yi-34B-Chat-4bit got CUDA out of memory

| 字段 | 值 |
| --- | --- |
| Issue | [#1877](https://github.com/vllm-project/vllm/issues/1877) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Yi-34B-Chat-4bit got CUDA out of memory

### Issue 正文摘录

when I run the 4bit model in vllm. I got following error. I am using rtx4090 (24G GPU memory). ![Screenshot from 2023-12-01 12-28-40](https://github.com/vllm-project/vllm/assets/3841400/0c8c6c02-5365-436a-83a9-86e1dd1c6043) ![Screenshot from 2023-12-01 12-28-09](https://github.com/vllm-project/vllm/assets/3841400/0714a0f8-4652-45bc-8a09-b952a7390b83)

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Yi-34B-Chat-4bit got CUDA out of memory when I run the 4bit model in vllm. I got following error. I am using rtx4090 (24G GPU memory). ![Screenshot from 2023-12-01 12-28-40](https://github.com/vllm-project/vllm/assets/3...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: n the 4bit model in vllm. I got following error. I am using rtx4090 (24G GPU memory). ![Screenshot from 2023-12-01 12-28-40](https://github.com/vllm-project/vllm/assets/3841400/0c8c6c02-5365-436a-83a9-86e1dd1c6043) ![Sc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Yi-34B-Chat-4bit got CUDA out of memory when I run the 4bit model in vllm. I got following error. I am using rtx4090 (24G GPU memory). ![Screenshot from 2023-12-01 12-28-40](https://github.com/vllm-project/vllm/assets/3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
