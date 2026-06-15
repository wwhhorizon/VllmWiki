# vllm-project/vllm#11814: [Bug]: Missing detection of BFloat16 for CPU ARM

| 字段 | 值 |
| --- | --- |
| Issue | [#11814](https://github.com/vllm-project/vllm/issues/11814) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;operator;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Missing detection of BFloat16 for CPU ARM

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug On CPU-ARM not all processors have support for bfloat16. In those case trying to run inference will crash like in the following stacktrace: ```log ERROR 01-07 18:11:29 engine.py:135] RuntimeError('"rms_norm_impl" not implemented for \'BFloat16\'') ERROR 01-07 18:11:29 engine.py:135] Traceback (most recent call last): ERROR 01-07 18:11:29 engine.py:135] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/multiprocessing/engine.py", line 133, in start ERROR 01-07 18:11:29 engine.py:135] self.run_engine_loop() ERROR 01-07 18:11:29 engine.py:135] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/multiprocessing/engine.py", line 196, in run_engine_loop ERROR 01-07 18:11:29 engine.py:135] request_outputs = self.engine_step() ERROR 01-07 18:11:29 engine.py:135] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/multiprocessing/engine.py", line 214, in engine_step ERROR 01-07 18:11:29 engine.py:135] raise e ERROR 01-07 18:11:29 engine.py:135] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/multiprocessing/engine.py", line 205, in engine_step ERROR 01-07 18:11:29 engine.py...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: t or not in vLLM code. I see to two ways to address this problem: - At build time: The easiest way. We need to check during the build for CPU if the host has support to it like in [cpu_extension.cpu](https://github.com/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Missing detection of BFloat16 for CPU ARM bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug On CPU-ARM not all processors have support for bfloat16. In those case t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: forward_cpu ERROR 01-07 18:11:29 engine.py:135] return self.forward_cuda(*args, **kwargs) ERROR 01-07 18:11:29 engine.py:135] File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/layernorm.py", line...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Missing detection of BFloat16 for CPU ARM bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug On CPU-ARM not all processors have support for bfloat16. In those case t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: n of BFloat16 for CPU ARM bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug On CPU-ARM not all processors have support for bfloat16. In those case trying to run inference...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
