# vllm-project/vllm#33508: [Bug]: AttributeError: 'Qwen3VLMoeConfig' object has no attribute 'vocab_size'

| 字段 | 值 |
| --- | --- |
| Issue | [#33508](https://github.com/vllm-project/vllm/issues/33508) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'Qwen3VLMoeConfig' object has no attribute 'vocab_size'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, thanks for the great work on vLLM. I am trying to deploy **Qwen/Qwen3-VL-235B-A22B-Instruct** locally following the official recipe: [https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-VL.html](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-VL.html) However, I encounter an error during startup. --- ### Command ```bash VLLM_USE_MODELSCOPE=true vllm serve \ --tensor-parallel-size 8 ``` --- ### Error Message ```text ERROR 02-01 01:50:11 engine.py:389] AttributeError: 'Qwen3VLMoeConfig' object has no attribute 'vocab_size' ``` --- ### Additional Information I checked the model’s `config.json`, and it **does include** the `vocab_size` field: ```json "vocab_size": 151936 ``` So it seems that `Qwen3VLMoeConfig` does not correctly expose or propagate `vocab_size`, even though it is present in the underlying config. --- ### Question * Is this a known compatibility issue between vLLM and `Qwen3VLMoeConfig`? * Is there a recommended workaround or patch? * Or is this a bug that should be fixed in vLLM? Any guidance would be appreciated. Thanks! ### Before submitting a new issue... - [x] Make sure you already searched...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: AttributeError: 'Qwen3VLMoeConfig' object has no attribute 'vocab_size' bug ### Your current environment ### 🐛 Describe the bug Hi, thanks for the great work on vLLM. I am trying to deploy **Qwen/Qwen3-VL-235B-A2...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: to deploy **Qwen/Qwen3-VL-235B-A22B-Instruct** locally following the official recipe: [https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-VL.html](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-VL.ht...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;speculative_decoding attention;cuda;operator;quantization;triton build_error;crash dtype;env_dependency;memory_layout Your current en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: AttributeError: 'Qwen3VLMoeConfig' object has no attribute 'vocab_size' bug ### Your current environment ### 🐛 Describe the bug Hi, thanks for the great work on vLLM. I am trying to deploy **Qwen/Qwen3-VL-235B-A2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
