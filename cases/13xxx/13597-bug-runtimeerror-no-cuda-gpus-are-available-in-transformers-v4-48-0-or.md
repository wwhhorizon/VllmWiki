# vllm-project/vllm#13597: [Bug]: RuntimeError: No CUDA GPUs are available in transformers v4.48.0 or above when running Ray RLHF example

| 字段 | 值 |
| --- | --- |
| Issue | [#13597](https://github.com/vllm-project/vllm/issues/13597) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: No CUDA GPUs are available in transformers v4.48.0 or above when running Ray RLHF example

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi for all! I failed to run the vLLM project RLHF example script. The code is exactly same as the vLLM docs page: https://docs.vllm.ai/en/latest/getting_started/examples/rlhf.html The error messages are: ``` (MyLLM pid=70946) ERROR 02-20 15:38:34 worker_base.py:574] Error executing method 'init_device'. This might cause deadlock in distributed execution. (MyLLM pid=70946) ERROR 02-20 15:38:34 worker_base.py:574] Traceback (most recent call last): (MyLLM pid=70946) ERROR 02-20 15:38:34 worker_base.py:574] File "/usr/local/miniconda3/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 566, in execute_method (MyLLM pid=70946) ERROR 02-20 15:38:34 worker_base.py:574] return run_method(target, method, args, kwargs) (MyLLM pid=70946) ERROR 02-20 15:38:34 worker_base.py:574] File "/usr/local/miniconda3/lib/python3.10/site-packages/vllm/utils.py", line 2220, in run_method (MyLLM pid=70946) ERROR 02-20 15:38:34 worker_base.py:574] return func(*args, **kwargs) (MyLLM pid=70946) ERROR 02-20 15:38:34 worker_base.py:574] File "/usr/local/miniconda3/lib/python3.10/site-packages/vllm/worker/worker.py", line 155, in init_device (MyLLM...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ove. Then I checked pip envs with `pip list` and found only transformers versions are different. I've tried to change vllm version between 0.7.0 and 0.7.2, the behavior is the same. I make a issue in transformers repo:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: A GPUs are available in transformers v4.48.0 or above when running Ray RLHF example bug;ray ### Your current environment ### 🐛 Describe the bug Hi for all! I failed to run the vLLM project RLHF example script. The code...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: RuntimeError: No CUDA GPUs are available in transformers v4.48.0 or above when running Ray RLHF example bug;ray ### Your current environment ### 🐛 Describe the bug Hi for all! I failed to run the vLLM project RLH...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error;crash env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: rker_base.py:574] Error executing method 'init_device'. This might cause deadlock in distributed execution. (MyLLM pid=70946) ERROR 02-20 15:38:34 worker_base.py:574] Traceback (most recent call last): (MyLLM pid=70946)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
