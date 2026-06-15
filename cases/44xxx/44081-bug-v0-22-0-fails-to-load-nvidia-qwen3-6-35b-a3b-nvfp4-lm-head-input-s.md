# vllm-project/vllm#44081: [Bug]: v0.22.0 fails to load nvidia/Qwen3.6-35B-A3B-NVFP4: lm_head.input_scale not registered

| 字段 | 值 |
| --- | --- |
| Issue | [#44081](https://github.com/vllm-project/vllm/issues/44081) |
| 状态 | open |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;moe;quantization;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | fp8;moe;quantization;triton |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.22.0 fails to load nvidia/Qwen3.6-35B-A3B-NVFP4: lm_head.input_scale not registered

### Issue 正文摘录

### Description `vllm/vllm-openai:v0.22.0` fails to load `nvidia/Qwen3.6-35B-A3B-NVFP4` with a `lm_head.input_scale` loader error. The same checkpoint previously loaded on a recent nightly image I had been using locally: - previous working image/version: `vllm/vllm-openai:nightly`, `0.21.1rc1.dev417+g22a58640b` - previous working image digest: `sha256:4cebac8c03f2cd9f5fabe72ac7c2a0b3aaa8450ef8f0e47429425fd1bfb83d42` After moving to the stable `v0.22.0` image, the model fails during weight loading before the server starts. ### Model `nvidia/Qwen3.6-35B-A3B-NVFP4` Local checkpoint index contains quantized `lm_head` entries: ```text lm_head.input_scale lm_head.weight lm_head.weight_scale lm_head.weight_scale_2 ``` ### Command ```bash docker run --rm \ --name vllm-qwen35-nvidia-sci \ --runtime nvidia \ --gpus all \ --ipc=host \ -p 8082:8000 \ -v /path/to/qwen3.6-35b-a3b-nvidia-nvfp4:/model:ro \ vllm/vllm-openai:v0.22.0 \ /model \ --served-model-name qwen35-nvidia-nvfp4-sci-thinking \ --host 0.0.0.0 \ --port 8000 \ --api-key local \ --trust-remote-code \ --max-model-len 131072 \ --max-num-seqs 1 \ --kv-cache-dtype fp8 \ --generation-config vllm \ --gpu-memory-utilization 0.94 \ --max-n...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: v0.22.0 fails to load nvidia/Qwen3.6-35B-A3B-NVFP4: lm_head.input_scale not registered ### Description `vllm/vllm-openai:v0.22.0` fails to load `nvidia/Qwen3.6-35B-A3B-NVFP4` with a `lm_head.input_scale` loader e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: recent nightly image I had been using locally: - previous working image/version: `vllm/vllm-openai:nightly`, `0.21.1rc1.dev417+g22a58640b` - previous working image digest: `sha256:4cebac8c03f2cd9f5fabe72ac7c2a0b3aaa8450...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: v0.22.0 fails to load nvidia/Qwen3.6-35B-A3B-NVFP4: lm_head.input_scale not registered ### Description `vllm/vllm-openai:v0.22.0` fails to load `nvidia/Qwen3.6-35B-A3B-NVFP4` with a `lm_head.input_scale` loader e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: --speculative-config '{"method":"mtp","num_speculative_tokens":3,"moe_backend":"triton"}' \ --quantization modelopt \ --enable-expert-parallel \ --enable-auto-tool-choice \ --reasoning-parser qwen3 \ --tool-call-parser...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ooks like a `ParallelLMHead` / quantized `lm_head` loader registration mismatch: the checkpoint provides `lm_head.input_scale`, `lm_head.weight_scale`, and `lm_head.weight_scale_2`, but vLLM only registers `lm_head.weig...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
