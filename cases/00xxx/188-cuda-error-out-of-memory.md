# vllm-project/vllm#188: CUDA error: out of memory

| 字段 | 值 |
| --- | --- |
| Issue | [#188](https://github.com/vllm-project/vllm/issues/188) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 54; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;sampling |
| 症状 | build_error;crash;mismatch;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> CUDA error: out of memory

### Issue 正文摘录

I successfully installed vLLM in WSL2, when I was trying to run the sample code, I got error info like this: ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="/mnt/d/github/text-generation-webui/models/facebook_opt-125m") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` INFO 06-21 21:40:02 llm_engine.py:59] Initializing an LLM engine with config: model='/mnt/d/github/text-generation-webui/models/facebook_opt-125m', dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 06-21 21:40:12 llm_engine.py:128] # GPU blocks: 37375, # CPU blocks: 7281 Traceback (most recent call last): File "/mnt/d/01Projects/vllm/prac_1.py", line 11, in llm = LLM(model="/mnt/d/github/text-generation-webui/models/facebook_opt-125m") File "/mnt/d/github/vllm/vllm/entrypoints...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: CUDA error: out of memory bug I successfully installed vLLM in WSL2, when I was trying to run the sample code, I got error info like this: ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: CUDA error: out of memory bug I successfully installed vLLM in WSL2, when I was trying to run the sample code, I got error info like this: ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is",
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: g: model='/mnt/d/github/text-generation-webui/models/facebook_opt-125m', dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 06-21 21:40:12 llm_eng...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ebui/models/facebook_opt-125m', dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 06-21 21:40:12 llm_engine.py:128] # GPU blocks: 37375, # CPU bl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="/mnt/d/github/text-generation-webui/models/facebook_opt-125m") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for out...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
