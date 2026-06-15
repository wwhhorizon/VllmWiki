# vllm-project/vllm#7581: [Bug]: Consuming gpu memory extremly when run server with vllm docker

| 字段 | 值 |
| --- | --- |
| Issue | [#7581](https://github.com/vllm-project/vllm/issues/7581) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Consuming gpu memory extremly when run server with vllm docker

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried to run vllm server with docker as below command. ```bash docker run --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN=HUGGING_FACE_HUB_TOKEN" \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model meta-llama/Meta-Llama-3.1-8B-Instruct ``` Run docker successfully but it consumes gpu memory about 72GiB. Here is the result of `nvidia-smi` ```bash nvidia-smi +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 550.67 Driver Version: 550.67 CUDA Version: 12.4 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA A100 80GB PCIe Off | 00000000:81:00.0 Off | 0 | | N/A 58C P0 83W / 300W | 72591MiB / 81920MiB | 5% Default | | | | Disabled | +-----------------------------------------+------------------------+----------------------+ +---------...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Consuming gpu memory extremly when run server with vllm docker bug ### Your current environment ### 🐛 Describe the bug I tried to run vllm server with docker as below command. ```bash docker run --gpus all \ -v ~...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: y but it consumes gpu memory about 72GiB. Here is the result of `nvidia-smi` ```bash nvidia-smi +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 550.67 Driver Vers...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: docker as below command. ```bash docker run --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN=HUGGING_FACE_HUB_TOKEN" \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: Consuming gpu memory extremly when run server with vllm docker bug ### Your current environment ### 🐛 Describe the bug I tried to run vllm server with docker as below command. ```bash docker run --gpus all \ -v ~...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
