# vllm-project/vllm#1718: ImportError: libcudart.so.12

| 字段 | 值 |
| --- | --- |
| Issue | [#1718](https://github.com/vllm-project/vllm/issues/1718) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ImportError: libcudart.so.12

### Issue 正文摘录

Was working yesterday. Today it gives the following error: ``` from vllm import cuda_utils ImportError: libcudart.so.12: cannot open shared object file: No such file or directory ``` I've tried turning it off and on again multiple times.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ImportError: libcudart.so.12 installation Was working yesterday. Today it gives the following error: ``` from vllm import cuda_utils ImportError: libcudart.so.12: cannot open shared object file: No such file or directory
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ImportError: libcudart.so.12 installation Was working yesterday. Today it gives the following error: ``` from vllm import cuda_utils ImportError: libcudart.so.12: cannot open shared object file: No such file or director...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
