# vllm-project/vllm#9340: [Installation]: Adding opentelemetry packages in container image 

| 字段 | 值 |
| --- | --- |
| Issue | [#9340](https://github.com/vllm-project/vllm/issues/9340) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Adding opentelemetry packages in container image 

### Issue 正文摘录

### Your current environment Using container image vllm/vllm-openai:v0.6.2 ```text Process SpawnProcess-1: Traceback (most recent call last): File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 388, in run_mp_engine engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 134, in from_engine_args engine_config = engine_args.create_engine_config() ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/engine/arg_utils.py", line 1046, in create_engine_config observability_config = ObservabilityConfig( ^^^^^^^^^^^^^^^^^^^^ File " ", line 6, in __init__ File "/usr/local/lib/python3.12/dist-packages/vllm/config.py", line 1834, in __post_init__ raise ValueError( ValueError: OpenTelemetry is not available. Unable to configure 'otlp_traces_endpoint'. Ensure OpenTelemetry...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: Adding opentelemetry packages in container image installation;stale ### Your current environment Using container image vllm/vllm-openai:v0.6.2 ```text Process SpawnProcess-1: Traceback (most recent call
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ine/multiprocessing/engine.py", line 134, in from_engine_args engine_config = engine_args.create_engine_config() ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/engine/arg_utils.py"...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: llation]: Adding opentelemetry packages in container image installation;stale ### Your current environment Using container image vllm/vllm-openai:v0.6.2 ```text Process SpawnProcess-1: Traceback (most recent call last):...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
