# vllm-project/vllm#7491: [Bug]: Unable to generate output when add_eos_token = True for Mistral 7b instruct v0.1

| 字段 | 值 |
| --- | --- |
| Issue | [#7491](https://github.com/vllm-project/vllm/issues/7491) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to generate output when add_eos_token = True for Mistral 7b instruct v0.1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When `add_eos_token` is set to `true` in the `tokenizer_config.json`, see [link](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1/blob/1b62ab75912119a486ec97ad3f1a33259882a764/tokenizer_config.json#L3), vllm will generate empty output. ``` from vllm import LLM, SamplingParams def format_chat_prompt(prompt): return f"[INST]{prompt}[/INST]" prompts = ["What is the captial of Taiwan", "Where is the CEO of Nvida was born?"] tensor_parallel_size = 2 sampling_params = SamplingParams( temperature=0, max_tokens=512, repetition_penalty=1, seed=0 ) model_id = "mistralai/Mistral-7B-Instruct-v0.1" llm = LLM( model=model_id, tensor_parallel_size=tensor_parallel_size, dtype="float32", trust_remote_code=True, guided_decoding_backend="lm-format-enforcer", ) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` ### empty result when `add_eos_token` is set to `true` ``` Processed prompts: 100%|██████████| 2/2 [00:00<00:00, 36.19it/s, est. speed input: 398.99 toks/s, outp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: en `add_eos_token` is set to `true` in the `tokenizer_config.json`, see [link](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1/blob/1b62ab75912119a486ec97ad3f1a33259882a764/tokenizer_config.json#L3), vllm will...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: escribe the bug When `add_eos_token` is set to `true` in the `tokenizer_config.json`, see [link](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1/blob/1b62ab75912119a486ec97ad3f1a33259882a764/tokenizer_config.j...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ze, dtype="float32", trust_remote_code=True, guided_decoding_backend="lm-format-enforcer", ) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ( model=model_id, tensor_parallel_size=tensor_parallel_size, dtype="float32", trust_remote_code=True, guided_decoding_backend="lm-format-enforcer", ) outputs = llm.generate(prompts, sampling_params) # Print the outputs....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: uild;distributed_parallel;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
