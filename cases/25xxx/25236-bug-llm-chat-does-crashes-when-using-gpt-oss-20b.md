# vllm-project/vllm#25236: [Bug]: llm.chat does crashes when using gpt-oss 20b

| 字段 | 值 |
| --- | --- |
| Issue | [#25236](https://github.com/vllm-project/vllm/issues/25236) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: llm.chat does crashes when using gpt-oss 20b

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running this script does work for generate but not chat ```python from vllm import LLM, EngineArgs from vllm.utils import FlexibleArgumentParser def print_outputs(outputs): print("\nGenerated Outputs:\n" + "-" * 80) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}\n") print(f"Generated text: {generated_text!r}") print("-" * 80) llm = LLM(model="openai/gpt-oss-20b", tensor_parallel_size=2, gpu_memory_utilization=0.7,kv_cache_memory_bytes=26086055936) # In this script, we demonstrate how to pass input to the chat method: sampling_params = llm.get_default_sampling_params() prompts = [ "Write an essay about the importance of higher education.", ] outputs = llm.generate(prompts, sampling_params, use_tqdm=False) print_outputs(outputs) print("ok") conversation = [ {"role": "system", "content": "You are a helpful assistant"}, {"role": "user", "content": "Hello"}, {"role": "assistant", "content": "Hello! How can I assist you today?"}, { "role": "user", "content": "Write an essay about the importance of higher education.", }, ] conversations = [conversation for _ in range(10)]...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ing this script does work for generate but not chat ```python from vllm import LLM, EngineArgs from vllm.utils import FlexibleArgumentParser def print_outputs(outputs): print("\nGenerated Outputs:\n" + "-" * 80) for out...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: llm.chat does crashes when using gpt-oss 20b bug;stale ### Your current environment ### 🐛 Describe the bug Running this script does work for generate but not chat ```python from vllm import LLM, EngineArgs from v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: =108134) INFO 09-19 09:50:20 [custom_all_reduce.py:203] Registering 4067 cuda graph addresses (EngineCore_DP0 pid=108128) (Worker_TP1 pid=108136) INFO 09-19 09:50:21 [custom_all_reduce.py:203] Registering 4067 cuda grap...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: llm.chat does crashes when using gpt-oss 20b bug;stale ### Your current environment ### 🐛 Describe the bug Running this script does work for generate but not chat ```python from vllm import LLM, EngineArgs from v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ngineCore_DP0 pid=108128) INFO 09-19 09:50:21 [core.py:214] init engine (profile, create kv cache, warmup model) took 12.02 seconds INFO 09-19 09:50:23 [llm.py:314] Supported_tasks: ['generate'] Generated Outputs: -----...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
