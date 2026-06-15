# vllm-project/vllm#24797: [Bug]: Failing Qwen MoE EP Test in CI

| 字段 | 值 |
| --- | --- |
| Issue | [#24797](https://github.com/vllm-project/vllm/issues/24797) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failing Qwen MoE EP Test in CI

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug reproduce command: ``` CUDA_VISIBLE_DEVICES=1,2 VLLM_ALL2ALL_BACKEND=deepep_high_throughput VLLM_USE_DEEP_GEMM=1 VLLM_LOGGING_LEVEL=DEBUG python3 examples/offline_inference/data_parallel.py --model Qwen/Qwen1.5-MoE-A2.7B --tp-size=1 --dp-size=2 --max-model-len 2048 ``` it's the Qwen Distrubted Tests defined in CI file [.buildkite/test-pipeline.yaml](https://github.com/vllm-project/vllm/blob/89e08d6d180c76019daa5aa1bbf7759dfaedde2e/.buildkite/test-pipeline.yaml#L1036). What's the condition of triggering this CI test? ``` (EngineCore_DP1 pid=1125856) ERROR 09-12 22:51:58 [v1/engine/core.py:718] Traceback (most recent call last): (EngineCore_DP1 pid=1125856) ERROR 09-12 22:51:58 [v1/engine/core.py:718] File "/data/users/yming/gitrepos/vllm/vllm/v1/engine/core.py", line 705, in run_engine_core (EngineCore_DP1 pid=1125856) ERROR 09-12 22:51:58 [v1/engine/core.py:718] engine_core = DPEngineCoreProc(*args, **kwargs) (EngineCore_DP1 pid=1125856) ERROR 09-12 22:51:58 [v1/engine/core.py:718] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP1 pid=1125856) ERROR 09-12 22:51:58 [v1/engine/core.py:718] File "/data/users/yming/gitrepos/vllm/vllm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Failing Qwen MoE EP Test in CI bug;stale ### Your current environment ### 🐛 Describe the bug reproduce command: ``` CUDA_VISIBLE_DEVICES=1,2 VLLM_ALL2ALL_BACKEND=deepep_high_throughput VLLM_USE_DEEP_GEMM=1 VLLM_L...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: py:718] ComputedBuffer(name='buf2', layout=FixedLayout('cuda:0', torch.bfloat16, size=[s72, 2048], stride=[2048, 1]), data=Pointwise(device=device(type='cuda', index=0), dtype=torch.bfloat16, inner_fn= .inner. .inner_fn...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Failing Qwen MoE EP Test in CI bug;stale ### Your current environment ### 🐛 Describe the bug reproduce command: ``` CUDA_VISIBLE_DEVICES=1,2 VLLM_ALL2ALL_BACKEND=deepep_high_throughput VLLM_USE_DEEP_GEMM=1 VLLM_L...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Failing Qwen MoE EP Test in CI bug;stale ### Your current environment ### 🐛 Describe the bug reproduce command: ``` CUDA_VISIBLE_DEVICES=1,2 VLLM_ALL2ALL_BACKEND=deepep_high_throughput VLLM_USE_DEEP_GEMM=1 VLLM_L...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e the bug reproduce command: ``` CUDA_VISIBLE_DEVICES=1,2 VLLM_ALL2ALL_BACKEND=deepep_high_throughput VLLM_USE_DEEP_GEMM=1 VLLM_LOGGING_LEVEL=DEBUG python3 examples/offline_inference/data_parallel.py --model Qwen/Qwen1....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
