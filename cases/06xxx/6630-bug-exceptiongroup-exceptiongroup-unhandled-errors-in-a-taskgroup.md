# vllm-project/vllm#6630: [Bug]: exceptiongroup.ExceptionGroup: unhandled errors in a TaskGroup

| 字段 | 值 |
| --- | --- |
| Issue | [#6630](https://github.com/vllm-project/vllm/issues/6630) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: exceptiongroup.ExceptionGroup: unhandled errors in a TaskGroup

### Issue 正文摘录

### Your current environment ubuntu 22.04 cuda driver： ![image](https://github.com/user-attachments/assets/7eb39509-08e7-437f-ab67-6fa7b2b50f77) use official image: 0.4.0 or 0.5.0post1 GPU: RTX 4090, or A800 run inference of Qwen1.5-32B-GPTQ-int4, or deepseek-coder-34B-Instruct-AWQ. enable-prefix-caching, gpu-memory-utilization=0.9, max-model-len=8192, tensor-parallel-size=2. ### 🐛 Describe the bug 2024-07-22T10:38:57.216715364+08:00 INFO 07-22 10:38:57 async_llm_engine.py:154] Aborted request cmpl-b6da16012b2d46cdb9773cace1dad626. 2024-07-22T10:38:57.218681532+08:00 ERROR: Exception in ASGI application 2024-07-22T10:38:57.218694849+08:00 Traceback (most recent call last): 2024-07-22T10:38:57.218703600+08:00 File "/usr/local/lib/python3.10/dist-packages/starlette/responses.py", line 265, in __call__ 2024-07-22T10:38:57.218711308+08:00 await wrap(partial(self.listen_for_disconnect, receive)) 2024-07-22T10:38:57.218718705+08:00 File "/usr/local/lib/python3.10/dist-packages/starlette/responses.py", line 261, in wrap 2024-07-22T10:38:57.218725837+08:00 await func() 2024-07-22T10:38:57.218733370+08:00 File "/usr/local/lib/python3.10/dist-packages/starlette/responses.py", line 238, in l...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: or 0.5.0post1 GPU: RTX 4090, or A800 run inference of Qwen1.5-32B-GPTQ-int4, or deepseek-coder-34B-Instruct-AWQ. enable-prefix-caching, gpu-memory-utilization=0.9, max-model-len=8192, tensor-parallel-size=2. ### 🐛 Descr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 18955078+08:00 File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 756, in __call__ 2024-07-22T10:38:57.218961714+08:00 await self.middleware_stack(scope, receive, send) 2024-07-22T10:38:57.2189683...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: m/user-attachments/assets/7eb39509-08e7-437f-ab67-6fa7b2b50f77) use official image: 0.4.0 or 0.5.0post1 GPU: RTX 4090, or A800 run inference of Qwen1.5-32B-GPTQ-int4, or deepseek-coder-34B-Instruct-AWQ. enable-prefix-ca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: led errors in a TaskGroup bug ### Your current environment ubuntu 22.04 cuda driver： ![image](https://github.com/user-attachments/assets/7eb39509-08e7-437f-ab67-6fa7b2b50f77) use official image: 0.4.0 or 0.5.0post1 GPU:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: cial image: 0.4.0 or 0.5.0post1 GPU: RTX 4090, or A800 run inference of Qwen1.5-32B-GPTQ-int4, or deepseek-coder-34B-Instruct-AWQ. enable-prefix-caching, gpu-memory-utilization=0.9, max-model-len=8192, tensor-parallel-s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
