# vllm-project/vllm#7554: [Bug]:  CTRL+C Not Killing Process with distributed_executor_backend=mp in VLLM v0.5.3.post1

| 字段 | 值 |
| --- | --- |
| Issue | [#7554](https://github.com/vllm-project/vllm/issues/7554) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  CTRL+C Not Killing Process with distributed_executor_backend=mp in VLLM v0.5.3.post1

### Issue 正文摘录

### Your current environment - `vllm==0.5.3.post1` - `python=3.9` ### 🐛 Describe the bug When using distributed_executor_backend=mp with VLLM version `vllm==0.5.3.post1,` the process does not respond to CTRL+C in the terminal to terminate the process. This issue did not occur with `vllm==0.5.0.post1.` 1. With tensor parallelism >1, the log shows that one process exits but another process on a different GPU continues to run. The terminal is unresponsive to CTRL+C signals in this case. `(VllmWorkerProcess pid=9486) INFO 08-15 11:37:35 multiproc_worker_utils.py:237] Worker exiting` 2. With tensor parallelism ==1, the terminal does not respond to the CTRL+C signal at all.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: CTRL+C Not Killing Process with distributed_executor_backend=mp in VLLM v0.5.3.post1 bug ### Your current environment - `vllm==0.5.3.post1` - `python=3.9` ### 🐛 Describe the bug When using distributed_executor_ba...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 🐛 Describe the bug When using distributed_executor_backend=mp with VLLM version `vllm==0.5.3.post1,` the process does not respond to CTRL+C in the terminal to terminate the process. This issue did not occur with `vllm==...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s issue did not occur with `vllm==0.5.0.post1.` 1. With tensor parallelism >1, the log shows that one process exits but another process on a different GPU continues to run. The terminal is unresponsive to CTRL+C signals...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
