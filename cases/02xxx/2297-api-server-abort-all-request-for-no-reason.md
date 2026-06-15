# vllm-project/vllm#2297: API server abort all request for no reason

| 字段 | 值 |
| --- | --- |
| Issue | [#2297](https://github.com/vllm-project/vllm/issues/2297) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;quantization;sampling |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> API server abort all request for no reason

### Issue 正文摘录

### **Bug Description** After running and test vllm successfully with [NousResearch/Llama-2-7b-chat-hf](https://huggingface.co/NousResearch/Llama-2-7b-chat-hf) and [TheBloke/Llama-2-7b-Chat-AWQ](https://huggingface.co/TheBloke/Llama-2-7B-Chat-AWQ), I change llm to [vilm/vinallama-2.7b-chat](https://huggingface.co/vilm/vinallama-2.7b-chat) - a llama-2 family model. This time the API server still run successfully but abort any received request and did not raise any error. As first, I look through issue #546 and decided to quantize the model (using auto AWQ). However the quantized model still got the same issue. It couldn't be #633 or #273 case because the prompt input length is only 49 tokens and #677 won't be the case too because it failed from the first request. I wonder if model train with `bfloat16` datatype is the cause for this issue because vllm still work excellent with `Llama-2-7b-Chat` but not `vinallama-2.7b-chat`. **Update**: I tried command from @viktor-ferenczi [recommend solution](https://github.com/vllm-project/vllm/issues/1206#issuecomment-1868100562) in #1206 but the issue still remain. ### **Build script** `python -m vllm.entrypoints.openai.api_server --model="vil...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: escription** After running and test vllm successfully with [NousResearch/Llama-2-7b-chat-hf](https://huggingface.co/NousResearch/Llama-2-7b-chat-hf) and [TheBloke/Llama-2-7b-Chat-AWQ](https://huggingface.co/TheBloke/Lla...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: and did not raise any error. As first, I look through issue #546 and decided to quantize the model (using auto AWQ). However the quantized model still got the same issue. It couldn't be #633 or #273 case because the pro...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ot raise any error. As first, I look through issue #546 and decided to quantize the model (using auto AWQ). However the quantized model still got the same issue. It couldn't be #633 or #273 case because the prompt input...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Bug Description** After running and test vllm successfully with [NousResearch/Llama-2-7b-chat-hf](https://huggingface.co/NousResearch/Llama-2-7b-chat-hf) and [TheBloke/Llama-2-7b-Chat-AWQ](https://huggingface.co/TheBlok...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: bort all request for no reason ### **Bug Description** After running and test vllm successfully with [NousResearch/Llama-2-7b-chat-hf](https://huggingface.co/NousResearch/Llama-2-7b-chat-hf) and [TheBloke/Llama-2-7b-Cha...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
