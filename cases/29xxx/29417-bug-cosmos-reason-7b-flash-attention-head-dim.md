# vllm-project/vllm#29417: [Bug]: Cosmos-Reason-7B Flash Attention head dim

| 字段 | 值 |
| --- | --- |
| Issue | [#29417](https://github.com/vllm-project/vllm/issues/29417) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support |
| 子分类 | throughput |
| Operator 关键词 | attention;operator |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cosmos-Reason-7B Flash Attention head dim

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug meet issue when benchmarking, and it is related to qwen2_5_vl model ```bash num_gpus=$(nvidia-smi --list-gpus | wc -l) num_prompts=768 output_len=256 gpu_memory_utilization=${GPU_UTILIZATION:-0.70} input_len=$output_len max_model_len=$((num_prompts+output_len)) cd $EXAMPLE_ROOT export VLLM_ATTENTION_BACKEND=FLASH_ATTN vllm bench throughput \ --tensor-parallel-size=$num_gpus \ --model=nvidia/Cosmos-Reason1-7B \ --load-format=dummy \ --num-prompts=$num_prompts \ --output-len=$output_len \ --input-len=$input_len \ --kv-cache-dtype=auto \ --gpu-memory-utilization=$gpu_memory_utilization \ --max-num-batched-tokens=2048 \ --max-num-seqs=768 \ --max-model-len=$max_model_len ``` ``` 2025-11-24T17:09:50.451359Z 01O [1;36m(EngineCore_DP0 pid=235)[0;0m ERROR 11-24 17:09:50 [core.py:842] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/qwen2_5_vl.py", line 400, in forward 2025-11-24T17:09:50.451361Z 01O [1;36m(EngineCore_DP0 pid=235)[0;0m ERROR 11-24 17:09:50 [core.py:842] context_layer = vit_flash_attn_wrapper( 2025-11-24T17:09:50.451363Z 01O [1;36m(EngineCore_DP0 pid=235)[0;0m ERROR 11-24 17:09:50 [core.py:842...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 0m ERROR 11-24 17:09:50 [core.py:842] RuntimeError: This flash attention build does not support headdim not being a multiple of 32. ``` ### Before submitting a new issue... - [x] Make sure you already searched for relev...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: # 🐛 Describe the bug meet issue when benchmarking, and it is related to qwen2_5_vl model ```bash num_gpus=$(nvidia-smi --list-gpus | wc -l) num_prompts=768 output_len=256 gpu_memory_utilization=${GPU_UTILIZATION:-0.70}...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ### Your current environment ### 🐛 Describe the bug meet issue when benchmarking, and it is related to qwen2_5_vl model ```bash num_gpus=$(nvidia-smi --list-gpus | wc -l) num_prompts=768 output_len=256 gpu_memory_utiliz...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Cosmos-Reason-7B Flash Attention head dim bug;stale ### Your current environment ### 🐛 Describe the bug meet issue when benchmarking, and it is related to qwen2_5_vl model ```bash num_gpus=$(nvidia-smi --list-gpu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Cosmos-Reason-7B Flash Attention head dim bug;stale ### Your current environment ### 🐛 Describe the bug meet issue when benchmarking, and it is related to qwen2_5_vl model ```bash num_gpus=$(nvidia-smi --list-gpu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
