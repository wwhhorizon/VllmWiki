# vllm-project/vllm#23077: [Feature]: Support Pipeline Parallelism for moonshotai/Kimi-VL-A3B-Thinking-2506

| 字段 | 值 |
| --- | --- |
| Issue | [#23077](https://github.com/vllm-project/vllm/issues/23077) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Pipeline Parallelism for moonshotai/Kimi-VL-A3B-Thinking-2506

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am trying to host this on vLLM with Pipeline Parallelism as I have 2 GPUs on 2 different nodes. But looks like its not support for this model. I have loaded some other models and pipeline parallelism is working well. stack trace: `(APIServer pid=35) File "/usr/lib/python3.12/contextlib.py", line 210, in aenter (APIServer pid=35) return await anext(self.gen) (APIServer pid=35) ^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=35) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 204, in build_async_engine_client_from_engine_args (APIServer pid=35) vllm_config = engine_args.create_engine_config(usage_context=usage_context) (APIServer pid=35) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=35) File "/usr/local/lib/python3.12/dist-packages/vllm/engine/arg_utils.py", line 1335, in create_engine_config (APIServer pid=35) config = VllmConfig( (APIServer pid=35) ^^^^^^^^^^^ (APIServer pid=35) File "/usr/local/lib/python3.12/dist-packages/pydantic/_internal/_dataclasses.py", line 120, in init (APIServer pid=35) s.pydantic_validator.validate_python(ArgsKwargs(args, kwargs), self_instance=s) (A...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Support Pipeline Parallelism for moonshotai/Kimi-VL-A3B-Thinking-2506 feature request ### 🚀 The feature, motivation and pitch I am trying to host this on vLLM with Pipeline Parallelism as I have 2 GPUs on 2 d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ave 2 GPUs on 2 different nodes. But looks like its not support for this model. I have loaded some other models and pipeline parallelism is working well. stack trace: `(APIServer pid=35) File "/usr/lib/python3.12/contex...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 204, in build_async_engine_client_from_engine_args (APIServer pid=35) vllm_config = engine_args.create_engine_config(usage_context=usage_context) (APIServ...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: rt Pipeline Parallelism for moonshotai/Kimi-VL-A3B-Thinking-2506 feature request ### 🚀 The feature, motivation and pitch I am trying to host this on vLLM with Pipeline Parallelism as I have 2 GPUs on 2 different nodes....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
