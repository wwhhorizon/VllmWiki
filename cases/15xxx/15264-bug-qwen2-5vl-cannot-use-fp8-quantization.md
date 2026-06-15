# vllm-project/vllm#15264: [Bug]: qwen2.5vl cannot use fp8 quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#15264](https://github.com/vllm-project/vllm/issues/15264) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen2.5vl cannot use fp8 quantization

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using vllm 0.8.1 to deploy the qwen2.5-vl-7B model, fp8 quantization cannot be used. How can I solve this problem? The deployment command is as follows: `vllm serve Qwen2.5-VL/Qwen2.5-VL-7B-Instruct --port 8083 --quantization fp8` The error is as follows: ``` ...... Loading safetensors checkpoint shards: 100% Completed | 5/5 [00:03<00:00, 1.51it/s] INFO 03-21 02:21:53 [loader.py:429] Loading weights took 3.47 seconds INFO 03-21 02:21:53 [gpu_model_runner.py:1176] Model loading took 8.9031 GB and 3.891568 seconds INFO 03-21 02:21:53 [gpu_model_runner.py:1421] Encoder cache will be initialized with a budget of 98304 tokens, and profiled with 1 video items of the maximum feature size. ERROR 03-21 02:21:57 [core.py:340] EngineCore hit an exception: Traceback (most recent call last): ERROR 03-21 02:21:57 [core.py:340] File "/opt/venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 332, in run_engine_core ERROR 03-21 02:21:57 [core.py:340] engine_core = EngineCoreProc(*args, **kwargs) ERROR 03-21 02:21:57 [core.py:340] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 03-21 02:21:57 [core.py:340] File "/opt/venv/lib/python3.12/site...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: qwen2.5vl cannot use fp8 quantization bug ### Your current environment ### 🐛 Describe the bug When using vllm 0.8.1 to deploy the qwen2.5-vl-7B model, fp8 quantization cannot be used. How can I solve this problem...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: qwen2.5vl cannot use fp8 quantization bug ### Your current environment ### 🐛 Describe the bug When using vllm 0.8.1 to deploy the qwen2.5-vl-7B model, fp8 quantization cannot be used. How can I solve this problem...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;sampling_logits cuda;fp8;operator;quantization;sampling;trit...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: , line 184, in apply ERROR 03-21 02:21:57 [core.py:340] output = ops.cutlass_scaled_mm(qinput, ERROR 03-21 02:21:57 [core.py:340] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 03-21 02:21:57 [core.py:340] File "/opt/venv/lib/pyth...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
