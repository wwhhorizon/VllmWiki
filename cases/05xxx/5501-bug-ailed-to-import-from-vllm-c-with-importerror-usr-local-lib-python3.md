# vllm-project/vllm#5501: [Bug]:  ailed to import from vllm._C with ImportError('/usr/local/lib/python3.8/dist-packages/vllm/_C.abi3.so: undefined symbol: _ZN5torch7LibraryC1ENS0_4KindESsSt8optionalIN3c1011DispatchKeyEEPKcj')

| 字段 | 值 |
| --- | --- |
| Issue | [#5501](https://github.com/vllm-project/vllm/issues/5501) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  ailed to import from vllm._C with ImportError('/usr/local/lib/python3.8/dist-packages/vllm/_C.abi3.so: undefined symbol: _ZN5torch7LibraryC1ENS0_4KindESsSt8optionalIN3c1011DispatchKeyEEPKcj')

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` import vllm WARNING 06-13 11:42:20 _custom_ops.py:11] Failed to import from vllm._C with ImportError('/usr/local/lib/python3.8/dist-packages/vllm/_C.abi3.so: undefined symbol: _ZN5torch7LibraryC1ENS0_4KindESsSt8optionalIN3c1011DispatchKeyEEPKcj') ### 🐛 Describe the bug import vllm WARNING 06-13 11:42:20 _custom_ops.py:11] Failed to import from vllm._C with ImportError('/usr/local/lib/python3.8/dist-packages/vllm/_C.abi3.so: undefined symbol: _ZN5torch7LibraryC1ENS0_4KindESsSt8optionalIN3c1011DispatchKeyEEPKcj') Does the `pip install vllm` supports torch2.3.0? If not, why not mentioned it in README?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: ailed to import from vllm._C with ImportError('/usr/local/lib/python3.8/dist-packages/vllm/_C.abi3.so: undefined symbol: _ZN5torch7LibraryC1ENS0_4KindESsSt8optionalIN3c1011DispatchKeyEEPKcj') bug;stale ### Your c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: so: undefined symbol: _ZN5torch7LibraryC1ENS0_4KindESsSt8optionalIN3c1011DispatchKeyEEPKcj') bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` import vllm WARNING 06-13 11:42:20 _c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: N5torch7LibraryC1ENS0_4KindESsSt8optionalIN3c1011DispatchKeyEEPKcj') bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` import vllm WARNING 06-13 11:42:20 _custom_ops.py:11] Failed...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
