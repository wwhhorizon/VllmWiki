# vllm-project/vllm#1291: ImportError: /opt/vllm/vllm/attention_ops.cpython-39-x86_64-linux-gnu.so: undefined symbol: _ZNK3c1010TensorImpl27throw_data_ptr_access_errorEv

| 字段 | 值 |
| --- | --- |
| Issue | [#1291](https://github.com/vllm-project/vllm/issues/1291) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ImportError: /opt/vllm/vllm/attention_ops.cpython-39-x86_64-linux-gnu.so: undefined symbol: _ZNK3c1010TensorImpl27throw_data_ptr_access_errorEv

### Issue 正文摘录

Excuse me, why is this mistake? ![image](https://github.com/vllm-project/vllm/assets/22927505/d676ff76-2745-4a74-8cbd-b3ac248e9a38)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ImportError: /opt/vllm/vllm/attention_ops.cpython-39-x86_64-linux-gnu.so: undefined symbol: _ZNK3c1010TensorImpl27throw_data_ptr_access_errorEv Excuse me, why is this mistake? ![image](https://github.com/vllm-project/vl

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
