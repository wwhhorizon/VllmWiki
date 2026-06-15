# vllm-project/vllm#27807: [Bug]: When using CPU to run examples/offline_inference/basic/basic.py, “RuntimeError: Device string must not be empty” is generated.

| 字段 | 值 |
| --- | --- |
| Issue | [#27807](https://github.com/vllm-project/vllm/issues/27807) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When using CPU to run examples/offline_inference/basic/basic.py, “RuntimeError: Device string must not be empty” is generated.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I use CPU to run examples/offline_inference/basic/basic.py, an error is generated: INFO 10-30 11:19:39 [__init__.py:245] No platform detected, vLLM is running on UnspecifiedPlatform INFO 10-30 11:19:40 [utils.py:328] non-default args: {'tensor_parallel_size': 2, 'disable_log_stats': True, 'enforce_eager': True, 'model': '/home/zwh/.cache/huggingface/Qwen3-8B'} Traceback (most recent call last): File "/home/zwh/workspace/vllm-cpu/test.py", line 34, in main() File "/home/zwh/workspace/vllm-cpu/test.py", line 18, in main llm = LLM(model="/home/zwh/.cache/huggingface/Qwen3-8B", enforce_eager=True, tensor_parallel_size=2) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/zwh/workspace/vllm-cpu/vllm/entrypoints/llm.py", line 270, in __init__ self.llm_engine = LLMEngine.from_engine_args( ^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/zwh/workspace/vllm-cpu/vllm/engine/llm_engine.py", line 485, in from_engine_args vllm_config = engine_args.create_engine_config(usage_context) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/zwh/workspace/vllm-cpu/vllm/engine/arg_utils.py",...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: or_parallel_size': 2, 'disable_log_stats': True, 'enforce_eager': True, 'model': '/home/zwh/.cache/huggingface/Qwen3-8B'} Traceback (most recent call last): File "/home/zwh/workspace/vllm-cpu/test.py", line 34, in main(...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 11:19:39 [__init__.py:245] No platform detected, vLLM is running on UnspecifiedPlatform INFO 10-30 11:19:40 [utils.py:328] non-default args: {'tensor_parallel_size': 2, 'disable_log_stats': True, 'enforce_eager': True,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pty ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ic.py, “RuntimeError: Device string must not be empty” is generated. bug;stale ### Your current environment ### 🐛 Describe the bug When I use CPU to run examples/offline_inference/basic/basic.py, an error is generated:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
