# vllm-project/vllm#19722: [Bug]: DeepGEMM does not work with CUDA Graph

| 字段 | 值 |
| --- | --- |
| Issue | [#19722](https://github.com/vllm-project/vllm/issues/19722) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepGEMM does not work with CUDA Graph

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` VLLM_ALL2ALL_BACKEND="deepep_high_throughput" VLLM_USE_DEEP_GEMM=1 vllm serve /data/deepseek-ai/DeepSeek-R1 -tp 8 -pp 2 --enable-expert-paralle ``` ``` (RayWorkerWrapper pid=3944622) (RayWorkerWrapper pid=3173774, ip=10.254.20.30) INFO 06-17 02:49:25 [gpu_model_runner.py:1659] Model loading took 41.0417 GiB and 15.405849 seconds (RayWorkerWrapper pid=3944613) DEBUG 06-17 02:49:26 [decorators.py:204] Start compiling function ERROR 06-17 02:49:27 [core.py:516] EngineCore failed to start. ERROR 06-17 02:49:27 [core.py:516] Traceback (most recent call last): ERROR 06-17 02:49:27 [core.py:516] File "/data/kebe/vllm/vllm/v1/engine/core.py", line 507, in run_engine_core ERROR 06-17 02:49:27 [core.py:516] engine_core = EngineCoreProc(*args, **kwargs) ERROR 06-17 02:49:27 [core.py:516] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 06-17 02:49:27 [core.py:516] File "/data/kebe/vllm/vllm/v1/engine/core.py", line 391, in __init__ ERROR 06-17 02:49:27 [core.py:516] super().__init__(vllm_config, executor_class, log_stats, ERROR 06-17 02:49:27 [core.py:516] File "/data/kebe/vllm/vllm/v1/engine/core.py", line 83, in __init__ ERROR 06-17 02:49:27 [co...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ne 239, in __call__ ERROR 06-17 02:49:27 [core.py:516] output = self.compiled_callable(*args, **kwargs) ERROR 06-17 02:49:27 [core.py:516] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 06-17 02:49:27 [core.py:516] File...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: d_impl ERROR 06-17 02:49:27 [core.py:516] final_hidden_states = self.quant_method.apply( ERROR 06-17 02:49:27 [core.py:516] File "/data/kebe/vllm/vllm/model_executor/layers/quantization/fp8.py", line 881, in apply ERROR...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: DeepGEMM does not work with CUDA Graph bug;stale ### Your current environment ### 🐛 Describe the bug ``` VLLM_ALL2ALL_BACKEND="deepep_high_throughput" VLLM_USE_DEEP_GEMM=1 vllm serve /data/deepseek-ai/DeepSeek-R1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: onment ### 🐛 Describe the bug ``` VLLM_ALL2ALL_BACKEND="deepep_high_throughput" VLLM_USE_DEEP_GEMM=1 vllm serve /data/deepseek-ai/DeepSeek-R1 -tp 8 -pp 2 --enable-expert-paralle ``` ``` (RayWorkerWrapper pid=3944622) (R...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: DeepGEMM does not work with CUDA Graph bug;stale ### Your current environment ### 🐛 Describe the bug ``` VLLM_ALL2ALL_BACKEND="deepep_high_throughput" VLLM_USE_DEEP_GEMM=1 vllm serve /data/deepseek-ai/DeepSeek-R1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
