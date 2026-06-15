# vllm-project/vllm#15400: [Bug]: LoRA Loading Error: 'GPUModelRunner' object has no attribute 'lora_manager'

| 字段 | 值 |
| --- | --- |
| Issue | [#15400](https://github.com/vllm-project/vllm/issues/15400) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LoRA Loading Error: 'GPUModelRunner' object has no attribute 'lora_manager'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Bug Description When attempting to serve a Vision-Language Model (Qwen2.5-VL-7B-Instruct) with a LoRA adapter using vLLM's CLI, I encounter a `ValueError` indicating that `'GPUModelRunner' object has no attribute 'lora_manager'`. This suggests that LoRA support may not be properly implemented for vision-language models in vLLM. ## Command Used ```bash vllm serve Qwen/Qwen2.5-VL-7B-Instruct --max-model-len 8192 --limit-mm-per-prompt image=32 --enforce-eager --tensor-parallel-size 1 --port 20529 --gpu-memory-utilization 0.95 --lora-modules '{"name": "qwen-storyteller", "path": "/tmp/u020529/qwen-story-reasoning-lora-r16-b64-lr2e4/lora_adapter_final", "base_model_name": "Qwen/Qwen2.5-VL-7B-Instruct"}' ``` ``` ERROR 03-24 14:09:36 [core.py:389] Invocation of add_lora method failed ERROR 03-24 14:09:36 [core.py:389] Traceback (most recent call last): ERROR 03-24 14:09:36 [core.py:389] File "/tmp/u020529/envs/vLLM/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 386, in _handle_client_request ERROR 03-24 14:09:36 [core.py:389] output.result = method( ERROR 03-24 14:09:36 [core.py:389] ^^^^^^^ ERROR 03-24 14:09:36 [core.py:...

## 现有链接修复摘要

#41606 Bump the minor-update group across 1 directory with 140 updates | #41766 Bump the minor-update group across 1 directory with 141 updates | #41859 Bump the minor-update group across 1 directory with 141 updates | #42056 Bump the minor-update group across 1 directory with 142 updates | #42717 Bump the minor-update group across 1 directory with 143 updates

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: LoRA Loading Error: 'GPUModelRunner' object has no attribute 'lora_manager' bug ### Your current environment ### 🐛 Describe the bug ## Bug Description When attempting to serve a Vision-Language Model (Qwen2.5-VL-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: .12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/tmp/u020529/envs/vLLM/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ Fil...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 2/site-packages/vllm/entrypoints/cli/main.py", line 75, in main args.dispatch_function(args) File "/tmp/u020529/envs/vLLM/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line 33, in cmd uvloop.run(run_serve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: n3.12/site-packages/vllm/v1/engine/core.py", line 386, in _handle_client_request ERROR 03-24 14:09:36 [core.py:389] output.result = method( ERROR 03-24 14:09:36 [core.py:389] ^^^^^^^ ERROR 03-24 14:09:36 [core.py:389] F...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41606](https://github.com/vllm-project/vllm/pull/41606) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 140 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15400">#15400</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#41766](https://github.com/vllm-project/vllm/pull/41766) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15400">#15400</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#41859](https://github.com/vllm-project/vllm/pull/41859) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15400">#15400</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#42056](https://github.com/vllm-project/vllm/pull/42056) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 142 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15400">#15400</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#42717](https://github.com/vllm-project/vllm/pull/42717) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 143 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15400">#15400</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
