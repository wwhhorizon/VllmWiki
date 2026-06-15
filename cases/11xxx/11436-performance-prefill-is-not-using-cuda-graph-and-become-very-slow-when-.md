# vllm-project/vllm#11436: [Performance]: Prefill is not using cuda graph and become very slow when LORA enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#11436](https://github.com/vllm-project/vllm/issues/11436) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Prefill is not using cuda graph and become very slow when LORA enabled

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I noticed that the captured cuda graph is not used in prefill stage: https://github.com/vllm-project/vllm/blob/e51719ae72dd1dcdf55436a99ac8bed245b51422/vllm/worker/model_runner.py#L1644 And thus when the lora enabled, the prefill become a bottleneck of first token latency. e.g. Simply profile with llama2 base, the prefill stage take about ~25ms ``` python llm = LLM(model="/home/zhn/g/Llama-2-7b-hf") llm.start_profile() sampling_params = SamplingParams( top_p=0.9, temperature=0.7, max_tokens=10, stop=["[/assistant]"] ) for i in range(2): outputs_1 = llm.generate( prompts, sampling_params ) llm.stop_profile() ``` ![image](https://github.com/user-attachments/assets/db26657a-40bc-4a9d-a9d8-2b7966f68363) Now apply the lora, the lora model is same as https://docs.vllm.ai/en/latest/usage/lora.html, the prefill stage take about 105ms? ``` python llm = LLM(model="/home/zhn/g/Llama-2-7b-hf", enable_lora=True) llm.start_profile() sampling_params = SamplingParams( top_p=0.9, temperature=0.7, max_tokens=10, stop=["[/assistant]"] ) for i in range(2): outputs_1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: ssue? Can I force to use the captured cuda graph(If I will pad to the specific length), and will it help? [llama_lora.gz](https://github.com/user-attachments/files/18230818/llama_lora.gz) [llama_base.gz](https://github....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Performance]: Prefill is not using cuda graph and become very slow when LORA enabled performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: m-project/vllm/blob/e51719ae72dd1dcdf55436a99ac8bed245b51422/vllm/worker/model_runner.py#L1644 And thus when the lora enabled, the prefill become a bottleneck of first token latency. e.g. Simply profile with llama2 base...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I noticed that the captured cuda graph is not used in prefill stage: https://github.com/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Performance]: Prefill is not using cuda graph and become very slow when LORA enabled performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
