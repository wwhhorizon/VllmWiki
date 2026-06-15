# vllm-project/vllm#2014: kernels UT error

| 字段 | 值 |
| --- | --- |
| Issue | [#2014](https://github.com/vllm-project/vllm/issues/2014) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 | install |
| Operator 关键词 | kernel |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> kernels UT error

### Issue 正文摘录

I got an error when I run tests/kernels/test_attention.py error screenshot: ![image](https://github.com/vllm-project/vllm/assets/7843730/d1d9c839-bef3-40e0-89a4-6f384e57dd56) anyone has idea on this error? It is ok to run on A100 but failed on V100 below is my GPU info: ![image](https://github.com/vllm-project/vllm/assets/7843730/97dcee49-b666-403e-b591-f99cae414653)

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0e0-89a4-6f384e57dd56) anyone has idea on this error? It is ok to run on A100 but failed on V100 below is my GPU info: ![image](https://github.com/vllm-project/vllm/assets/7843730/97dcee49-b666-403e-b591-f99cae414653) d...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: kernels UT error I got an error when I run tests/kernels/test_attention.py error screenshot: ![image](https://github.com/vllm-project/vllm/assets/7843730/d1d9c839-bef3-40e0-89a4-6f384e57dd56) anyone has idea on this err...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
