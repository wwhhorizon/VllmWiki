# vllm-project/vllm#14997: [Usage]: How to use vllm in parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#14997](https://github.com/vllm-project/vllm/issues/14997) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cuda;sampling |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to use vllm in parallel

### Issue 正文摘录

### Your current environment from vllm import LLM, SamplingParams llm = LLM( model="/Models/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B", tensor_parallel_size=2, # 2 张 GPU 处理张量并行 pipeline_parallel_size=2, # 2 张 GPU 处理管道并行 dtype="bfloat16", disable_ray=True ) # 采样参数 sampling_params = SamplingParams(temperature=0.7, top_p=0.9) # 生成测试文本 prompts = ["你好，大语言模型是什么？"] outputs = llm.generate(prompts, sampling_params) # 输出结果 for output in outputs: print(f"Prompt: {output.prompt}\nGenerated text: {output.outputs[0].text}") CUDA_VISIBLE_DEVICES=2,3 python code/API.py ### How would you like to use vllm 2025-03-18 11:21:32,945 INFO worker.py:1636 -- Connecting to existing Ray cluster at address: 192.168.1.216:6379... 2025-03-18 11:21:32,958 INFO worker.py:1812 -- Connected to Ray cluster. View the dashboard at 127.0.0.1:8265 WARNING 03-18 11:21:32 ray_utils.py:320] The number of required GPUs exceeds the total number of available GPUs in the placement group. INFO 03-18 11:21:42 ray_utils.py:214] Waiting for creating a placement group of specs for 10 seconds. specs=[{'node:192.168.1.216': 0.001, 'GPU': 1.0}, {'GPU': 1.0}, {'GPU': 1.0}, {'GPU': 1.0}]. Check `ray status` to see if you have enough res...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: use vllm in parallel usage;stale ### Your current environment from vllm import LLM, SamplingParams llm = LLM( model="/Models/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B", tensor_parallel_size=2, # 2 张 GPU 处理张量并行 pipeline_p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 2, # 2 张 GPU 处理张量并行 pipeline_parallel_size=2, # 2 张 GPU 处理管道并行 dtype="bfloat16", disable_ray=True ) # 采样参数 sampling_params = SamplingParams(temperature=0.7, top_p=0.9) # 生成测试文本 prompts = ["你好，大语言模型是什么？"] outputs = llm.g...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: urrent environment from vllm import LLM, SamplingParams llm = LLM( model="/Models/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B", tensor_parallel_size=2, # 2 张 GPU 处理张量并行 pipeline_parallel_size=2, # 2 张 GPU 处理管道并行 dtype="bfl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: How to use vllm in parallel usage;stale ### Your current environment from vllm import LLM, SamplingParams llm = LLM( model="/Models/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B", tensor_parallel_size=2, # 2 张 GPU 处...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t(f"Prompt: {output.prompt}\nGenerated text: {output.outputs[0].text}") CUDA_VISIBLE_DEVICES=2,3 python code/API.py ### How would you like to use vllm 2025-03-18 11:21:32,945 INFO worker.py:1636 -- Connecting to existin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
