# vllm-project/vllm#23730: [Bug]: Only can run InternlVL3-8B-hf in eager mode, otherwise will face torch._dynamo.exc.Unsupported: Data-dependent branching problem.

| 字段 | 值 |
| --- | --- |
| Issue | [#23730](https://github.com/vllm-project/vllm/issues/23730) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Only can run InternlVL3-8B-hf in eager mode, otherwise will face torch._dynamo.exc.Unsupported: Data-dependent branching problem.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I tried to run the service: ```Shell vllm serve /OpenGVLab/InternVL3-8B-hf --host 0.0.0.0 --port 8080 ``` I got the bug messages like: ```log INFO 08-11 07:15:40 [default_loader.py:262] Loading weights took 6.57 seconds INFO 08-11 07:15:41 [gpu_model_runner.py:1970] Model loading took 14.8405 GiB and 17.700944 seconds INFO 08-11 07:15:43 [gpu_model_runner.py:2470] Encoder cache will be initialized with a budget of 2562 tokens, and profiled with 1 image items of the maximum feature size. ERROR 08-11 07:15:58 [core.py:667] EngineCore failed to start. ERROR 08-11 07:15:58 [core.py:667] Traceback (most recent call last): ERROR 08-11 07:15:58 [core.py:667] File "/workspace/project/vllm/vllm/v1/engine/core.py", line 658, in run_engine_core ERROR 08-11 07:15:58 [core.py:667] engine_core = EngineCoreProc(*args, **kwargs) ERROR 08-11 07:15:58 [core.py:667] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 08-11 07:15:58 [core.py:667] File "/workspace/project/vllm/vllm/v1/engine/core.py", line 474, in __init__ ERROR 08-11 07:15:58 [core.py:667] super().__init__(vllm_config, executor_class, log_stats, ERROR 08-11 07:15:58 [core.py:667] File "/work...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Only can run InternlVL3-8B-hf in eager mode, otherwise will face torch._dynamo.exc.Unsupported: Data-dependent branching problem. bug ### Your current environment ### 🐛 Describe the bug When I tried to run the se...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: /main.py", line 54, in main [1;36m(APIServer pid=201967)[0;0m args.dispatch_function(args) [1;36m(APIServer pid=201967)[0;0m File "/workspace/project/vllm/vllm/entrypoints/cli/serve.py", line 52, in cmd [1;36m(APIS...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ne 272, in __call__ ERROR 08-11 07:15:58 [core.py:667] output = self.compiled_callable(*args, **kwargs) ERROR 08-11 07:15:58 [core.py:667] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 08-11 07:15:58 [core.py:667] File...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: alLM has no vLLM implementation, and enforce eager mode will disable the CUDA Graph and Torch Dynamo, and avoid torch._dynamo.exc.Unsupported occur in the compile stage. However, in this way, the model will run in trans...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 470] Encoder cache will be initialized with a budget of 2562 tokens, and profiled with 1 image items of the maximum feature size. ERROR 08-11 07:15:58 [core.py:667] EngineCore failed to start. ERROR 08-11 07:15:58 [core...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23739: Should have ROCm label: NO (0 matches) #23730: Should have ROCm label: NO (0 matches) #23724: Should have ROCm label: NO (0 matches) #23720: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
