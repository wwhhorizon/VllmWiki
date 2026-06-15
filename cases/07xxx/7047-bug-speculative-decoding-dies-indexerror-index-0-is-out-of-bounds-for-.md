# vllm-project/vllm#7047: [Bug]: speculative decoding dies:  IndexError: index 0 is out of bounds for dimension 0 with size 0

| 字段 | 值 |
| --- | --- |
| Issue | [#7047](https://github.com/vllm-project/vllm/issues/7047) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;model_support;scheduler_memory;speculative_decoding |
| 子分类 | runtime_err |
| Operator 关键词 | triton |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: speculative decoding dies:  IndexError: index 0 is out of bounds for dimension 0 with size 0

### Issue 正文摘录

### Your current environment ``` docker pull vllm/vllm-openai:latest docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=1"' \ --shm-size=10.24gb \ -p 5001:5001 \ -e NCCL_IGNORE_DISABLED_P2P=1 \ -e VLLM_NCCL_SO_PATH=/usr/local/lib/python3.10/dist-packages/nvidia/nccl/lib/libnccl.so.2 \ -e HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN \ -v /etc/passwd:/etc/passwd:ro \ -v /etc/group:/etc/group:ro \ -u `id -u`:`id -g` \ -v "${HOME}"/.cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name phi3mini \ vllm/vllm-openai:latest \ --port=5001 \ --host=0.0.0.0 \ --model=microsoft/Phi-3-mini-128k-instruct \ --seed 1234 \ --trust-remote-code \ --tensor-parallel-size=1 \ --max-num-batched-tokens=131072 --max-log-len=100 \ --max-model-len=131072 \ --max-num-seqs=17 \ --use-v2-block-manager \ --num-speculative-tokens=5 \ --ngram-prompt-lookup-max=4 \ --speculative-model="[ngram]" \ --download-dir=$HOME/.cache/huggingface/hub &>> logs.vllm_server.phi3.txt ``` ### 🐛 Describe the bug ``` ERROR 08-01 21:27:03 async_llm_engine.py:56] File "/usr/local/lib/python3.10/dist-packages/vllm/spec_decode/spec_decode_worker.py", lin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: bounds for dimension 0 with size 0 bug ### Your current environment ``` docker pull vllm/vllm-openai:latest docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=1"' \ --shm-size=10.24gb \ -p 5001:5001 \ -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: speculative decoding dies: IndexError: index 0 is out of bounds for dimension 0 with size 0 bug ### Your current environment ``` docker pull vllm/vllm-openai:latest docker run -d --restart=always \ --runtime=nvid...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: -u `id -u`:`id -g` \ -v "${HOME}"/.cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name phi3mini \ vllm/vllm-openai:latest \ --port=5001 \ --host=0.0.0.0...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: --max-model-len=131072 \ --max-num-seqs=17 \ --use-v2-block-manager \ --num-speculative-tokens=5 \ --ngram-prompt-lookup-max=4 \ --speculative-model="[ngram]" \ --download-dir=$HOME/.cache/huggingface/hub &>> logs.vllm_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: .cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name phi3mini \ vllm/vllm-openai:latest \ --port=5001 \ --host=0.0.0.0 \ --model=microsoft/Phi-3-mini-128...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
