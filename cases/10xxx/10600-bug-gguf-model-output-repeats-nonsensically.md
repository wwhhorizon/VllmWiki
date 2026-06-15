# vllm-project/vllm#10600: [Bug]: GGUF Model Output Repeats Nonsensically

| 字段 | 值 |
| --- | --- |
| Issue | [#10600](https://github.com/vllm-project/vllm/issues/10600) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GGUF Model Output Repeats Nonsensically

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using the following models: `MaziyarPanahi/Llama-3.2-1B-Instruct-GGUF`, `MaziyarPanahi/Llama-3.2-3B-Instruct-GGUF`, `Qwen/Qwen2-0.5B-Instruct-GGUF`, `Qwen/Qwen2.5-0.5B-Instruct-GGUF`, and `MaziyarPanahi/Qwen2-1.5B-Instruct-GGUF`, the models load correctly without errors. However, the output generated is nonsensical and consists only of repetitive characters such as "!!!!!!!!!!!!!!!!!!!!!!" instead of meaningful text. The following code and output are generated using Qwen/Qwen2.5-0.5B-Instruct. The code and results for the other models are similar. code: ```python import os os.environ['VLLM_LOGGING_LEVEL'] = 'DEBUG' from vllm import LLM, SamplingParams # In this script, we demonstrate how to pass input to the chat method: conversation = [ { "role": "system", "content": "You are a helpful assistant" }, { "role": "user", "content": "Hello" }, { "role": "assistant", "content": "Hello! How can I assist you today?" }, { "role": "user", "content": "Write an essay about the importance of higher education.", }, ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: GGUF Model Output Repeats Nonsensically bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using the following models: `MaziyarPanahi/Llama-3.2-1B-Instruct-GGUF`, `Ma...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: The code and results for the other models are similar. code: ```python import os os.environ['VLLM_LOGGING_LEVEL'] = 'DEBUG' from vllm import LLM, SamplingParams # In this script, we demonstrate how to pass input to the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: gguf_inference.py INFO 11-24 11:30:27 config.py:1861] Downcasting torch.float32 to torch.float16. INFO 11-24 11:30:32 config.py:350] This model supports multiple tasks: {'generate', 'embedding'}. Defaulting to 'generate...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 5B-Instruct") # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.chat(conversation, sampling_params) # Print...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: nfig=None, tokenizer='Qwen/Qwen2.5-0.5B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
