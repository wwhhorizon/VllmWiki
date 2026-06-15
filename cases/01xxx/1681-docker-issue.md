# vllm-project/vllm#1681: docker issue

| 字段 | 值 |
| --- | --- |
| Issue | [#1681](https://github.com/vllm-project/vllm/issues/1681) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> docker issue

### Issue 正文摘录

1. docker run --gpus all -it --rm --ipc=host nvcr.io/nvidia/pytorch:22.12-py3 2. pip install vllm ![image](https://github.com/vllm-project/vllm/assets/38581531/eb61d60f-d7bc-4ae9-af8e-5d514ae6b529) When i start a server, there is an error. ![image](https://github.com/vllm-project/vllm/assets/38581531/f90cecec-5c6b-47f1-ba52-0a667e363c82)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: docker issue 1. docker run --gpus all -it --rm --ipc=host nvcr.io/nvidia/pytorch:22.12-py3 2. pip install vllm ![image](https://github.com/vllm-project/vllm/assets/38581531/eb61d60f-d7bc-4ae9-af8e-5d514ae6b529) When i st

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
