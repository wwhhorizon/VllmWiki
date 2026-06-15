# vllm-project/vllm#35686: [Bug][UX]: Unclean shutdown from ctrl-c with AR Fusion

| 字段 | 值 |
| --- | --- |
| Issue | [#35686](https://github.com/vllm-project/vllm/issues/35686) |
| 状态 | closed |
| 标签 | bug;help wanted;good first issue |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][UX]: Unclean shutdown from ctrl-c with AR Fusion

### Issue 正文摘录

### Your current environment on b200, we now enable ar fusions. the log looks like this when i click ctrl-c ``` (Worker pid=2552998) (Worker_TP0 pid=2552998) Exception ignored in: (Worker pid=2552998) (Worker_TP0 pid=2552998) Traceback (most recent call last): (Worker pid=2552998) (Worker_TP0 pid=2552998) File "/home/robertgshaw2-redhat/vllm/.venv/lib/python3.12/site-packages/flashinfer/comm/workspace_base.py", line 72, in __del__ (Worker pid=2552998) (Worker_TP0 pid=2552998) ImportError: sys.meta_path is None, Python is likely shutting down (Worker pid=2553001) (Worker_TP3 pid=2553001) Exception ignored in: (Worker pid=2553001) (Worker_TP3 pid=2553001) Traceback (most recent call last): (Worker pid=2553001) (Worker_TP3 pid=2553001) File "/home/robertgshaw2-redhat/vllm/.venv/lib/python3.12/site-packages/flashinfer/comm/workspace_base.py", line 72, in __del__ (Worker pid=2553001) (Worker_TP3 pid=2553001) ImportError: sys.meta_path is None, Python is likely shutting down (Worker pid=2552999) (Worker_TP1 pid=2552999) Exception ignored in: (Worker pid=2552999) (Worker_TP1 pid=2552999) Traceback (most recent call last): (Worker pid=2552999) (Worker_TP1 pid=2552999) File "/home/robertgs...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Fusion bug;help wanted;good first issue ### Your current environment on b200, we now enable ar fusions. the log looks like this when i click ctrl-c ``` (Worker pid=2552998) (Worker_TP0 pid=2552998) Exception ignored in:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: File "/home/robertgshaw2-redhat/vllm/.venv/lib/python3.12/site-packages/flashinfer/comm/workspace_base.py", line 72, in __del__ (Worker pid=2552998) (Worker_TP0 pid=2552998) ImportError: sys.meta_path is None, Python is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e.py", line 72, in __del__ (Worker pid=2552998) (Worker_TP0 pid=2552998) ImportError: sys.meta_path is None, Python is likely shutting down (Worker pid=2553001) (Worker_TP3 pid=2553001) Exception ignored in: (Worker pid...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
