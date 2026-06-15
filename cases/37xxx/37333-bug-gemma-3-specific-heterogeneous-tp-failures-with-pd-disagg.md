# vllm-project/vllm#37333: [Bug]: Gemma-3 specific heterogeneous TP failures with PD disagg

| 字段 | 值 |
| --- | --- |
| Issue | [#37333](https://github.com/vllm-project/vllm/issues/37333) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Gemma-3 specific heterogeneous TP failures with PD disagg

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # [NixlConnector] Gemma-3 specific heterogeneous TP failures with PD disagg `google/gemma-3-4b-it` uses sliding-window + full-attention. When running with PD disagg in heterogeneous TP (1 prefill + 2 decodes or 2 prefills + 1 decode), `gemma-3-4b-it` has ~0% accuracy on GSM8K 5-shot, down from ~76%. Existing sweep in `tests/v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh` only tests `gemma-3-4b-it` with 1 prefill + 1 decode. So this is not caught in CI. ### To reproduce: Pull #37069, which adds to the existing test suite, and run `python3 tests/v1/kv_connector/nixl_integration/test_config.py '*gemma*'`. ``` ======================================================================== SUMMARY ======================================================================== [PASS] tp_gemma_sw_fa.yaml 167.7s logs: /home/yzong-rh/vllm/tests/v1/kv_connector/nixl_integration/logs/20260317_163330/tp_gemma_sw_fa.{stdout,stderr} [PASS] tp_gemma_sw_fa_hma.yaml 171.1s logs: /home/yzong-rh/vllm/tests/v1/kv_connector/nixl_integration/logs/20260317_163330/tp_gemma_sw_fa_hma.{stdout,stderr} [PASS] tp_gemma_sw_fa_hma_2p2d.yaml 200.4s logs: /hom...

## 现有链接修复摘要

#37069 [Test][Nixl] Add YAML-driven test runner for PD accuracy configs

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Gemma-3 specific heterogeneous TP failures with PD disagg bug ### Your current environment ### 🐛 Describe the bug # [NixlConnector] Gemma-3 specific heterogeneous TP failures with PD disagg `google/gemma-3-4b-it`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Gemma-3 specific heterogeneous TP failures with PD disagg bug ### Your current environment ### 🐛 Describe the bug # [NixlConnector] Gemma-3 specific heterogeneous TP failures with PD disagg `google/gemma-3-4b-it`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: decodes or 2 prefills + 1 decode), `gemma-3-4b-it` has ~0% accuracy on GSM8K 5-shot, down from ~76%. Existing sweep in `tests/v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh` only tests `gemma-3-4b-it` wi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ow + full-attention. When running with PD disagg in heterogeneous TP (1 prefill + 2 decodes or 2 prefills + 1 decode), `gemma-3-4b-it` has ~0% accuracy on GSM8K 5-shot, down from ~76%. Existing sweep in `tests/v1/kv_con...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: 1 prefill + 2 decodes or 2 prefills + 1 decode), `gemma-3-4b-it` has ~0% accuracy on GSM8K 5-shot, down from ~76%. Existing sweep in `tests/v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh` only tests `gem...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37069](https://github.com/vllm-project/vllm/pull/37069) | mentioned | 0.45 | [Test][Nixl] Add YAML-driven test runner for PD accuracy configs | ill + 1 decode. so this is not caught in ci. ### to reproduce: pull #37069, which adds to the existing test suite, and run `python3 tests/v1/kv_connector/nixl_integration/test_con… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
