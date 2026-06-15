# vllm-project/vllm#28052: [Bug]: rocm/vllm:rocm7.0.0_vllm_0.11.1_20251103 has an error with flash attention

| 字段 | 值 |
| --- | --- |
| Issue | [#28052](https://github.com/vllm-project/vllm/issues/28052) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: rocm/vllm:rocm7.0.0_vllm_0.11.1_20251103 has an error with flash attention

### Issue 正文摘录

### Your current environment rocm/vllm:rocm7.0.0_vllm_0.11.1_20251103 (Note, this does work with rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006) Docker: ``` ARG BASE_IMAGE=python:3.12-slim # passed in rocm/latest FROM ${BASE_IMAGE} WORKDIR /app # Install Rust, required build tools, pkg-config, and OpenSSL development libraries RUN apt-get update && apt-get install -y --no-install-recommends \ curl \ gcc \ build-essential \ pkg-config \ libssl-dev \ poppler-utils \ && curl https://sh.rustup.rs -sSf | sh -s -- -y \ && apt-get clean \ && rm -rf /var/lib/apt/lists/* ENV PATH="/root/.cargo/bin:${PATH}" COPY ./requirements.txt /app/flask_server/requirements.txt RUN pip install --upgrade pip RUN pip install --no-cache-dir -r /app/flask_server/requirements.txt COPY . /app/flask_server ENV PORT=8000 EXPOSE $PORT HEALTHCHECK --interval=300s --timeout=5s --start-period=10s --retries=3 \ CMD curl --fail http://localhost:$PORT/$BASE_URL || exit 1 CMD ["python", "-m", "flask_server"] ``` environment: (some of these are likely unhelpful :/) ``` QWEN_CHECKPOINT: ${QWEN_CHECKPOINT:-Qwen/Qwen2.5-VL-3B-Instruct} MAX_MODEL_LEN: ${MAX_MODEL_LEN:-45000} MAX_NUM_SEQS: ${MAX_NUM_SEQS:-1} GPU_MEMORY_UTILIZATION...

## 现有链接修复摘要

#31062 [ROCm][Docker] Add gfx1103 support to Docker builds

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: 3 (Note, this does work with rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006) Docker: ``` ARG BASE_IMAGE=python:3.12-slim # passed in rocm/latest FROM ${BASE_IMAGE} WORKDIR /app # Install Rust, required build tools, pkg-config...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: M ${BASE_IMAGE} WORKDIR /app # Install Rust, required build tools, pkg-config, and OpenSSL development libraries RUN apt-get update && apt-get install -y --no-install-recommends \ curl \ gcc \ build-essential \ pkg-conf...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ocm7.0.0_vllm_0.11.1_20251103 has an error with flash attention bug;rocm;stale ### Your current environment rocm/vllm:rocm7.0.0_vllm_0.11.1_20251103 (Note, this does work with rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006) D...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: rocm/vllm:rocm7.0.0_vllm_0.11.1_20251103 has an error with flash attention bug;rocm;stale ### Your current environment rocm/vllm:rocm7.0.0_vllm_0.11.1_20251103 (Note, this does work with rocm/vllm:rocm7.0.0_vllm_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=10960, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31062](https://github.com/vllm-project/vllm/pull/31062) | closes_keyword | 0.95 | [ROCm][Docker] Add gfx1103 support to Docker builds | Fixes #28052 by adding gfx1103 (AMD Radeon 780M and similar RDNA 3 integrated graphics) to the default GPU architectures in Docker builds. ## Problem Users with AMD Radeon 780M (g |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
