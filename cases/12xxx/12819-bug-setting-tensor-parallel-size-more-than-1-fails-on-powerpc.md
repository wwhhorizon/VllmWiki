# vllm-project/vllm#12819: [Bug]: Setting `tensor-parallel-size` more than 1 fails on PowerPC

| 字段 | 值 |
| --- | --- |
| Issue | [#12819](https://github.com/vllm-project/vllm/issues/12819) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Setting `tensor-parallel-size` more than 1 fails on PowerPC

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While inferencing the model with `--tensor-parallel-size` 2, it fails for completion requests: ``` # vllm serve facebook/opt-125m -tp 2 ``` Request: ``` # curl http://localhost:8000/v1/completions -H "Content-Type: application/json" -d '{ "model": "facebook/opt-125m", "prompt": "San Francisco is a", "max_tokens": 7, "temperature": 0 }' ``` vLLM Error: ``` ERROR 02-06 09:12:05 engine.py:139] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised: ERROR 02-06 09:12:05 engine.py:139] InvalidCxxCompiler: No working C++ compiler found in torch._inductor.config.cpp.cxx: (None, 'g++') ERROR 02-06 09:12:05 engine.py:139] ERROR 02-06 09:12:05 engine.py:139] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information ERROR 02-06 09:12:05 engine.py:139] ERROR 02-06 09:12:05 engine.py:139] ERROR 02-06 09:12:05 engine.py:139] You can suppress this exception and fall back to eager by setting: ERROR 02-06 09:12:05 engine.py:139] import torch._dynamo ERROR 02-06 09:12:05 engine.py:139] torch._dynamo.config.suppress_errors = True ERROR 02-06 09:12:05 engine.py:139] INFO 02-06 09:12:05 multiproc_worker_utils.py:128] Killing...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ug ### Your current environment ### 🐛 Describe the bug While inferencing the model with `--tensor-parallel-size` 2, it fails for completion requests: ``` # vllm serve facebook/opt-125m -tp 2 ``` Request: ``` # curl http...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ur current environment ### 🐛 Describe the bug While inferencing the model with `--tensor-parallel-size` 2, it fails for completion requests: ``` # vllm serve facebook/opt-125m -tp 2 ``` Request: ``` # curl http://localh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: xt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ` vLLM Error: ``` ERROR 02-06 09:12:05 engine.py:139] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised: ERROR 02-06 09:12:05 engine.py:139] InvalidCxxCompiler: No working C++ compiler found in torch._i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ncing the model with `--tensor-parallel-size` 2, it fails for completion requests: ``` # vllm serve facebook/opt-125m -tp 2 ``` Request: ``` # curl http://localhost:8000/v1/completions -H "Content-Type: application/json...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
