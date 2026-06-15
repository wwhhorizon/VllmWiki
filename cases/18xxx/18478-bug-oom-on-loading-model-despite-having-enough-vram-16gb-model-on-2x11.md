# vllm-project/vllm#18478: [Bug]: OOM on loading model despite having enough VRAM (16gb model on 2x11gb gpu)

| 字段 | 值 |
| --- | --- |
| Issue | [#18478](https://github.com/vllm-project/vllm/issues/18478) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: OOM on loading model despite having enough VRAM (16gb model on 2x11gb gpu)

### Issue 正文摘录

### Your current environment `vllm.__version__` `> '0.9.1.dev5+gd98139677'` ### 🐛 Describe the bug I'm trying to load qwen 2.5 7b model on system with 2 2080ti gpus(each is 11gb, total model size is ~16gb). \ ```python llm = LLM(model=model_path, dtype='float16', tensor_parallel_size=2, # gpu_memory_utilization=0.65, # 0.8 max_seq_len_to_capture=512, # 2048 #cpu_offload_gb=8 ) ``` and I'm catching OOM with any combination of `gpu_memory_utilization` and `max_seq_len_to_capture`. When I set up `cpu_offload_gb=8` then model correctly loads with default `gpu_memory_utilization` (it's 0.9 I believe) and in nvidia-smi I see approximate load of `7284MiB` per GPU, which sounds correct since model is around 16gb, and I'm loading with small `max_seq_len_to_capture=2048`. \ I'm suspecting something weird happens on loading step since in logs I see `max_seq_len=32768` inside full model config and `INFO 05-21 13:27:59 [executor_base.py:117] Maximum concurrency for 32768 tokens per request: 6.05x` , so maybe on preload model tries to initialize full context in some way? Or am I doing something wrong? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues,...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: OOM on loading model despite having enough VRAM (16gb model on 2x11gb gpu) bug ### Your current environment `vllm.__version__` `> '0.9.1.dev5+gd98139677'` ### 🐛 Describe the bug I'm trying to load qwen 2.5 7b mod...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: model size is ~16gb). \ ```python llm = LLM(model=model_path, dtype='float16', tensor_parallel_size=2, # gpu_memory_utilization=0.65, # 0.8 max_seq_len_to_capture=512, # 2048 #cpu_offload_gb=8 ) ``` and I'm catching OOM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: with default `gpu_memory_utilization` (it's 0.9 I believe) and in nvidia-smi I see approximate load of `7284MiB` per GPU, which sounds correct since model is around 16gb, and I'm loading with small `max_seq_len_to_captu...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: OOM on loading model despite having enough VRAM (16gb model on 2x11gb gpu) bug ### Your current environment `vllm.__version__` `> '0.9.1.dev5+gd98139677'` ### 🐛 Describe the bug I'm trying to load qwen 2.5 7b mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: RAM (16gb model on 2x11gb gpu) bug ### Your current environment `vllm.__version__` `> '0.9.1.dev5+gd98139677'` ### 🐛 Describe the bug I'm trying to load qwen 2.5 7b model on system with 2 2080ti gpus(each is 11gb, total...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
