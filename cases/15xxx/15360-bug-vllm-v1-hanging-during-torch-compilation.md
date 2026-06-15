# vllm-project/vllm#15360: [Bug]: vLLM v1 hanging during Torch compilation

| 字段 | 值 |
| --- | --- |
| Issue | [#15360](https://github.com/vllm-project/vllm/issues/15360) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale;needs reproduction |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM v1 hanging during Torch compilation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Experiencing a hanging issue when running the offline LLM API. Using Qwen2.5-7b previously saved to disk. (Per the [docs](https://docs.vllm.ai/en/latest/design/multiprocessing.html), I set the multiproc method to spawn to avoid CUDA reinitialization error). ```python import os os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn" from vllm import LLM llm = LLM(model="Qwen/Qwen2.5-7B-Instruct", gpu_memory_utilization=0.9, max_model_len=6600) ``` The above hangs after `Dynamo bytecode transform time`, when I believe Torch compilation should occur: ```text /databricks/python/lib/python3.11/site-packages/torch/utils/_pytree.py:185: FutureWarning: optree is installed but the version is too old to support PyTorch Dynamo in C++ pytree. C++ pytree support is disabled. Please consider upgrading optree using `python3 -m pip install --upgrade 'optree>=0.13.0'`. warnings.warn( 2025-03-23 16:29:28.424785: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations. To enable the following instructions: AVX2 FMA, in other operations, rebuild Tensor...

## 现有链接修复摘要

#41606 Bump the minor-update group across 1 directory with 140 updates | #41766 Bump the minor-update group across 1 directory with 141 updates | #41859 Bump the minor-update group across 1 directory with 141 updates | #42056 Bump the minor-update group across 1 directory with 142 updates | #42717 Bump the minor-update group across 1 directory with 143 updates

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: vLLM v1 hanging during Torch compilation bug;torch.compile;stale;needs reproduction ### Your current environment ### 🐛 Describe the bug Experiencing a hanging issue when running the offline LLM API. Using Qwen2.5...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: vLLM v1 hanging during Torch compilation bug;torch.compile;stale;needs reproduction ### Your current environment ### 🐛 Describe the bug Experiencing a hanging issue when running the offline LLM API. Using Qwen2.5...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=6600, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ug Experiencing a hanging issue when running the offline LLM API. Using Qwen2.5-7b previously saved to disk. (Per the [docs](https://docs.vllm.ai/en/latest/design/multiprocessing.html), I set the multiproc method to spa...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41606](https://github.com/vllm-project/vllm/pull/41606) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 140 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15360">#15360</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#41766](https://github.com/vllm-project/vllm/pull/41766) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15360">#15360</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#41859](https://github.com/vllm-project/vllm/pull/41859) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15360">#15360</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#42056](https://github.com/vllm-project/vllm/pull/42056) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 142 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15360">#15360</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#42717](https://github.com/vllm-project/vllm/pull/42717) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 143 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15360">#15360</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
