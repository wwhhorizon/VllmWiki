# vllm-project/vllm#19043: [Bug]: vllm profiling result contains invalid utf-8 code

| 字段 | 值 |
| --- | --- |
| Issue | [#19043](https://github.com/vllm-project/vllm/issues/19043) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm profiling result contains invalid utf-8 code

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Profile result for meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 contains invalid utf-8 code Code to run the profile: ``` import os import time from vllm import LLM, SamplingParams # enable torch profiler, can also be set on cmd line os.environ["VLLM_TORCH_PROFILER_DIR"] = "/home/lunwenh/vllm/trace" # Sample prompts. prompts = [ "The future of AI is", "The future of AI is", "The future of AI is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=1) if __name__ == "__main__": # Create an LLM. llm = LLM( model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8", tensor_parallel_size=8, enforce_eager=True, seed=42, max_model_len=8000) llm.start_profile() # Generate texts from the prompts. The output is a list of RequestOutput # objects that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) llm.stop_profile() # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") # Add a buffe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: E-Instruct-FP8 contains invalid utf-8 code Code to run the profile: ``` import os import time from vllm import LLM, SamplingParams # enable torch profiler, can also be set on cmd line os.environ["VLLM_TORCH_PROFILER_DIR...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: he bug Profile result for meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 contains invalid utf-8 code Code to run the profile: ``` import os import time from vllm import LLM, SamplingParams # enable torch profiler, ca...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: current environment ### 🐛 Describe the bug Profile result for meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 contains invalid utf-8 code Code to run the profile: ``` import os import time from vllm import LLM, Sampli...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: vllm profiling result contains invalid utf-8 code bug;stale ### Your current environment ### 🐛 Describe the bug Profile result for meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 contains invalid utf-8 code Cod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: vllm profiling result contains invalid utf-8 code bug;stale ### Your current environment ### 🐛 Describe the bug Profile result for meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 contains invalid utf-8 code Cod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
