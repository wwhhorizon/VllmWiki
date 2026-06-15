# vllm-project/vllm#1177: 源码安装 报错 undefined symbol: _ZNSt15__exception_ptr13exception_ptr9_M_addrefEv

| 字段 | 值 |
| --- | --- |
| Issue | [#1177](https://github.com/vllm-project/vllm/issues/1177) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 源码安装 报错 undefined symbol: _ZNSt15__exception_ptr13exception_ptr9_M_addrefEv

### Issue 正文摘录

源码安装 pip install -e . 启动报错： /vllm/activation_ops.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZNSt15__exception_ptr13exception_ptr9_M_addrefEv

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 源码安装 报错 undefined symbol: _ZNSt15__exception_ptr13exception_ptr9_M_addrefEv 源码安装 pip install -e . 启动报错： /vllm/activation_ops.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZNSt15__exception_ptr13exception_ptr9_M_ad...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
