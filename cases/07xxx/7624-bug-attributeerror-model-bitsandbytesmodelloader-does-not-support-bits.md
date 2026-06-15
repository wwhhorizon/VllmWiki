# vllm-project/vllm#7624: [Bug]: AttributeError: Model BitsAndBytesModelLoader does not support BitsAndBytes quantization yet

| 字段 | 值 |
| --- | --- |
| Issue | [#7624](https://github.com/vllm-project/vllm/issues/7624) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: Model BitsAndBytesModelLoader does not support BitsAndBytes quantization yet

### Issue 正文摘录

### Your current environment LLM : v0.5.4 ``` llm = LLM(model= "unsloth/Qwen2-7B-Instruct-bnb-4bit" , dtype='bfloat16', gpu_memory_utilization=0.95, quantization="bitsandbytes", load_format="bitsandbytes", enforce_eager=True ) ``` I try to do inference using vllm from models in unsloth: https://huggingface.co/collections/unsloth/4bit-instruct-models-6624b1c17fd76cbcf4d435c8 however, some of the models work, such as `unsloth/Mistral-Nemo-Base-2407-bnb-4bit` , `unsloth/Phi-3-mini-4k-instruct-bnb-4bit` but some of them, such as `unsloth/Qwen2-7B-Instruct-bnb-4bit` , `unsloth/gemma-2-9b-it-bnb-4bit` May I know the reasons ? ### 🐛 Describe the bug > WARNING 08-17 07:20:49 config.py:254] bitsandbytes quantization is not fully optimized yet. The speed can be slower than non-quantized models. > INFO 08-17 07:20:49 llm_engine.py:174] Initializing an LLM engine (v0.5.4) with config: model='unsloth/Qwen2-7B-Instruct-bnb-4bit', speculative_config=None, tokenizer='unsloth/Qwen2-7B-Instruct-bnb-4bit', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, > dtype=torch.bfloat16, max_seq_len=32768, down...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: AttributeError: Model BitsAndBytesModelLoader does not support BitsAndBytes quantization yet bug ### Your current environment LLM : v0.5.4 ``` llm = LLM(model= "unsloth/Qwen2-7B-Instruct-bnb-4bit" , dtype='bfloat...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ributeError: Model BitsAndBytesModelLoader does not support BitsAndBytes quantization yet bug ### Your current environment LLM : v0.5.4 ``` llm = LLM(model= "unsloth/Qwen2-7B-Instruct-bnb-4bit" , dtype='bfloat16', gpu_m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: sModelLoader does not support BitsAndBytes quantization yet. performance ci_build;frontend_api;model_support;quantization cuda;quantization crash;slowdown dtype;env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: bug ### Your current environment LLM : v0.5.4 ``` llm = LLM(model= "unsloth/Qwen2-7B-Instruct-bnb-4bit" , dtype='bfloat16', gpu_memory_utilization=0.95, quantization="bitsandbytes", load_format="bitsandbytes", enforce_e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: AttributeError: Model BitsAndBytesModelLoader does not support BitsAndBytes quantization yet bug ### Your current environment LLM : v0.5.4 ``` llm = LLM(model= "unsloth/Qwen2-7B-Instruct-bnb-4bit" , dtype='bfloat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
