# vllm-project/vllm#19656: [Bug]: Inductor codegen: fatal error: stddef.h: No such file or directory

| 字段 | 值 |
| --- | --- |
| Issue | [#19656](https://github.com/vllm-project/vllm/issues/19656) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inductor codegen: fatal error: stddef.h: No such file or directory

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Run a simple code with FA3. torch inductor seems to fail with a Triton compilation error. Tried to upgrade gcc but still facing same error. Stack trace: ```text INFO 06-14 21:52:14 [gpu_model_runner.py:1656] Model loading took 0.2389 GiB and 0.340157 seconds INFO 06-14 21:52:16 [backends.py:508] Using cache directory: /home/quinnzhu/.cache/vllm/torch_compile_cache/9eb7e1ffe1/rank_0_0/backbone for vLLM's torch.compile INFO 06-14 21:52:16 [backends.py:519] Dynamo bytecode transform time: 1.30 s In file included from /data/users/quinnzhu/venv/p312env/lib/python3.12/site-packages/triton/backends/nvidia/include/cuda.h:56, from /tmp/tmp23j1qrsv/main.c:1: /usr/include/stdlib.h:31:10: fatal error: stddef.h: No such file or directory 31 | #include | ^~~~~~~~~~ compilation terminated. ERROR 06-14 21:52:16 [core.py:515] EngineCore failed to start. ERROR 06-14 21:52:16 [core.py:515] Traceback (most recent call last): ERROR 06-14 21:52:16 [core.py:515] File "/data/users/quinnzhu/gitrepos/vllm/vllm/v1/engine/core.py", line 506, in run_engine_core ERROR 06-14 21:52:16 [core.py:515] engine_core = EngineCoreProc(*args, **kwargs) ERROR 06-14 21:52...

## 现有链接修复摘要

#16946 Update Qwen1.5-MoE-W4A16-compressed-tensors.yaml

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ctor codegen: fatal error: stddef.h: No such file or directory bug;torch.compile ### Your current environment ### 🐛 Describe the bug Run a simple code with FA3. torch inductor seems to fail with a Triton compilation err...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: r current environment ### 🐛 Describe the bug Run a simple code with FA3. torch inductor seems to fail with a Triton compilation error. Tried to upgrade gcc but still facing same error. Stack trace: ```text INFO 06-14 21...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: still facing same error. Stack trace: ```text INFO 06-14 21:52:14 [gpu_model_runner.py:1656] Model loading took 0.2389 GiB and 0.340157 seconds INFO 06-14 21:52:16 [backends.py:508] Using cache directory: /home/quinnzhu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: vailable_memory ERROR 06-14 21:52:16 [core.py:515] self.model_runner.profile_run() ERROR 06-14 21:52:16 [core.py:515] File "/data/users/quinnzhu/gitrepos/vllm/vllm/v1/worker/gpu_model_runner.py", line 2045, in profile_r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: venv/p312env/lib/python3.12/site-packages/triton/backends/nvidia/include/cuda.h:56, from /tmp/tmp23j1qrsv/main.c:1: /usr/include/stdlib.h:31:10: fatal error: stddef.h: No such file or directory 31 | #include | ^~~~~~~~~...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#16946](https://github.com/vllm-project/vllm/pull/16946) | mentioned | 0.6 | Update Qwen1.5-MoE-W4A16-compressed-tensors.yaml | om/vllm/ci/builds/18040/steps?jid=019656da-9848-4e2b-8586-58a9834eb439#019656da-9848-4e2b-8586-58a9834eb439/196-3109 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
