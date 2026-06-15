# vllm-project/vllm#9326: [Bug]: Gemma 27B Produces no Outputs (2B and 9B work fine)

| 字段 | 值 |
| --- | --- |
| Issue | [#9326](https://github.com/vllm-project/vllm/issues/9326) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 27B Produces no Outputs (2B and 9B work fine)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The 27B model does not produce outputs (9B and 2B do): ``` from vllm import LLM, SamplingParams # Set the model ID model_id = "google/gemma-2-27b-it" # Change model as needed tensor_parallel_size = 1 # Adjust as per your hardware # Sampling parameters sampling_params = SamplingParams( temperature=0.1, ) # Create an LLM instance llm = LLM( model=model_id, dtype="float16", max_model_len=4096, tensor_parallel_size=tensor_parallel_size, disable_custom_all_reduce=True, ) # Sample prompts prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Generate texts from the prompts outputs = llm.generate(prompts, sampling_params) # Print the outputs for output in outputs: prompt = output.prompt answer = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {answer!r}") # Output (no response): # Processed prompts: 100%|██████████| 4/4 [00:00<00:00, 10.31it/s, est. speed input: 67.01 toks/s, output: 164.95 toks/s] # Prompt: 'Hello, my name is', Generated text: '' # Prompt: 'The president of the United States is', Generated t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: g The 27B model does not produce outputs (9B and 2B do): ``` from vllm import LLM, SamplingParams # Set the model ID model_id = "google/gemma-2-27b-it" # Change model as needed tensor_parallel_size = 1 # Adjust as per y...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ture=0.1, ) # Create an LLM instance llm = LLM( model=model_id, dtype="float16", max_model_len=4096, tensor_parallel_size=tensor_parallel_size, disable_custom_all_reduce=True, ) # Sample prompts prompts = [ "Hello, my n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Gemma 27B Produces no Outputs (2B and 9B work fine) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The 27B model does not produce outputs (9B and 2B do): ``` fro
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Gemma 27B Produces no Outputs (2B and 9B work fine) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The 27B model does not produce outputs (9B and 2B do): ``` fro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
