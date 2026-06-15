# vllm-project/vllm#4344: [Bug]: mistralai/Mixtral-8x22B-Instruct-v0.1 fails to load 2/3 times on aae08249acca69060d0a8220cab920e00520932c

| 字段 | 值 |
| --- | --- |
| Issue | [#4344](https://github.com/vllm-project/vllm/issues/4344) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;model_support;moe |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;moe;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: mistralai/Mixtral-8x22B-Instruct-v0.1 fails to load 2/3 times on aae08249acca69060d0a8220cab920e00520932c

### Issue 正文摘录

### Your current environment ```text DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag vllm/vllm-openai --build-arg max_jobs=20 --build-arg nvcc_threads=20 ``` ``` docker run -d \ --runtime=nvidia \ --gpus '"device=0,1,2,3,4,5,6,7"' \ --shm-size=10.24gb \ -p 5010:5010 \ -e NCCL_IGNORE_DISABLED_P2P=1 \ -e VLLM_NCCL_SO_PATH=/usr/local/lib/python3.10/dist-packages/nvidia/nccl/lib/libnccl.so.2 \ -e HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN \ -v /etc/passwd:/etc/passwd:ro \ -v /etc/group:/etc/group:ro \ -u `id -u`:`id -g` \ -v "${HOME}"/.cache:$HOME/.cache/ \ -v "${HOME}"/.config:$HOME/.config/ \ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ vllm/vllm-openai:latest \ --port=5010 \ --host=0.0.0.0 \ --model=mistralai/Mixtral-8x22B-Instruct-v0.1 \ --seed 1234 \ --tensor-parallel-size=8 \ --max-num-batched-tokens=131072 --max-log-len=100 \ --download-dir=$HOME/.cache/huggingface/hub &>> logs.vllm_server.mistral822instruct.txt ``` ### 🐛 Describe the bug Trial 1/3: ``` (RayWorkerWrapper pid=6306) INFO 04-25 02:42:07 fused_moe.py:299] Using configuration from /usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/fused_moe/configs/E=8,N=2048,device_name=NVI...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: 0d0a8220cab920e00520932c bug;stale ### Your current environment ```text DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag vllm/vllm-openai --build-arg max_jobs=20 --build-arg nvcc_threads=20 ``` ``` docker run...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: lm/model_executor/layers/fused_moe/configs/E=8,N=2048,device_name=NVIDIA_H100_80GB_HBM3.json for MoE layer. (RayWorkerWrapper pid=6756) INFO 04-25 02:42:01 model_runner.py:173] Loading model weights took 32.7642 GB [rep...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: -u`:`id -g` \ -v "${HOME}"/.cache:$HOME/.cache/ \ -v "${HOME}"/.config:$HOME/.config/ \ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ vllm/vllm-openai:latest \ --port=5010 \ --host=0.0.0.0 \ --model=mistralai/M...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 42:08 worker_base.py:157] Error executing method determine_num_available_blocks. This might cause deadlock in distributed execution. (RayWorkerWrapper pid=6673) ERROR 04-25 02:42:08 worker_base.py:157] Traceback (most r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: fails to load 2/3 times on aae08249acca69060d0a8220cab920e00520932c bug;stale ### Your current environment ```text DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag vllm/vllm-openai --build-arg max_jobs=20 --b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
