# vllm-project/vllm#2248: Recent vLLMs ask for too much memory: ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initializing the engine.

| 字段 | 值 |
| --- | --- |
| Issue | [#2248](https://github.com/vllm-project/vllm/issues/2248) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 54; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Recent vLLMs ask for too much memory: ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initializing the engine.

### Issue 正文摘录

Since vLLM 0.2.5, we can't even run llama-2 70B 4bit AWQ on 4*A10G anymore, have to use old vLLM. Similar problems even trying to be two 7b models on 80B A100. For small models, like 7b with 4k tokens, vLLM fails for "cache blocks" even though alot more memory is left. E.g. building docker image with cuda 11.8 and vllm 0.2.5 or 0.2.6 and running like: ``` port=5001 tokens=8192 docker run -d \ --runtime=nvidia \ --gpus '"device=1"' \ --shm-size=10.24gb \ -p $port:$port \ --entrypoint /h2ogpt_conda/vllm_env/bin/python3.10 \ -e NCCL_IGNORE_DISABLED_P2P=1 \ -v /etc/passwd:/etc/passwd:ro \ -v /etc/group:/etc/group:ro \ -u `id -u`:`id -g` \ -v "${HOME}"/.cache:/workspace/.cache \ --network host \ gcr.io/vorvan/h2oai/h2ogpt-runtime:0.1.0 -m vllm.entrypoints.openai.api_server \ --port=$port \ --host=0.0.0.0 \ --model=defog/sqlcoder2 \ --seed 1234 \ --trust-remote-code \ --max-num-batched-tokens $tokens \ --max-model-len=$tokens \ --gpu-memory-utilization 0.4 \ --download-dir=/workspace/.cache/huggingface/hub &>> logs.vllm_server.sqlcoder2.txt port=5002 tokens=4096 docker run -d \ --runtime=nvidia \ --gpus '"device=1"' \ --shm-size=10.24gb \ -p $port:$port \ --entrypoint /h2ogpt_conda/vllm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: LM fails for "cache blocks" even though alot more memory is left. E.g. building docker image with cuda 11.8 and vllm 0.2.5 or 0.2.6 and running like: ``` port=5001 tokens=8192 docker run -d \ --runtime=nvidia \ --gpus '...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: initializing the engine. bug;unstale Since vLLM 0.2.5, we can't even run llama-2 70B 4bit AWQ on 4*A10G anymore, have to use old vLLM. Similar problems even trying to be two 7b models on 80B A100. For small models, like...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: o use old vLLM. Similar problems even trying to be two 7b models on 80B A100. For small models, like 7b with 4k tokens, vLLM fails for "cache blocks" even though alot more memory is left. E.g. building docker image with...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: t vLLMs ask for too much memory: ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initializing the engine. bug;unstale Since vLLM 0.2.5, we can't even run llama-2 70B 4b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ld 0.4 util out of 80GB be a problem? performance ci_build;model_support;quantization cuda;quantization crash env_dependency Since vLLM 0.2.5, we can't even run llama-2 70B 4bit AWQ on 4*A10G anymore, have to use old vL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
