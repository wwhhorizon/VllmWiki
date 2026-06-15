# vllm-project/vllm#20337: [Bug]: Meta-Llama-3.1-8B-Instruct-quantized.w8a8 fails to run on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#20337](https://github.com/vllm-project/vllm/issues/20337) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Meta-Llama-3.1-8B-Instruct-quantized.w8a8 fails to run on B200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It is easy to reproduce: `vllm bench throughput --model RedHatAI/Meta-Llama-3.1-8B-Instruct-quantized.w8a8 --load-format dummy --input-len 1000 --output-len 100 --max-model-len 32768` And we get error report: ```bash DEBUG 07-01 17:35:37 [wrapper.py:111] Dynamo transformed code saved to /home/wentao/.cache/vllm/torch_compile_cache/eed7e7c715/rank_0_0/backbone/transformed_code.py ERROR 07-01 17:35:38 [core.py:519] EngineCore failed to start. ERROR 07-01 17:35:38 [core.py:519] Traceback (most recent call last): ERROR 07-01 17:35:38 [core.py:519] File "/home/wentao/vllm-source/vllm/v1/engine/core.py", line 510, in run_engine_core ERROR 07-01 17:35:38 [core.py:519] engine_core = EngineCoreProc(*args, **kwargs) ERROR 07-01 17:35:38 [core.py:519] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 07-01 17:35:38 [core.py:519] File "/home/wentao/vllm-source/vllm/v1/engine/core.py", line 394, in __init__ ERROR 07-01 17:35:38 [core.py:519] super().__init__(vllm_config, executor_class, log_stats, ERROR 07-01 17:35:38 [core.py:519] File "/home/wentao/vllm-source/vllm/v1/engine/core.py", line 82, in __init__ ERROR 07-01 17:35:38 [core.py:519] self._initia...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: .py:111] Dynamo transformed code saved to /home/wentao/.cache/vllm/torch_compile_cache/eed7e7c715/rank_0_0/backbone/transformed_code.py ERROR 07-01 17:35:38 [core.py:519] EngineCore failed to start. ERROR 07-01 17:35:38...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Meta-Llama-3.1-8B-Instruct-quantized.w8a8 fails to run on B200 bug ### Your current environment ### 🐛 Describe the bug It is easy to reproduce: `vllm bench throughput --model RedHatAI/Meta-Llama-3.1-8B-Instruct-q...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ronment ### 🐛 Describe the bug It is easy to reproduce: `vllm bench throughput --model RedHatAI/Meta-Llama-3.1-8B-Instruct-quantized.w8a8 --load-format dummy --input-len 1000 --output-len 100 --max-model-len 32768` And...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: py:519] File "/home/wentao/vllm-source/vllm/compilation/cuda_piecewise_backend.py", line 112, in __call__ ERROR 07-01 17:35:38 [core.py:519] return self.compiled_graph_for_general_shape(*args) ERROR 07-01 17:35:38 [core...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Meta-Llama-3.1-8B-Instruct-quantized.w8a8 fails to run on B200 bug ### Your current environment ### 🐛 Describe the bug It is easy to reproduce: `vllm bench throughput --model RedHatAI/Meta-Llama-3.1-8B-Instruct-q...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
