# vllm-project/vllm#26195: [Bug]: Missing cached item in the MultiModalReceiverCache

| 字段 | 值 |
| --- | --- |
| Issue | [#26195](https://github.com/vllm-project/vllm/issues/26195) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 39; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Missing cached item in the MultiModalReceiverCache

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Observed missing cached item in the MultiModalReceiverCache when serving with large bs and multi media per request. @ywang96 ``` EngineCore_DP0 pid=2080) /dev/shm/uid-99/7b4afbe2-seed-nspid4026556718_cgpid1697541-ns-4026556715/vllm/v1/engine/core.py:830: ResourceWarning: Destroying context with unclosed socket (EngineCore_DP0 pid=2080) with ExitStack() as stack, zmq.Context() as ctx: (EngineCore_DP0 pid=2080) ResourceWarning: Enable tracemalloc to get the object allocation traceback (EngineCore_DP0 pid=2080) Exception in thread Thread-2 (process_input_sockets): (EngineCore_DP0 pid=2080) Traceback (most recent call last): (EngineCore_DP0 pid=2080) File "/usr/local/fbcode/platform010/lib/python3.10/threading.py", line 1016, in _bootstrap_inner (EngineCore_DP0 pid=2080) self.run() (EngineCore_DP0 pid=2080) File "/usr/local/fbcode/platform010/lib/python3.10/threading.py", line 953, in run (EngineCore_DP0 pid=2080) self._target(*self._args, **self._kwargs) (EngineCore_DP0 pid=2080) File "/dev/shm/uid-99/7b4afbe2-seed-nspid4026556718_cgpid1697541-ns-4026556715/vllm/v1/engine/core.py", line 879, in process_input_sockets (EngineCore_DP0...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Missing cached item in the MultiModalReceiverCache bug ### Your current environment ### 🐛 Describe the bug Observed missing cached item in the MultiModalReceiverCache when serving with large bs and multi media pe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e MultiModalReceiverCache when serving with large bs and multi media per request. @ywang96 ``` EngineCore_DP0 pid=2080) /dev/shm/uid-99/7b4afbe2-seed-nspid4026556718_cgpid1697541-ns-4026556715/vllm/v1/engine/core.py:830...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
