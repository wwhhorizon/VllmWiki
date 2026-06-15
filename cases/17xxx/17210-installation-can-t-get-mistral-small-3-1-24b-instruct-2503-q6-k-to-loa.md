# vllm-project/vllm#17210: [Installation]: Can't get Mistral-Small-3.1-24B-Instruct-2503-Q6_K to load on Docker (local or HF)

| 字段 | 值 |
| --- | --- |
| Issue | [#17210](https://github.com/vllm-project/vllm/issues/17210) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Can't get Mistral-Small-3.1-24B-Instruct-2503-Q6_K to load on Docker (local or HF)

### Issue 正文摘录

Hello, I've been searching on the Issues here, but I don't seem to find anyone having this issue when using Docker. I have this: ``` services: llm: container_name: llm image: public.ecr.aws/q9t5s3a7/vllm-cpu-release-repo:v0.8.4 environment: - VLLM_CPU_KVCACHE_SPACE=8G # max RAM - VLLM_CPU_OMP_THREADS_BIND=10 # max CPU threads - VLLM_LOGGING_LEVEL=DEBUG volumes: - /models:/models restart: no command: > --dtype bfloat16 --model /models/Mistral-Small-3.1-24B-Instruct-2503-Q6_K/Mistral-Small-3.1-24B-Instruct-2503-Q6_K.gguf --hf-config-path /models/Mistral-Small-3.1-24B-Instruct-2503-Q6_K/config.json --tokenizer-mode mistral --config-format mistral --load-format mistral --tool-call-parser mistral --enable-auto-tool-choice --limit-mm-per-prompt 'image=10' # --tensor-parallel-size 2 shm_size: '16g' privileged: true ``` I've tried with and without `--hf-config-path`. But as long as I put a local path in `--model`, I get this: > huggingface_hub.errors.HFValidationError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': '/models/Mistral-Small-3.1-24B-Instruct-2503-Q6_K/config.json'. Use `repo_type` argument if needed. -- If I try: `--model /models/Mistral-Small-3.1-24B-Instr...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: get Mistral-Small-3.1-24B-Instruct-2503-Q6_K to load on Docker (local or HF) installation;stale Hello, I've been searching on the Issues here, but I don't seem to find anyone having this issue when using Docker. I have...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: Can't get Mistral-Small-3.1-24B-Instruct-2503-Q6_K to load on Docker (local or HF) installation;stale Hello, I've been searching on the Issues here, but I don't seem to find anyone having this issue when
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: volumes: - /models:/models restart: no command: > --dtype bfloat16 --model /models/Mistral-Small-3.1-24B-Instruct-2503-Q6_K/Mistral-Small-3.1-24B-Instruct-2503-Q6_K.gguf --hf-config-path /models/Mistral-Small-3.1-24B-In...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: Can't get Mistral-Small-3.1-24B-Instruct-2503-Q6_K to load on Docker (local or HF) installation;stale Hello, I've been searching on the Issues here, but I don't seem to find anyone having this issue when...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: -3.1-24B-Instruct-2503-Q6_K to load on Docker (local or HF) installation;stale Hello, I've been searching on the Issues here, but I don't seem to find anyone having this issue when using Docker. I have this: ``` service...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
