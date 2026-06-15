# vllm-project/vllm#36245: [Bug]: Gemma3 mmproj-*.gguf is not downloaded in 'download_gguf'

| 字段 | 值 |
| --- | --- |
| Issue | [#36245](https://github.com/vllm-project/vllm/issues/36245) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma3 mmproj-*.gguf is not downloaded in 'download_gguf'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving gemma 3 gguf through the cli the mmproj-*.gguf file does not get downloaded from the 'download_gguf'. Minimal example: ``` vllm serve unsloth/gemma-3-27b-it-GGUF:Q4_K_S ``` Error: ``` (EngineCore_DP0 pid=951143) WARNING 03-06 18:12:47 [gguf_utils.py:119] (EngineCore_DP0 pid=951143) ERROR 03-06 18:12:48 [core.py:1006] EngineCore failed to start. (EngineCore_DP0 pid=951143) ERROR 03-06 18:12:48 [core.py:1006] Traceback (most recent call last): (EngineCore_DP0 pid=951143) ERROR 03-06 18:12:48 [core.py:1006] File "/raid/conda/envs/dacslab_vllm/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 996, in run_engine_core (EngineCore_DP0 pid=951143) ERROR 03-06 18:12:48 [core.py:1006] engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs) (EngineCore_DP0 pid=951143) ERROR 03-06 18:12:48 [core.py:1006] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=951143) ERROR 03-06 18:12:48 [core.py:1006] File "/raid/conda/envs/dacslab_vllm/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 740, in __init__ (EngineCore_DP0 pid=951143) ERROR 03-06 18:12:48 [core.py:1006] super().__init_...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Gemma3 mmproj-*.gguf is not downloaded in 'download_gguf' bug ### Your current environment ### 🐛 Describe the bug When serving gemma 3 gguf through the cli the mmproj-*.gguf file does not get downloaded from the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;ope...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: le. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ERROR 03-06 18:12:48 [core.py:1006] self.model_runner.load_model(eep_scale_up=eep_scale_up) (EngineCore_DP0 pid=951143) ERROR 03-06 18:12:48 [core.py:1006] File "/raid/conda/envs/dacslab_vllm/lib/python3.12/site-package...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
