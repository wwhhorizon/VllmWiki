# vllm-project/vllm#3878: [Bug]: vllm 0.4.0.post1 crashed when loading dbrx-instruct on AMD MI250x

| 字段 | 值 |
| --- | --- |
| Issue | [#3878](https://github.com/vllm-project/vllm/issues/3878) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.4.0.post1 crashed when loading dbrx-instruct on AMD MI250x

### Issue 正文摘录

### Your current environment * vllm (commit `db2a6a41e206abecf4128aba25117fcaf7bebe12`) + ROCm 6.0 Docker image built with the [fix of Dockerfile.rocm](https://github.com/vllm-project/vllm/issues/3862#issuecomment-2040448292) * 4x AMD MI250x GPUs (each MI250x has 2 GPU dies, total 512GB GPU memory) * model: [databricks/dbrx-instruct](https://huggingface.co/databricks/dbrx-instruct) ### 🐛 Describe the bug Ran vllm Docker image with `docker run --network=host --group-add=video --ipc=host --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --shm-size 32G --device /dev/kfd --device /dev/dri -v $model_dir:/app/model vllm-rocm:v0.4.0.post1 python -m vllm.entrypoints.openai.api_server --port 7860 --model /app/model/models--databricks--dbrx-instruct/snapshots/17365204e9cf13e2296ee984c1ab48071e861efa --trust-remote-code --tensor-parallel-size 8` The vllm server crashed soon after loading the model. ``` INFO 04-05 23:49:30 llm_engine.py:81] Initializing an LLM engine (v0.4.0.post1) with config: model='/app/model/models--databricks--dbrx-instruct/snapshots/17365204e9cf13e2296ee 984c1ab48071e861efa', speculative_config=None, tokenizer='/app/model/models--databricks--dbrx-instruct/snapshots...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: t * vllm (commit `db2a6a41e206abecf4128aba25117fcaf7bebe12`) + ROCm 6.0 Docker image built with the [fix of Dockerfile.rocm](https://github.com/vllm-project/vllm/issues/3862#issuecomment-2040448292) * 4x AMD MI250x GPUs...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=8, disable_c ustom_all_reduce=True, quantization...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: x AMD MI250x GPUs (each MI250x has 2 GPU dies, total 512GB GPU memory) * model: [databricks/dbrx-instruct](https://huggingface.co/databricks/dbrx-instruct) ### 🐛 Describe the bug Ran vllm Docker image with `docker run -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: INFO 04-05 23:49:46 selector.py:34] Cannot use FlashAttention backend for AMD GPUs. INFO 04-05 23:49:46 selector.py:25] Using XFormers backend.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ]: vllm 0.4.0.post1 crashed when loading dbrx-instruct on AMD MI250x bug;rocm;stale ### Your current environment * vllm (commit `db2a6a41e206abecf4128aba25117fcaf7bebe12`) + ROCm 6.0 Docker image built with the [fix of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
