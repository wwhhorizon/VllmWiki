# vllm-project/vllm#10556: [Usage]: Docker w/ CPU fails when defining VLLM_CPU_OMP_THREADS_BIND

| 字段 | 值 |
| --- | --- |
| Issue | [#10556](https://github.com/vllm-project/vllm/issues/10556) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Docker w/ CPU fails when defining VLLM_CPU_OMP_THREADS_BIND

### Issue 正文摘录

### Your current environment ### How would you like to use vllm What I did along with following the [installation with CPU guide](https://docs.vllm.ai/en/stable/getting_started/cpu-installation.html#quick-start-using-dockerfile) and [deploy with docker guide](https://docs.vllm.ai/en/stable/serving/deploying_with_docker.html#deploying-with-docker) ```bash sudo su cd git clone https://github.com/vllm-project/vllm.git cd vllm docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g . docker run -it --rm --network=host --ipc=host \ -v /local/apps/tools/aiModels:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN= " \ --env "VLLM_CPU_KVCACHE_SPACE=512" \ vllm-cpu-env --model meta-llama/Llama-3.1-70B-Instruct ``` this works fine, it is when I attempt to set `VLLM_CPU_OMP_THREADS_BIND` and `-tp 2` that I run into issues. Since I have 128 cores with 2 CPUs (64 on each CPU), I tried ```bash docker run -it --rm --network=host --ipc=host \ -v /local/apps/tools/aiModels:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN= " \ --env "VLLM_CPU_KVCACHE_SPACE=512" \ --env "VLLM_CPU_OMP_THREADS_BIND=0-63|64-127" \ vllm-cpu-env --model meta-llama/Llama-3.1-70B-Instruct -tp 2 ``` and g...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Usage]: Docker w/ CPU fails when defining VLLM_CPU_OMP_THREADS_BIND usage ### Your current environment ### How would you like to use vllm What I did along with following the [installation with CPU guide](https://docs.v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: cker run -it --rm --network=host --ipc=host \ -v /local/apps/tools/aiModels:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN= " \ --env "VLLM_CPU_KVCACHE_SPACE=512" \ vllm-cpu-env --model meta-llama/Llama-3.1-70...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory cache;cuda;operator;quantization;triton build_error;crash;oom dtype;env_dependency;memory_layout Your current enviro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: l_support;quantization;scheduler_memory cache;cuda;operator;quantization;triton build_error;crash;oom dtype;env_dependency;memory_layout Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: d_api;hardware_porting;model_support;quantization;scheduler_memory cache;cuda;operator;quantization;triton build_error;crash;oom dtype;env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
