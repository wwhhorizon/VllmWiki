# vllm-project/vllm#43528: [Bug]: vllm-openai nightly Docker image still fails due to missing pytest during EngineCore startup

| 字段 | 值 |
| --- | --- |
| Issue | [#43528](https://github.com/vllm-project/vllm/issues/43528) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm-openai nightly Docker image still fails due to missing pytest during EngineCore startup

### Issue 正文摘录

### Your current environment Docker image: vllm/vllm-openai:nightly https://hub.docker.com/layers/vllm/vllm-openai/nightly/images/sha256-2b5f940431016b25c461761cb813cebd1f02a9e4ba1069226a5c1c9ffb6834c6 vLLM version: 0.21.1rc1.dev262+g33d7cbe02 Model: RedHatAI/gemma-4-31B-it-NVFP4 Related issue: #43480 ### 🐛 Describe the bug I previously reported a similar startup failure in #43480, where the nightly Docker image failed because `pytest` was not installed and was imported indirectly via `humming` / `cupy.testing`. After pulling a newer nightly image, the original failure path seems to have changed, but the server still fails to start because `pytest` is missing. In this newer build, the model is loaded successfully, but `EngineCore` fails during startup while vLLM is initializing KV caches and running the profiling dummy run. The failure path is now roughly: ```text EngineCore startup -> _initialize_kv_caches -> determine_available_memory -> gpu_worker.profile_run -> gpu_model_runner._dummy_run -> torch._dynamo AOT compile -> torch.distributed.tensor.experimental._context_parallel._cp_custom_ops -> torch.library.custom_op / _register_fake -> inspect.getframeinfo / inspect.getmodule...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: vllm-openai nightly Docker image still fails due to missing pytest during EngineCore startup bug ### Your current environment Docker image: vllm/vllm-openai:nightly https://hub.docker.com/layers/vllm/vllm-openai/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: LLM version: 0.21.1rc1.dev262+g33d7cbe02 Model: RedHatAI/gemma-4-31B-it-NVFP4 Related issue: #43480 ### 🐛 Describe the bug I previously reported a similar startup failure in #43480, where the nightly Docker image failed...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: vllm-openai nightly Docker image still fails due to missing pytest during EngineCore startup bug ### Your current environment Docker image: vllm/vllm-openai:nightly https://hub.docker.com/layers/vllm/vllm-openai/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: a9e4ba1069226a5c1c9ffb6834c6 vLLM version: 0.21.1rc1.dev262+g33d7cbe02 Model: RedHatAI/gemma-4-31B-it-NVFP4 Related issue: #43480 ### 🐛 Describe the bug I previously reported a similar startup failure in #43480, where t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: File "/usr/lib/python3.12/inspect.py", line 1007, in getmodule if ismodule(module) and hasattr(module, '__file__'): File "/usr/local/lib/python3.12/dist-packages/cupy/testing/__init__.py", line 50, in from cupy.testing....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
