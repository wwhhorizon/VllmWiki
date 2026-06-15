# vllm-project/vllm#9321: [Bug]: vLLM was installed and used without issues, but recently, during more frequent usage, it suddenly throws an error on a particular request and stops working entirely. Even nvidia-smi cannot return any output. The log is as follows:

| 字段 | 值 |
| --- | --- |
| Issue | [#9321](https://github.com/vllm-project/vllm/issues/9321) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;kernel |
| 症状 | slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: vLLM was installed and used without issues, but recently, during more frequent usage, it suddenly throws an error on a particular request and stops working entirely. Even nvidia-smi cannot return any output. The log is as follows:

### Issue 正文摘录

### Your current environment ### Model Input Dumps 761, 286, 330, 3628, 5857, 794, 330, 4963, 6125, 8318, 6046, 11, 6125, 8318, 21792, 11, 49554, 6046, 11, 49554, 21792, 220, 4393, 61198, 69, 285, 372, 55397, 5401, 3775, 2062, 21170, 7832, 3443, 16, 28337, 220, 323, 1522, 2062, 21170, 7832, 3443, 17, 28337, 6360, 262, 457, 22414, 128009, 128006, 78191, 128007, 271], lora_request: None, prompt_adapter_request: None. WARNING 10-12 22:20:45 preprocess.py:86] Falling back on for decoder start token id because decoder start token id is not available. INFO 10-12 22:20:45 engine.py:288] Added request chat-aa6539ac536f45d1b61db2a663c09dae. INFO 10-12 22:20:49 metrics.py:351] Avg prompt throughput: 2834.0 tokens/s, Avg generation throughput: 8.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 17.9%, CPU KV cache usage: 0.0%. INFO 10-12 22:20:54 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 21.9 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 18.0%, CPU KV cache usage: 0.0%. INFO 10-12 22:20:59 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 25.6 tokens/s, Runn...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: during more frequent usage, it suddenly throws an error on a particular request and stops working entirely. Even nvidia-smi cannot return any output. The log is as follows: bug;stale ### Your current environment ### Mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: vLLM was installed and used without issues, but recently, during more frequent usage, it suddenly throws an error on a particular request and stops working entirely. Even nvidia-smi cannot return any output. The...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: an error on a particular request and stops working entirely. Even nvidia-smi cannot return any output. The log is as follows: bug;stale ### Your current environment ### Model Input Dumps 761, 286, 330, 3628, 5857, 794,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: cess pid=3106) WARNING 10-12 22:22:22 shm_broadcast.py:396] No available block found in 60 second. (VllmWorkerProcess pid=3107) WARNING 10-12 22:22:22 shm_broadcast.py:396] No available block found in 60 second. (VllmWo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t. The log is as follows: bug;stale ### Your current environment ### Model Input Dumps 761, 286, 330, 3628, 5857, 794, 330, 4963, 6125, 8318, 6046, 11, 6125, 8318, 21792, 11, 49554, 6046, 11, 49554, 21792, 220, 4393, 61...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | m-env/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so) frame #4: <unknown function> + 0xdbbf4 (0x7fc7d82dbbf4 in /home/alex/miniconda3/envs/vllm-env/lib/python3.10/site-pa… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | + 0x9ca94 (0x7fc7e169ca94 in /lib/x86_64-linux-gnu/libc.so.6) frame #6: <unknown function> + 0x129c3c (0x7fc7e1729c3c in /lib/x86_64-linux-gnu/libc.so.6) ### 🐛 describe the bug |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
