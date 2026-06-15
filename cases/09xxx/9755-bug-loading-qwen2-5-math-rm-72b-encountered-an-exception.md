# vllm-project/vllm#9755: [Bug]: Loading qwen2.5-math-rm-72b encountered an exception

| 字段 | 值 |
| --- | --- |
| Issue | [#9755](https://github.com/vllm-project/vllm/issues/9755) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Loading qwen2.5-math-rm-72b encountered an exception

### Issue 正文摘录

**Loading qwen2.5-math-rm-72b encountered an exception. Exception information as follows:** Traceback (most recent call last): File "/usr/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/usr/lib/python3.10/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/multiprocessing/engine.py", line 390, in run_mp_engine engine = MQLLMEngine.from_engine_args(engine_args=engine_args, File "/usr/local/lib/python3.10/dist-packages/vllm/engine/multiprocessing/engine.py", line 139, in from_engine_args return cls( File "/usr/local/lib/python3.10/dist-packages/vllm/engine/multiprocessing/engine.py", line 78, in __init__ self.engine = LLMEngine(*args, **kwargs) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 334, in __init__ self.model_executor = executor_class( File "/usr/local/lib/python3.10/dist-packages/vllm/executor/distributed_gpu_executor.py", line 26, in __init__ super().__init__(*args, **kwargs) File "/usr/local/lib/python3.10/dist-packages/vllm/executor/executor_base.py", line 47, in __init__ self._init_executor() File "/usr/loca...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Loading qwen2.5-math-rm-72b encountered an exception bug **Loading qwen2.5-math-rm-72b encountered an exception. Exception information as follows:** Traceback (most recent call last): File "/usr/lib/python3.10/mu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ger ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
