# vllm-project/vllm#24681: [Bug]: ModuleNotFoundError: No module named 'vllm._C'

| 字段 | 值 |
| --- | --- |
| Issue | [#24681](https://github.com/vllm-project/vllm/issues/24681) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ModuleNotFoundError: No module named 'vllm._C'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm encountering a persistent error when using vllm. Whenever I run any model with the vllm serve command (e.g., vllm serve deepseek-ai/DeepSeek-R1-0528), I consistently get the following error: > ModuleNotFoundError: No module named 'vllm._C' ``` (vllm) root@node02:~/vllm# vllm serve Qwen/Qwen3-235B-A22B-Thinking-2507 INFO 09-12 00:52:19 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=1168) INFO 09-12 00:52:22 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=1168) INFO 09-12 00:52:22 [utils.py:326] non-default args: {'model_tag': 'Qwen/Qwen3-235B-A22B-Thinking-2507', 'model': 'Qwen/Qwen3-235B-A22B-Thinking-2507'} (APIServer pid=1168) ERROR 09-12 00:52:32 [registry.py:424] Error in inspecting model architecture 'Qwen3MoeForCausalLM' (APIServer pid=1168) ERROR 09-12 00:52:32 [registry.py:424] Traceback (most recent call last): (APIServer pid=1168) ERROR 09-12 00:52:32 [registry.py:424] File "/root/vllm/.venv/lib/python3.12/site-packages/vllm/model_executor/models/registry.py", line 834, in _run_in_subprocess (APIServer pid=1168) ERROR 09-12 00:52:32 [registry.py:424] returned.check_return...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: erver pid=1168) INFO 09-12 00:52:22 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=1168) INFO 09-12 00:52:22 [utils.py:326] non-default args: {'model_tag': 'Qwen/Qwen3-235B-A22B-Thinking-2507', 'mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: I'm encountering a persistent error when using vllm. Whenever I run any model with the vllm serve command (e.g., vllm serve deepseek-ai/DeepSeek-R1-0528), I consistently get the following error: > ModuleNotFoundError: N...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: entrypoints/cli/main.py", line 54, in main (APIServer pid=1168) args.dispatch_function(args) (APIServer pid=1168) File "/root/vllm/.venv/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line 50, in cmd (APIS...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 07 INFO 09-12 00:52:19 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=1168) INFO 09-12 00:52:22 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=1168) INFO 09-12 00:52:22 [uti...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: ModuleNotFoundError: No module named 'vllm._C' bug;stale ### Your current environment ### 🐛 Describe the bug I'm encountering a persistent error when using vllm. Whenever I run any model with the vllm serve comma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
