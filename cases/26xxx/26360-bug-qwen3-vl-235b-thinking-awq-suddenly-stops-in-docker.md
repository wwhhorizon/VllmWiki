# vllm-project/vllm#26360: [Bug]: Qwen3-VL-235b-thinking-awq suddenly stops in docker.

| 字段 | 值 |
| --- | --- |
| Issue | [#26360](https://github.com/vllm-project/vllm/issues/26360) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;moe;quantization |
| 症状 | crash;import_error;oom;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-235b-thinking-awq suddenly stops in docker.

### Issue 正文摘录

### Your current environment problem with official docker container: vllm/vllm-openai:v0.11.0 It started with command: docker run --log-opt max-size=10m --log-opt max-file=1 --rm -it --gpus '"device=0,1"' -p 8000:8000 -e VLLM_SKIP_SPECIAL_TOKENS=true vllm/vllm-openai:v0.11.0 --model QuantTrio/Qwen3-VL-235B-A22B-Thinking-AWQ --gpu-memory-utilization 0.95 --max-model-len 100000 --trust-remote-code --swap-space 32 --tensor-parallel-size 2 --port 8000 --max-num-seqs 32 --tokenizer-mode auto --no-enable-prefix-caching --enforce-eager envirenment script not working: kuliev.vitaliy@pmg-matcher-gpu-svc-01:~$ python3 collect_env.py Traceback (most recent call last): File "/home/kuliev.vitaliy/collect_env.py", line 20, in from vllm.envs import environment_variables ModuleNotFoundError: No module named 'vllm' ~$ nvidia-smi Tue Oct 7 18:28:43 2025 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 570.133.07 Driver Version: 570.133.07 CUDA Version: 12.8 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Qwen3-VL-235b-thinking-awq suddenly stops in docker. bug;stale ### Your current environment problem with official docker container: vllm/vllm-openai:v0.11.0 It started with command: docker run --log-opt max-size=...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-VL-235b-thinking-awq suddenly stops in docker. bug;stale ### Your current environment problem with official docker container: vllm/vllm-openai:v0.11.0 It started with command: docker run --log-opt max-size=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ronment_variables ModuleNotFoundError: No module named 'vllm' ~$ nvidia-smi Tue Oct 7 18:28:43 2025 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 570.133.07 Dri...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: l quality is great! Model works with api fine, but randomly crashed. GPU OOM errors fixed before - about 2-3Gb of gpu ram available. Ram and disk are also available. I have tried options(No one solved the problem): --no...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Qwen3-VL-235b-thinking-awq suddenly stops in docker. bug;stale ### Your current environment problem with official docker container: vllm/vllm-openai:v0.11.0 It started with command: docker run --log-opt max-size=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
