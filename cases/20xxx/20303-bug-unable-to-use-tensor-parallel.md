# vllm-project/vllm#20303: [Bug]: Unable to use tensor parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#20303](https://github.com/vllm-project/vllm/issues/20303) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to use tensor parallel

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Failed to execute tensor parallel inference code: ``` python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="LLM-Research/Meta-Llama-3.1-8B-Instruct", tensor_parallel_size=8) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` crucial stderr output as below: ``` Failures have been detected while processing an MLIR pass pipeline /usr/local/bwlsoft/miniconda3/envs/kvcake/lib/python3.12/site-packages/vllm/attention/ops/prefix_prefill.py:36:0: note: Pipeline failed while executing [`ConvertTritonGPUToLLVM` on 'builtin.module' operation]: reproducer generated at `std::errs, please share the reproducer above with Triton project.` /usr/local/bwlsoft/miniconda3/envs/kvcake/lib/python3.12/site-packages/vllm/attention/ops/prefix_prefill.py:36:0: error: Failures have been detecte...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Failed to execute tensor parallel inference code: ``` python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="LLM-Research/Meta-Llama-3.1-8B-Instruct", tensor_parallel_size=8) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in output...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Unable to use tensor parallel bug;stale ### Your current environment ### 🐛 Describe the bug Failed to execute tensor parallel inference code: ``` python from vllm import LLM, SamplingParams prompts = [ "Hello, my...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: s/prefix_prefill.py:36:0: note: Pipeline failed while executing [`ConvertTritonGPUToLLVM` on 'builtin.module' operation]: reproducer generated at `std::errs, please share the reproducer above with Triton project.` /usr/...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [rank0]: return lambda *args, **kwargs: self.run(grid=grid, warmup=False, *args, **kwargs) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/usr/local/bwlsoft/miniconda3/envs/kvcake/lib/python3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
