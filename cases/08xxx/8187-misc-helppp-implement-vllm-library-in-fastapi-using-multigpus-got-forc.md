# vllm-project/vllm#8187: [Misc]: HELPPP! Implement vLLM Library in FastAPI using MultiGPUS got Force Shutdown after some warning

| 字段 | 值 |
| --- | --- |
| Issue | [#8187](https://github.com/vllm-project/vllm/issues/8187) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;sampling |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Misc]: HELPPP! Implement vLLM Library in FastAPI using MultiGPUS got Force Shutdown after some warning

### Issue 正文摘录

I try to create a FastApi to run vLLM using 2 gpus RTX4060, in the VLLM i use this code to load the model: ``` LLM(model=self.model_path, tensor_parallel_size=torch.cuda.device_count()) ``` after start the fastapi using uvicorn `uvicorn app:app --host 0.0.0.0 --port 1000`, all is good, but after a few predictions, sometimes i got `[1;36m(VllmWorkerProcess pid=32388)[0;0m WARNING 09-05 14:51:40 shm_broadcast.py:386] No available block found in 60 second.` or `Processed prompts: 0%| | 0/2 [00:00 \nselamat siang\n \n\nClassification:'}], 'max_new_tokens': 1024, 'do_sample': True, 'temperature': 0.7, 'top_k': 50, 'top_p': 0.95} INFO:app:2024-09-05 14:49:37.161217 [I] Prompt: ' [INST] Given the user question below, classify user intention.\n\nDo not respond with more than one word.\n\n`Greeting`: If the user greets you \n`Question`: If the user asks a general question about the company\n`Summary`: If the user specifically ask you to create a summary of the chat\n`Farewell`: If the user says goodbye\n`Saran`: Ketika user memberikan saran tentang kasir, toko, atau produk Indomaret\n`Kritik`: Ketika user memberikan komplain tentang layanan, toko, atau produk Indomaret\n`Daftar Waralaba`...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Library in FastAPI using MultiGPUS got Force Shutdown after some warning stale I try to create a FastApi to run vLLM using 2 gpus RTX4060, in the VLLM i use this code to load the model: ``` LLM(model=self.model_path, te...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: d=32388)[0;0m WARNING 09-05 14:51:40 shm_broadcast.py:386] No available block found in 60 second.` or `Processed prompts: 0%| | 0/2 [00:00 \nselamat siang\n \n\nClassification:'}], 'max_new_tokens': 1024, 'do_sample':...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ser asks a general question about the company\n`Summary`: If the user specifically ask you to create a summary of the chat\n`Farewell`: If the user says goodbye\n`Saran`: Ketika user memberikan saran tentang kasir, toko...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: er some warning stale I try to create a FastApi to run vLLM using 2 gpus RTX4060, in the VLLM i use this code to load the model: ``` LLM(model=self.model_path, tensor_parallel_size=torch.cuda.device_count()) ``` after s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: o run vLLM using 2 gpus RTX4060, in the VLLM i use this code to load the model: ``` LLM(model=self.model_path, tensor_parallel_size=torch.cuda.device_count()) ``` after start the fastapi using uvicorn `uvicorn app:app -...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | onda3/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #4: <unknown function> + 0xdbbf4 (0x7dd6574dbbf4 in /home/hanif/miniconda3/bin/../lib/libstdc++.so.6) frame #5: |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | + 0x9ca94 (0x7dd65a09ca94 in /lib/x86_64-linux-gnu/libc.so.6) frame #6: <unknown function> + 0x129c3c (0x7dd65a129c3c in /lib/x86_64-linux-gnu/libc.so.6) [rank0]:[e905 14:56:52. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
