# vllm-project/vllm#7495: [Usage]: Is there an option to reduce GPU memory usage？

| 字段 | 值 |
| --- | --- |
| Issue | [#7495](https://github.com/vllm-project/vllm/issues/7495) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Is there an option to reduce GPU memory usage？

### Issue 正文摘录

### How would you like to use vllm Using google/gemma-2-27b-it model start by vllm with GPU L40x2, but used about 45G per GPU by default. When input a long token, it will OOM. Is there a way to reduce GPU memory usage when start? Maybe can lose some performance? cmd: ``` export VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=2,3 python3 -m vllm.entrypoints.openai.api_server --port=8081 --host=0.0.0.0 --model /mnt/vol-5ojabq86/models/gemma-2-27b-it --dtype bfloat16 --trust-remote-code --tensor-parallel-size 2 --max-model-len 4096 ```

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rt=8081 --host=0.0.0.0 --model /mnt/vol-5ojabq86/models/gemma-2-27b-it --dtype bfloat16 --trust-remote-code --tensor-parallel-size 2 --max-model-len 4096 ```
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: n start? Maybe can lose some performance? cmd: ``` export VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=2,3 python3 -m vllm.entrypoints.openai.api_server --port=8081 --host=0.0.0.0 --model /mnt/vol-5ojabq86/mod...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Usage]: Is there an option to reduce GPU memory usage？ usage ### How would you like to use vllm Using google/gemma-2-27b-it model start by vllm with GPU L40x2, but used about 45G per GPU by default. When input a long t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: GPU memory usage？ usage ### How would you like to use vllm Using google/gemma-2-27b-it model start by vllm with GPU L40x2, but used about 45G per GPU by default. When input a long token, it will OOM. Is there a way to r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ose some performance? cmd: ``` export VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=2,3 python3 -m vllm.entrypoints.openai.api_server --port=8081 --host=0.0.0.0 --model /mnt/vol-5ojabq86/models/gemma-2-27b-it -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
