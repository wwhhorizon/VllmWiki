# vllm-project/vllm#21932: [Bug]: vLLM can't load a unsloth-finetuned unsloth/Qwen3-8B-unsloth-bnb-4bit Model

| 字段 | 值 |
| --- | --- |
| Issue | [#21932](https://github.com/vllm-project/vllm/issues/21932) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM can't load a unsloth-finetuned unsloth/Qwen3-8B-unsloth-bnb-4bit Model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Before the finetune, I tried to load the unsloth/Qwen3-8B-unsloth-bnb-4bit model using vllm, and it works well. But after I finetuned the model following the unsloth document with QLora, and saved the merged 4bit model, the model can't be loaded with vllm with the following Error: Loading safetensors checkpoint shards: 0% Completed | 0/2 [00:00<?, ?it/s] ERROR 07-30 20:37:22 [core.py:586] EngineCore failed to start. ERROR 07-30 20:37:22 [core.py:586] Traceback (most recent call last): ERROR 07-30 20:37:22 [core.py:586] File "/root/miniconda3/envs/RunLLM/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 577, in run_engine_core ERROR 07-30 20:37:22 [core.py:586] engine_core = EngineCoreProc(*args, **kwargs) ERROR 07-30 20:37:22 [core.py:586] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 07-30 20:37:22 [core.py:586] File "/root/miniconda3/envs/RunLLM/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 404, in __init__ ERROR 07-30 20:37:22 [core.py:586] super().__init__(vllm_config, executor_class, log_stats, ERROR 07-30 20:37:22 [core.py:586] File "/root/miniconda3/envs/RunLLM/lib/python3.11/site-packages/vllm/v1/engine/core...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support cuda;triton build_error;crash env_dependency;shape Your current environme...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vLLM can't load a unsloth-finetuned unsloth/Qwen3-8B-unsloth-bnb-4bit Model bug ### Your current environment ### 🐛 Describe the bug Before the finetune, I tried to load the unsloth/Qwen3-8B-unsloth-bnb-4bit model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ror ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ild;distributed_parallel;gemm_linear;hardware_porting;model_support cuda;triton build_error;crash env_dependency;shape Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: vLLM can't load a unsloth-finetuned unsloth/Qwen3-8B-unsloth-bnb-4bit Model bug ### Your current environment ### 🐛 Describe the bug Before the finetune, I tried to load the unsloth/Qwen3-8B-unsloth-bnb-4bit model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
