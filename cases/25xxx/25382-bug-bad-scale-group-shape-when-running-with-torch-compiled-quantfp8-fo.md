# vllm-project/vllm#25382: [Bug]: Bad scale group shape when running with torch-compiled QuantFP8::forward_native

| 字段 | 值 |
| --- | --- |
| Issue | [#25382](https://github.com/vllm-project/vllm/issues/25382) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Bad scale group shape when running with torch-compiled QuantFP8::forward_native

### Issue 正文摘录

### 🐛 Describe the bug When running inference on block-quantized fp8 model (I used `llm = LLM(model="Qwen/Qwen3-30B-A3B-FP8")`) with torch.compile enabled, and `QuantFP8` interface, I'm running into this issue when running through compiled `forward_native()`: ``` (EngineCore_DP0 pid=862670) ERROR 09-22 07:40:53 [core.py:712] EngineCore failed to start. (EngineCore_DP0 pid=862670) ERROR 09-22 07:40:53 [core.py:712] Traceback (most recent call last): (EngineCore_DP0 pid=862670) ERROR 09-22 07:40:53 [core.py:712] File "/home/ElizaWszola/vllm/vllm/v1/engine/core.py", line 703, in run_engine_core (EngineCore_DP0 pid=862670) ERROR 09-22 07:40:53 [core.py:712] engine_core = EngineCoreProc(*args, **kwargs) (EngineCore_DP0 pid=862670) ERROR 09-22 07:40:53 [core.py:712] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=862670) ERROR 09-22 07:40:53 [core.py:712] File "/home/ElizaWszola/vllm/vllm/v1/engine/core.py", line 502, in __init__ (EngineCore_DP0 pid=862670) ERROR 09-22 07:40:53 [core.py:712] super().__init__(vllm_config, executor_class, log_stats, (EngineCore_DP0 pid=862670) ERROR 09-22 07:40:53 [core.py:712] File "/home/ElizaWszola/vllm/vllm/v1/engine/core.py", line 90, in __init__...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: e.py:712] File "/home/ElizaWszola/vllm/vllm/compilation/cuda_piecewise_backend.py", line 90, in __call__ (EngineCore_DP0 pid=862670) ERROR 09-22 07:40:53 [core.py:712] return self.compiled_graph_for_general_shape(*args)...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Bad scale group shape when running with torch-compiled QuantFP8::forward_native bug ### 🐛 Describe the bug When running inference on block-quantized fp8 model (I used `llm = LLM(model="Qwen/Qwen3-30B-A3B-FP8")`)...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Bad scale group shape when running with torch-compiled QuantFP8::forward_native bug ### 🐛 Describe the bug When running inference on block-quantized fp8 model (I used `llm = LLM(model="Qwen/Qwen3-30B-A3B-FP8")`)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: 2 07:40:53 [core.py:712] File "/home/ElizaWszola/vllm/vllm/compilation/cuda_graph.py", line 119, in __call__ (EngineCore_DP0 pid=862670) ERROR 09-22 07:40:53 [core.py:712] return self.runnable(*args, **kwargs) (EngineCo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ug ### 🐛 Describe the bug When running inference on block-quantized fp8 model (I used `llm = LLM(model="Qwen/Qwen3-30B-A3B-FP8")`) with torch.compile enabled, and `QuantFP8` interface, I'm running into this issue when r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
