# vllm-project/vllm#10156: [Bug]: Unable to load Llama-3.1-70B-Instruct using either `vllm serve` or `vllm-openai` docker

| 字段 | 值 |
| --- | --- |
| Issue | [#10156](https://github.com/vllm-project/vllm/issues/10156) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to load Llama-3.1-70B-Instruct using either `vllm serve` or `vllm-openai` docker

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Tried to run model using vllm pip package: version: `0.6.3.post1` Command that I ran: ```bash vllm serve $model --host 0.0.0.0 --port 8010 --dtype bfloat16 --enforce-eager --gpu-memory-utilization 0.95 --api-key RnD12345 --max-model-len 4098 --tensor-parallel-size 4 --quantization bitsandbytes --load-format bitsandbytes ``` Tried using docker image as well: `docker image inspect` output: ``` [ { "Id": "sha256:9de570dfcdfca4effabe006779215326faf1f812c1d522652c5010801b8e6d78", "RepoTags": [ "vllm/vllm-openai:latest" ], "RepoDigests": [ "vllm/vllm-openai@sha256:facbbd4a92c1754675b239a5f22a281ed3aa8bde64662db8919d85d670673aa7" ], "Parent": "", "Comment": "buildkit.dockerfile.v0", "Created": "2024-10-17T10:54:46.210678506-07:00", "DockerVersion": "", "Author": "", "Config": { "Hostname": "", "Domainname": "", "User": "", "AttachStdin": false, "AttachStdout": false, "AttachStderr": false, "Tty": false, "OpenStdin": false, "StdinOnce": false, "Env": [ "PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "NVARCH=x86_64", "NVIDIA_REQUIRE_CUDA=cud...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: o load Llama-3.1-70B-Instruct using either `vllm serve` or `vllm-openai` docker bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Tried to run model using vllm pip package: vers...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: mmand that I ran: ```bash vllm serve $model --host 0.0.0.0 --port 8010 --dtype bfloat16 --enforce-eager --gpu-memory-utilization 0.95 --api-key RnD12345 --max-model-len 4098 --tensor-parallel-size 4 --quantization bitsa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Unable to load Llama-3.1-70B-Instruct using either `vllm serve` or `vllm-openai` docker bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Tried to run model using vllm pi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: "Env": [ "PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "NVARCH=x86_64", "NVIDIA_REQUIRE_CUDA=cuda>=12.4 brand=tesla,driver>=470,driver =470,driver =470,dr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ead2aac22/diff:/var/lib/docker/overlay2/0ea99b169b186ada6653ac6dda2617f17fa3da9112e6ee339937fff09ca69751/diff:/var/lib/docker/overlay2/8821136cefb26d4a59cc1bc75b3c7c57d2c65d5415e6f9e52994098a92969757/diff:/var/lib/docke...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
