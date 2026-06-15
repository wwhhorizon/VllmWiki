# vllm-project/vllm#4108: [Bug]: NCCL watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#4108](https://github.com/vllm-project/vllm/issues/4108) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: NCCL watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ```text vllm 0.4.0.post1 docker image ``` how ran: ``` docker run -d \ --runtime=nvidia \ --gpus '"device=0,1"' \ --shm-size=10.24gb \ -p 5002:5002 \ -e NCCL_IGNORE_DISABLED_P2P=1 \ -v /etc/passwd:/etc/passwd:ro \ -v /etc/group:/etc/group:ro \ -u `id -u`:`id -g` \ -v "${HOME}"/.cache:/home/ubuntu/.cache/ -v "${HOME}"/.config:/home/ubuntu/.config/ -v "${HOME}"/.config:/home/ubuntu/.triton/ \ --network host \ vllm/vllm-openai:latest \ --port=5002 \ --host=0.0.0.0 \ --model=mistralai/Mixtral-8x7B-Instruct-v0.1 \ --seed 1234 \ --trust-remote-code \ --tensor-parallel-size=2 \ --dtype auto \ --max-num-batched-tokens 131072 \ --max-log-len=100 \ --download-dir=/home/ubuntu/.cache/huggingface/hub &>> logs.vllm_server.2gpus.mixtral.txt ``` On: ``` Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.31 Python version: 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0] (64-bit runtime) Python pl...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: s encountered bug ### Your current environment ```text vllm 0.4.0.post1 docker image ``` how ran: ``` docker run -d \ --runtime=nvidia \ --gpus '"device=0,1"' \ --shm-size=10.24gb \ -p 5002:5002 \ -e NCCL_IGNORE_DISABLE...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: NCCL watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered bug ### Your current environment ```text vllm 0.4.0.post1 docker image ``` how ran: ``` docker run -d \ --runti...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: {HOME}"/.config:/home/ubuntu/.config/ -v "${HOME}"/.config:/home/ubuntu/.triton/ \ --network host \ vllm/vllm-openai:latest \ --port=5002 \ --host=0.0.0.0 \ --model=mistralai/Mixtral-8x7B-Instruct-v0.1 \ --seed 1234 \ -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: -u`:`id -g` \ -v "${HOME}"/.cache:/home/ubuntu/.cache/ -v "${HOME}"/.config:/home/ubuntu/.config/ -v "${HOME}"/.config:/home/ubuntu/.triton/ \ --network host \ vllm/vllm-openai:latest \ --port=5002 \ --host=0.0.0.0 \ --...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: nvironment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2)...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #4: c10d::processgroupnccl::worknccl::iscompleted() + 0x58 (0x7f48432c9078 in /usr/local/lib/python3.10/dist-p… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x78 (0x7f48432dfc18 in /usr/local/lib/python3.10/dist-packag… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xdc253 (0x7f4887ab0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #8: <unknow |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
