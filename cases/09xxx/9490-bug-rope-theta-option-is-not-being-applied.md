# vllm-project/vllm#9490: [Bug]: rope_theta option is not being applied.

| 字段 | 值 |
| --- | --- |
| Issue | [#9490](https://github.com/vllm-project/vllm/issues/9490) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: rope_theta option is not being applied.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```bash VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 \ python -m vllm.entrypoints.openai.api_server \ --model google/gemma-2-9b-it \ --max-model-len 16384 \ --rope-theta 80000 \ --gpu-memory-utilization 0.9 ``` When running vLLLM with the rope-theta setting as shown above, it doesn't seem to be applied. If it exceeds the default max-model-len (8192), it either doesn't output anything or generates strange words. However, when setting rope-theta through Hugging Face as shown below, it works well. It generates properly even when exceeding the default context length (8192). ```python model = AutoModelForCausalLM.from_pretrained( "google/gemma-2-9b-it", torch_dtype=torch.bfloat16, device_map='auto' ) mode.config.rope_theta = 80000 ``` I tried changing 'rope_theta' in config.json and running it with vLLM just in case, but it still doesn't work properly. How can I apply rope_theta? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots o...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error dtype;env_dependency Your curre...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: oModelForCausalLM.from_pretrained( "google/gemma-2-9b-it", torch_dtype=torch.bfloat16, device_map='auto' ) mode.config.rope_theta = 80000 ``` I tried changing 'rope_theta' in config.json and running it with vLLM just in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ta option is not being applied. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```bash VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 \ python -m vllm.entrypoints.openai.api_server \ --mode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ta? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
