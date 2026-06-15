# vllm-project/vllm#2269: llama 70b load failed on A100 4*40960MiB

| 字段 | 值 |
| --- | --- |
| Issue | [#2269](https://github.com/vllm-project/vllm/issues/2269) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> llama 70b load failed on A100 4*40960MiB

### Issue 正文摘录

Shell Got Params: --port 10088 --model /data/bigqgpt --dtype float16 --tensor-parallel-size 4 --max_tokens 4096 --trust-remote-code --gpu-memory-utilization 0.98 CUDA Support: True : 4 devices WARNING 12-26 07:06:20 config.py:406] Casting torch.bfloat16 to torch.float16. 2023-12-26 07:06:23,383 INFO worker.py:1673 -- Started a local Ray instance. INFO 12-26 07:06:25 llm_engine.py:73] Initializing an LLM engine with config: model='/data/bigqgpt', tokenizer='/data/bigqgpt', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=4, quantization=None, seed=0) 2023-12-26 07:10:19,486 WARNING worker.py:2074 -- A worker died or was killed while executing a task by an unexpected system error. To troubleshoot the problem, check the logs for the dead worker. RayTask ID: ffffffffffffffffb493243e1b84395062c7e05501000000 Worker ID: 3d5e5fbf6f64171ddf74fc4bf55565e2151534f6de6822f4e422ac65 Node ID: 0744a0e2a85b4ef9650f6c943dd3ac3e25f1f79eae5046d740302221 Worker IP address: Worker port: 22778 Worker PID: 7953 Worker exit type: SYSTEM_ERROR Worker exit detail: Worker unexp...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: n A100 4*40960MiB Shell Got Params: --port 10088 --model /data/bigqgpt --dtype float16 --tensor-parallel-size 4 --max_tokens 4096 --trust-remote-code --gpu-memory-utilization 0.98 CUDA Support: True : 4 devices WARNING...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: llama 70b load failed on A100 4*40960MiB Shell Got Params: --port 10088 --model /data/bigqgpt --dtype float16 --tensor-parallel-size 4 --max_tokens 4096 --trust-remote-code --gpu-memory-utilization 0.98 CUDA Support: Tr
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ashed unexpectedly due to SIGSEGV or other unexpected errors performance ci_build;distributed_parallel;frontend_api;model_support;quantization cuda;quantization crash;oom dtype;env_dependency Shell Got Params: --port 10...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: llama 70b load failed on A100 4*40960MiB Shell Got Params: --port 10088 --model /data/bigqgpt --dtype float16 --tensor-parallel-size 4 --max_tokens 4096 --trust-remote-code --gpu-memory-utilization 0.98 CUDA Support: Tr...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected erro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
