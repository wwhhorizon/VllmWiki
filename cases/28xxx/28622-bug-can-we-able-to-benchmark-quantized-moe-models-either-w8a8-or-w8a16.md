# vllm-project/vllm#28622: [Bug]: Can we able to benchmark Quantized MOE models Either W8A8 or W8A16 ?

| 字段 | 值 |
| --- | --- |
| Issue | [#28622](https://github.com/vllm-project/vllm/issues/28622) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can we able to benchmark Quantized MOE models Either W8A8 or W8A16 ?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Python Code which I used to Quantize the DeepseekMOE model ```from transformers import AutoTokenizer, AutoModelForCausalLM MODEL_ID = "deepseek-ai/deepseek-moe-16b-base" model = AutoModelForCausalLM.from_pretrained( MODEL_ID, device_map="auto", trust_remote_code=True ) tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True) from datasets import load_dataset NUM_CALIBRATION_SAMPLES = 1 MAX_SEQUENCE_LENGTH = 1 tokenizer.chat_template = """{% for message in messages %} {% if message['role'] == 'user' %}User: {{ message['content'] }} {% elif message['role'] == 'assistant' %}Assistant: {{ message['content'] }} {% endif %}{% endfor %}""" # Load and preprocess the dataset ds = load_dataset("HuggingFaceH4/ultrachat_200k", split="train_sft") ds = ds.shuffle(seed=42).select(range(NUM_CALIBRATION_SAMPLES)) def preprocess(example): return {"text": tokenizer.apply_chat_template(example["messages"], tokenize=False)} ds = ds.map(preprocess) def tokenize(sample): return tokenizer(sample["text"], padding=False, max_length=MAX_SEQUENCE_LENGTH, truncation=True, add_special_tokens=False) ds = ds.map(tokenize, remove_columns=ds.co...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: de which I used to Quantize the DeepseekMOE model ```from transformers import AutoTokenizer, AutoModelForCausalLM MODEL_ID = "deepseek-ai/deepseek-moe-16b-base" model = AutoModelForCausalLM.from_pretrained( MODEL_ID, de...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: 08] File "/data/users/logesh/vllm_new/env/lib/python3.10/site-packages/triton/language/core.py", line 42, in wrapper (EngineCore_DP0 pid=4149074) ERROR 11-13 12:51:26 [core.py:708] return fn(*args, **kwargs) (EngineCore...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Can we able to benchmark Quantized MOE models Either W8A8 or W8A16 ? bug;stale ### Your current environment ### 🐛 Describe the bug Python Code which I used to Quantize the DeepseekMOE model ```from transformers i...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: [Bug]: Can we able to benchmark Quantized MOE models Either W8A8 or W8A16 ? bug;stale ### Your current environment ### 🐛 Describe the bug Python Code which I used to Quantize the DeepseekMOE model ```from transformers i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: .modifiers.quantization import GPTQModifier from llmcompressor.modifiers.smoothquant import SmoothQuantModifier # Configure the quantization algorithms recipe = [ GPTQModifier( targets="Linear", scheme="W8A8", ignore=[...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
