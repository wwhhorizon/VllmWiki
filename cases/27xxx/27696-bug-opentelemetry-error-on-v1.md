# vllm-project/vllm#27696: [Bug]: OpenTelemetry Error on V1

| 字段 | 值 |
| --- | --- |
| Issue | [#27696](https://github.com/vllm-project/vllm/issues/27696) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OpenTelemetry Error on V1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I want to use OpenTelemetry tracing, so I passed in the following flags to vLLM: ```sh --collect-detailed-traces="all" \ --otlp-traces-endpoint="grpc://localhost:4317" ``` I'm using vLLM in NVIDIA Dynamo. vLLM is initialized in NVIDIA Dynamo [here](https://github.com/ai-dynamo/dynamo/blob/65f12d7db4b70b8404d70a726647c164d5f7fe47/components/backends/vllm/src/dynamo/vllm/main.py#L121-L127), which is resulting in the following error: ``` Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/home/ubuntu/dynamo/dynamo/lib/python3.10/site-packages/dynamo/vllm/__main__.py", line 7, in main() File "/home/ubuntu/dynamo/dynamo/lib/python3.10/site-packages/dynamo/vllm/main.py", line 330, in main uvloop.run(worker()) File "/home/ubuntu/dynamo/dynamo/lib/python3.10/site-packages/uvloop/__init__.py", line 69, in run return loop.run_until_complete(wrapper()) File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete File "/home/ubuntu/dynamo/dynamo/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: t environment ### 🐛 Describe the bug I want to use OpenTelemetry tracing, so I passed in the following flags to vLLM: ```sh --collect-detailed-traces="all" \ --otlp-traces-endpoint="grpc://localhost:4317" ``` I'm using...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: i-dynamo/dynamo/blob/65f12d7db4b70b8404d70a726647c164d5f7fe47/components/backends/vllm/src/dynamo/vllm/main.py#L121-L127), which is resulting in the following error: ``` Traceback (most recent call last): File "/usr/lib...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: or? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ackages/dynamo/vllm/main.py", line 89, in worker await init(runtime, config) File "/home/ubuntu/dynamo/dynamo/lib/python3.10/site-packages/dynamo/vllm/main.py", line 215, in init engine_client, vllm_config, default_samp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: OpenTelemetry Error on V1 bug;stale ### Your current environment ### 🐛 Describe the bug I want to use OpenTelemetry tracing, so I passed in the following flags to vLLM: ```sh --collect-detailed-traces="all" \ --o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
