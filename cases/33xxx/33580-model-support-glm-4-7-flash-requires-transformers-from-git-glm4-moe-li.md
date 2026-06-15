# vllm-project/vllm#33580: [Model Support] GLM-4.7-Flash requires transformers from git (glm4_moe_lite architecture)

| 字段 | 值 |
| --- | --- |
| Issue | [#33580](https://github.com/vllm-project/vllm/issues/33580) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;speculative_decoding |
| 子分类 | install |
| Operator 关键词 | cache |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Model Support] GLM-4.7-Flash requires transformers from git (glm4_moe_lite architecture)

### Issue 正文摘录

## Summary GLM-4.7-Flash (`zai-org/GLM-4.7-Flash`) fails to load with vLLM because the model uses the `glm4_moe_lite` architecture which is only available in transformers `main` branch, not in any released PyPI version. ## Error ``` pydantic_core._pydantic_core.ValidationError: 1 validation error for ModelConfig Value error, The checkpoint you are trying to load has model type `glm4_moe_lite` but Transformers does not recognize this architecture. ``` ## Environment - vLLM: 0.15.0 (latest) - vllm/vllm-openai:latest Docker image - Model: zai-org/GLM-4.7-Flash ## Workaround Install vLLM first, then force reinstall transformers from source: ```python # After pip install vllm pip install --upgrade huggingface_hub pip install --force-reinstall --no-deps git+https://github.com/huggingface/transformers.git@main ``` ## Request 1. Consider updating transformers version constraints once a release includes `glm4_moe_lite` 2. Add GLM-4.7-Flash to supported models documentation 3. The `glm47` tool-call-parser works, but `glm47` reasoning-parser doesn't exist (had to use `glm45`) ## Additional Context Successfully deployed with: - 1x H100 (80GB) - `--max-model-len 90000` (200k doesn't fit in KV...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: s only available in transformers `main` branch, not in any released PyPI version. ## Error ``` pydantic_core._pydantic_core.ValidationError: 1 validation error for ModelConfig Value error, The checkpoint you are trying...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Model Support] GLM-4.7-Flash requires transformers from git (glm4_moe_lite architecture) ## Summary GLM-4.7-Flash (`zai-org/GLM-4.7-Flash`) fails to load with vLLM because the model uses the `glm4_moe_lite` architecture
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: del Support] GLM-4.7-Flash requires transformers from git (glm4_moe_lite architecture) ## Summary GLM-4.7-Flash (`zai-org/GLM-4.7-Flash`) fails to load with vLLM because the model uses the `glm4_moe_lite` architecture w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: no-deps git+https://github.com/huggingface/transformers.git@main ``` ## Request 1. Consider updating transformers version constraints once a release includes `glm4_moe_lite` 2. Add GLM-4.7-Flash to supported models docu...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ed with: - 1x H100 (80GB) - `--max-model-len 90000` (200k doesn't fit in KV cache on single GPU) - `--speculative-config.method mtp --speculative-config.num_speculative_tokens 1` - `--tool-call-parser glm47 --reasoning-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
