# vllm-project/vllm#20475: [Bug]: The dual_chunk_flash_attn.py is not compatible with  vllm_flash_attn/flash_attn_interface

| 字段 | 值 |
| --- | --- |
| Issue | [#20475](https://github.com/vllm-project/vllm/issues/20475) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The dual_chunk_flash_attn.py is not compatible with  vllm_flash_attn/flash_attn_interface

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from transformers import AutoTokenizer from vllm import LLM, SamplingParams import os os.environ["VLLM_ATTENTION_BACKEND"] = 'DUAL_CHUNK_FLASH_ATTN' # Initialize the tokenizer tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B-Instruct-1M") # Pass the default decoding hyperparameters of Qwen2.5-7B-Instruct # max_tokens is for the maximum length for generation. sampling_params = SamplingParams(temperature=0.7, top_p=0.8, repetition_penalty=1.05, max_tokens=512) # Input the model name or path. See below for parameter explanation (after the example of openai-like server). llm = LLM(model="Qwen/Qwen2.5-7B-Instruct-1M", tensor_parallel_size=4, max_model_len=1010000, enable_chunked_prefill=True, max_num_batched_tokens=131072, enforce_eager=True, # quantization="fp8", # Enabling FP8 quantization for model weights can reduce memory usage. ) # Prepare your prompts prompt = "Tell me something about large language models." messages = [ {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."}, {"role": "user", "content": prompt} ] text = tokenizer.apply_chat_template( messages, t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rent environment ### 🐛 Describe the bug ```python from transformers import AutoTokenizer from vllm import LLM, SamplingParams import os os.environ["VLLM_ATTENTION_BACKEND"] = 'DUAL_CHUNK_FLASH_ATTN' # Initialize the tok...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: l=True, max_num_batched_tokens=131072, enforce_eager=True, # quantization="fp8", # Enabling FP8 quantization for model weights can reduce memory usage. ) # Prepare your prompts prompt = "Tell me something about large la...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: N' # Initialize the tokenizer tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B-Instruct-1M") # Pass the default decoding hyperparameters of Qwen2.5-7B-Instruct # max_tokens is for the maximum length for genera...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: om vllm import LLM, SamplingParams import os os.environ["VLLM_ATTENTION_BACKEND"] = 'DUAL_CHUNK_FLASH_ATTN' # Initialize the tokenizer tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B-Instruct-1M") # Pass the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ot! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
