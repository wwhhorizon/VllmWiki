# vllm-project/vllm#36450: [Bug]: Qwen3.5 AWQ models crash during inference on RTX 5090 (Blackwell) with Triton OOM in solve_tril despite successful model load

| 字段 | 值 |
| --- | --- |
| Issue | [#36450](https://github.com/vllm-project/vllm/issues/36450) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | shape_align |
| Operator 关键词 | attention;cache;cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;oom |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 AWQ models crash during inference on RTX 5090 (Blackwell) with Triton OOM in solve_tril despite successful model load

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving Qwen3.5 AWQ models with vLLM on an RTX 5090 (32GB VRAM), the model loads successfully, but crashes when the first inference request is sent. The server starts normally and finishes loading weights, but as soon as a request hits /v1/chat/completions, the engine crashes with: > RuntimeError: Triton Error [CUDA]: out of memory Important observation: - Model loads successfully - Crash only happens during inference - Happens with very small prompts - Happens with small models as well (9B AWQ) cmd used ``` docker run --gpus all \ -p 8888:8888 \ --ipc=host \ -v ~/.cache/huggingface:/root/.cache/huggingface \ vllm/vllm-openai:cu130-nightly \ QuantTrio/Qwen3.5-27B-AWQ \ --port 8888 \ --tensor-parallel-size 1 \ --reasoning-parser qwen3 \ --max-model-len 4096 \ --max-num-batched-tokens 4096 \ --enforce-eager ``` Example request: ``` { "model": "QuantTrio/Qwen3.5-27B-AWQ", "messages": [ {"role": "user", "content": "Hello"} ], "max_tokens": 64 } ``` model tested: > 1. QuantTrio/Qwen3.5-27B-AWQ > 2. QuantTrio/Qwen3.5-9B-AWQ > 3. ykarout/Qwen3.5-9b-nvfp4 > 4. cyankiwi/Qwen3.5-35B-A3B-AWQ-4bit Log: > /usr/local/lib/python3.12/dist-p...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: Qwen3.5 AWQ models crash during inference on RTX 5090 (Blackwell) with Triton OOM in solve_tril despite successful model load bug ### Your current environment ### 🐛 Describe the bug When serving Qwen3.5 AWQ model...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ngine crashes with: > RuntimeError: Triton Error [CUDA]: out of memory Important observation: - Model loads successfully - Crash only happens during inference - Happens with very small prompts - Happens with small model...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: gingface:/root/.cache/huggingface \ vllm/vllm-openai:cu130-nightly \ QuantTrio/Qwen3.5-27B-AWQ \ --port 8888 \ --tensor-parallel-size 1 \ --reasoning-parser qwen3 \ --max-model-len 4096 \ --max-num-batched-tokens 4096 \...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: RAM), the model loads successfully, but crashes when the first inference request is sent. The server starts normally and finishes loading weights, but as soon as a request hits /v1/chat/completions, the engine crashes w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: : Qwen3.5 AWQ models crash during inference on RTX 5090 (Blackwell) with Triton OOM in solve_tril despite successful model load bug ### Your current environment ### 🐛 Describe the bug When serving Qwen3.5 AWQ models wit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
