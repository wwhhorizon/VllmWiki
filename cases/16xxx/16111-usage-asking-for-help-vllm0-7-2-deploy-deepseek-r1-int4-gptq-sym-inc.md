# vllm-project/vllm#16111: [Usage]: Asking for help: vllm0.7.2 deploy DeepSeek-R1-int4-gptq-sym-inc

| 字段 | 值 |
| --- | --- |
| Issue | [#16111](https://github.com/vllm-project/vllm/issues/16111) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;moe;quantization |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Asking for help: vllm0.7.2 deploy DeepSeek-R1-int4-gptq-sym-inc

### Issue 正文摘录

### Your current environment - version: vllm0.7.2, python3.10 - devices: 8×H800 80G ### How would you like to use vllm I want to do INT4 Inference on CUDA but both offline and online failed, why? - model: [OPEA/DeepSeek-R1-int4-gptq-sym-inc](https://huggingface.co/OPEA/DeepSeek-R1-int4-gptq-sym-inc) follows the standard GPTQ format. - Offline inference: I used the recommended setting moe_wna16, but even after reducing the gpu_memory_utilization, I still encountered an OOM error at the very beginning. Additionally, moe_wna16 disables MLA (Model Linear Attention), and I'm not sure if this has any impact on performance. - Online serving: The vllm server can run normally, and I can access it using openai client. (examples/online_serving/openai_completion_client.py). However, when I use client.chat.completions.create, it times out. When I use client.completions.create, I do get a response, but the output text is garbled and unreadable. The codes and logs are below. ### 1. offline inference ``` from vllm import LLM, SamplingParams from transformers import AutoTokenizer model_path = "/data/public/model/DeepSeek-R1-int4-gptq-sym-inc" max_length = 1024 sampling_params = SamplingParams(max_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: eepSeek-R1-int4-gptq-sym-inc usage;stale ### Your current environment - version: vllm0.7.2, python3.10 - devices: 8×H800 80G ### How would you like to use vllm I want to do INT4 Inference on CUDA but both offline and on...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: to do INT4 Inference on CUDA but both offline and online failed, why? - model: [OPEA/DeepSeek-R1-int4-gptq-sym-inc](https://huggingface.co/OPEA/DeepSeek-R1-int4-gptq-sym-inc) follows the standard GPTQ format. - Offline...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ]: Asking for help: vllm0.7.2 deploy DeepSeek-R1-int4-gptq-sym-inc usage;stale ### Your current environment - version: vllm0.7.2, python3.10 - devices: 8×H800 80G ### How would you like to use vllm I want to do INT4 Inf...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Usage]: Asking for help: vllm0.7.2 deploy DeepSeek-R1-int4-gptq-sym-inc usage;stale ### Your current environment - version: vllm0.7.2, python3.10 - devices: 8×H800 80G ### How would you like to use vllm I want to do IN...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: andard GPTQ format. - Offline inference: I used the recommended setting moe_wna16, but even after reducing the gpu_memory_utilization, I still encountered an OOM error at the very beginning. Additionally, moe_wna16 disa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
