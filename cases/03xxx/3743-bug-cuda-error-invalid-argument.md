# vllm-project/vllm#3743: [Bug]: CUDA error: invalid argument 

| 字段 | 值 |
| --- | --- |
| Issue | [#3743](https://github.com/vllm-project/vllm/issues/3743) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA error: invalid argument 

### Issue 正文摘录

### Your current environment 在A800（80G显存） 2卡机器上启动两个qwen-14B的模型，一张卡上一个模型，第一个模型启动正常，但是在启动第二个模型的时候，vllm版本是0.3.3 ### 🐛 Describe the bug WARNING 03-29 18:28:18 tokenizer.py:64] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast tokenizer instead. INFO 03-29 18:28:50 llm_engine.py:357] # GPU blocks: 3531, # CPU blocks: 327 2024-03-29 18:28:51,319 xinference.core.worker 75 ERROR Failed to load model merge_qwen_ccb-1-0 Traceback (most recent call last): File "/app/xinference/xinference/core/worker.py", line 569, in launch_builtin_model await model_ref.load() File "/opt/xinference/xinference_venv/lib/python3.10/site-packages/xoscar/backends/context.py", line 227, in send return self._process_result_message(result) File "/opt/xinference/xinference_venv/lib/python3.10/site-packages/xoscar/backends/context.py", line 102, in _process_result_message raise message.as_instanceof_cause() File "/opt/xinference/xinference_venv/lib/python3.10/site-packages/xoscar/backends/pool.py", line 659, in send result = await self._run_coro(message.message_id, coro) File "/opt/xinference/xinference_venv/lib/python3.10/site-packages/xoscar/backends/pool.py", line 370, in _run_c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ght be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1. Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. 2024-03-29 18:28:51,875 xinference.api.restful_api 8 ERROR [address=0.0.0.0:43...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: argument bug;stale ### Your current environment 在A800（80G显存） 2卡机器上启动两个qwen-14B的模型，一张卡上一个模型，第一个模型启动正常，但是在启动第二个模型的时候，vllm版本是0.3.3 ### 🐛 Describe the bug WARNING 03-29 18:28:18 tokenizer.py:64] Using a slow tokenizer. This...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: CUDA error: invalid argument bug;stale ### Your current environment 在A800（80G显存） 2卡机器上启动两个qwen-14B的模型，一张卡上一个模型，第一个模型启动正常，但是在启动第二个模型的时候，vllm版本是0.3.3 ### 🐛 Describe the bug WARNING 03-29 18:28:18 tokenizer.py:64] U...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: g a fast tokenizer instead. INFO 03-29 18:28:50 llm_engine.py:357] # GPU blocks: 3531, # CPU blocks: 327 2024-03-29 18:28:51,319 xinference.core.worker 75 ERROR Failed to load model merge_qwen_ccb-1-0 Traceback (most re...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ile "/opt/xinference/xinference_venv/lib/python3.10/site-packages/xoscar/backends/context.py", line 227, in send return self._process_result_message(result) File "/opt/xinference/xinference_venv/lib/python3.10/site-pack...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
