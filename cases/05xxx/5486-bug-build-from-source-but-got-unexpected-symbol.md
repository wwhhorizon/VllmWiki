# vllm-project/vllm#5486: [Bug]: Build from source but got unexpected symbol

| 字段 | 值 |
| --- | --- |
| Issue | [#5486](https://github.com/vllm-project/vllm/issues/5486) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Build from source but got unexpected symbol

### Issue 正文摘录

### Your current environment ```text WARNING 06-13 04:15:46 _custom_ops.py:11] Failed to import from vllm._C with ImportError('/data/libs/vllm/vllm/_C.abi3.so: undefined symbol: _ZN5torch7LibraryC1ENS0_4KindESsSt8optionalIN3c1011DispatchKeyEEPKcj')``` ### 🐛 Describe the bug git clone xxx && pip install -e . Already cleaned old build, actually this is a fresh clone.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Build from source but got unexpected symbol bug;stale ### Your current environment ```text WARNING 06-13 04:15:46 _custom_ops.py:11] Failed to import from vllm._C with ImportError('/data/libs/vllm/vllm/_C.abi3.so...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: so: undefined symbol: _ZN5torch7LibraryC1ENS0_4KindESsSt8optionalIN3c1011DispatchKeyEEPKcj')``` ### 🐛 Describe the bug git clone xxx && pip install -e . Already cleaned old build, actually this is a fresh clone.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Build from source but got unexpected symbol bug;stale ### Your current environment ```text WARNING 06-13 04:15:46 _custom_ops.py:11] Failed to import from vllm._C with ImportError('/data/libs/vllm/vllm/_C.abi3.so...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
