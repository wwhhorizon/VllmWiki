# vllm-project/vllm#19427: [Bug]: Magistral-Small-2506 doesn't work

| 字段 | 值 |
| --- | --- |
| Issue | [#19427](https://github.com/vllm-project/vllm/issues/19427) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Magistral-Small-2506 doesn't work

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running it with the command where CUDA0, 1, 3, and 5 are 3090's `CUDA_VISIBLE_DEVICES=0,1,3,5 vllm serve /mnt/llms/models/mistralai/Magistral-Small-2506/ -tp 4 --max-model-len 12000 --host 0.0.0.0 --port 5000` Installed with: `uv venv --python 3.12 --seed` `source .venv/bin/activate.fish` `uv pip install -U vllm --extra-index-url https://wheels.vllm.ai/0.9.1rc1 --torch-backend=auto` I get the following error: ``` NFO 06-10 16:51:39 [__init__.py:244] Automatically detected platform cuda. INFO 06-10 16:51:47 [api_server.py:1287] vLLM API server version 0.9.1rc1 INFO 06-10 16:51:48 [cli_args.py:309] non-default args: {'host': '0.0.0.0', 'port': 5000, 'model': '/mnt/llms/models/mistralai/Magistral-Small-2506/', 'max_model_len': 12000, 'tensor_parallel_size': 4} INFO 06-10 16:52:00 [config.py:823] This model supports multiple tasks: {'score', 'embed', 'generate', 'classify', 'reward'}. Defaulting to 'generate'. INFO 06-10 16:52:00 [config.py:1946] Defaulting to use mp for distributed inference INFO 06-10 16:52:00 [config.py:2195] Chunked prefill is enabled with max_num_batched_tokens=2048. You are using the default legacy behaviour of...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: al-Small-2506/ -tp 4 --max-model-len 12000 --host 0.0.0.0 --port 5000` Installed with: `uv venv --python 3.12 --seed` `source .venv/bin/activate.fish` `uv pip install -U vllm --extra-index-url https://wheels.vllm.ai/0.9...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 3, and 5 are 3090's `CUDA_VISIBLE_DEVICES=0,1,3,5 vllm serve /mnt/llms/models/mistralai/Magistral-Small-2506/ -tp 4 --max-model-len 12000 --host 0.0.0.0 --port 5000` Installed with: `uv venv --python 3.12 --seed` `sourc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: nstall -U vllm --extra-index-url https://wheels.vllm.ai/0.9.1rc1 --torch-backend=auto` I get the following error: ``` NFO 06-10 16:51:39 [__init__.py:244] Automatically detected platform cuda. INFO 06-10 16:51:47 [api_s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Magistral-Small-2506 doesn't work bug ### Your current environment ### 🐛 Describe the bug Running it with the command where CUDA0, 1, 3, and 5 are 3090's `CUDA_VISIBLE_DEVICES=0,1,3,5 vllm serve /mnt/llms/models/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: p for distributed inference INFO 06-10 16:52:00 [config.py:2195] Chunked prefill is enabled with max_num_batched_tokens=2048. You are using the default legacy behaviour of the . This is expected, and simply means that t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
