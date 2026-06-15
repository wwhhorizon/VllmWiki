# vllm-project/vllm#8367: [Bug]: vLLM 0.6.0 produces CUDA error when loading quantized models (FP8)

| 字段 | 值 |
| --- | --- |
| Issue | [#8367](https://github.com/vllm-project/vllm/issues/8367) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;gemm_linear;model_support;quantization;sampling_logits |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;fp8;quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.6.0 produces CUDA error when loading quantized models (FP8)

### Issue 正文摘录

### Your current environment ```text Pytorch: 2.4.0-cuda12.1-cudnn9-devel Python: 3.11.9 vLLM: 0.6.0 ``` ### 🐛 Describe the bug **I try to run the following script to load the quantized model:** ```from vllm import LLM, SamplingParams from transformers import AutoTokenizer model_id = "neuralmagic/Qwen2-1.5B-Instruct-FP8" sampling_params = SamplingParams(temperature=0.6, top_p=0.9, max_tokens=256) tokenizer = AutoTokenizer.from_pretrained(model_id) messages = [ {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"}, {"role": "user", "content": "Who are you?"}, ] prompts = tokenizer.apply_chat_template(messages, tokenize=False) llm = LLM(model=model_id) outputs = llm.generate(prompts, sampling_params) generated_text = outputs[0].outputs[0].text print(generated_text) ``` **And I get the following CUDA error:** ```Loading safetensors checkpoint shards: 0% Completed | 0/1 [00:00<?, ?it/s] Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 4.25it/s] Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 4.25it/s] INFO 09-11 10:49:33 model_runner.py:926] Loading model weights took 1.6933 GB Process SpawnPro...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: to run the following script to load the quantized model:** ```from vllm import LLM, SamplingParams from transformers import AutoTokenizer model_id = "neuralmagic/Qwen2-1.5B-Instruct-FP8" sampling_params = SamplingParams...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: vLLM 0.6.0 produces CUDA error when loading quantized models (FP8) bug ### Your current environment ```text Pytorch: 2.4.0-cuda12.1-cudnn9-devel Python: 3.11.9 vLLM: 0.6.0 ``` ### 🐛 Describe the bug **I try to ru...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: vLLM 0.6.0 produces CUDA error when loading quantized models (FP8) bug ### Your current environment ```text Pytorch: 2.4.0-cuda12.1-cudnn9-devel Python: 3.11.9 vLLM: 0.6.0 ``` ### 🐛 Describe the bug **I try to ru...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: you?"}, ] prompts = tokenizer.apply_chat_template(messages, tokenize=False) llm = LLM(model=model_id) outputs = llm.generate(prompts, sampling_params) generated_text = outputs[0].outputs[0].text print(generated_text) ``...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vLLM 0.6.0 produces CUDA error when loading quantized models (FP8) bug ### Your current environment ```text Pytorch: 2.4.0-cuda12.1-cudnn9-devel Python: 3.11.9 vLLM: 0.6.0 ``` ### 🐛 Describe the bug **I try to ru...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
