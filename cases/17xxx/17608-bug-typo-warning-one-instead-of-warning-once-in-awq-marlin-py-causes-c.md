# vllm-project/vllm#17608: [Bug]: Typo `warning_one` instead of `warning_once` in `awq_marlin.py` causes crash with AWQ MoE models and TP

| 字段 | 值 |
| --- | --- |
| Issue | [#17608](https://github.com/vllm-project/vllm/issues/17608) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Typo `warning_one` instead of `warning_once` in `awq_marlin.py` causes crash with AWQ MoE models and TP

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **🐛 Describe the bug** When attempting to load an AWQ-quantized MoE model (`CognitiveComputations/Qwen3-30B-A3B-AWQ`) with tensor parallelism (`tensor-parallel-size=4`), the vLLM server fails to start due to a typo in the AWQ Marlin quantization code. Specifically, the code tries to call `logger.warning_one` which does not exist, instead of the correct method `logger.warning_once`. This occurs in the `get_quant_method` function within `vllm/model_executor/layers/quantization/awq_marlin.py`. **Reproduction Steps** 1. Install vLLM (tested with version `0.8.5.post1`). 2. Run the following command: ```bash python -m vllm.entrypoints.api_server \ --model CognitiveComputations/Qwen3-30B-A3B-AWQ \ --gpu-memory-utilization 0.9 \ --max-model-len 2048 \ --max-num-seqs 64 \ --tensor-parallel-size 4 ``` **Actual Behavior** The server fails to start. One of the worker processes crashes during model initialization with the following traceback, leading to an overall engine initialization failure: (VllmWorker rank=3 pid=1796) ERROR 05-03 05:43:44 [multiproc_executor.py:435] WorkerProc failed to start.(VllmWorker rank=3 pid=1796) ERROR 05-03 05:4...

## 现有链接修复摘要

#17605 fix typo in logging

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ver fails to start due to a typo in the AWQ Marlin quantization code. Specifically, the code tries to call `logger.warning_one` which does not exist, instead of the correct method `logger.warning_once`. This occurs in t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ` instead of `warning_once` in `awq_marlin.py` causes crash with AWQ MoE models and TP bug ### Your current environment ### 🐛 Describe the bug **🐛 Describe the bug** When attempting to load an AWQ-quantized MoE model (`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: E model (`CognitiveComputations/Qwen3-30B-A3B-AWQ`) with tensor parallelism (`tensor-parallel-size=4`), the vLLM server fails to start due to a typo in the AWQ Marlin quantization code. Specifically, the code tries to c...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: _one` instead of `warning_once` in `awq_marlin.py` causes crash with AWQ MoE models and TP bug ### Your current environment ### 🐛 Describe the bug **🐛 Describe the bug** When attempting to load an AWQ-quantized MoE mode...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: OR 05-03 05:43:44 [multiproc_executor.py:435] lambda prefix: Qwen3MoeDecoderLayer(config=config,(VllmWorker rank=3 pid=1796) ERROR 05-03 05:43:44 [multiproc_executor.py:435] File "/usr/local/lib/python3.10/dist-packages...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#17605](https://github.com/vllm-project/vllm/pull/17605) | closes_keyword | 0.95 | fix typo in logging | FIX #17608 - Updated the logging method from `warning_one` to `warning_once` in both: - `vllm/model_executor/layers/quantization/awq_marlin.py` - `vllm/model_executor/layers/q |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
