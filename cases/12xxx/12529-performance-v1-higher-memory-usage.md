# vllm-project/vllm#12529: [Performance]: V1 higher memory usage

| 字段 | 值 |
| --- | --- |
| Issue | [#12529](https://github.com/vllm-project/vllm/issues/12529) |
| 状态 | closed |
| 标签 | performance;v1 |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: V1 higher memory usage

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression *Hardware:* 4x RTX 3070 = 32GB VRAM *Issue:* I was able to run `Qwen/Qwen2.5-Coder-32B-Instruct-GPTQ-Int4` with 12K context length with 0.6.x, now with `0.7.0 + VLLM_USE_V1=1` I cannot push the context length higher than 3K or encountering a CUDA OOM error. Of course, I can reconfigure it to avoid OOM, my question is: *Is V1 expected to consume more memory?* Some of the libraries: ``` flashinfer==0.1.6+cu124torch2.4 torch==2.5.1 transformers==4.48.1 vllm==0.7.0 ``` *VLLM command* ``` - vllm - serve - Qwen/Qwen2.5-Coder-32B-Instruct-GPTQ-Int4 - --gpu-memory-utilization=1 - --tensor-parallel-size=4 - --load-format=auto - --enforce-eager - --swap-space=0 - --max-model-len=12K - --max-num-batched-tokens=12K - --disable-fastapi-docs - --trust-remote-code - --enable-auto-tool-choice - --tool-call-parser=hermes ``` Thanks ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ession *Hardware:* 4x RTX 3070 = 32GB VRAM *Issue:* I was able to run `Qwen/Qwen2.5-Coder-32B-Instruct-GPTQ-Int4` with 12K context length with 0.6.x, now with `0.7.0 + VLLM_USE_V1=1` I cannot push the context length hig...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: B VRAM *Issue:* I was able to run `Qwen/Qwen2.5-Coder-32B-Instruct-GPTQ-Int4` with 12K context length with 0.6.x, now with `0.7.0 + VLLM_USE_V1=1` I cannot push the context length higher than 3K or encountering a CUDA O...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nce _No response_ ### Report of performance regression *Hardware:* 4x RTX 3070 = 32GB VRAM *Issue:* I was able to run `Qwen/Qwen2.5-Coder-32B-Instruct-GPTQ-Int4` with 12K context length with 0.6.x, now with `0.7.0 + VLL...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression *Hardware:* 4x RTX 3070 = 32GB VRAM *Issue:* I was able to run `Qwen/Qwen2.5-Coder-32B-Instruct-GPTQ-Int4` with 12K context length with 0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: is: *Is V1 expected to consume more memory?* Some of the libraries: ``` flashinfer==0.1.6+cu124torch2.4 torch==2.5.1 transformers==4.48.1 vllm==0.7.0 ``` *VLLM command* ``` - vllm - serve - Qwen/Qwen2.5-Coder-32B-Instru...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
