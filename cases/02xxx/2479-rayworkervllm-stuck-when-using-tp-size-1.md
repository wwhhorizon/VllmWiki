# vllm-project/vllm#2479: RayWorkerVllm stuck when using tp size > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#2479](https://github.com/vllm-project/vllm/issues/2479) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> RayWorkerVllm stuck when using tp size > 1

### Issue 正文摘录

I used llama 7b model with tp size = 2. server is stuck after receiving ~15 requests. command: ``` python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-7b-chat-hf --tensor-parallel-size 2 ``` Client ``` import requests request_param = { "model": "meta-llama/Llama-2-7b-chat-hf", "prompt": "what is vllm in ML?", "max_tokens": 1024, } count = 0 while True: resp = requests.post("http://127.0.0.1:8000/v1/completions", json=request_param) print(count) count += 1 import time; time.sleep(1) ``` RayVllmWorker stuck at ``` Thread 96488 (active): "MainThread" all_gather_into_tensor (torch/distributed/distributed_c10d.py:2897) wrapper (torch/distributed/c10d_logger.py:47) tensor_model_parallel_all_gather (vllm/model_executor/parallel_utils/communication_op.py:40) _get_logits (vllm/model_executor/layers/sampler.py:105) forward (vllm/model_executor/layers/sampler.py:46) _call_impl (torch/nn/modules/module.py:1527) _wrapped_call_impl (torch/nn/modules/module.py:1518) sample (vllm/model_executor/models/llama.py:295) execute_model (vllm/worker/model_runner.py:354) decorate_context (torch/utils/_contextlib.py:115) execute_model (vllm/worker/worker.py:159) decorate_context (torch/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: RayWorkerVllm stuck when using tp size > 1 I used llama 7b model with tp size = 2. server is stuck after receiving ~15 requests. command: ``` python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-7b-ch...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: l meta-llama/Llama-2-7b-chat-hf --tensor-parallel-size 2 ``` Client ``` import requests request_param = { "model": "meta-llama/Llama-2-7b-chat-hf", "prompt": "what is vllm in ML?", "max_tokens": 1024, } count = 0 while...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: sed llama 7b model with tp size = 2. server is stuck after receiving ~15 requests. command: ``` python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-7b-chat-hf --tensor-parallel-size 2 ``` Client ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
