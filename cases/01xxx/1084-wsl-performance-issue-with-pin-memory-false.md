# vllm-project/vllm#1084: WSL performance issue with pin_memory=False

| 字段 | 值 |
| --- | --- |
| Issue | [#1084](https://github.com/vllm-project/vllm/issues/1084) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> WSL performance issue with pin_memory=False

### Issue 正文摘录

Has anyone benchmarked performance of WSL ubuntu and VLLM? I seem to be getting lower performance, but there are too many variables to say for sure. Any optimized settings to use/consider? I get this warning as well. Any idea what to do? WARNING 09-18 10:59:09 cache_engine.py:96] Using 'pin_memory=False' as WSL is detected. This may slow down the performance.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: WSL performance issue with pin_memory=False Has anyone benchmarked performance of WSL ubuntu and VLLM? I seem to be getting lower performance, but there are too many variables to say for sure. Any optimized settings to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: WSL performance issue with pin_memory=False Has anyone benchmarked performance of WSL ubuntu and VLLM? I seem to be getting lower performance, but there are too many variables to say for sure. Any optimized settings to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
