# vllm-project/vllm#18060: [Performance]: PD disagg StatelessProcessGroup whether it supports single GPU？

| 字段 | 值 |
| --- | --- |
| Issue | [#18060](https://github.com/vllm-project/vllm/issues/18060) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: PD disagg StatelessProcessGroup whether it supports single GPU？

### Issue 正文摘录

### Your current environment I am currently using version 0.8.3 to test the PD separation experiment. I want to do the PD separation experiment on a single card. The running steps are as follows: To clarify, I am using h100 80gb video memory, 40% gpu utilization is definitely enough！ ``` ## 1p NCCL_SOCKET_IFNAME=bond0 \ GLOO_SOCKET_IFNAME=bond0 \ NCCL_IB_HCA=mlx5 \ NCCL_DEBUG=TRACE \ VLLM_HOST_IP=10.63.13.51 \ CUDA_VISIBLE_DEVICES=0 python3 \ -m vllm.entrypoints.openai.api_server \ --tensor-parallel-size 1 \ --model /work/Qwen/Qwen2.5-0.5B-Instruct \ --port 8100 \ --gpu-memory-utilization 0.4 \ --kv-transfer-config \ '{"kv_connector":"PyNcclConnector","kv_role":"kv_producer","kv_rank":0,"kv_parallel_size":2,"kv_buffer_size":5e9}' ## 1d NCCL_SOCKET_IFNAME=bond0 \ GLOO_SOCKET_IFNAME=bond0 \ NCCL_IB_HCA=mlx5 \ NCCL_DEBUG=TRACE \ VLLM_HOST_IP=10.63.13.51 \ CUDA_VISIBLE_DEVICES=0 python3 \ -m vllm.entrypoints.openai.api_server \ --tensor-parallel-size 1 \ --model /work/Qwen/Qwen2.5-0.5B-Instruct \ --port 8200 \ --gpu-memory-utilization 0.4 \ --kv-transfer-config \ '{"kv_connector":"PyNcclConnector","kv_role":"kv_consumer","kv_rank":1,"kv_parallel_size":2,"kv_buffer_size":5e9}' ## proxy...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ngle GPU？ usage;stale ### Your current environment I am currently using version 0.8.3 to test the PD separation experiment. I want to do the PD separation experiment on a single card. The running steps are as follows: T...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: llm.entrypoints.openai.api_server \ --tensor-parallel-size 1 \ --model /work/Qwen/Qwen2.5-0.5B-Instruct \ --port 8100 \ --gpu-memory-utilization 0.4 \ --kv-transfer-config \ '{"kv_connector":"PyNcclConnector","kv_role":...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ]: PD disagg StatelessProcessGroup whether it supports single GPU？ usage;stale ### Your current environment I am currently using version 0.8.3 to test the PD separation experiment. I want to do the PD separation experim...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: a single card. The running steps are as follows: To clarify, I am using h100 80gb video memory, 40% gpu utilization is definitely enough！ ``` ## 1p NCCL_SOCKET_IFNAME=bond0 \ GLOO_SOCKET_IFNAME=bond0 \ NCCL_IB_HCA=mlx5...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
