# vllm-project/vllm#30813: [Bug]: compilation_config.backend="eager" doesn't work aot mode (yet).

| 字段 | 值 |
| --- | --- |
| Issue | [#30813](https://github.com/vllm-project/vllm/issues/30813) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: compilation_config.backend="eager" doesn't work aot mode (yet).

### Issue 正文摘录

### Your current environment Should be able to be reproed on any env with the following option: ``` compilation_config = CompilationConfig( backend="eager", ) ``` Talked with @zou3519 about this offline and we will disable aot for eager in the short term (https://github.com/vllm-project/vllm/pull/30810). I can follow up with proper eager backend support later. ### 🐛 Describe the bug This is currently mitigated by https://github.com/vllm-project/vllm/pull/30810. Basically aot compilation will have this error when backend="eager": ``` [2025-12-15T20:52:30Z] (Worker_PP1_TP1 pid=36155) ERROR 12-15 12:52:30 [multiproc_executor.py:824] return forward_call(*args, **kwargs) [2025-12-15T20:52:30Z] (Worker_PP1_TP1 pid=36155) ERROR 12-15 12:52:30 [multiproc_executor.py:824] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [2025-12-15T20:52:30Z] (Worker_PP1_TP1 pid=36155) ERROR 12-15 12:52:30 [multiproc_executor.py:824] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/llama.py", line 623, in forward [2025-12-15T20:52:30Z] (Worker_PP1_TP1 pid=36155) ERROR 12-15 12:52:30 [multiproc_executor.py:824] model_output = self.model( [2025-12-15T20:52:30Z] (Worker_PP1_TP1 pid=36155) ERROR 12-15 12:...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: compilation_config.backend="eager" doesn't work aot mode (yet). bug;torch.compile;stale ### Your current environment Should be able to be reproed on any env with the following option: ``` compilation_config = Com...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: or.py:824] File "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/eval_frame.py", line 808, in aot_compile [2025-12-15T20:52:30Z] (Worker_PP1_TP1 pid=36155) ERROR 12-15 12:52:30 [multiproc_executor.py:824] return a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: compilation_config.backend="eager" doesn't work aot mode (yet). bug;torch.compile;stale ### Your current environment Should be able to be reproed on any env with the following option: ``` compilation_config = Com...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ompilation_config.backend="eager" doesn't work aot mode (yet). bug;torch.compile;stale ### Your current environment Should be able to be reproed on any env with the following option: ``` compilation_config = Compilation...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
