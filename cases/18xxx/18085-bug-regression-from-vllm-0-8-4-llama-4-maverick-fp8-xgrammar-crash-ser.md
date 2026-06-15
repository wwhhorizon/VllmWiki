# vllm-project/vllm#18085: [Bug]: regression from vllm==0.8.4 - Llama 4 Maverick FP8 + xgrammar crash server

| 字段 | 值 |
| --- | --- |
| Issue | [#18085](https://github.com/vllm-project/vllm/issues/18085) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;gemm;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: regression from vllm==0.8.4 - Llama 4 Maverick FP8 + xgrammar crash server

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When [the official Maverick FP8 hugginface checkpoint](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8) is launched with `--guided-decoding-backend xgrammar` (or auto, which defaults to xgrammar anyway), any guided json request would crash the server while the model server responds with gibberish outputs. command to launch vLLM server: ```bash vllm serve meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 \ --served-model-name meta-llama/llama-4-maverick-17b-128e-instruct-fp8 \ --gpu-memory-utilization 0.93 \ --tensor-parallel-size 8 \ --max-model-len 1048576 \ --enable-chunked-prefill \ --max-num-batched-tokens 16384 \ --max-num-seqs 16 \ --kv-cache-dtype fp8 \ --enable-auto-tool-choice \ --tool-call-parser llama4_json \ --limit-mm-per-prompt 'image=5' \ --override-generation-config '{"attn_temperature_tuning":true}' ``` sample guided decoding request (any kind of `guided_json` request that I have tried would crash, no "safe" sample request AFAIK) ```python from openai import OpenAI client = OpenAI(base_url="http://localhost:8080/v1") messages=[ {"role": "user", "content": "\nYou are an expert data analyst...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ## Your current environment ### 🐛 Describe the bug When [the official Maverick FP8 hugginface checkpoint](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8) is launched with `--guided-decoding-bac...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: regression from vllm==0.8.4 - Llama 4 Maverick FP8 + xgrammar crash server bug ### Your current environment ### 🐛 Describe the bug When [the official Maverick FP8 hugginface checkpoint](https://huggingface.co/met...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: xgrammar` (or auto, which defaults to xgrammar anyway), any guided json request would crash the server while the model server responds with gibberish outputs. command to launch vLLM server: ```bash vllm serve meta-llama...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: regression from vllm==0.8.4 - Llama 4 Maverick FP8 + xgrammar crash server bug ### Your current environment ### 🐛 Describe the bug When [the official Maverick FP8 hugginface checkpoint](https://huggingface.co/met...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ma-4-Maverick-17B-128E-Instruct-FP8) is launched with `--guided-decoding-backend xgrammar` (or auto, which defaults to xgrammar anyway), any guided json request would crash the server while the model server responds wit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
