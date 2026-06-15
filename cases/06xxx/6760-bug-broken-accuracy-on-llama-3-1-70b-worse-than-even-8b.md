# vllm-project/vllm#6760: [Bug]: Broken accuracy on LLaMa 3.1 70B -- worse than even 8B

| 字段 | 值 |
| --- | --- |
| Issue | [#6760](https://github.com/vllm-project/vllm/issues/6760) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;model_support |
| 子分类 | race_cond |
| Operator 关键词 | triton |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Broken accuracy on LLaMa 3.1 70B -- worse than even 8B

### Issue 正文摘录

### Your current environment 4*H100 for 70Bs or for 8B 1*H100 Docker 0.5.3.post1 for both, ran like: ``` docker pull vllm/vllm-openai:latest docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=4,5,6,7"' \ --shm-size=10.24gb \ -p 5020:5020 \ -e NCCL_IGNORE_DISABLED_P2P=1 \ -e HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN \ -e VLLM_NCCL_SO_PATH=/usr/local/lib/python3.10/dist-packages/nvidia/nccl/lib/libnccl.so.2 \ -v /etc/passwd:/etc/passwd:ro \ -v /etc/group:/etc/group:ro \ -u `id -u`:`id -g` \ -v "${HOME}"/.cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name llama31-70b \ vllm/vllm-openai:latest \ --port=5020 \ --host=0.0.0.0 \ --model=meta-llama/Meta-Llama-3.1-70B-Instruct \ --seed 1234 \ --tensor-parallel-size=4 \ --max-model-len=131072 \ --max-num-batched-tokens=131072 --max-log-len=100 \ --served-model-name meta-llama/Meta-Llama-3.1-70B-Instruct meta-llama/Meta-Llama-3-70B-Instruct \ --download-dir=$HOME/.cache/huggingface/hub &>> logs.vllm_server.llama31.txt ``` and for 8B: ``` docker pull vllm/vllm-openai:latest docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=0"' \ --shm-si...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Broken accuracy on LLaMa 3.1 70B -- worse than even 8B bug ### Your current environment 4*H100 for 70Bs or for 8B 1*H100 Docker 0.5.3.post1 for both, ran like: ``` docker pull vllm/vllm-openai:latest docker run -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: n 8B bug ### Your current environment 4*H100 for 70Bs or for 8B 1*H100 Docker 0.5.3.post1 for both, ran like: ``` docker pull vllm/vllm-openai:latest docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: LLaMa 3.1 70B -- worse than even 8B bug ### Your current environment 4*H100 for 70Bs or for 8B 1*H100 Docker 0.5.3.post1 for both, ran like: ``` docker pull vllm/vllm-openai:latest docker run -d --restart=always \ --run...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Broken accuracy on LLaMa 3.1 70B -- worse than even 8B bug ### Your current environment 4*H100 for 70Bs or for 8B 1*H100 Docker 0.5.3.post1 for both, ran like: ``` docker pull vllm/vllm-openai:latest docker run -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: .cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name llama31-70b \ vllm/vllm-openai:latest \ --port=5020 \ --host=0.0.0.0 \ --model=meta-llama/Meta-Llama...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
