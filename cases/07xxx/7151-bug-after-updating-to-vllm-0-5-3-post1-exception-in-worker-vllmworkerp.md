# vllm-project/vllm#7151: [Bug]: After updating to vllm 0.5.3.post1, "Exception in worker VllmWorkerProcess while processing method init_device: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method."

| 字段 | 值 |
| --- | --- |
| Issue | [#7151](https://github.com/vllm-project/vllm/issues/7151) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: After updating to vllm 0.5.3.post1, "Exception in worker VllmWorkerProcess while processing method init_device: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method."

### Issue 正文摘录

### Your current environment Same as in issue [#7077](https://github.com/vllm-project/vllm/issues/7077#issuecomment-2268423776). ### 🐛 Describe the bug I met the same problem as in issue [#7077](https://github.com/vllm-project/vllm/issues/7077#issuecomment-2268423776), but the issue was closed without solutions. I would like to raise this issue again and seek for kind help.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: mWorkerProcess while processing method init_device: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method." bug ### Your current environment Same as in i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
