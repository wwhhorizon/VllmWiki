# vllm-project/vllm#3303: OAI Chat completions response contains chatml tokens for phi-2

| 字段 | 值 |
| --- | --- |
| Issue | [#3303](https://github.com/vllm-project/vllm/issues/3303) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> OAI Chat completions response contains chatml tokens for phi-2

### Issue 正文摘录

#### Context I am doing some performance comparison between [llama.cpp](https://github.com/ggerganov/llama.cpp/blob/master/examples/server/README.md) and vLLM in https://github.com/ggerganov/llama.cpp/pull/5941. When I am running vLLM 0bba88df03754c40bd9135fc2ff9554ffca59c87 with: ```shell python -m vllm.entrypoints.openai.api_server \ --model ai-dive/phi-2_GPTQ \ --served-model-name phi \ --trust-remote-code \ --gpu-memory-utilization 0.9 \ --max-num-seqs 8 ``` With the following chat completions request: ```shell curl -X POST http://localhost:8000/v1/chat/completions -H 'content-type:application/json' --data '{"messages":[{"role":"system","content":"You are ChatGPT, an AI assistant."},{"role":"user","content":"Summarize the main ideas of Jeff Walker''''s Product Launch Formula into bullet points as it pertains to a growth marketing agency implementing these strategies and tactics for their clients..."}],"model":"phi","stream":false,"max_tokens":512}' ``` I got: ```json { "id": "cmpl-50146e536acb49778d7341db4a7fd7b2", "object": "chat.completion", "created": 1924, "model": "phi", "choices": [ { "index": 0, "message": { "role": "assistant", "content": "The main ideas of Jeff Walker...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ategy that effectively communicates the value proposition\n- Utilizing social media and digital marketing channels to reach the target audience\n- Implementing a sales strategy that focuses on lead generation and conver...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: for phi-2 #### Context I am doing some performance comparison between [llama.cpp](https://github.com/ggerganov/llama.cpp/blob/master/examples/server/README.md) and vLLM in https://github.com/ggerganov/llama.cpp/pull/594...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: eas of Jeff Walkers Product Launch Formula are:\n- Conducting market research and analysis to understand the competition and the target audience\n- Developing a unique value proposition for the product or service\n- Cre...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: .co/ai-dive/phi-2_GPTQ/tree/main) ? Note: I want to compare results on quantized models (phi-gptq vs phi-gguf-q4_k_m) on small GPU device, here a `NVIDIA GeForce RTX 3050`. Thanks performance frontend_api;model_support;...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: strategies and tactics for their clients..."}],"model":"phi","stream":false,"max_tokens":512}' ``` I got: ```json { "id": "cmpl-50146e536acb49778d7341db4a7fd7b2", "object": "chat.completion", "created": 1924, "model": "...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
