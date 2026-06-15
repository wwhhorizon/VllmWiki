# vllm-project/vllm#19494: [Bug]: Docker CPU AVX2 Based installation failed when requesting API locally [Mistral]

| 字段 | 值 |
| --- | --- |
| Issue | [#19494](https://github.com/vllm-project/vllm/issues/19494) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Docker CPU AVX2 Based installation failed when requesting API locally [Mistral]

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Building the docker image fom git sources with `docker build -f docker/Dockerfile.cpu --build-arg VLLM_CPU_DISABLE_AVX512="true" --tag vllm-cpu-env --target vllm-openai`` or directly using `public.ecr.aws/q9t5s3a7/vllm-cpu-release-repo:v0.9.1` Running VLLM in docker mode and CPU Only with the command ``` docker run -d \ --shm-size=4g \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -p 8000:8000 \ -e HUGGING_FACE_HUB_TOKEN=TOKEN \ vllm-cpu-env \ --model=mistralai/Mistral-7B-Instruct-v0.1 \ --tokenizer-mode=mistral ``` Here is the complete logs of vllm start and crash ``` docker logs 88663f38daf29918cdbfc34595e1fbfd1dcb4c7dbdb28221f40910dcef6ffc00 -f [W611 15:11:33.423717024 OperatorEntry.cpp:154] Warning: Warning only once for all operators, other operators may also be overridden. Overriding a previously registered kernel for the same operator and the same dispatch key operator: aten::_addmm_activation(Tensor self, Tensor mat1, Tensor mat2, *, Scalar beta=1, Scalar alpha=1, bool use_gelu=False) -> Tensor registered at /pytorch/build/aten/src/ATen/RegisterSchema.cpp:6 dispatch key: AutocastCPU previous kernel: registered at /py...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: Docker CPU AVX2 Based installation failed when requesting API locally [Mistral] bug ### Your current environment ### 🐛 Describe the bug Building the docker image fom git sources with `docker build -f docker/Docke...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ` docker run -d \ --shm-size=4g \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -p 8000:8000 \ -e HUGGING_FACE_HUB_TOKEN=TOKEN \ vllm-cpu-env \ --model=mistralai/Mistral-7B-Instruct-v0.1 \ --tokenizer-mo
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Docker CPU AVX2 Based installation failed when requesting API locally [Mistral] bug ### Your current environment ### 🐛 Describe the bug Building the docker image fom git sources with `docker build -f docker/Docke...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: riding a previously registered kernel for the same operator and the same dispatch key operator: aten::_addmm_activation(Tensor self, Tensor mat1, Tensor mat2, *, Scalar beta=1, Scalar alpha=1, bool use_gelu=False) -> Te...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
