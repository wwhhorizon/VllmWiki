# vllm-project/vllm#1927: vLLM model serving server hangs when GPU KV cache usage reaches 10%

| 字段 | 值 |
| --- | --- |
| Issue | [#1927](https://github.com/vllm-project/vllm/issues/1927) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cache;cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> vLLM model serving server hangs when GPU KV cache usage reaches 10%

### Issue 正文摘录

Hello everybody, The server hangs when the GPU KV cache usage reaches 10%. ## Issue in Detail I attempted to serve the Llama2 7B Hugging Face model via vLLM on GPU by following the [API Server Quickstart guide](https://docs.vllm.ai/en/latest/getting_started/quickstart.html#api-server). In some instances, the model serving works correctly, processing the input prompt request successfully and returning a response. However, there are times when the model serving server accepts the input prompt request but becomes unresponsive and fails to provide any response to our request. Upon debugging, I identified that the issue is related to the GPU Key-Value cache usage. The model operates as expected when the GPU Key-Value cache usage is at 0.8%, but the server becomes unresponsive when it reaches 10%. ![working_case](https://github.com/vllm-project/vllm/assets/8547387/7786c229-505a-464c-87fc-63e53427aba2) The first image illustrates a **successful case** where the input prompt request works as expected, and the GPU KV cache usage is 0.8% (highlighted in yellow) ![non_working_case](https://github.com/vllm-project/vllm/assets/8547387/315547b3-afd7-43ff-9ab1-3e44503cbb3a) The second image depi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: hted in yellow). #### Details - GPU: NVIDIA Tesla T4 (16GB vRAM) - CUDA Version: 12.0 - Driver Version: 525.85.12 - vLLM version: 0.2.1.post1 - Hugginface model: meta-llama/Llama-2-7b-hf ## Steps to the replicate the er...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: vLLM model serving server hangs when GPU KV cache usage reaches 10% Hello everybody, The server hangs when the GPU KV cache usage reaches 10%. ## Issue in Detail I attempted to serve the Llama2 7B Hugging Face model via...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ghlighted in yellow). #### Details - GPU: NVIDIA Tesla T4 (16GB vRAM) - CUDA Version: 12.0 - Driver Version: 525.85.12 - vLLM version: 0.2.1.post1 - Hugginface model: meta-llama/Llama-2-7b-hf ## Steps to the replicate t...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: vLLM model serving server hangs when GPU KV cache usage reaches 10% Hello everybody, The server hangs when the GPU KV cache usage reaches 10%. ## Issue in Detail I attempted to serve the Llama2 7B Hugging Face model via...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nstances, the model serving works correctly, processing the input prompt request successfully and returning a response. However, there are times when the model serving server accepts the input prompt request but becomes...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
