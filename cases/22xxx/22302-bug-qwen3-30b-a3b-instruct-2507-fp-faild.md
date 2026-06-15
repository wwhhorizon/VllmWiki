# vllm-project/vllm#22302: [Bug]: Qwen3-30B-A3B-Instruct-2507-FP faild

| 字段 | 值 |
| --- | --- |
| Issue | [#22302](https://github.com/vllm-project/vllm/issues/22302) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;moe;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;fp8;operator;sampling |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-30B-A3B-Instruct-2507-FP faild

### Issue 正文摘录

### Your current environment vllm==0.9.2 export CUDA_VISIBLE_DEVICES=1,2 vllm serve /mnt/general/models/Qwen3-30B-A3B-Instruct-2507-FP8 \ --served-model-name Qwen3-30B-A3B-Instruct-2507-FP8 \ --tensor-parallel-size 2 \ --pipeline-parallel-size 1 \ --gpu-memory-utilization 0.9 \ --port 8011 \ --trust-remote-code \ --max-model-len 64000 \ --enforce_eager true ### 🐛 Describe the bug (VllmWorker rank=1 pid=2061) INFO 08-06 03:25:54 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_f7a8b0b2'), local_subscribe_addr='ipc:///tmp/1a1334a6-02fd-4cba-b1ab-53c8e9ddeff2', remote_subscribe_addr=None, remote_addr_ipv6=False) (VllmWorker rank=0 pid=2057) INFO 08-06 03:26:00 [__init__.py:1375] Found nccl from library libnccl.so.2 (VllmWorker rank=0 pid=2057) INFO 08-06 03:26:00 [pynccl.py:70] vLLM is using nccl==2.26.2 (VllmWorker rank=1 pid=2061) INFO 08-06 03:26:00 [__init__.py:1375] Found nccl from library libnccl.so.2 (VllmWorker rank=1 pid=2061) INFO 08-06 03:26:00 [pynccl.py:70] vLLM is using nccl==2.26.2 (VllmWorker rank=0 pid=2057) INFO 08-06 03:26:00 [custom_all_reduce_utils.py:246] reading GPU P2P access ca...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: Worker rank=0 pid=2057) WARNING 08-06 03:26:00 [topk_topp_sampler.py:59] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best performance, please install...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: _DEVICES=1,2 vllm serve /mnt/general/models/Qwen3-30B-A3B-Instruct-2507-FP8 \ --served-model-name Qwen3-30B-A3B-Instruct-2507-FP8 \ --tensor-parallel-size 2 \ --pipeline-parallel-size 1 \ --gpu-memory-utilization 0.9 \...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: uct-2507-FP faild bug ### Your current environment vllm==0.9.2 export CUDA_VISIBLE_DEVICES=1,2 vllm serve /mnt/general/models/Qwen3-30B-A3B-Instruct-2507-FP8 \ --served-model-name Qwen3-30B-A3B-Instruct-2507-FP8 \ --ten...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-30B-A3B-Instruct-2507-FP faild bug ### Your current environment vllm==0.9.2 export CUDA_VISIBLE_DEVICES=1,2 vllm serve /mnt/general/models/Qwen3-30B-A3B-Instruct-2507-FP8 \ --served-model-name Qwen3-30B-A3B...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: P rank 1, EP rank 1 (VllmWorker rank=0 pid=2057) WARNING 08-06 03:26:00 [topk_topp_sampler.py:59] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best pe...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
