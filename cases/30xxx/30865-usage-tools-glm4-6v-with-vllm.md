# vllm-project/vllm#30865: [Usage]:Tools GLM4.6v with vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#30865](https://github.com/vllm-project/vllm/issues/30865) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:Tools GLM4.6v with vLLM

### Issue 正文摘录

### Your current environment Hello, I am running tests on this model, which I find excellent. However, I am encountering a few issues and would like to know whether it is possible to fix them or if I am simply asking for the impossible. First of all, here is my vLLM configuration: `docker run -d \ --name vllm-llm \ --gpus '"device=4,5,6,7"' \ -e NVIDIA_DRIVER_CAPABILITIES=compute,utility \ -e VLLM_OBJECT_STORAGE_SHM_BUFFER_NAME="${SHM_NAME}" \ -v /raid/workspace/qladane/vllm/hf-cache:/root/.cache/huggingface \ --env "HF_TOKEN=${HF_TOKEN:-}" \ -p 8003:8000 \ --ipc=host \ --restart unless-stopped \ vllm-openai:glm46v \ zai-org/GLM-4.6V-FP8 \ --tensor-parallel-size 4 \ --enforce-eager \ --served-model-name ImagineAI \ --allowed-local-media-path / \ --limit-mm-per-prompt '{"image": 1, "video": 0}' \ --max-model-len 131072 \ --dtype auto \ --kv-cache-dtype fp8 \ --gpu-memory-utilization 0.85 \ --reasoning-parser glm45 \ --tool-call-parser glm45 \ --enable-auto-tool-choice \ --enable-expert-parallel \ --mm-encoder-tp-mode data \ --mm-processor-cache-type shm` Next, here is my OpenWebUI configuration: I would like to know whether, with GLM-4.6V and OpenWebUI, it is possible to make the m...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: e;stale ### Your current environment Hello, I am running tests on this model, which I find excellent. However, I am encountering a few issues and would like to know whether it is possible to fix them or if I am simply a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: king for the impossible. First of all, here is my vLLM configuration: `docker run -d \ --name vllm-llm \ --gpus '"device=4,5,6,7"' \ -e NVIDIA_DRIVER_CAPABILITIES=compute,utility \ -e VLLM_OBJECT_STORAGE_SHM_BUFFER_NAME...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: =host \ --restart unless-stopped \ vllm-openai:glm46v \ zai-org/GLM-4.6V-FP8 \ --tensor-parallel-size 4 \ --enforce-eager \ --served-model-name ImagineAI \ --allowed-local-media-path / \ --limit-mm-per-prompt '{"image":...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: when it considers them relevant. At the moment: If it is an internet search, I have to manually activate the button, even though access is already available. If it is Python code, I have to click “execute”; it does not...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: t '{"image": 1, "video": 0}' \ --max-model-len 131072 \ --dtype auto \ --kv-cache-dtype fp8 \ --gpu-memory-utilization 0.85 \ --reasoning-parser glm45 \ --tool-call-parser glm45 \ --enable-auto-tool-choice \ --enable-ex...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
