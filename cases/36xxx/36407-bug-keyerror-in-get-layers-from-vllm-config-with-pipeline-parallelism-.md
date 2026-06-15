# vllm-project/vllm#36407: [Bug]: KeyError in get_layers_from_vllm_config with pipeline parallelism (vLLM 0.16.0)

| 字段 | 值 |
| --- | --- |
| Issue | [#36407](https://github.com/vllm-project/vllm/issues/36407) |
| 状态 | open |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization |
| 子分类 |  |
| Operator 关键词 | attention;fp8;moe;operator |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: KeyError in get_layers_from_vllm_config with pipeline parallelism (vLLM 0.16.0)

### Issue 正文摘录

### Your current environment ## Environment - **vLLM version:** 0.16.0 - **Python version:** 3.12 - **GPU:** H100 NVL - **Distributed setup:** 3 nodes × 2 GPUs, Ray distributed executor - **Model:** Qwen/Qwen3-VL-235B-A22B-Instruct-FP8 - **Flags:** `--tensor-parallel-size=2 --pipeline-parallel-size=3 --distributed-executor-backend=ray` ### 🐛 Describe the bug # vLLM 0.16.0 Bug: `get_layers_from_vllm_config` KeyErrors in Pipeline Parallel Mode ## Summary `get_layers_from_vllm_config` in `vllm/config/vllm.py` raises `KeyError` during `initialize_attn_backend` when `--pipeline-parallel-size > 1`. Every worker crashes before the server starts. ## Affected version vLLM **0.16.0** (latest as of 2026-03-06). ## Reproduction ``` Model : Qwen/Qwen3-VL-235B-A22B-Instruct-FP8 Command: vllm serve /models/qwen-vl \ --tensor-parallel-size=2 \ --pipeline-parallel-size=3 \ --distributed-executor-backend=ray Cluster: 3 nodes × 2× H100 NVL (6 GPUs total via KubeRay) ``` After all checkpoint shards load and KV-cache sizing completes, every `RayWorkerWrapper` process throws: ``` ERROR [core.py] EngineCore failed to start. ... File "vllm/config/vllm.py", line 1596, in get_layers_from_vllm_config if isi...

## 现有链接修复摘要

#36243 [Bugfix] Skip out-of-stage layers in get_layers_from_vllm_config for pipeline parallel

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: KeyError in get_layers_from_vllm_config with pipeline parallelism (vLLM 0.16.0) bug ### Your current environment ## Environment - **vLLM version:** 0.16.0 - **Python version:** 3.12 - **GPU:** H100 NVL - **Distri...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: (vLLM 0.16.0) bug ### Your current environment ## Environment - **vLLM version:** 0.16.0 - **Python version:** 3.12 - **GPU:** H100 NVL - **Distributed setup:** 3 nodes × 2 GPUs, Ray distributed executor - **Model:** Qw...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: KeyError in get_layers_from_vllm_config with pipeline parallelism (vLLM 0.16.0) bug ### Your current environment ## Environment - **vLLM version:** 0.16.0 - **Python version:** 3.12 - **GPU:** H100 NVL - **Distri...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: , Ray distributed executor - **Model:** Qwen/Qwen3-VL-235B-A22B-Instruct-FP8 - **Flags:** `--tensor-parallel-size=2 --pipeline-parallel-size=3 --distributed-executor-backend=ray` ### 🐛 Describe the bug # vLLM 0.16.0 Bug...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ashes before the server starts. ## Affected version vLLM **0.16.0** (latest as of 2026-03-06). ## Reproduction ``` Model : Qwen/Qwen3-VL-235B-A22B-Instruct-FP8 Command: vllm serve /models/qwen-vl \ --tensor-parallel-siz...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36243](https://github.com/vllm-project/vllm/pull/36243) | mentioned | 0.45 | [Bugfix] Skip out-of-stage layers in get_layers_from_vllm_config for pipeline parallel | wer lots of frequently asked questions. fix linked to this pr fixes #36243 bug |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
