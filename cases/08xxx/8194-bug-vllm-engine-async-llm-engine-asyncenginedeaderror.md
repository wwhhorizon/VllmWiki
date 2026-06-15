# vllm-project/vllm#8194: [Bug]: vllm.engine.async_llm_engine.AsyncEngineDeadError

| 字段 | 值 |
| --- | --- |
| Issue | [#8194](https://github.com/vllm-project/vllm/issues/8194) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm.engine.async_llm_engine.AsyncEngineDeadError

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, I am using vLLM v0.6.0 from the commit https://github.com/vllm-project/vllm/commit/8685ba1a1ec08d2c14df924b6e2b499be14405e7 and I built the docker image using this command : `DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag vllm/vllm-openai:v0.6.0-flashinfer --build-arg max_jobs=32 --build-arg nvcc_threads=8 --build-arg torch_cuda_arch_list=""` I built the image on my own because of [this](https://github.com/vllm-project/vllm/pull/8173) but not matter. Here is the command I try to use : ``` docker run --rm --runtime nvidia --gpus all \ --name vllm-mistral \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e NVIDIA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e VLLM_ATTENTION_BACKEND=FLASHINFER \ -p 8090:8000 \ -v /data/vllm/huggingface:/root/vllm/huggingface \ -v /data/models/mistral/mistral-large-instruct-2407-awq:/root/data/mistral-large-instruct-2407-awq \ --ipc=host \ vllm/vllm-openai:v0.6.0-flashinfer \ --host 0.0.0.0 \ --model /root/data/mistral-large-instruct-2407-awq \ --disable-custom-all-reduce \ --distributed-executor-backend ray \ --tensor-parallel-size 4 \ --max-model-len $((1024*100)) \ --max-num-seqs 16 \ --num-sche...

## 现有链接修复摘要

#7928 [multi-step] add flashinfer backend

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: DKIT=1 docker build . --target vllm-openai --tag vllm/vllm-openai:v0.6.0-flashinfer --build-arg max_jobs=32 --build-arg nvcc_threads=8 --build-arg torch_cuda_arch_list=""` I built the image on my own because of [this](h...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: allel-size 4 \ --max-model-len $((1024*100)) \ --max-num-seqs 16 \ --num-scheduler-steps 8 \ --trust-remote-code \ --kv-cache-dtype fp8_e4m3 \ --use-v2-block-manager \ --enable-chunked-prefill=False \ --quantization awq...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ect/vllm/commit/8685ba1a1ec08d2c14df924b6e2b499be14405e7 and I built the docker image using this command : `DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag vllm/vllm-openai:v0.6.0-flashinfer --build-arg max_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ler-steps 8 \ --trust-remote-code \ --kv-cache-dtype fp8_e4m3 \ --use-v2-block-manager \ --enable-chunked-prefill=False \ --quantization awq_marlin ``` Here is the bug I get when I send a request : ``` ERROR 09-05 05:00...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: num-seqs 16 \ --num-scheduler-steps 8 \ --trust-remote-code \ --kv-cache-dtype fp8_e4m3 \ --use-v2-block-manager \ --enable-chunked-prefill=False \ --quantization awq_marlin ``` Here is the bug I get when I send a reque...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7928](https://github.com/vllm-project/vllm/pull/7928) | closes_keyword | 0.95 | [multi-step] add flashinfer backend | FIX #8194 (*link existing issues this PR will resolve*) **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
