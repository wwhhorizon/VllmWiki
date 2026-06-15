# vllm-project/vllm#26381: [Bug]: FlashInfer autotuning crash with CUDA 13.0

| 字段 | 值 |
| --- | --- |
| Issue | [#26381](https://github.com/vllm-project/vllm/issues/26381) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FlashInfer autotuning crash with CUDA 13.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running the following command results in a crash: ``` python examples/offline_inference/basic/generate.py --model=redhatai/meta-Llama-3.1-8B-FP8 ``` The same happens with `nvidia/Llama-4-Scout-17B-16E-Instruct-FP8`. I tried with `--kv-cache-dtype=fp8` as well, same issue. I also tried `VLLM_ATTENTION_BACKEND=TRITON_ATTN`, same issue. `meta-llama/Llama-3.1-8B` seems to work fine. CUDA 12.9 also works fine. Logs ``` python examples/offline_inference/basic/generate.py --model=redhatai/meta-Llama-3.1-8B-FP8 --max-model-len=1024 Reserved 1 GPU(s): [3] for command execution /home/ProExpertProg/git/vllm/.venv/lib/python3.12/site-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml for you. import pynvml # type: ignore[import] INFO 10-07 17:36:18 [__init__.py:215] Automatically detected platform cuda. INFO 10-07 17:36:22 [utils.py:233] non-default args: {'max_model_len': 1024, 'num_redundant_experts': None, 'eplb_window_size': None, 'eplb_step_interval': No...

## 现有链接修复摘要

#34648 [Feature] Add VLLM_TRITON_AUTOTUNE with functional autotune control

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: /__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: s in a crash: ``` python examples/offline_inference/basic/generate.py --model=redhatai/meta-Llama-3.1-8B-FP8 ``` The same happens with `nvidia/Llama-4-Scout-17B-16E-Instruct-FP8`. I tried with `--kv-cache-dtype=fp8` as...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: FlashInfer autotuning crash with CUDA 13.0 bug;unstale ### Your current environment ### 🐛 Describe the bug Running the following command results in a crash: ``` python examples/offline_inference/basic/generate.py...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: FlashInfer autotuning crash with CUDA 13.0 bug;unstale ### Your current environment ### 🐛 Describe the bug Running the following command results in a crash: ``` python examples/offline_inference/basic/generate.py...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: s/offline_inference/basic/generate.py --model=redhatai/meta-Llama-3.1-8B-FP8 ``` The same happens with `nvidia/Llama-4-Scout-17B-16E-Instruct-FP8`. I tried with `--kv-cache-dtype=fp8` as well, same issue. I also tried `...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34648](https://github.com/vllm-project/vllm/pull/34648) | mentioned | 0.6 | [Feature] Add VLLM_TRITON_AUTOTUNE with functional autotune control | ability** — same model + same hardware can produce different results (#26381) ### Solution - **`VLLM_TRITON_AUTOTUNE=0`** (default): passes only `configs[:1]` to `triton.autotune`… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
