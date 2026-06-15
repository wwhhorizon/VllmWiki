# vllm-project/vllm#18301: [Bug]: Not support device type: cpu

| 字段 | 值 |
| --- | --- |
| Issue | [#18301](https://github.com/vllm-project/vllm/issues/18301) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Not support device type: cpu

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug As described in the documentation: https://docs.vllm.ai/en/latest/serving/serve_args.html#vllm.entrypoints.openai.cli_args-create_parser_for_docs-deviceconfig [--device {auto,cpu,cuda,hpu,neuron,tpu,xpu}], we can choose cpu as the device. However, after I ran `vllm serve facebook/opt-125m --device cpu` , the following error occurred: Error Message: ``` ERROR 05-17 08:13:54 [core.py:489] EngineCore failed to start. ERROR 05-17 08:13:54 [core.py:489] Traceback (most recent call last): ERROR 05-17 08:13:54 [core.py:489] File "/workspace/vllm/vllm/v1/engine/core.py", line 480, in run_engine_core ERROR 05-17 08:13:54 [core.py:489] engine_core = EngineCoreProc(*args, **kwargs) ERROR 05-17 08:13:54 [core.py:489] File "/workspace/vllm/vllm/v1/engine/core.py", line 379, in __init__ ERROR 05-17 08:13:54 [core.py:489] super().__init__(vllm_config, executor_class, log_stats, ERROR 05-17 08:13:54 [core.py:489] File "/workspace/vllm/vllm/v1/engine/core.py", line 67, in __init__ ERROR 05-17 08:13:54 [core.py:489] self.model_executor = executor_class(vllm_config) ERROR 05-17 08:13:54 [core.py:489] File "/workspace/vllm/vllm/executor/executor_bas...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: trypoints/openai/api_server.py", line 1324, in run_server async with build_async_engine_client(args) as engine_client: File "/usr/lib/python3.10/contextlib.py", line 199, in __aenter__ return await anext(self.gen) File...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: /workspace/vllm/vllm/entrypoints/cli/main.py", line 53, in main args.dispatch_function(args) File "/workspace/vllm/vllm/entrypoints/cli/serve.py", line 40, in cmd uvloop.run(run_server(args)) File "/usr/local/lib/python...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .openai.cli_args-create_parser_for_docs-deviceconfig [--device {auto,cpu,cuda,hpu,neuron,tpu,xpu}], we can choose cpu as the device. However, after I ran `vllm serve facebook/opt-125m --device cpu` , the following error...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: _args.html#vllm.entrypoints.openai.cli_args-create_parser_for_docs-deviceconfig [--device {auto,cpu,cuda,hpu,neuron,tpu,xpu}], we can choose cpu as the device. However, after I ran `vllm serve facebook/opt-125m --device...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
