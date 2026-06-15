# vllm-project/vllm#6870: [Bug]: Error: Failed to initialize the TMA descriptor 700 for LLaMa 3.1 405B on 8*H100 -- prefill error?

| 字段 | 值 |
| --- | --- |
| Issue | [#6870](https://github.com/vllm-project/vllm/issues/6870) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;triton |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Error: Failed to initialize the TMA descriptor 700 for LLaMa 3.1 405B on 8*H100 -- prefill error?

### Issue 正文摘录

### Your current environment latest docker image ``` docker stop llama31-405b ; docker remove llama31-405b docker pull vllm/vllm-openai:latest docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=0,1,2,3,4,5,6,7"' \ --shm-size=10.24gb \ -p 5020:5020 \ -e NCCL_IGNORE_DISABLED_P2P=1 \ -e HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN \ -e VLLM_NCCL_SO_PATH=/usr/local/lib/python3.10/dist-packages/nvidia/nccl/lib/libnccl.so.2 \ -v /etc/passwd:/etc/passwd:ro \ -v /etc/group:/etc/group:ro \ -u `id -u`:`id -g` \ -v "${HOME}"/.cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name llama31-405b \ vllm/vllm-openai:latest \ --port=5020 \ --host=0.0.0.0 \ --model=meta-llama/Meta-Llama-3.1-405B-Instruct-FP8 \ --seed 1234 \ --tensor-parallel-size=8 \ --max-log-len=100 \ --max-model-len=65536 \ --max-num-batched-tokens=512 \ --max_num_seqs=16 \ --gpu-memory-utilization 0.98 \ --enable_chunked_prefill=True \ --enforce-eager \ --download-dir=$HOME/.cache/huggingface/hub &>> logs.vllm_server.llama31_405b2.txt ``` ### 🐛 Describe the bug Complete logs [llama31-405b.log.zip](https://github.com/user-attachments/files/16402018...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 05B on 8*H100 -- prefill error? bug ### Your current environment latest docker image ``` docker stop llama31-405b ; docker remove llama31-405b docker pull vllm/vllm-openai:latest docker run -d --restart=always \ --runti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ror: Failed to initialize the TMA descriptor 700 for LLaMa 3.1 405B on 8*H100 -- prefill error? bug ### Your current environment latest docker image ``` docker stop llama31-405b ; docker remove llama31-405b docker pull...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Error: Failed to initialize the TMA descriptor 700 for LLaMa 3.1 405B on 8*H100 -- prefill error? bug ### Your current environment latest docker image ``` docker stop llama31-405b ; docker remove llama31-405b doc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --host=0.0.0.0 \ --model=meta-llama/Meta-Llama-3.1-405B-Instruct-FP8 \ --seed 1234 \ --tensor-parallel-size=8 \ --max-log-len=100 \ --max-model-len=65536 \ --max-num-batched-tokens=512 \ --max_num_seqs=16 \ --gpu-memory...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: .cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name llama31-405b \ vllm/vllm-openai:latest \ --port=5020 \ --host=0.0.0.0 \ --model=meta-llama/Meta-Llam...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #4: c10d::processgroupnccl::worknccl::iscompleted() + 0x58 (0x7e095bc8e9e8 in /usr/local/lib/python3.10/dist-p… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x10c (0x7e095bc94dcc in /usr/local/lib/python3.10/dist-packa… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xd6df4 (0x7e09a774bdf4 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #8: <unknow |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
