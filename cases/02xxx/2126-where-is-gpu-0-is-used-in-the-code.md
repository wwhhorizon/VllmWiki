# vllm-project/vllm#2126: where is GPU:0 is used in the code？

| 字段 | 值 |
| --- | --- |
| Issue | [#2126](https://github.com/vllm-project/vllm/issues/2126) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> where is GPU:0 is used in the code？

### Issue 正文摘录

i revised /python3.9/site-packages/vllm/worker/worker.py line 56 ： local_rank = int(os.getenv("LOCAL_RANK", "5")) but got this error:**Expected all tensors to be on the same device, but found at least two devices, cuda:5 and cuda:0!** where is another GPU:0 is used in the code

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed all tensors to be on the same device, but found at least two devices, cuda:5 and cuda:0!** where is another GPU:0 is used in the code development cuda i revised /python3.9/site-packages/vllm/worker/worker.py line 56...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
