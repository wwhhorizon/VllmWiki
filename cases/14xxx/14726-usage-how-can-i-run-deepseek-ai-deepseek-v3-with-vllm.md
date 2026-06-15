# vllm-project/vllm#14726: [Usage]: how can i run deepseek-ai/deepseek-V3 with vllm?

| 字段 | 值 |
| --- | --- |
| Issue | [#14726](https://github.com/vllm-project/vllm/issues/14726) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;fp8;operator;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: how can i run deepseek-ai/deepseek-V3 with vllm?

### Issue 正文摘录

### Your current environment i have two nodes，each node has 8 L40 GPU（48GiB per GPU）；we used ray+vllm to run deepseek-ai/deepseek-V3，however it throw error with CUDA out of memory： ``` vllm serve /root/.cache/huggingface/deepseek-V3/ --tensor-parallel-size 8 --pipeline-parallel-size 2 --trust-remote-code --gpu-memory-utilization 1 --kv-cache-dtype fp8 --distributed-executor-backend ray --max-num-seqs 1 --dtype half (RayWorkerWrapper pid=8776, ip=192.168.10.103) ERROR 03-12 19:41:13 worker_base.py:581] File "/usr/local/lib/python3.12/dist-packages/vllm/attention/backends/mla/utils.py", line 378, in process_weights_after_loading [repeated 2x across cluster] (RayWorkerWrapper pid=8776, ip=192.168.10.103) ERROR 03-12 19:41:13 worker_base.py:581] self.impl.process_weights_after_loading(act_dtype) (RayWorkerWrapper pid=8776, ip=192.168.10.103) ERROR 03-12 19:41:13 worker_base.py:581] W_UV_O, W_UV_O_scales = scaled_quantize( (RayWorkerWrapper pid=8776, ip=192.168.10.103) ERROR 03-12 19:41:13 worker_base.py:581] ^^^^^^^^^^^^^^^^ (RayWorkerWrapper pid=8776, ip=192.168.10.103) ERROR 03-12 19:41:13 worker_base.py:581] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/q...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: arallel-size 2 --trust-remote-code --gpu-memory-utilization 1 --kv-cache-dtype fp8 --distributed-executor-backend ray --max-num-seqs 1 --dtype half (RayWorkerWrapper pid=8776, ip=192.168.10.103) ERROR 03-12 19:41:13 wor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: CUDA out of memory. Tried to allocate 112.00 MiB. GPU 4 has a total capacity of 44.43 GiB of which 72.31 MiB is free. Process 197385 has 44.35 GiB memory in use. Of the allocated memory 43.49 GiB is allocated by PyTorch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: used ray+vllm to run deepseek-ai/deepseek-V3，however it throw error with CUDA out of memory： ``` vllm serve /root/.cache/huggingface/deepseek-V3/ --tensor-parallel-size 8 --pipeline-parallel-size 2 --trust-remote-code -...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ipeline-parallel-size 2 --trust-remote-code --gpu-memory-utilization 1 --kv-cache-dtype fp8 --distributed-executor-backend ray --max-num-seqs 1 --dtype half (RayWorkerWrapper pid=8776, ip=192.168.10.103) ERROR 03-12 19:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: this process. In rare cases this process can exit before this point and block the progress of another member of the process group. This constraint has always been present, but this warning has only been added since PyTo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
