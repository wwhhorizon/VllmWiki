# vllm-project/vllm#17344: [Bug]: Running `vllm serve Qwen2.5-VL-72B-Instruct-AWQ` results in an error when upgrading the vLLM version to 0.8.5.

| 字段 | 值 |
| --- | --- |
| Issue | [#17344](https://github.com/vllm-project/vllm/issues/17344) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Running `vllm serve Qwen2.5-VL-72B-Instruct-AWQ` results in an error when upgrading the vLLM version to 0.8.5.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Reproduce command: vllm serve /data/modelscope/Qwen2.5-VL-72B-Instruct-AWQ --max-model-len=32768 --limit-mm-per-prompt '{"image"=16}' --gpu-memory-utilization=0.9 Error output like below: ``` ERROR 04-29 10:42:00 [core.py:396] EngineCore failed to start. ERROR 04-29 10:42:00 [core.py:396] Traceback (most recent call last): ERROR 04-29 10:42:00 [core.py:396] File "/home/lucas/envs/nlp-vllm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 387, in run_engine_core ERROR 04-29 10:42:00 [core.py:396] engine_core = EngineCoreProc(*args, **kwargs) ERROR 04-29 10:42:00 [core.py:396] File "/home/lucas/envs/nlp-vllm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 329, in __init__ ERROR 04-29 10:42:00 [core.py:396] super().__init__(vllm_config, executor_class, log_stats, ERROR 04-29 10:42:00 [core.py:396] File "/home/lucas/envs/nlp-vllm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 71, in __init__ ERROR 04-29 10:42:00 [core.py:396] self._initialize_kv_caches(vllm_config) ERROR 04-29 10:42:00 [core.py:396] File "/home/lucas/envs/nlp-vllm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 129, in _init...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Qwen2.5-VL-72B-Instruct-AWQ` results in an error when upgrading the vLLM version to 0.8.5. bug;torch.compile ### Your current environment ### 🐛 Describe the bug Reproduce command: vllm serve /data/modelscope/Qwen2.5-VL-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: vailable_memory ERROR 04-29 10:42:00 [core.py:396] self.model_runner.profile_run() ERROR 04-29 10:42:00 [core.py:396] File "/home/lucas/envs/nlp-vllm/lib/python3.10/site-packages/vllm/v1/worker/gpu_model_runner.py", lin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: "/home/lucas/envs/nlp-vllm/lib/python3.10/site-packages/vllm/compilation/backends.py", line 612, in __call__ ERROR 04-29 10:42:00 [core.py:396] return self.compiled_graph_for_general_shape(*args) ERROR 04-29 10:42:00 [c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 96] File "/home/lucas/envs/nlp-vllm/lib/python3.10/site-packages/torch/cuda/__init__.py", line 985, in synchronize ERROR 04-29 10:42:00 [core.py:396] return torch._C._cuda_synchronize() ERROR 04-29 10:42:00 [core.py:396...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Running `vllm serve Qwen2.5-VL-72B-Instruct-AWQ` results in an error when upgrading the vLLM version to 0.8.5. bug;torch.compile ### Your current environment ### 🐛 Describe the bug Reproduce command: vllm serve /...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
