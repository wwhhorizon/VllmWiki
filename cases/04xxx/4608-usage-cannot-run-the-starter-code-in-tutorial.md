# vllm-project/vllm#4608: [Usage]: Cannot run the starter code in tutorial

| 字段 | 值 |
| --- | --- |
| Issue | [#4608](https://github.com/vllm-project/vllm/issues/4608) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Cannot run the starter code in tutorial

### Issue 正文摘录

### Your current environment I am a new user who recently ran this starter code on my lab server: ``` import torch from vllm import LLM, SamplingParams # Clear any leftover memory from previous models torch.cuda.set_device('cuda:3') torch.cuda.empty_cache() prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="allenai/OLMo-1B-hf", device='cuda:3') outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` This piece of code always throws error: ``` --------------------------------------------------------------------------- AssertionError Traceback (most recent call last) Cell In[9], [line 16](vscode-notebook-cell:?execution_count=9&line=16) [8](vscode-notebook-cell:?execution_count=9&line=8) prompts = [ [9](vscode-notebook-cell:?execution_count=9&line=9) "Hello, my name is", [10](vscode-notebook-cell:?execution_count=9&line=10) "The president of the United States is",...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: I am a new user who recently ran this starter code on my lab server: ``` import torch from vllm import LLM, SamplingParams # Clear any leftover memory from previous models torch.cuda.set_device('cuda:3') torch.cuda.empt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: , SamplingParams # Clear any leftover memory from previous models torch.cuda.set_device('cuda:3') torch.cuda.empty_cache() prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: lm import LLM, SamplingParams # Clear any leftover memory from previous models torch.cuda.set_device('cuda:3') torch.cuda.empty_cache() prompts = [ "Hello, my name is", "The president of the United States is", "The capi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ard/.venv/lib/python3.10/site-packages/vllm/entrypoints/llm.py:125) self.request_counter = Counter() ... [153](https://vscode-remote+ssh-002dremote-002bdocjk-002dgpu-002d02.vscode-resource.vscode-cdn.net/home/21zz42/ope...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: izer_mode, skip_tokenizer_init, trust_remote_code, tensor_parallel_size, dtype, quantization, revision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, enforce_eager, max_context_len_to_capture, max_seq_le...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
