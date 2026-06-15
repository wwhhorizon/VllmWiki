# vllm-project/vllm#28838: [Bug]: engine monitor outputs unexpected error though the engine works well

| 字段 | 值 |
| --- | --- |
| Issue | [#28838](https://github.com/vllm-project/vllm/issues/28838) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: engine monitor outputs unexpected error though the engine works well

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am just running a minimal example, the `generate` ends with `finished=True` and returns successfully, but during the end of the program the engine monitor outputs `[core_client.py:598] Engine core proc EngineCore_DP0 died unexpectedly, shutting down client.` Related issue #23517 , but the solution to wrap the call in `main()` does not work for me. And there's no functionality issue, but this monitor and message seem to be confusing. ``` from vllm import LLM, SamplingParams if __name__ == '__main__': prompts = [ "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="QWen/QWen3-0.6B", max_model_len=512, max_num_seqs=4, gpu_memory_utilization=0.6) outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: issue, but this monitor and message seem to be confusing. ``` from vllm import LLM, SamplingParams if __name__ == '__main__': prompts = [ "The capital of France is", "The future of AI is", ] sampling_params = SamplingPa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="QWen/QWen3-0.6B", max_model_len=512, max_num_seqs=4, gpu_memory_utilization=0.6) outputs = llm.generate(prompts, sampling_params) for output in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: engine monitor outputs unexpected error though the engine works well bug;stale ### Your current environment ### 🐛 Describe the bug I am just running a minimal example, the `generate` ends with `finished=True` and return...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
