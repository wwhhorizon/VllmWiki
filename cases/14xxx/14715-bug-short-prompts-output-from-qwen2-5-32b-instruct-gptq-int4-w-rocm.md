# vllm-project/vllm#14715: [Bug]: Short prompts -> !!!!!!! output from Qwen2.5-32B-Instruct-GPTQ-Int4 w/ROCm

| 字段 | 值 |
| --- | --- |
| Issue | [#14715](https://github.com/vllm-project/vllm/issues/14715) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Short prompts -> !!!!!!! output from Qwen2.5-32B-Instruct-GPTQ-Int4 w/ROCm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using this exact model: https://huggingface.co/Qwen/Qwen2.5-32B-Instruct-GPTQ-Int4 Generation with ROCm generates a string of neverending `!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!` with short prompts. If the prompt is longer (e.g. tools are provided, or the user simply asks a longer question) then generation is fine. The same model works fine on CUDA. Command: ``` vllm serve --dtype auto --gpu-memory-utilization 0.95 --served-model-name qwen2.5:32b \ --max-model-len 16384 ~/models/Qwen2.5-32B-Instruct-GPTQ-Int4/ --enable-auto-tool-choice \ --tool-call-parser llama3_json --generation-config auto ``` Successful generation: ``` curl -sS -X POST http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{ "messages": [{"role": "user", "content": "hello"}], "stream": false, "model": "qwen2.5:32b" }' ``` Result: ``` {"id":"chatcmpl-06b26b685535420ba52eacebfce2a025","object":"chat.completion","created":1741829679,"model":"qwen2.5:32b","choices":[{"index":0,"message":{"role":"assistant","reasoning_content":null, "content":"Hello! How can I assist you today?","tool_calls":[]},"logprobs":null,"finish_reason":"stop","stop_reaso...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Short prompts -> !!!!!!! output from Qwen2.5-32B-Instruct-GPTQ-Int4 w/ROCm bug;stale ### Your current environment ### 🐛 Describe the bug Using this exact model: https://huggingface.co/Qwen/Qwen2.5-32B-Instruct-GP...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: equently asked questions. correctness activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_de...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Short prompts -> !!!!!!! output from Qwen2.5-32B-Instruct-GPTQ-Int4 w/ROCm bug;stale ### Your current environment ### 🐛 Describe the bug Using this exact model: https://huggingface.co/Qwen/Qwen2.5-32B-Instruct-GP...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ]: Short prompts -> !!!!!!! output from Qwen2.5-32B-Instruct-GPTQ-Int4 w/ROCm bug;stale ### Your current environment ### 🐛 Describe the bug Using this exact model: https://huggingface.co/Qwen/Qwen2.5-32B-Instruct-GPTQ-I...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: prompts -> !!!!!!! output from Qwen2.5-32B-Instruct-GPTQ-Int4 w/ROCm bug;stale ### Your current environment ### 🐛 Describe the bug Using this exact model: https://huggingface.co/Qwen/Qwen2.5-32B-Instruct-GPTQ-Int4 Gener...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
