# vllm-project/vllm#26480: [Bug][v0.11.0]: gpt-oss-120b generates with no output

| 字段 | 值 |
| --- | --- |
| Issue | [#26480](https://github.com/vllm-project/vllm/issues/26480) |
| 状态 | open |
| 标签 | bug |
| 评论 | 45; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][v0.11.0]: gpt-oss-120b generates with no output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Opening this issue after a request of @bbrowning in #22308 I am using gpt-oss-120b with tool calling capabilities. I have no problems with vLLM v0.10.2, but with the new release (v0.11.0), I find that one in two queries hangs indefinitely without a response. Looking at the vLLM logs, it seems that the model is generating, but no output is being generated. The problem exists in both streaming and non-streaming modes. I'm running vLLM in docker on Ubuntu 24.04 with 2x A100 80GB. Below you have the docker-compose I'm using, the vLLM logs (if you see I sent two identically requests, one returned a response and the second instead triggered an infinite hanging generation) and a sample request to reproduce the issue. --- My docker compose: ``` services: vllm: container_name: vllm image: vllm/vllm-openai:v0.11.0 # v0.10.2 was working command: "--model openai/gpt-oss-120b --tool-call-parser openai --enable-auto-tool-choice --max-model-len 131072 --gpu-memory-utilization 0.85 --tensor-parallel-size 2 --api-key XXXX --ssl-keyfile /certs/privkey.pem --ssl-certfile /certs/fullchain.pem" environment: TZ: "Europe/Rome" HUGGING_FACE_HUB_TOKEN: "...

## 现有链接修复摘要

#40376 [Perf] Enable FlashInfer top-k/top-p sampler by default

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: ze': 2, 'gpu_memory_utilization': 0.85} vllm | (APIServer pid=1) `torch_dtype` is deprecated! Use `dtype` instead! vllm | (APIServer pid=1) INFO 10-09 10:58:08 [model.py:547] Resolved architecture: GptOssForCausalLM Par...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: rrent environment ### 🐛 Describe the bug Opening this issue after a request of @bbrowning in #22308 I am using gpt-oss-120b with tool calling capabilities. I have no problems with vLLM v0.10.2, but with the new release...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: em exists in both streaming and non-streaming modes. I'm running vLLM in docker on Ubuntu 24.04 with 2x A100 80GB. Below you have the docker-compose I'm using, the vLLM logs (if you see I sent two identically requests,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: non-streaming modes. I'm running vLLM in docker on Ubuntu 24.04 with 2x A100 80GB. Below you have the docker-compose I'm using, the vLLM logs (if you see I sent two identically requests, one returned a response and the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug][v0.11.0]: gpt-oss-120b generates with no output bug ### Your current environment ### 🐛 Describe the bug Opening this issue after a request of @bbrowning in #22308 I am using gpt-oss-120b with tool calling capabili...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40376](https://github.com/vllm-project/vllm/pull/40376) | mentioned | 0.6 | [Perf] Enable FlashInfer top-k/top-p sampler by default | sues/23814) * [[Bug][v0.11.0]: gpt-oss-120b generates with no output #26480 (comment)](https://github.com/vllm-project/vllm/issues/26480#issuecomment-3390003242) The root cause of… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
