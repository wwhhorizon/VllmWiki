# vllm-project/vllm#953: running vllm engine in two gpus with a Falcon fine-tunned model

| 字段 | 值 |
| --- | --- |
| Issue | [#953](https://github.com/vllm-project/vllm/issues/953) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | attention;cuda |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> running vllm engine in two gpus with a Falcon fine-tunned model

### Issue 正文摘录

I have this error when I tried to get a response from model using API example RuntimeError: CUDA error: an illegal memory access was encountered ## Error trace File "/home/moises/.local/lib/python3.10/site-packages/vllm/engine/ray_utils.py", line 25, in execute_method return executor(*args, **kwargs) File "/opt/conda/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) File "/home/moises/.local/lib/python3.10/site-packages/vllm/worker/worker.py", line 293, in execute_model output = self.model( File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl return forward_call(*args, **kwargs) File "/home/moises/.local/lib/python3.10/site-packages/vllm/model_executor/models/falcon.py", line 401, in forward hidden_states = self.transformer( File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl return forward_call(*args, **kwargs) File "/home/moises/.local/lib/python3.10/site-packages/vllm/model_executor/models/falcon.py", line 369, in forward hidden_states = layer( File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py",...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: zer model --tensor-parallel-size 2 ``` ### Server code main_vll.py ``` import argparse import json from typing import AsyncGenerator from fastapi import BackgroundTasks, FastAPI, Request from fastapi.responses import JS...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ing import AsyncGenerator from fastapi import BackgroundTasks, FastAPI, Request from fastapi.responses import JSONResponse, Response, StreamingResponse import uvicorn from vllm.engine.arg_utils import AsyncEngineArgs fr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n I tried to get a response from model using API example RuntimeError: CUDA error: an illegal memory access was encountered ## Error trace File "/home/moises/.local/lib/python3.10/site-packages/vllm/engine/ray_utils.py"...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: t = request_dict.pop("prompt") stream = request_dict.pop("stream", False) sampling_params = SamplingParams(**request_dict) request_id = random_uuid() results_generator = engine.generate(prompt, sampling_params, request_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: running vllm engine in two gpus with a Falcon fine-tunned model I have this error when I tried to get a response from model using API example RuntimeError: CUDA error: an illegal memory access was encountered ## Error t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
