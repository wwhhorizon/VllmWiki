# vllm-project/vllm#12386: [Usage]: v0.6.6.post1 is incompatible with `pynvml==12.0.0`

| 字段 | 值 |
| --- | --- |
| Issue | [#12386](https://github.com/vllm-project/vllm/issues/12386) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: v0.6.6.post1 is incompatible with `pynvml==12.0.0`

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug # description - current vLLM version is trying to access cuda compatibility info via `pynvml.nvmlDeviceGetCudaComputeCapability(handle)` (`vllm/platforms/cuda.py:160`) - but instead is getting an error: `AttributeError: module 'pynvml' has no attribute 'nvmlDeviceGetCudaComputeCapability'` - resolved when I downgraded pynvml from 12.0.0 to 11.5.3 ## suggested action I'm still not sure if this was just my setup, but from my results it seems there's an incompatibility between vLLM & pynvml. I did a bit of searching & found out pynvml mirrors `nvidia-ml-py`, which is listed in the dependency tree of this version of vLLM w/o further research I'd suggest setting back the version of `nvidia-ml-py` in the required dependencies to be compatible with `pynvml==11.5.3` ![Image](https://github.com/user-attachments/assets/de419004-d58a-4395-8114-d4283d50f9e6) ![Image](https://github.com/user-attachments/assets/270bebae-dd75-4bc2-803e-896c2d9e6562) ## responsible code ```python vllm = LLM( model=config.base_model if config.base_model else config.model_id, tensor_parallel_size=num_gpus, dtype="auto", quantiza...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: mps _No response_ ### 🐛 Describe the bug # description - current vLLM version is trying to access cuda compatibility info via `pynvml.nvmlDeviceGetCudaComputeCapability(handle)` (`vllm/platforms/cuda.py:160`) - but inst...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ib/python3.10/site-packages/vllm/worker/model_runner.py:1048) needs_attn_backend = (num_attn_heads != 0 [1049](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/ad17a/OneDrive/Desktop/hackathons/aimo2/misc/aimo-pr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: scribe the bug # description - current vLLM version is trying to access cuda compatibility info via `pynvml.nvmlDeviceGetCudaComputeCapability(handle)` (`vllm/platforms/cuda.py:160`) - but instead is getting an error: `...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ompatible with `pynvml==12.0.0` bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug # description - current vLLM version is trying to access cuda compatibility info via `pynvml.nv...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: envs/aimo/lib/python3.10/site-packages/vllm/entrypoints/llm.py:233) self.request_counter = Counter() File ~/anaconda3/envs/aimo/lib/python3.10/site-packages/vllm/engine/llm_engine.py:517, in LLMEngine.from_engine_args(c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
