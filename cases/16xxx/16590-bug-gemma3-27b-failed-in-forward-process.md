# vllm-project/vllm#16590: [Bug]: Gemma3-27B failed in forward process

| 字段 | 值 |
| --- | --- |
| Issue | [#16590](https://github.com/vllm-project/vllm/issues/16590) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma3-27B failed in forward process

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams if __name__ == '__main__': # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model = 'models/gemma-3-27b-it',tensor_parallel_size=2,enable_prefix_caching=True) # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. print("\nGenerated Outputs:\n" + "-" * 60) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}") print(f"Output: {generated_text!r}") print("-" * 60) ``` ```bash ERROR 04-14 20:10:53 [core.py:390] Traceback (most recent call last): ERROR 04-14 20:10:53 [core.py:390] File "/mnt/dolphinfs/ssd_pool/docker/user/hadoop-aipnlp/INS/ruanjunhao04/miniforge3/envs/sglang/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 376,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams if __name__ == '__main__': # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Gemma3-27B failed in forward process bug;stale ### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams if __name__ == '__main__': # Sample prompts. prompts = [
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Gemma3-27B failed in forward process bug;stale ### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams if __name__ == '__main__': # Sample prompts. prompts = [ "Hello, m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: vailable_memory ERROR 04-14 20:10:53 [core.py:390] self.model_runner.profile_run() ERROR 04-14 20:10:53 [core.py:390] File "/mnt/dolphinfs/ssd_pool/docker/user/hadoop-aipnlp/INS/ruanjunhao04/miniforge3/envs/sglang/lib/p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
