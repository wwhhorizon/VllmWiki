# vllm-project/vllm#10344: [Misc]: Snowflake Arctic out of memory error with TP-8

| 字段 | 值 |
| --- | --- |
| Issue | [#10344](https://github.com/vllm-project/vllm/issues/10344) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: Snowflake Arctic out of memory error with TP-8

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", # "The president of the United States is", # "The capital of France is", # "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model="snowflake/snowflake-arctic-instruct", quantization="deepspeedfp", tensor_parallel_size=8, trust_remote_code=True, enforce_eager = True, load_format="auto", ) # gpu_memory_utilization=1,) # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` Error ```bash [rank0]: self.input_q = torch.ones(self.num_groups, [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.07 GiB. GPU 0 has a total capacity of 79.11 GiB...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", # "The president of the United States is", # "The capital of France is",...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Misc]: Snowflake Arctic out of memory error with TP-8 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams # Sample prompts. p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.07 GiB. GPU 0 has a total capacity of 79.11 GiB of which 1018.94 MiB is free. Process 2381604 has 78.11 GiB memory in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: of memory error with TP-8 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ion;sampling_logits;scheduler_memory cuda;operator;quantization;sampling;triton build_error;nan_inf;oom env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
