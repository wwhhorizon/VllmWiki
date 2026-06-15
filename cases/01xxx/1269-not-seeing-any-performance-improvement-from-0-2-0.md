# vllm-project/vllm#1269: Not seeing any performance improvement from 0.2.0

| 字段 | 值 |
| --- | --- |
| Issue | [#1269](https://github.com/vllm-project/vllm/issues/1269) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Not seeing any performance improvement from 0.2.0

### Issue 正文摘录

It was mentioned to have 60% performance improvement in latest release, I'm unable to utilize quantization since my GPU version is not compatible but compared to 0.1.8, the runtime performance is the same at 2.1 seconds. Am I doing something wrong in my config? Here are my specs: OS: Ubuntu 20.04 CUDA Version: 11.2 CPU: Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz CPU RAM: 200 GPU: Tesla V100-SXM2 32GB ``` prompts = """ Summarize the message below, delimited by triple backticks, using short bullet points. ```{message}``` BULLET POINT SUMMARY: """ from vllm import LLM, SamplingParams llm = LLM(model='meta-llama/Llama-2-13b-chat-hf, trust_remote_code=True, dtype="float16", tensor_parallel_size=1, gpu_memory_utilization=.95, disable_log_stats=True, tokenizer='hf-internal-testing/llama-tokenizer') sampling_params = SamplingParams(n = 1, best_of = 1, presence_penalty = 0, frequency_penalty = 0, temperature=0, top_p=1.0, top_k=-1, use_beam_search=False, stop=" ", max_tokens=1024) outputs = llm.generate(prompts, sampling_params) ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: performance is the same at 2.1 seconds. Am I doing something wrong in my config? Here are my specs: OS: Ubuntu 20.04 CUDA Version: 11.2 CPU: Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz CPU RAM: 200 GPU: Tesla V100-SXM2 32...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ment in latest release, I'm unable to utilize quantization since my GPU version is not compatible but compared to 0.1.8, the runtime performance is the same at 2.1 seconds. Am I doing something wrong in my config? Here...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ve 60% performance improvement in latest release, I'm unable to utilize quantization since my GPU version is not compatible but compared to 0.1.8, the runtime performance is the same at 2.1 seconds. Am I doing something...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: oing something wrong in my config? Here are my specs: OS: Ubuntu 20.04 CUDA Version: 11.2 CPU: Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz CPU RAM: 200 GPU: Tesla V100-SXM2 32GB ``` prompts = """ Summarize the message bel...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: uency_penalty = 0, temperature=0, top_p=1.0, top_k=-1, use_beam_search=False, stop=" ", max_tokens=1024) outputs = llm.generate(prompts, sampling_params) ``` performance frontend_api;model_support;quantization;sampling_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
