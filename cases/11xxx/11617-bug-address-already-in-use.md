# vllm-project/vllm#11617: [Bug]: Address already in use

| 字段 | 值 |
| --- | --- |
| Issue | [#11617](https://github.com/vllm-project/vllm/issues/11617) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Address already in use

### Issue 正文摘录

### Your current environment ### Model Input Dumps CUDA_VISIBLE_DEVICES=13 python3 -m vllm.entrypoints.openai.api_server \ --model ./models/Qwen2.5-0.5B-Instruct \ --port 8000 \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.5 \ --served-model-name Qwen2.5-0.5B \ --max-model-len 3000 \ --max-num-seqs 1 ### 🐛 Describe the bug always run into this error: Traceback (most recent call last): File "/miniforge3/envs/vllm/lib/python3.10/site-packages/vllm/utils.py", line 572, in get_open_port s.bind(("", 0)) OSError: [Errno 98] Address already in use or this one: File "/miniforge3/envs/vllm/lib/python3.10/site-packages/torch/distributed/rendezvous.py", line 186, in _create_c10d_store return TCPStore( RuntimeError: The server socket has failed to listen on any local network address. useIpv6: 0, code: -98, name: EADDRINUSE, message: address already in use i have checked the port 8000 by "lsof" command and confirmed that the "VLLM_PORT" is None i also have attempted to change other port, but it still doesnt work ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation pa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ready in use bug ### Your current environment ### Model Input Dumps CUDA_VISIBLE_DEVICES=13 python3 -m vllm.entrypoints.openai.api_server \ --model ./models/Qwen2.5-0.5B-Instruct \ --port 8000 \ --tensor-parallel-size 1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Address already in use bug ### Your current environment ### Model Input Dumps CUDA_VISIBLE_DEVICES=13 python3 -m vllm.entrypoints.openai.api_server \ --model ./models/Qwen2.5-0.5B-Instruct \ --port 8000 \ --tenso...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
