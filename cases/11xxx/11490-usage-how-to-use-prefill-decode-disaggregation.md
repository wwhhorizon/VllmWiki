# vllm-project/vllm#11490: [Usage]: how to use prefill-decode disaggregation ??

| 字段 | 值 |
| --- | --- |
| Issue | [#11490](https://github.com/vllm-project/vllm/issues/11490) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: how to use prefill-decode disaggregation ??

### Issue 正文摘录

### Your current environment vllm official images: v0.6.5 device: RTX4090 cuda driver: 550.78 cuda toolkit: 12.4 ### How would you like to use vllm I want to know how to use prefilling-decoding disaggregation, i use it in the following command but failed: ```shell # prefilling instance docker run --runtime nvidia --rm -itd --gpus '"device=3"' -v /storage/nfs2/ModelHub/QwenLM/Qwen2.5:/models -p 24050:24050 --ipc=host --name pds-prefill vllm/vllm-openai:v0.6.5 --model /models/Qwen2.5-1.5B-Instruct --port 24050 --max-model-len 100 --gpu-memory-utilization 0.8 --kv-transfer-config '{"kv_connector":"PyNcclConnector","kv_role":"kv_producer","kv_rank":0,"kv_parallel_size":2,"kv_ip":"127.0.0.1", "kv_port":24050}' ``` ```shell # decoding instance docker run --runtime nvidia --rm -itd --gpus '"device=4"' -v /storage/nfs2/ModelHub/QwenLM/Qwen2.5:/models -p 24051:24051 --ipc=host --name pds-decode vllm/vllm-openai:v0.6.5 --model /models/Qwen2.5-1.5B-Instruct --port 24051 --max-model-len 100 --gpu-memory-utilization 0.8 --kv-transfer-config '{"kv_connector":"PyNcclConnector","kv_role":"kv_producer","kv_rank":0,"kv_parallel_size":2,"kv_ip":"127.0.0.1","kv_port":24051}' ``` then I run the `pytho...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ode disaggregation ?? usage;stale ### Your current environment vllm official images: v0.6.5 device: RTX4090 cuda driver: 550.78 cuda toolkit: 12.4 ### How would you like to use vllm I want to know how to use prefilling-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: stale ### Your current environment vllm official images: v0.6.5 device: RTX4090 cuda driver: 550.78 cuda toolkit: 12.4 ### How would you like to use vllm I want to know how to use prefilling-decoding disaggregation, i u...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ker run --runtime nvidia --rm -itd --gpus '"device=3"' -v /storage/nfs2/ModelHub/QwenLM/Qwen2.5:/models -p 24050:24050 --ipc=host --name pds-prefill vllm/vllm-openai:v0.6.5 --model /models/Qwen2.5-1.5B-Instruct --port 2...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: how to use prefill-decode disaggregation ?? usage;stale ### Your current environment vllm official images: v0.6.5 device: RTX4090 cuda driver: 550.78 cuda toolkit: 12.4 ### How would you like to use vllm I want...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ,"kv_ip":"127.0.0.1","kv_port":24051}' ``` then I run the `python3 ../benchmarks/disagg_benchmarks/disagg_prefill_proxy_server.py` after modified the port. but the model deployment failed, so I want to inquire the comma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
